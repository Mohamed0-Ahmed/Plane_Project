import numpy as np
import pandas as pd
from ADRpy import atmospheres
import os
import sys
import pickle

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from utils import calculate_fuel_consumption, calculate_emissions, calculate_metrics, calculate_drag_coefficient, calculate_metrics_m, calculate_lift_coefficient_climb

def simulate_cruise_phase(params, wind_speed_scenario, crosswind_speed_scenario, initial_weight, initial_time, initial_horizontal_distance, previous_engine_power=None, cumulative_fuel_consumed=0, total_carbon_emissions=0, total_co_emissions=0, total_nox_emissions=0, total_so2_emissions=0):
    initial_altitude = params['initial_altitude'] * 0.3048  # feet to meters
    initial_airspeed = params['initial_airspeed'] * 0.51444  # knots to m/s
    final_airspeed = params['final_airspeed'] * 0.51444  # knots to m/s
    acceleration_duration = params['acceleration_duration']  # seconds
    cruise_distance = params['cruise_distance'] * 1000  # km to meters
    total_cruise_distance = initial_horizontal_distance + cruise_distance
    initial_weight = initial_weight * 9.81  # kg to N

    num_motors = params['num_motors']
    num_engines = params['num_engines']
    gearbox_efficiency = params['gearbox_efficiency']
    inverter_efficiency = params['inverter_efficiency']
    battery_capacity_kWh = params['battery_capacity_kWh']
    usable_capacity_factor = params['usable_capacity_factor']
    steady_state_motor_power_kW = params['steady_state_motor_power_kW']

    C_D0 = params['C_D0']
    k = params['k']
    S = params['S']
    
    isa = atmospheres.Atmosphere()
    
    # Determine the directory of this script
    script_dir = os.path.dirname(__file__)
    spline_function_path = os.path.join(script_dir, 'spline_function.pkl')

    with open(spline_function_path, 'rb') as f:
        loaded_spline = pickle.load(f)

    airspeed = initial_airspeed
    weight = initial_weight
    time = initial_time
    horizontal_distance = initial_horizontal_distance
    phase_time = 0  # New variable to track time within the cruise phase
    acceleration_rate = (final_airspeed - initial_airspeed) / acceleration_duration

    times = []
    altitudes = []
    airspeeds = []
    true_airspeeds = []
    groundspeeds = []
    power_drag_list = []
    total_powers = []
    engine_powers = []
    drags = []
    lifts = []
    pressures = []
    weights = []
    headings = []
    drag_coefficients = []
    horizontal_distances = []
    fuel_consumptions = []
    cumulative_fuel_consumptions = []
    carbon_emissions = []
    cumulative_carbon_emissions = []
    co_emissions = []
    cumulative_co_emissions = []
    nox_emissions = []
    cumulative_nox_emissions = []
    so2_emissions = []
    cumulative_so2_emissions = []

    while horizontal_distance < total_cruise_distance:
        wind_speed = wind_speed_scenario(time)
        crosswind_speed = crosswind_speed_scenario(time)

        if phase_time <= acceleration_duration:
            airspeed += acceleration_rate * params['time_step']
            airspeed = min(airspeed, final_airspeed)  # Ensure airspeed does not exceed final_airspeed
        else:
            airspeed = final_airspeed

        # Debugging statements
        #print(f"Time: {time}, Phase Time: {phase_time}, Airspeed: {airspeed}, Horizontal Distance: {horizontal_distance}, Acceleration Rate: {acceleration_rate}, Acceleration Duration: {acceleration_duration}")

        true_airspeed = airspeed
        ground_speed = np.sqrt((true_airspeed + wind_speed)**2 + crosswind_speed**2)
        heading = np.arctan2(crosswind_speed, true_airspeed + wind_speed)
        rho = isa.airdens_kgpm3(initial_altitude)
        pressure = isa.airpress_pa(initial_altitude)
        C_L = weight / (0.5 * rho * true_airspeed**2 * S)  # Level flight assumption
        C_D = calculate_drag_coefficient(C_D0, k, C_L)
        drag = (0.5 * rho * true_airspeed**2 * C_D * S)
        power_drag = (drag * true_airspeed)
        total_power = power_drag

        # Ensure engine_power is not negative
        engine_power = max(total_power, 0)

        # Divide engine power by number of engines
        engine_power_per_engine = engine_power / num_engines

        metrics_engine = calculate_metrics(engine_power_per_engine / 1000, params['time_step'], loaded_spline)

        current_fuel_consumed = metrics_engine['fuel_consumed_kg_total']  # Incremental fuel consumption
        cumulative_fuel_consumed += current_fuel_consumed
        weight -= current_fuel_consumed * 9.81  # kg to N

        total_carbon_emissions += metrics_engine['carbon_emissions_kg_total']
        total_co_emissions += metrics_engine['co_emissions_kg_total']
        total_nox_emissions += metrics_engine['nox_emissions_kg_total']
        total_so2_emissions += metrics_engine['so2_emissions_kg_total']

        horizontal_distance += ground_speed * params['time_step']
        horizontal_distances.append(horizontal_distance)

        fuel_consumptions.append(current_fuel_consumed)
        cumulative_fuel_consumptions.append(cumulative_fuel_consumed)
        carbon_emissions.append(metrics_engine['carbon_emissions_kg_total'])
        cumulative_carbon_emissions.append(total_carbon_emissions)
        co_emissions.append(metrics_engine['co_emissions_kg_total'])
        cumulative_co_emissions.append(total_co_emissions)
        nox_emissions.append(metrics_engine['nox_emissions_kg_total'])
        cumulative_nox_emissions.append(total_nox_emissions)
        so2_emissions.append(metrics_engine['so2_emissions_kg_total'])
        cumulative_so2_emissions.append(total_so2_emissions)

        times.append(time)
        altitudes.append(initial_altitude)
        airspeeds.append(airspeed)
        true_airspeeds.append(true_airspeed)
        groundspeeds.append(ground_speed)
        power_drag_list.append(power_drag)
        total_powers.append(total_power)
        engine_powers.append(engine_power)
        drags.append(drag)
        lifts.append(weight)
        pressures.append(pressure)
        weights.append(weight)
        headings.append(np.degrees(heading))
        drag_coefficients.append(C_D)

        time += params['time_step']
        phase_time += params['time_step']  # Increment phase_time

    results = pd.DataFrame({
        'Time (s)': times,
        'Altitude (m)': altitudes,
        'Airspeed (m/s)': airspeeds,
        'True Airspeed (m/s)': true_airspeeds,
        'Groundspeed (m/s)': groundspeeds,
        'Power Drag (W)': power_drag_list,
        'Total Power (W)': total_powers,
        'Engine Power (W)': engine_powers,
        'Drag (N)': drags,
        'Lift (N)': lifts,
        'Pressure (Pa)': pressures,
        'Weight (N)': weights,
        'Heading (degrees)': headings,
        'Drag Coefficient': drag_coefficients,
        'Horizontal Distance (m)': horizontal_distances,
        'Fuel Consumption (kg)': fuel_consumptions,
        'Cumulative Fuel Consumption (kg)': cumulative_fuel_consumptions,
        'Carbon Emissions (kg)': carbon_emissions,
        'Cumulative Carbon Emissions (kg)': cumulative_carbon_emissions,
        'CO Emissions (kg)': co_emissions,
        'Cumulative CO Emissions (kg)': cumulative_co_emissions,
        'NOx Emissions (kg)': nox_emissions,
        'Cumulative NOx Emissions (kg)': cumulative_nox_emissions,
        'SO2 Emissions (kg)': so2_emissions,
        'Cumulative SO2 Emissions (kg)': cumulative_so2_emissions
    })

    return results, weight, time, horizontal_distance, cumulative_fuel_consumed, total_carbon_emissions, total_co_emissions, total_nox_emissions, total_so2_emissions
