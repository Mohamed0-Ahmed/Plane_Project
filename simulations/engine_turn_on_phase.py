import numpy as np
import pandas as pd
from ADRpy import atmospheres
import sys
import os
import pickle
import matplotlib.pyplot as plt

# Adjust the Python path to include the root directory of your project
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from utils import calculate_fuel_consumption, calculate_emissions, calculate_metrics, calculate_drag_coefficient, calculate_lift_coefficient_descent

def engine_turn_on_phase(params, initial_time, initial_horizontal_distance, num_engines=2, cumulative_fuel_consumed_turn_on=0, total_carbon_emissions_turn_on=0, total_co_emissions_turn_on=0, total_nox_emissions_turn_on=0, total_so2_emissions_turn_on=0):
    idle_power_kW = params['idle_power_kw']
    time_step = params['time_step']
    turn_on_duration = params['turn_on_duration']  # Turn-on duration in seconds
    initial_weight = params['initial_weight']
    initial_altitude = 0  # Start from ground level altitude
    altitudes = initial_altitude
    isa = atmospheres.Atmosphere()
    pressure = isa.airpress_pa(0)

    times = []
    altitudes = []
    distances = []
    velocities = []
    total_powers = []
    fuel_consumptions = []
    cumulative_fuel_consumed = cumulative_fuel_consumed_turn_on
    total_carbon_emissions = total_carbon_emissions_turn_on
    total_co_emissions = total_co_emissions_turn_on
    total_nox_emissions = total_nox_emissions_turn_on
    total_so2_emissions = total_so2_emissions_turn_on
    dynamic_weights = []
    pressures = []
    true_airspeeds = []
    groundspeeds = []

    # Determine the directory of this script
    script_dir = os.path.dirname(__file__)
    spline_function_path = os.path.join(script_dir, 'spline_function.pkl')

    with open(spline_function_path, 'rb') as f:
        loaded_spline = pickle.load(f)

    # Static phase for the turn-on duration to reach idle power
    for time in np.arange(0, turn_on_duration, time_step):
        power = 2*(time / turn_on_duration) * idle_power_kW  # Linear increase to idle power
        times.append(time + initial_time)
        distances.append(initial_horizontal_distance)
        velocities.append(0)
        total_powers.append(power * 1000)  # Convert kW to W
        altitudes.append(0)
        pressures.append(pressure)
        true_airspeeds.append(0)
        groundspeeds.append(0)
        # Calculate metrics for engines
        metrics_engine = calculate_metrics(power / 2, time_step, loaded_spline, num_engines=num_engines) 
        current_fuel_consumed = metrics_engine['fuel_consumed_kg_total']
        cumulative_fuel_consumed += current_fuel_consumed
        
        total_carbon_emissions += metrics_engine['carbon_emissions_kg_total']
        total_co_emissions += metrics_engine['co_emissions_kg_total']
        total_nox_emissions += metrics_engine['nox_emissions_kg_total']
        total_so2_emissions += metrics_engine['so2_emissions_kg_total']
        cumulative_carbon_emissions=total_carbon_emissions
        cumulative_co_emissions=total_co_emissions
        cumulative_nox_emissions=total_nox_emissions
        cumulative_so2_emissions=total_so2_emissions
        fuel_consumptions.append(current_fuel_consumed)
        cumulative_fuel_consumptions = fuel_consumptions
        dynamic_weights.append(initial_weight - cumulative_fuel_consumed * 9.81)  # Update weight based on fuel consumption

    results = pd.DataFrame({
        'Time (s)': times,
        'Distance (m)': distances,
        'Altitude (m)': altitudes,
        'Velocity (m/s)': velocities,
        'Total Power (W)': total_powers,
        'Cumulative Fuel Consumption (kg)': cumulative_fuel_consumptions,
        'Fuel Consumption (kg)': fuel_consumptions,
        'Dynamic Weight (N)': dynamic_weights,
        'Carbon Emissions (kg)': total_carbon_emissions,
        'CO Emissions (kg)': total_co_emissions,
        'NOx Emissions (kg)': total_nox_emissions,
        'SO2 Emissions (kg)': total_so2_emissions,
        'Pressure (Pa)': pressures,
        'True Airspeed (m/s)': true_airspeeds,
        'Groundspeed (m/s)': groundspeeds,
        'Cumulative Carbon Emissions (kg)': cumulative_carbon_emissions,
        'Cumulative CO Emissions (kg)': cumulative_co_emissions,
        'Cumulative NOx Emissions (kg)': cumulative_nox_emissions,
        'Cumulative SO2 Emissions (kg)': cumulative_so2_emissions
    })

    # # Plot results for checking
    # plt.figure(figsize=(14, 8))

    # plt.subplot(2, 2, 1)
    # plt.plot(results['Time (s)'], results['Velocity (m/s)'], label='Velocity')
    # plt.xlabel('Time (s)')
    # plt.ylabel('Velocity (m/s)')
    # plt.title('Velocity over Time')
    # plt.legend()
    # plt.grid(True)

    # plt.subplot(2, 2, 2)
    # plt.plot(results['Time (s)'], results['Distance (m)'], label='Distance', color='orange')
    # plt.xlabel('Time (s)')
    # plt.ylabel('Distance (m)')
    # plt.title('Distance over Time')
    # plt.legend()
    # plt.grid(True)

    # plt.subplot(2, 2, 3)
    # plt.plot(results['Time (s)'], results['Total Power (W)'], label='Total Power', color='green')
    # plt.xlabel('Time (s)')
    # plt.ylabel('Total Power (W)')
    # plt.title('Total Power over Time')
    # plt.legend()
    # plt.grid(True)

    # plt.subplot(2, 2, 4)
    # plt.plot(results['Time (s)'], results['Fuel Consumption (kg)'].cumsum(), label='Cumulative Fuel Consumption', color='red')
    # plt.xlabel('Time (s)')
    # plt.ylabel('Fuel Consumption (kg)')
    # plt.title('Cumulative Fuel Consumption over Time')
    # plt.legend()
    # plt.grid(True)

    # plt.tight_layout()
    # plt.show()

    return results, dynamic_weights[-1], time + initial_time, distances[-1], idle_power_kW * 1000, cumulative_fuel_consumed, total_carbon_emissions, total_co_emissions, total_nox_emissions, total_so2_emissions

