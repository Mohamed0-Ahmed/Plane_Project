# import numpy as np
# import pandas as pd
# import pickle
# import os
# from ADRpy import atmospheres
# import sys
# import matplotlib.pyplot as plt

# # Adjust the Python path to include the root directory of your project
# sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

# from utils import calculate_fuel_consumption, calculate_emissions, calculate_metrics, calculate_drag_coefficient, calculate_lift_coefficient_climb, enforce_power_limits

# def simulate_climb_phase_int(params, wind_speed_scenario, crosswind_speed_scenario, initial_weight, initial_time, initial_horizontal_distance, initial_roc, final_roc, total_climb_time, num_engines=2, cumulative_fuel_consumed=0, total_carbon_emissions=0, total_co_emissions=0, total_nox_emissions=0, total_so2_emissions=0):
#     def roc_scenario(time, initial_roc, final_roc, total_climb_time):
#         if initial_roc == final_roc:
#             return initial_roc * 0.00508  # Convert to m/s directly
#         climb_progress = min((time - initial_time) / total_climb_time, 1)
#         roc = initial_roc + climb_progress * (final_roc - initial_roc)
#         return roc * 0.00508  # Convert to m/s

#     initial_altitude = params['initial_altitude'] * 0.3048  # feet to meters
#     initial_airspeed = params['initial_airspeed'] * 0.51444  # knots to m/s
#     final_airspeed = params['final_airspeed'] * 0.51444  # knots to m/s
#     initial_weight = initial_weight * 9.81  # kg to N
#     C_D0 = params['C_D0']
#     k = params['k']
#     S = params['S']
#     max_power_kw = params['max_power_kw']
#     idle_power_kw = params['idle_power_kw']
#     time_step = params['time_step']

#     isa = atmospheres.Atmosphere()

#     # Determine the directory of this script
#     script_dir = os.path.dirname(__file__)
#     spline_function_path = os.path.join(script_dir, 'spline_function.pkl')

#     with open(spline_function_path, 'rb') as f:
#         loaded_spline = pickle.load(f)

#     altitude = initial_altitude
#     airspeed = initial_airspeed
#     weight = initial_weight
#     time = initial_time
#     horizontal_distance = initial_horizontal_distance

#     times = []
#     altitudes = []
#     airspeeds = []
#     true_airspeeds = []
#     groundspeeds = []
#     power_drag_list = []
#     power_climb_list = []
#     total_powers = []
#     engine_powers = []
#     drags = []
#     lifts = []
#     climb_angles = []
#     pressures = []
#     weights = []
#     headings = []
#     drag_coefficients = []
#     lift_coefficients = []
#     horizontal_distances = []
#     fuel_consumptions = []
#     cumulative_fuel_consumptions = []
#     carbon_emissions = []
#     cumulative_carbon_emissions = []
#     co_emissions = []
#     cumulative_co_emissions = []
#     nox_emissions = []
#     cumulative_nox_emissions = []
#     so2_emissions = []
#     cumulative_so2_emissions = []

#     while time < initial_time + total_climb_time:
#         wind_speed = wind_speed_scenario(time)
#         crosswind_speed = crosswind_speed_scenario(time)

#         # Get the current rate of climb
#         roc = roc_scenario(time, initial_roc, final_roc, total_climb_time)

#         altitude += roc * time_step
#         airspeed = initial_airspeed + (final_airspeed - initial_airspeed) * ((time - initial_time) / total_climb_time)
#         true_airspeed = airspeed
#         ground_speed = np.sqrt((true_airspeed + wind_speed)**2 + crosswind_speed**2)
#         heading = np.arctan2(crosswind_speed, true_airspeed + wind_speed)
#         climb_angle = np.arctan(roc / true_airspeed)
#         rho = isa.airdens_kgpm3(altitude)
#         pressure = isa.airpress_pa(altitude)
#         C_L = calculate_lift_coefficient_climb(weight, climb_angle, rho, true_airspeed, S)  # Calculate lift coefficient
#         C_D = calculate_drag_coefficient(C_D0, k, C_L)
#         drag = 0.5 * rho * true_airspeed**2 * C_D * S
#         power_drag = drag * true_airspeed
#         power_climb = weight * roc
#         total_power = power_drag + power_climb

#         # Apply power limits
#         total_power = enforce_power_limits(total_power, max_power_kw, idle_power_kw, num_engines)

#         # Ensure engine_power is not negative
#         engine_power = max(total_power, 0)

#         # Divide engine power by number of engines
#         engine_power_per_engine = engine_power / num_engines

#         metrics_engine = calculate_metrics(engine_power_per_engine / 1000, time_step, loaded_spline)

#         current_fuel_consumed = metrics_engine['fuel_consumed_kg_total']  # Incremental fuel consumption
#         cumulative_fuel_consumed += current_fuel_consumed
#         weight -= current_fuel_consumed * 9.81  # kg to N

#         total_carbon_emissions += metrics_engine['carbon_emissions_kg_total']
#         total_co_emissions += metrics_engine['co_emissions_kg_total']
#         total_nox_emissions += metrics_engine['nox_emissions_kg_total']
#         total_so2_emissions += metrics_engine['so2_emissions_kg_total']

#         horizontal_ground_speed = ground_speed * np.cos(climb_angle)
#         horizontal_distance += horizontal_ground_speed * time_step
#         horizontal_distances.append(horizontal_distance)

#         fuel_consumptions.append(current_fuel_consumed)
#         cumulative_fuel_consumptions.append(cumulative_fuel_consumed)
#         carbon_emissions.append(metrics_engine['carbon_emissions_kg_total'])
#         cumulative_carbon_emissions.append(total_carbon_emissions)
#         co_emissions.append(metrics_engine['co_emissions_kg_total'])
#         cumulative_co_emissions.append(total_co_emissions)
#         nox_emissions.append(metrics_engine['nox_emissions_kg_total'])
#         cumulative_nox_emissions.append(total_nox_emissions)
#         so2_emissions.append(metrics_engine['so2_emissions_kg_total'])
#         cumulative_so2_emissions.append(total_so2_emissions)

#         times.append(time)
#         altitudes.append(altitude)
#         airspeeds.append(airspeed)
#         true_airspeeds.append(true_airspeed)
#         groundspeeds.append(ground_speed)
#         power_drag_list.append(power_drag)
#         power_climb_list.append(power_climb)
#         total_powers.append(total_power)
#         engine_powers.append(engine_power)
#         drags.append(drag)
#         lifts.append(weight * np.cos(climb_angle))
#         climb_angles.append(np.degrees(climb_angle))
#         pressures.append(pressure)
#         weights.append(weight)
#         headings.append(np.degrees(heading))
#         drag_coefficients.append(C_D)
#         lift_coefficients.append(C_L)

#         time += time_step

#     results = pd.DataFrame({
#         'Time (s)': times,
#         'Altitude (m)': altitudes,
#         'Airspeed (m/s)': airspeeds,
#         'True Airspeed (m/s)': true_airspeeds,
#         'Groundspeed (m/s)': groundspeeds,
#         'Power Drag (W)': power_drag_list,
#         'Power Climb (W)': power_climb_list,
#         'Total Power (W)': total_powers,
#         'Engine Power (W)': engine_powers,
#         'Drag (N)': drags,
#         'Lift (N)': lifts,
#         'Climb Angle (degrees)': climb_angles,
#         'Pressure (Pa)': pressures,
#         'Weight (N)': weights,
#         'Heading (degrees)': headings,
#         'Drag Coefficient': drag_coefficients,
#         'Lift Coefficient': lift_coefficients,
#         'Horizontal Distance (m)': horizontal_distances,
#         'Fuel Consumption (kg)': fuel_consumptions,
#         'Cumulative Fuel Consumption (kg)': cumulative_fuel_consumptions,
#         'Carbon Emissions (kg)': carbon_emissions,
#         'Cumulative Carbon Emissions (kg)': cumulative_carbon_emissions,
#         'CO Emissions (kg)': co_emissions,
#         'Cumulative CO Emissions (kg)': cumulative_co_emissions,
#         'NOx Emissions (kg)': nox_emissions,
#         'Cumulative NOx Emissions (kg)': cumulative_nox_emissions,
#         'SO2 Emissions (kg)': so2_emissions,
#         'Cumulative SO2 Emissions (kg)': cumulative_so2_emissions
#     })

#     # # Plotting the interpolated climb phase
#     # plt.figure(figsize=(14, 8))

#     # # Plot altitude vs. time
#     # plt.subplot(2, 2, 1)
#     # plt.plot(results['Time (s)'], results['Altitude (m)'], label='Altitude (m)', color='b')
#     # plt.xlabel('Time (s)')
#     # plt.ylabel('Altitude (m)')
#     # plt.title('Altitude over Time')
#     # plt.legend()
#     # plt.grid(True)

#     # # Plot airspeed vs. time
#     # plt.subplot(2, 2, 2)
#     # plt.plot(results['Time (s)'], results['Airspeed (m/s)'], label='Airspeed (m/s)', color='g')
#     # plt.xlabel('Time (s)')
#     # plt.ylabel('Airspeed (m/s)')
#     # plt.title('Airspeed over Time')
#     # plt.legend()
#     # plt.grid(True)

#     # # Plot cumulative fuel consumption vs. time
#     # plt.subplot(2, 2, 3)
#     # plt.plot(results['Time (s)'], results['Cumulative Fuel Consumption (kg)'], label='Cumulative Fuel Consumption (kg)', color='r')
#     # plt.xlabel('Time (s)')
#     # plt.ylabel('Cumulative Fuel Consumption (kg)')
#     # plt.title('Cumulative Fuel Consumption over Time')
#     # plt.legend()
#     # plt.grid(True)

#     # # Plot total power vs. time
#     # plt.subplot(2, 2, 4)
#     # plt.plot(results['Time (s)'], results['Total Power (W)'], label='Total Power (W)', color='m')
#     # plt.xlabel('Time (s)')
#     # plt.ylabel('Total Power (W)')
#     # plt.title('Total Power over Time')
#     # plt.legend()
#     # plt.grid(True)

#     # plt.tight_layout()
#     # plt.show()

#     return results, weight, time, horizontal_distance, total_power, cumulative_fuel_consumed, total_carbon_emissions, total_co_emissions, total_nox_emissions, total_so2_emissions, altitude  # Include final altitude


import numpy as np
import pandas as pd
import pickle
import os
from ADRpy import atmospheres
import sys
import matplotlib.pyplot as plt

# Adjust the Python path to include the root directory of your project
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from utils import calculate_fuel_consumption, calculate_emissions, calculate_metrics, calculate_drag_coefficient, calculate_lift_coefficient_climb, enforce_power_limits, calculate_metrics_m

def simulate_climb_phase_int(params, wind_speed_scenario, crosswind_speed_scenario, initial_weight, initial_time, initial_horizontal_distance, initial_roc, final_roc, total_climb_time, num_engines=2, cumulative_fuel_consumed=0, total_carbon_emissions=0, total_co_emissions=0, total_nox_emissions=0, total_so2_emissions=0):
    def roc_scenario(time, initial_roc, final_roc, total_climb_time):
        if initial_roc == final_roc:
            return initial_roc * 0.00508  # Convert to m/s directly
        climb_progress = min((time - initial_time) / total_climb_time, 1)
        roc = initial_roc + climb_progress * (final_roc - initial_roc)
        return roc * 0.00508  # Convert to m/s

    initial_altitude = params['initial_altitude'] * 0.3048  # feet to meters
    initial_airspeed = params['initial_airspeed'] * 0.51444  # knots to m/s
    final_airspeed = params['final_airspeed'] * 0.51444  # knots to m/s
    initial_weight = initial_weight * 9.81  # kg to N
    C_D0 = params['C_D0']
    k = params['k']
    S = params['S']
    max_power_kw = params['max_power_kw']
    idle_power_kw = params['idle_power_kw']
    degree_of_hybridization = params['DOH']
    max_motor_power_kW = params['max_motor_power_kW']
    time_step = params['time_step']
    usable_battery_capacity_kWh = params['battery_capacity_kWh'] * params['usable_capacity_factor']
    propeller_efficiency= params['propeller_efficiency']

    isa = atmospheres.Atmosphere()

    # Determine the directory of this script
    script_dir = os.path.dirname(__file__)
    spline_function_path = os.path.join(script_dir, 'spline_function.pkl')

    with open(spline_function_path, 'rb') as f:
        loaded_spline = pickle.load(f)

    with open('motor_efficiency_interpolation.pkl', 'rb') as file:
        motor_efficiency_spline = pickle.load(file)

    altitude = initial_altitude
    airspeed = initial_airspeed
    weight = initial_weight
    time = initial_time
    horizontal_distance = initial_horizontal_distance

    cumulative_battery_energy_consumed = 0

    times = []
    altitudes = []
    airspeeds = []
    true_airspeeds = []
    groundspeeds = []
    power_drag_list = []
    power_climb_list = []
    total_powers = []
    engine_powers = []
    motor_powers = []
    drags = []
    lifts = []
    climb_angles = []
    pressures = []
    weights = []
    headings = []
    drag_coefficients = []
    lift_coefficients = []
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
    battery_energy_consumptions = []
    cumulative_battery_energy_list = []

    while time < initial_time + total_climb_time:
        wind_speed = wind_speed_scenario(time)
        crosswind_speed = crosswind_speed_scenario(time)

        # Get the current rate of climb
        roc = roc_scenario(time, initial_roc, final_roc, total_climb_time)

        altitude += roc * time_step
        airspeed = initial_airspeed + (final_airspeed - initial_airspeed) * ((time - initial_time) / total_climb_time)
        true_airspeed = airspeed
        ground_speed = np.sqrt((true_airspeed + wind_speed)**2 + crosswind_speed**2)
        heading = np.arctan2(crosswind_speed, true_airspeed + wind_speed)
        climb_angle = np.arctan(roc / true_airspeed)
        rho = isa.airdens_kgpm3(altitude)
        pressure = isa.airpress_pa(altitude)
        C_L = calculate_lift_coefficient_climb(weight, climb_angle, rho, true_airspeed, S)  # Calculate lift coefficient
        C_D = calculate_drag_coefficient(C_D0, k, C_L)
        drag = 0.5 * rho * true_airspeed**2 * C_D * S
        power_drag = drag * true_airspeed
        power_climb = weight * roc
        total_power = power_drag + power_climb
        total_power = total_power/ propeller_efficiency
        # Hybridization
        motor_power = min(total_power * degree_of_hybridization, max_motor_power_kW * 2 * 1000)
        engine_power = total_power - motor_power

        # Ensure motor power does not exceed capabilities
        motor_power = max(min(motor_power, max_motor_power_kW * 1000 * 2), 0)
        engine_power = total_power - motor_power

        motor_power_per = motor_power / 2
        engine_power_per = engine_power / 2

        # Calculate metrics for motors and engines
        metrics_motor = calculate_metrics_m(motor_power_per / 1000, time_step, motor_efficiency_spline, params['gearbox_efficiency'], params['inverter_efficiency'], num_motors=2)
        metrics_engine = calculate_metrics(engine_power_per / 1000, time_step, loaded_spline, num_engines=2)

        current_battery_energy_consumed = metrics_motor['energy_consumed_kWh_total_m']
        cumulative_battery_energy_consumed += current_battery_energy_consumed

        current_fuel_consumed = metrics_engine['fuel_consumed_kg_total']  # Incremental fuel consumption
        cumulative_fuel_consumed += current_fuel_consumed
        weight -= current_fuel_consumed * 9.81  # kg to N

        total_carbon_emissions += metrics_engine['carbon_emissions_kg_total']
        total_co_emissions += metrics_engine['co_emissions_kg_total']
        total_nox_emissions += metrics_engine['nox_emissions_kg_total']
        total_so2_emissions += metrics_engine['so2_emissions_kg_total']

        horizontal_ground_speed = ground_speed * np.cos(climb_angle)
        horizontal_distance += horizontal_ground_speed * time_step
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
        battery_energy_consumptions.append(current_battery_energy_consumed)
        cumulative_battery_energy_list.append(cumulative_battery_energy_consumed)

        times.append(time)
        altitudes.append(altitude)
        airspeeds.append(airspeed)
        true_airspeeds.append(true_airspeed)
        groundspeeds.append(ground_speed)
        power_drag_list.append(power_drag)
        power_climb_list.append(power_climb)
        total_powers.append(total_power)
        engine_powers.append(engine_power)
        motor_powers.append(motor_power)
        drags.append(drag)
        lifts.append(weight * np.cos(climb_angle))
        climb_angles.append(np.degrees(climb_angle))
        pressures.append(pressure)
        weights.append(weight)
        headings.append(np.degrees(heading))
        drag_coefficients.append(C_D)
        lift_coefficients.append(C_L)

        time += time_step
    required_batteries = np.ceil(cumulative_battery_energy_consumed / usable_battery_capacity_kWh)
    print(f'battey amount {required_batteries:2f}')

    results = pd.DataFrame({
        'Time (s)': times,
        'Altitude (m)': altitudes,
        'Airspeed (m/s)': airspeeds,
        'True Airspeed (m/s)': true_airspeeds,
        'Groundspeed (m/s)': groundspeeds,
        'Power Drag (W)': power_drag_list,
        'Power Climb (W)': power_climb_list,
        'Total Power (W)': total_powers,
        'Engine Power (W)': engine_powers,
        'Motor Power (W)': motor_powers,
        'Drag (N)': drags,
        'Lift (N)': lifts,
        'Climb Angle (degrees)': climb_angles,
        'Pressure (Pa)': pressures,
        'Weight (N)': weights,
        'Heading (degrees)': headings,
        'Drag Coefficient': drag_coefficients,
        'Lift Coefficient': lift_coefficients,
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
        'Cumulative SO2 Emissions (kg)': cumulative_so2_emissions,
        'Battery Energy Consumption (kWh)': battery_energy_consumptions,
        'Cumulative Battery Energy Consumption (kWh)': cumulative_battery_energy_list
    })
    plt.figure(figsize=(14, 8))

    plt.subplot(2, 2, 1)
    plt.plot(results['Time (s)'], results['True Airspeed (m/s)'], label='True Airspeed')
    plt.xlabel('Time (s)')
    plt.ylabel('True Airspeed (m/s)')
    plt.title('True Airspeed over Time')
    plt.legend()
    plt.grid(True)

    plt.subplot(2, 2, 2)
    plt.plot(results['Time (s)'], results['Altitude (m)'], label='Altitude', color='orange')
    plt.xlabel('Time (s)')
    plt.ylabel('Altitude (m)')
    plt.title('Altitude over Time')
    plt.legend()
    plt.grid(True)

    plt.subplot(2, 2, 3)
    plt.plot(results['Time (s)'], results['Total Power (W)'], label='Total Power', color='green')
    plt.plot(results['Time (s)'], results['Engine Power (W)'], label='Engine Power', color='blue')
    plt.plot(results['Time (s)'], results['Motor Power (W)'], label='Motor Power', color='purple')
    plt.xlabel('Time (s)')
    plt.ylabel('Power (W)')
    plt.title('Power over Time')
    plt.legend()
    plt.grid(True)

    plt.subplot(2, 2, 4)
    plt.plot(results['Time (s)'], results['Cumulative Fuel Consumption (kg)'], label='Cumulative Fuel Consumption', color='red')
    plt.xlabel('Time (s)')
    plt.ylabel('Cumulative Fuel Consumption (kg)')
    plt.title('Cumulative Fuel Consumption over Time')
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(14, 8))

    plt.subplot(2, 2, 1)
    plt.plot(results['Time (s)'], results['Battery Energy Consumption (kWh)'], label='Battery Energy Consumption', color='purple')
    plt.xlabel('Time (s)')
    plt.ylabel('Battery Energy Consumption (kWh)')
    plt.title('Battery Energy Consumption over Time')
    plt.legend()
    plt.grid(True)

    plt.subplot(2, 2, 2)
    plt.plot(results['Time (s)'], results['Cumulative Battery Energy Consumption (kWh)'], label='Cumulative Battery Energy Consumption', color='brown')
    plt.xlabel('Time (s)')
    plt.ylabel('Cumulative Battery Energy Consumption (kWh)')
    plt.title('Cumulative Battery Energy Consumption over Time')
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.show()

    return results, weight, time, horizontal_distance, total_power,cumulative_battery_energy_consumed, cumulative_fuel_consumed, total_carbon_emissions, total_co_emissions, total_nox_emissions, total_so2_emissions, altitude, required_batteries



