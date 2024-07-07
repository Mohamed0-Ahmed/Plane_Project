# import os
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# import pickle
# from ADRpy import atmospheres
# import sys

# # Adjust the Python path to include the root directory of your project
# sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
# from utils import calculate_metrics

# def simulate_takeoff_phase(params, wind_speed_scenario, crosswind_speed_scenario, initial_weight, initial_time, initial_horizontal_distance, previous_engine_power=None, cumulative_fuel_consumed=0, total_carbon_emissions=0, total_co_emissions=0, total_nox_emissions=0, total_so2_emissions=0):
#     # Aircraft and environmental parameters
#     C_T = params['C_T']
#     n = params['n']  # RPS
#     D = params['D']  # meters
#     initial_altitude = params['initial_altitude'] * 0.3048  # feet to meters
#     W = initial_weight * 9.81  # N (example weight for Q200 Dash, convert from kg to N)
#     S = params['S']  # m² (example wing area)
#     C_D = params['C_D']  # example drag coefficient
#     C_L_MAX = params['C_L_MAX']  # maximum lift coefficient for stall speed calculation
#     C_L_AVG = params['C_L_AVG']  # average lift coefficient for takeoff roll
#     mu = params['mu']  # example coefficient of friction
#     propeller_efficiency = params['propeller_efficiency']  # propeller efficiency during takeoff
#     warm_up_duration = params['warmup_duration']
#     isa = atmospheres.Atmosphere()
#     rho = isa.airdens_kgpm3(initial_altitude)
#     mass = initial_weight  # kg (example mass for Q200 Dash)
#     time_step = params['time_step']  # time step for simulation

#     idle_power_kW = params['idle_power_kW']  # kW per engine
#     max_power_kW = params['max_power_kW']  # kW per engine
#     initial_angle = params['initial_angle']  # degrees
#     final_angle = params['final_angle']  # degrees

#     # Static thrust calculation
#     def calculate_static_thrust(C_T, rho, n, D):
#         return C_T * rho * (n**2) * (D**4)

#     T_static = calculate_static_thrust(C_T, rho, n, D)
#     T_static_total = 2 * T_static  # for two engines

#     # Calculate stall speed and liftoff speed
#     def calculate_stall_speed(W, rho, S, C_L_MAX):
#         return np.sqrt((2 * W) / (rho * S * C_L_MAX))

#     V_stall = calculate_stall_speed(W, rho, S, C_L_MAX)
#     V_lof = 1.1 * V_stall

#     # Load the spline functions
#     script_dir = os.path.dirname(__file__)
#     spline_function_path = os.path.join(script_dir, 'spline_function.pkl')
#     with open(spline_function_path, 'rb') as f:
#         loaded_spline = pickle.load(f)

#     altitude = initial_altitude  # Start from ground level altitude
#     velocity = 0
#     distance = initial_horizontal_distance
#     time = initial_time

#     time += warm_up_duration


#     times = []
#     altitudes = []
#     distances = []
#     velocities = []
#     accelerations = []
#     total_powers = []
#     engine_powers = []
#     motor_powers = []
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
#     angles = []
#     weights = []

#     print(f"Starting warm-up phase with initial weight {initial_weight} kg")

#     warm_time = time

#     # Warm-up phase
#     while time < warm_time + params['warmup_duration']:
#         power_increase_rate = (max_power_kW - idle_power_kW) / params['warmup_duration']
#         engine_power_kW = idle_power_kW + power_increase_rate * (time - warm_time)
#         engine_power_kW_per_engine = engine_power_kW / 2
        
#         # Ensure the power is within the specified limits
#         engine_power_kW_per_engine = np.clip(engine_power_kW_per_engine, idle_power_kW / 2, max_power_kW / 2)

#         # Calculate metrics for engines
#         metrics_engine = calculate_metrics(engine_power_kW_per_engine, time_step, loaded_spline, num_engines=2)

#         current_fuel_consumed = metrics_engine['fuel_consumed_kg_total']  # Incremental fuel consumption
#         cumulative_fuel_consumed += current_fuel_consumed

#         total_carbon_emissions += metrics_engine['carbon_emissions_kg_total']
#         total_co_emissions += metrics_engine['co_emissions_kg_total']
#         total_nox_emissions += metrics_engine['nox_emissions_kg_total']
#         total_so2_emissions += metrics_engine['so2_emissions_kg_total']

#         # Append current values to the lists
#         times.append(time)
#         altitudes.append(altitude)
#         distances.append(distance)
#         velocities.append(velocity)
#         accelerations.append(0)
#         total_powers.append(engine_power_kW * 2 * 1000)  # Convert kW to W for total power
#         engine_powers.append(engine_power_kW * 1000)  # Convert kW to W
#         motor_powers.append(0)
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
#         angles.append(initial_angle)
#         weights.append(W - cumulative_fuel_consumed * 9.81)

#         time += time_step

#     print("Completed warm-up phase. Starting takeoff roll phase.")

#     # Takeoff roll phase
#     while velocity < V_lof:
#         wind_speed = wind_speed_scenario(time)
#         crosswind_speed = crosswind_speed_scenario(time)

#         # Calculate drag and friction forces
#         D = 0.5 * rho * velocity**2 * C_D * S
#         F_d = mu * W

#         # Calculate thrust
#         T = T_static_total - 0.02 * velocity**2
#         T = min(T, T_static_total)  # Ensure thrust does not exceed static thrust

#         # Calculate acceleration
#         a = (T - D - F_d) / mass

#         # Calculate power required considering propeller efficiency
#         power_required = (T * velocity) / propeller_efficiency

#         # Update velocity and distance
#         velocity += a * time_step
#         distance += velocity * time_step

#         # Set engine power to maximum during takeoff roll
#         engine_power_kW_per_engine = max_power_kW

#         # Calculate metrics for engines
#         metrics_engine = calculate_metrics(engine_power_kW_per_engine, time_step, loaded_spline, num_engines=2)

#         current_fuel_consumed = metrics_engine['fuel_consumed_kg_total']  # Incremental fuel consumption
#         cumulative_fuel_consumed += current_fuel_consumed

#         total_carbon_emissions += metrics_engine['carbon_emissions_kg_total']
#         total_co_emissions += metrics_engine['co_emissions_kg_total']
#         total_nox_emissions += metrics_engine['nox_emissions_kg_total']
#         total_so2_emissions += metrics_engine['so2_emissions_kg_total']

#         # Calculate rotation angle
#         if velocity > V_stall:
#             angle = initial_angle + (velocity - V_stall) / (V_lof - V_stall) * (final_angle - initial_angle)
#         else:
#             angle = initial_angle

#         # Append current values to the lists
#         times.append(time)
#         altitudes.append(altitude)
#         distances.append(distance)
#         velocities.append(velocity)
#         accelerations.append(a)
#         total_powers.append(engine_power_kW_per_engine * 2 * 1000)  # Convert kW to W for total power
#         engine_powers.append(engine_power_kW_per_engine * 1000)  # Convert kW to W for per engine power
#         motor_powers.append(0)
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
#         angles.append(angle)
#         weights.append(W - cumulative_fuel_consumed * 9.81)

#         time += time_step

#     results = pd.DataFrame({
#         'Time (s)': times,
#         'Altitude (m)': altitudes,
#         'Distance (m)': distances,
#         'True Airspeed (m/s)': velocities,
#         'Groundspeed (m/s)': velocities,  # Assuming groundspeed is the same as airspeed in this simplified case
#         'Acceleration (m/s^2)': accelerations,
#         'Total Power (W)': total_powers,
#         'Engine Power (W)': engine_powers,
#         'Motor Power (W)': motor_powers,
#         'Fuel Consumption (kg)': fuel_consumptions,
#         'Cumulative Fuel Consumption (kg)': cumulative_fuel_consumptions,
#         'Carbon Emissions (kg)': carbon_emissions,
#         'Cumulative Carbon Emissions (kg)': cumulative_carbon_emissions,
#         'CO Emissions (kg)': co_emissions,
#         'Cumulative CO Emissions (kg)': cumulative_co_emissions,
#         'NOx Emissions (kg)': nox_emissions,
#         'Cumulative NOx Emissions (kg)': cumulative_nox_emissions,
#         'SO2 Emissions (kg)': so2_emissions,
#         'Cumulative SO2 Emissions (kg)': cumulative_so2_emissions,
#         'Climb Angle (degrees)': angles,
#         'Weight (N)': weights
#     })

#     print("Completed takeoff roll phase. Here are some sample results:")
#     print(results.head())

#     # # Plot results for checking
#     # plt.figure(figsize=(14, 8))

#     # plt.subplot(2, 2, 1)
#     # plt.plot(results['Time (s)'], results['True Airspeed (m/s)'], label='True Airspeed')
#     # plt.xlabel('Time (s)')
#     # plt.ylabel('True Airspeed (m/s)')
#     # plt.title('True Airspeed over Time')
#     # plt.legend()
#     # plt.grid(True)

#     # plt.subplot(2, 2, 2)
#     # plt.plot(results['Time (s)'], results['Distance (m)'], label='Distance', color='orange')
#     # plt.xlabel('Time (s)')
#     # plt.ylabel('Distance (m)')
#     # plt.title('Distance over Time')
#     # plt.legend()
#     # plt.grid(True)

#     # plt.subplot(2, 2, 3)
#     # plt.plot(results['Time (s)'], results['Total Power (W)'], label='Total Power', color='green')
#     # plt.xlabel('Time (s)')
#     # plt.ylabel('Total Power (W)')
#     # plt.title('Total Power over Time')
#     # plt.legend()
#     # plt.grid(True)

#     # plt.subplot(2, 2, 4)
#     # plt.plot(results['Time (s)'], results['Cumulative Fuel Consumption (kg)'], label='Cumulative Fuel Consumption', color='red')
#     # plt.xlabel('Time (s)')
#     # plt.ylabel('Cumulative Fuel Consumption (kg)')
#     # plt.title('Cumulative Fuel Consumption over Time')
#     # plt.legend()
#     # plt.grid(True)

#     # plt.tight_layout()
#     # plt.show()

#     return results, weights[-1], time, distance, engine_power_kW_per_engine * 1000, cumulative_fuel_consumed, total_carbon_emissions, total_co_emissions, total_nox_emissions, total_so2_emissions

# # import numpy as np
# # import pandas as pd
# # import pickle
# # import os
# # import matplotlib.pyplot as plt
# # from ADRpy import atmospheres
# # import sys

# # # Adjust the Python path to include the root directory of your project
# # sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

# # from utils import calculate_metrics

# # def simulate_takeoff_phase(params, wind_speed_scenario, crosswind_speed_scenario, initial_weight, initial_time, initial_horizontal_distance, warm_up_duration, previous_engine_power, cumulative_fuel_consumed, total_carbon_emissions, total_co_emissions, total_nox_emissions, total_so2_emissions):
# #     print("Starting takeoff phase...")
# #     initial_weight = initial_weight * 9.81  # Convert kg to N

# #     times = []
# #     distances = []
# #     velocities = []
# #     accelerations = []
# #     powers = []
# #     fuel_consumptions = []
# #     cumulative_fuel_consumptions = []
# #     carbon_emissions = []
# #     cumulative_carbon_emissions = []
# #     co_emissions = []
# #     cumulative_co_emissions = []
# #     nox_emissions = []
# #     cumulative_nox_emissions = []
# #     so2_emissions = []
# #     cumulative_so2_emissions = []
# #     weights = []

# #     time = initial_time
# #     distance = initial_horizontal_distance
# #     velocity = 0
# #     weight = initial_weight
# #     acceleration = 0
# #     power_kw = previous_engine_power
# #     V_lof = params['takeoff_speed']

# #     # Load the spline function if not provided
# #     script_dir = os.path.dirname(__file__)
# #     spline_function_path = os.path.join(script_dir, 'spline_function.pkl')
# #     with open(spline_function_path, 'rb') as f:
# #         spline_function = pickle.load(f)

# #     for t in np.arange(0, warm_up_duration, params['time_step']):
# #         power_kw = previous_engine_power + (params['max_power_kW'] - previous_engine_power) * (t / warm_up_duration)
# #         metrics = calculate_metrics(power_kw, params['time_step'], spline_function, num_engines=2)

# #         current_fuel_consumed = metrics['fuel_consumed_kg_total']
# #         cumulative_fuel_consumed += current_fuel_consumed
# #         weight -= current_fuel_consumed * 9.81

# #         total_carbon_emissions += metrics['carbon_emissions_kg_total']
# #         total_co_emissions += metrics['co_emissions_kg_total']
# #         total_nox_emissions += metrics['nox_emissions_kg_total']
# #         total_so2_emissions += metrics['so2_emissions_kg_total']

# #         times.append(time)
# #         distances.append(distance)
# #         velocities.append(velocity)
# #         accelerations.append(acceleration)
# #         powers.append(power_kw * 1000)  # Convert kW to W
# #         fuel_consumptions.append(current_fuel_consumed)
# #         cumulative_fuel_consumptions.append(cumulative_fuel_consumed)
# #         carbon_emissions.append(metrics['carbon_emissions_kg_total'])
# #         cumulative_carbon_emissions.append(total_carbon_emissions)
# #         co_emissions.append(metrics['co_emissions_kg_total'])
# #         cumulative_co_emissions.append(total_co_emissions)
# #         nox_emissions.append(metrics['nox_emissions_kg_total'])
# #         cumulative_nox_emissions.append(total_nox_emissions)
# #         so2_emissions.append(metrics['so2_emissions_kg_total'])
# #         cumulative_so2_emissions.append(total_so2_emissions)
# #         weights.append(weight)

# #         time += params['time_step']

# #     print("Completed warm-up phase. Starting takeoff roll phase.")

# #     # Takeoff roll phase
# #     while velocity < V_lof:
# #         acceleration = (power_kw * params['propeller_efficiency']) / weight - params['mu'] * 9.81
# #         velocity += acceleration * params['time_step']
# #         distance += velocity * params['time_step']

# #         power_kw = params['max_power_kW']
# #         metrics = calculate_metrics(power_kw, params['time_step'], spline_function, num_engines=2)

# #         current_fuel_consumed = metrics['fuel_consumed_kg_total']
# #         cumulative_fuel_consumed += current_fuel_consumed
# #         weight -= current_fuel_consumed * 9.81

# #         total_carbon_emissions += metrics['carbon_emissions_kg_total']
# #         total_co_emissions += metrics['co_emissions_kg_total']
# #         total_nox_emissions += metrics['nox_emissions_kg_total']
# #         total_so2_emissions += metrics['so2_emissions_kg_total']

# #         times.append(time)
# #         distances.append(distance)
# #         velocities.append(velocity)
# #         accelerations.append(acceleration)
# #         powers.append(power_kw * 1000)  # Convert kW to W
# #         fuel_consumptions.append(current_fuel_consumed)
# #         cumulative_fuel_consumptions.append(cumulative_fuel_consumed)
# #         carbon_emissions.append(metrics['carbon_emissions_kg_total'])
# #         cumulative_carbon_emissions.append(total_carbon_emissions)
# #         co_emissions.append(metrics['co_emissions_kg_total'])
# #         cumulative_co_emissions.append(total_co_emissions)
# #         nox_emissions.append(metrics['nox_emissions_kg_total'])
# #         cumulative_nox_emissions.append(total_nox_emissions)
# #         so2_emissions.append(metrics['so2_emissions_kg_total'])
# #         cumulative_so2_emissions.append(total_so2_emissions)
# #         weights.append(weight)

# #         print(f"Time: {time:.2f}, Velocity: {velocity:.2f}, Acceleration: {acceleration:.2f}, Distance: {distance:.2f}")

# #         if velocity < 0:  # Safety check to prevent infinite loop
# #             print("Error: Negative velocity detected, breaking out of the loop.")
# #             break

# #         time += params['time_step']
    
# #     print(f"Takeoff phase complete with final weight {weight / 9.81} kg")

# #     results = pd.DataFrame({
# #         'Time (s)': times,
# #         'Distance (m)': distances,
# #         'Velocity (m/s)': velocities,
# #         'Acceleration (m/s^2)': accelerations,
# #         'Power (W)': powers,
# #         'Fuel Consumption (kg)': fuel_consumptions,
# #         'Cumulative Fuel Consumption (kg)': cumulative_fuel_consumptions,
# #         'Carbon Emissions (kg)': carbon_emissions,
# #         'Cumulative Carbon Emissions (kg)': cumulative_carbon_emissions,
# #         'CO Emissions (kg)': co_emissions,
# #         'Cumulative CO Emissions (kg)': cumulative_co_emissions,
# #         'NOx Emissions (kg)': nox_emissions,
# #         'Cumulative NOx Emissions (kg)': cumulative_nox_emissions,
# #         'SO2 Emissions (kg)': so2_emissions,
# #         'Cumulative SO2 Emissions (kg)': cumulative_so2_emissions,
# #         'Weight (N)': weights
# #     })

# #     print("Completed takeoff roll phase. Here are some sample results:")
# #     print(results.head())

# #     # Plot results for checking
# #     plt.figure(figsize=(14, 8))

# #     plt.subplot(2, 2, 1)
# #     plt.plot(results['Time (s)'], results['True Airspeed (m/s)'], label='True Airspeed')
# #     plt.xlabel('Time (s)')
# #     plt.ylabel('True Airspeed (m/s)')
# #     plt.title('True Airspeed over Time')
# #     plt.legend()
# #     plt.grid(True)

# #     plt.subplot(2, 2, 2)
# #     plt.plot(results['Time (s)'], results['Distance (m)'], label='Distance', color='orange')
# #     plt.xlabel('Time (s)')
# #     plt.ylabel('Distance (m)')
# #     plt.title('Distance over Time')
# #     plt.legend()
# #     plt.grid(True)

# #     plt.subplot(2, 2, 3)
# #     plt.plot(results['Time (s)'], results['Total Power (W)'], label='Total Power', color='green')
# #     plt.xlabel('Time (s)')
# #     plt.ylabel('Total Power (W)')
# #     plt.title('Total Power over Time')
# #     plt.legend()
# #     plt.grid(True)

# #     plt.subplot(2, 2, 4)
# #     plt.plot(results['Time (s)'], results['Cumulative Fuel Consumption (kg)'], label='Cumulative Fuel Consumption', color='red')
# #     plt.xlabel('Time (s)')
# #     plt.ylabel('Cumulative Fuel Consumption (kg)')
# #     plt.title('Cumulative Fuel Consumption over Time')
# #     plt.legend()
# #     plt.grid(True)

# #     plt.tight_layout()
# #     plt.show()


# #     return (
# #         results, 
# #         weight / 9.81,  # Convert N to kg
# #         time, 
# #         distance, 
# #         power_kw * 1000, 
# #         cumulative_fuel_consumed, 
# #         total_carbon_emissions, 
# #         total_co_emissions, 
# #         total_nox_emissions, 
# #         total_so2_emissions
# #     )

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pickle
from ADRpy import atmospheres
import sys

# Adjust the Python path to include the root directory of your project
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from utils import calculate_metrics

def simulate_takeoff_phase(params, wind_speed_scenario, crosswind_speed_scenario, initial_weight, initial_time, initial_horizontal_distance, previous_engine_power=None, cumulative_fuel_consumed=0, total_carbon_emissions=0, total_co_emissions=0, total_nox_emissions=0, total_so2_emissions=0):
    # Aircraft and environmental parameters
    C_T = params['C_T']
    n = params['n']  # RPS
    D = params['D']  # meters
    initial_altitude = params['initial_altitude'] * 0.3048  # feet to meters
    W = initial_weight * 9.81  # N (example weight for Q200 Dash, convert from kg to N)
    S = params['S']  # m² (example wing area)
    C_D = params['C_D']  # example drag coefficient
    C_L_MAX = params['C_L_MAX']  # maximum lift coefficient for stall speed calculation
    C_L_AVG = params['C_L_AVG']  # average lift coefficient for takeoff roll
    mu = params['mu']  # example coefficient of friction
    propeller_efficiency = params['propeller_efficiency']  # propeller efficiency during takeoff
    warm_up_duration = params['warmup_duration']
    isa = atmospheres.Atmosphere()
    rho = isa.airdens_kgpm3(initial_altitude)
    mass = initial_weight  # kg (example mass for Q200 Dash)
    time_step = params['time_step']  # time step for simulation

    idle_power_kW = params['idle_power_kW']  # kW per engine
    max_power_kW = params['max_power_kW']  # kW per engine
    initial_angle = params['initial_angle']  # degrees
    final_angle = params['final_angle']  # degrees

    # Static thrust calculation
    def calculate_static_thrust(C_T, rho, n, D):
        return C_T * rho * (n**2) * (D**4)

    T_static = calculate_static_thrust(C_T, rho, n, D)
    T_static_total = 2 * T_static  # for two engines

    # Calculate stall speed and liftoff speed
    def calculate_stall_speed(W, rho, S, C_L_MAX):
        return np.sqrt((2 * W) / (rho * S * C_L_MAX))

    V_stall = calculate_stall_speed(W, rho, S, C_L_MAX)
    V_lof = 1.1 * V_stall

    # Load the spline functions
    script_dir = os.path.dirname(__file__)
    spline_function_path = os.path.join(script_dir, 'spline_function.pkl')
    with open(spline_function_path, 'rb') as f:
        loaded_spline = pickle.load(f)

    altitude = initial_altitude  # Start from ground level altitude
    velocity = 0
    distance = initial_horizontal_distance
    time = initial_time

    time += warm_up_duration


    times = []
    altitudes = []
    distances = []
    velocities = []
    accelerations = []
    total_powers = []
    engine_powers = []
    motor_powers = []
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
    angles = []
    weights = []

    print(f"Starting warm-up phase with initial weight {initial_weight} kg")

    warm_time = time

    # Warm-up phase
    while time < warm_time + params['warmup_duration']:
        power_increase_rate = (max_power_kW - idle_power_kW) / params['warmup_duration']
        engine_power_kW = idle_power_kW + power_increase_rate * (time - warm_time)
        engine_power_kW_per_engine = engine_power_kW / 2
        
        # Ensure the power is within the specified limits
        engine_power_kW_per_engine = np.clip(engine_power_kW_per_engine, idle_power_kW / 2, max_power_kW / 2)

        # Calculate metrics for engines
        metrics_engine = calculate_metrics(engine_power_kW_per_engine, time_step, loaded_spline, num_engines=2)

        current_fuel_consumed = metrics_engine['fuel_consumed_kg_total']  # Incremental fuel consumption
        cumulative_fuel_consumed += current_fuel_consumed

        total_carbon_emissions += metrics_engine['carbon_emissions_kg_total']
        total_co_emissions += metrics_engine['co_emissions_kg_total']
        total_nox_emissions += metrics_engine['nox_emissions_kg_total']
        total_so2_emissions += metrics_engine['so2_emissions_kg_total']

        # Append current values to the lists
        times.append(time)
        altitudes.append(altitude)
        distances.append(distance)
        velocities.append(velocity)
        accelerations.append(0)
        total_powers.append(engine_power_kW * 2 * 1000)  # Convert kW to W for total power
        engine_powers.append(engine_power_kW * 1000)  # Convert kW to W
        motor_powers.append(0)
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
        angles.append(initial_angle)
        weights.append(W - cumulative_fuel_consumed * 9.81)

        time += time_step

    print("Completed warm-up phase. Starting takeoff roll phase.")

    # Takeoff roll phase
    while velocity < V_lof:
        wind_speed = wind_speed_scenario(time)
        crosswind_speed = crosswind_speed_scenario(time)

        # Calculate drag and friction forces
        D = 0.5 * rho * velocity**2 * C_D * S
        F_d = mu * W

        # Calculate thrust
        T = T_static_total - 0.02 * velocity**2
        T = min(T, T_static_total)  # Ensure thrust does not exceed static thrust

        # Calculate acceleration
        a = (T - D - F_d) / mass

        # Calculate power required considering propeller efficiency
        power_required = (T * velocity) / propeller_efficiency

        # Update velocity and distance
        velocity += a * time_step
        distance += velocity * time_step

        # Set engine power to maximum during takeoff roll
        engine_power_kW_per_engine = max_power_kW

        # Calculate metrics for engines
        metrics_engine = calculate_metrics(engine_power_kW_per_engine, time_step, loaded_spline, num_engines=2)

        current_fuel_consumed = metrics_engine['fuel_consumed_kg_total']  # Incremental fuel consumption
        cumulative_fuel_consumed += current_fuel_consumed

        total_carbon_emissions += metrics_engine['carbon_emissions_kg_total']
        total_co_emissions += metrics_engine['co_emissions_kg_total']
        total_nox_emissions += metrics_engine['nox_emissions_kg_total']
        total_so2_emissions += metrics_engine['so2_emissions_kg_total']

        # Calculate rotation angle
        if velocity > V_stall:
            angle = initial_angle + (velocity - V_stall) / (V_lof - V_stall) * (final_angle - initial_angle)
        else:
            angle = initial_angle

        # Append current values to the lists
        times.append(time)
        altitudes.append(altitude)
        distances.append(distance)
        velocities.append(velocity)
        accelerations.append(a)
        total_powers.append(engine_power_kW_per_engine * 2 * 1000)  # Convert kW to W for total power
        engine_powers.append(engine_power_kW_per_engine * 1000)  # Convert kW to W for per engine power
        motor_powers.append(0)
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
        angles.append(angle)
        weights.append(W - cumulative_fuel_consumed * 9.81)

        time += time_step

    results = pd.DataFrame({
        'Time (s)': times,
        'Altitude (m)': altitudes,
        'Distance (m)': distances,
        'True Airspeed (m/s)': velocities,
        'Groundspeed (m/s)': velocities,  # Assuming groundspeed is the same as airspeed in this simplified case
        'Acceleration (m/s^2)': accelerations,
        'Total Power (W)': total_powers,
        'Engine Power (W)': engine_powers,
        'Motor Power (W)': motor_powers,
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
        'Climb Angle (degrees)': angles,
        'Weight (N)': weights
    })

    print("Completed takeoff roll phase. Here are some sample results:")
    print(results.head())

    # Plot results for checking
    plt.figure(figsize=(14, 8))

    plt.subplot(2, 2, 1)
    plt.plot(results['Time (s)'], results['True Airspeed (m/s)'], label='True Airspeed')
    plt.xlabel('Time (s)')
    plt.ylabel('True Airspeed (m/s)')
    plt.title('True Airspeed over Time')
    plt.legend()
    plt.grid(True)

    plt.subplot(2, 2, 2)
    plt.plot(results['Time (s)'], results['Distance (m)'], label='Distance', color='orange')
    plt.xlabel('Time (s)')
    plt.ylabel('Distance (m)')
    plt.title('Distance over Time')
    plt.legend()
    plt.grid(True)

    plt.subplot(2, 2, 3)
    plt.plot(results['Time (s)'], results['Total Power (W)'], label='Total Power', color='green')
    plt.xlabel('Time (s)')
    plt.ylabel('Total Power (W)')
    plt.title('Total Power over Time')
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

    return results, weights[-1], time, distance, engine_power_kW_per_engine * 1000, cumulative_fuel_consumed, total_carbon_emissions, total_co_emissions, total_nox_emissions, total_so2_emissions