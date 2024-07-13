# # import numpy as np
# # import pandas as pd
# # import pickle
# # import os
# # from ADRpy import atmospheres
# # import sys
# # import matplotlib.pyplot as plt

# # # Adjust the Python path to include the root directory of your project
# # sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

# # from utils import calculate_metrics

# # def simulate_taxi_phase(params, wind_speed_scenario, crosswind_speed_scenario, initial_weight, initial_time, initial_horizontal_distance,cumulative_fuel_consumed=0, total_carbon_emissions=0, total_co_emissions=0, total_nox_emissions=0, total_so2_emissions=0):
# #     taxi_duration = params['taxi_duration']
# #     max_taxi_speed = params['max_taxi_speed'] * 0.51444  # Convert knots to m/s
# #     acceleration_time = params['acceleration_time']
# #     deceleration_time = params['deceleration_time']
# #     idle_power_kw = params['idle_power_kw']
# #     time_step = params['time_step']

# #     isa = atmospheres.Atmosphere()
    
# #     # Load the spline function if not provided
# #     script_dir = os.path.dirname(__file__)
# #     spline_function_path = os.path.join(script_dir, 'spline_function.pkl')
# #     with open(spline_function_path, 'rb') as f:
# #         spline_function = pickle.load(f)

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
# #     cumulative_fuel_consumed = 0
# #     total_carbon_emissions = 0
# #     total_co_emissions = 0
# #     total_nox_emissions = 0
# #     total_so2_emissions = 0
# #     weight = initial_weight * 9.81  # Convert kg to N

# #     # Taxi phase
# #     acceleration = max_taxi_speed / acceleration_time
# #     deceleration = max_taxi_speed / deceleration_time

# #     # Accelerate to taxi speed
# #     while velocity < max_taxi_speed and time < initial_time + acceleration_time:
# #         velocity += acceleration * time_step
# #         distance += velocity * time_step

# #         power_kw = idle_power_kw
# #         metrics = calculate_metrics(power_kw, time_step, spline_function, num_engines=2)

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

# #         time += time_step

# #     # Constant speed taxiing
# #     while time < initial_time + acceleration_time + taxi_duration:
# #         distance += velocity * time_step

# #         power_kw = idle_power_kw
# #         metrics = calculate_metrics(power_kw, time_step, spline_function, num_engines=2)

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
# #         accelerations.append(0)
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

# #         time += time_step

# #     # Decelerate to stop
# #     while velocity > 0 and time < initial_time + acceleration_time + taxi_duration + deceleration_time:
# #         velocity -= deceleration * time_step
# #         distance += max(velocity, 0) * time_step

# #         power_kw = idle_power_kw
# #         metrics = calculate_metrics(power_kw, time_step, spline_function, num_engines=2)

# #         current_fuel_consumed = metrics['fuel_consumed_kg_total']
# #         cumulative_fuel_consumed += current_fuel_consumed
# #         weight -= current_fuel_consumed * 9.81

# #         total_carbon_emissions += metrics['carbon_emissions_kg_total']
# #         total_co_emissions += metrics['co_emissions_kg_total']
# #         total_nox_emissions += metrics['nox_emissions_kg_total']
# #         total_so2_emissions += metrics['so2_emissions_kg_total']

# #         times.append(time)
# #         distances.append(distance)
# #         velocities.append(max(velocity, 0))
# #         accelerations.append(-deceleration)
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

# #         time += time_step

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

# #     engine_power_kW_per_engine = idle_power_kw  # Adjust this if necessary
# # # Plot results for checking
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
# #         weights[-1], 
# #         time, 
# #         distance, 
# #         engine_power_kW_per_engine * 1000, 
# #         cumulative_fuel_consumed, 
# #         total_carbon_emissions, 
# #         total_co_emissions, 
# #         total_nox_emissions, 
# #         total_so2_emissions
# #     )


# import numpy as np
# import pandas as pd
# import pickle
# import os
# from ADRpy import atmospheres
# import sys
# import matplotlib.pyplot as plt

# # Adjust the Python path to include the root directory of your project
# sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

# from utils import calculate_metrics

# def simulate_taxi_phase(params, wind_speed_scenario, crosswind_speed_scenario, initial_weight, initial_time, initial_horizontal_distance,cumulative_fuel_consumed, total_carbon_emissions, total_co_emissions, total_nox_emissions, total_so2_emissions, num_engines=2):
#     taxi_duration = params['taxi_duration']
#     max_taxi_speed = params['max_taxi_speed'] * 0.51444  # Convert knots to m/s
#     acceleration_time = params['acceleration_time']
#     deceleration_time = params['deceleration_time']
#     idle_power_kw = params['idle_power_kw']
#     time_step = params['time_step']
#     initial_altitude = 0
#     altitudes = initial_altitude
#     isa = atmospheres.Atmosphere()
    
#     # Load the spline function if not provided
#     script_dir = os.path.dirname(__file__)
#     spline_function_path = os.path.join(script_dir, 'spline_function.pkl')
#     with open(spline_function_path, 'rb') as f:
#         spline_function = pickle.load(f)

#     times = []
#     distances = []
#     altitudes = []
#     velocities = []
#     accelerations = []
#     powers = []
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
#     weights = []

#     time = initial_time
#     distance = initial_horizontal_distance
#     velocity = 0
#     cumulative_fuel_consumed = 0
#     total_carbon_emissions = 0
#     total_co_emissions = 0
#     total_nox_emissions = 0
#     total_so2_emissions = 0
#     weight = initial_weight * 9.81  # Convert kg to N

#     # Taxi phase
#     acceleration = max_taxi_speed / acceleration_time
#     deceleration = max_taxi_speed / deceleration_time

#     # Accelerate to taxi speed
#     while velocity < max_taxi_speed and time < initial_time + acceleration_time:
#         velocity += acceleration * time_step
#         distance += velocity * time_step

#         power_kw = idle_power_kw
#         metrics = calculate_metrics(power_kw, time_step, spline_function, num_engines=num_engines)

#         current_fuel_consumed = metrics['fuel_consumed_kg_total']
#         cumulative_fuel_consumed += current_fuel_consumed
#         weight -= current_fuel_consumed * 9.81

#         total_carbon_emissions += metrics['carbon_emissions_kg_total']
#         total_co_emissions += metrics['co_emissions_kg_total']
#         total_nox_emissions += metrics['nox_emissions_kg_total']
#         total_so2_emissions += metrics['so2_emissions_kg_total']

#         times.append(time)
#         altitudes.append(0)
#         distances.append(distance)
#         velocities.append(velocity)
#         accelerations.append(acceleration)
#         powers.append(power_kw * 1000)  # Convert kW to W
#         fuel_consumptions.append(current_fuel_consumed)
#         cumulative_fuel_consumptions.append(cumulative_fuel_consumed)
#         carbon_emissions.append(metrics['carbon_emissions_kg_total'])
#         cumulative_carbon_emissions.append(total_carbon_emissions)
#         co_emissions.append(metrics['co_emissions_kg_total'])
#         cumulative_co_emissions.append(total_co_emissions)
#         nox_emissions.append(metrics['nox_emissions_kg_total'])
#         cumulative_nox_emissions.append(total_nox_emissions)
#         so2_emissions.append(metrics['so2_emissions_kg_total'])
#         cumulative_so2_emissions.append(total_so2_emissions)
#         weights.append(weight)

#         time += time_step

#     # Constant speed taxiing
#     while time < initial_time + acceleration_time + taxi_duration:
#         distance += velocity * time_step

#         power_kw = idle_power_kw
#         metrics = calculate_metrics(power_kw, time_step, spline_function, num_engines=num_engines)

#         current_fuel_consumed = metrics['fuel_consumed_kg_total']
#         cumulative_fuel_consumed += current_fuel_consumed
#         weight -= current_fuel_consumed * 9.81

#         total_carbon_emissions += metrics['carbon_emissions_kg_total']
#         total_co_emissions += metrics['co_emissions_kg_total']
#         total_nox_emissions += metrics['nox_emissions_kg_total']
#         total_so2_emissions += metrics['so2_emissions_kg_total']

#         times.append(time)
#         distances.append(distance)
#         velocities.append(velocity)
#         accelerations.append(0)
#         altitudes.append(0)
#         powers.append(power_kw * 1000)  # Convert kW to W
#         fuel_consumptions.append(current_fuel_consumed)
#         cumulative_fuel_consumptions.append(cumulative_fuel_consumed)
#         carbon_emissions.append(metrics['carbon_emissions_kg_total'])
#         cumulative_carbon_emissions.append(total_carbon_emissions)
#         co_emissions.append(metrics['co_emissions_kg_total'])
#         cumulative_co_emissions.append(total_co_emissions)
#         nox_emissions.append(metrics['nox_emissions_kg_total'])
#         cumulative_nox_emissions.append(total_nox_emissions)
#         so2_emissions.append(metrics['so2_emissions_kg_total'])
#         cumulative_so2_emissions.append(total_so2_emissions)
#         weights.append(weight)

#         time += time_step

#     # Decelerate to stop
#     while velocity > 0 and time < initial_time + acceleration_time + taxi_duration + deceleration_time:
#         velocity -= deceleration * time_step
#         distance += max(velocity, 0) * time_step

#         power_kw = idle_power_kw
#         metrics = calculate_metrics(power_kw, time_step, spline_function, num_engines=num_engines)

#         current_fuel_consumed = metrics['fuel_consumed_kg_total']
#         cumulative_fuel_consumed += current_fuel_consumed
#         weight -= current_fuel_consumed * 9.81

#         total_carbon_emissions += metrics['carbon_emissions_kg_total']
#         total_co_emissions += metrics['co_emissions_kg_total']
#         total_nox_emissions += metrics['nox_emissions_kg_total']
#         total_so2_emissions += metrics['so2_emissions_kg_total']

#         times.append(time)
#         distances.append(distance)
#         velocities.append(max(velocity, 0))
#         altitudes.append(0)
#         accelerations.append(-deceleration)
#         powers.append(power_kw * 1000)  # Convert kW to W
#         fuel_consumptions.append(current_fuel_consumed)
#         cumulative_fuel_consumptions.append(cumulative_fuel_consumed)
#         carbon_emissions.append(metrics['carbon_emissions_kg_total'])
#         cumulative_carbon_emissions.append(total_carbon_emissions)
#         co_emissions.append(metrics['co_emissions_kg_total'])
#         cumulative_co_emissions.append(total_co_emissions)
#         nox_emissions.append(metrics['nox_emissions_kg_total'])
#         cumulative_nox_emissions.append(total_nox_emissions)
#         so2_emissions.append(metrics['so2_emissions_kg_total'])
#         cumulative_so2_emissions.append(total_so2_emissions)
#         weights.append(weight)

#         time += time_step

#     results = pd.DataFrame({
#         'Time (s)': times,
#         'Distance (m)': distances,
#         'Velocity (m/s)': velocities,
#         'Acceleration (m/s^2)': accelerations,
#         'Power (W)': powers,
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
#         'Altitude (m)': altitudes,
#         'Weight (N)': weights
#     })

#     engine_power_kW_per_engine = idle_power_kw  # Adjust this if necessary

#     # Plot results for checking
#     plt.figure(figsize=(14, 8))

#     plt.subplot(2, 2, 1)
#     plt.plot(results['Time (s)'], results['Velocity (m/s)'], label='Velocity')
#     plt.xlabel('Time (s)')
#     plt.ylabel('Velocity (m/s)')
#     plt.title('Velocity over Time')
#     plt.legend()
#     plt.grid(True)

#     plt.subplot(2, 2, 2)
#     plt.plot(results['Time (s)'], results['Distance (m)'], label='Distance', color='orange')
#     plt.xlabel('Time (s)')
#     plt.ylabel('Distance (m)')
#     plt.title('Distance over Time')
#     plt.legend()
#     plt.grid(True)

#     plt.subplot(2, 2, 3)
#     plt.plot(results['Time (s)'], results['Power (W)'], label='Power', color='green')
#     plt.xlabel('Time (s)')
#     plt.ylabel('Power (W)')
#     plt.title('Power over Time')
#     plt.legend()
#     plt.grid(True)

#     plt.subplot(2, 2, 4)
#     plt.plot(results['Time (s)'], results['Cumulative Fuel Consumption (kg)'], label='Cumulative Fuel Consumption', color='red')
#     plt.xlabel('Time (s)')
#     plt.ylabel('Cumulative Fuel Consumption (kg)')
#     plt.title('Cumulative Fuel Consumption over Time')
#     plt.legend()
#     plt.grid(True)

#     plt.tight_layout()
#     plt.show()

#     return (
#         results, 
#         weights[-1], 
#         time, 
#         distance, 
#         engine_power_kW_per_engine * 1000, 
#         cumulative_fuel_consumed, 
#         total_carbon_emissions, 
#         total_co_emissions, 
#         total_nox_emissions, 
#         total_so2_emissions
#     )

import numpy as np
import pandas as pd
import pickle
import os
from ADRpy import atmospheres
import sys
import matplotlib.pyplot as plt

# Adjust the Python path to include the root directory of your project
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from utils import calculate_metrics

def simulate_taxi_phase(params, wind_speed_scenario, crosswind_speed_scenario, initial_weight, initial_time, initial_horizontal_distance, cumulative_fuel_consumed=0, total_carbon_emissions=0, total_co_emissions=0, total_nox_emissions=0, total_so2_emissions=0, num_engines=2):
    taxi_duration = params['taxi_duration']
    max_taxi_speed = params['max_taxi_speed'] * 0.51444  # Convert knots to m/s
    acceleration_time = params['acceleration_time']
    deceleration_time = params['deceleration_time']
    idle_power_kw = params['idle_power_kw']
    time_step = params['time_step']
    initial_altitude = 0
    
    isa = atmospheres.Atmosphere()
    pressure = isa.airpress_pa(0)

    # Load the spline function if not provided
    script_dir = os.path.dirname(__file__)
    spline_function_path = os.path.join(script_dir, 'spline_function.pkl')
    with open(spline_function_path, 'rb') as f:
        spline_function = pickle.load(f)

    times = []
    distances = []
    altitudes = []
    velocities = []
    accelerations = []
    powers = []
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
    weights = []
    pressures = []

    time = initial_time
    distance = initial_horizontal_distance
    velocity = 0
    weight = initial_weight * 9.81  # Convert kg to N

    print(f"Start Taxi Phase: Initial Cumulative Fuel = {cumulative_fuel_consumed}")

    # Taxi phase
    acceleration = max_taxi_speed / acceleration_time
    deceleration = max_taxi_speed / deceleration_time

    # Accelerate to taxi speed
    while velocity < max_taxi_speed and time < initial_time + acceleration_time:
        velocity += acceleration * time_step
        distance += velocity * time_step

        power_kw = idle_power_kw
        metrics = calculate_metrics(power_kw, time_step, spline_function, num_engines=num_engines)

        current_fuel_consumed = metrics['fuel_consumed_kg_total']
        cumulative_fuel_consumed += current_fuel_consumed
        weight -= current_fuel_consumed * 9.81

        total_carbon_emissions += metrics['carbon_emissions_kg_total']
        total_co_emissions += metrics['co_emissions_kg_total']
        total_nox_emissions += metrics['nox_emissions_kg_total']
        total_so2_emissions += metrics['so2_emissions_kg_total']

        times.append(time)
        altitudes.append(0)
        distances.append(distance)
        velocities.append(velocity)
        accelerations.append(acceleration)
        pressures.append(pressure)
        powers.append(2*power_kw * 1000)  # Convert kW to W
        fuel_consumptions.append(current_fuel_consumed)
        cumulative_fuel_consumptions.append(cumulative_fuel_consumed)
        carbon_emissions.append(metrics['carbon_emissions_kg_total'])
        cumulative_carbon_emissions.append(total_carbon_emissions)
        co_emissions.append(metrics['co_emissions_kg_total'])
        cumulative_co_emissions.append(total_co_emissions)
        nox_emissions.append(metrics['nox_emissions_kg_total'])
        cumulative_nox_emissions.append(total_nox_emissions)
        so2_emissions.append(metrics['so2_emissions_kg_total'])
        cumulative_so2_emissions.append(total_so2_emissions)
        weights.append(weight)

        time += time_step

    # Constant speed taxiing
    while time < initial_time + acceleration_time + taxi_duration:
        distance += velocity * time_step

        power_kw = idle_power_kw
        metrics = calculate_metrics(power_kw, time_step, spline_function, num_engines=num_engines)

        current_fuel_consumed = metrics['fuel_consumed_kg_total']
        cumulative_fuel_consumed += current_fuel_consumed
        weight -= current_fuel_consumed * 9.81

        total_carbon_emissions += metrics['carbon_emissions_kg_total']
        total_co_emissions += metrics['co_emissions_kg_total']
        total_nox_emissions += metrics['nox_emissions_kg_total']
        total_so2_emissions += metrics['so2_emissions_kg_total']

        times.append(time)
        distances.append(distance)
        velocities.append(velocity)
        accelerations.append(0)
        altitudes.append(0)
        pressures.append(pressure)
        powers.append(2*power_kw * 1000)  # Convert kW to W
        fuel_consumptions.append(current_fuel_consumed)
        cumulative_fuel_consumptions.append(cumulative_fuel_consumed)
        carbon_emissions.append(metrics['carbon_emissions_kg_total'])
        cumulative_carbon_emissions.append(total_carbon_emissions)
        co_emissions.append(metrics['co_emissions_kg_total'])
        cumulative_co_emissions.append(total_co_emissions)
        nox_emissions.append(metrics['nox_emissions_kg_total'])
        cumulative_nox_emissions.append(total_nox_emissions)
        so2_emissions.append(metrics['so2_emissions_kg_total'])
        cumulative_so2_emissions.append(total_so2_emissions)
        weights.append(weight)

        time += time_step

    # Decelerate to stop
    while velocity > 0 and time < initial_time + acceleration_time + taxi_duration + deceleration_time:
        velocity -= deceleration * time_step
        distance += max(velocity, 0) * time_step

        power_kw = idle_power_kw
        metrics = calculate_metrics(power_kw, time_step, spline_function, num_engines=num_engines)

        current_fuel_consumed = metrics['fuel_consumed_kg_total']
        cumulative_fuel_consumed += current_fuel_consumed
        weight -= current_fuel_consumed * 9.81

        total_carbon_emissions += metrics['carbon_emissions_kg_total']
        total_co_emissions += metrics['co_emissions_kg_total']
        total_nox_emissions += metrics['nox_emissions_kg_total']
        total_so2_emissions += metrics['so2_emissions_kg_total']

        times.append(time)
        distances.append(distance)
        velocities.append(max(velocity, 0))
        altitudes.append(0)
        pressures.append(pressure)
        accelerations.append(-deceleration)
        powers.append(2*power_kw * 1000)  # Convert kW to W
        fuel_consumptions.append(current_fuel_consumed)
        cumulative_fuel_consumptions.append(cumulative_fuel_consumed)
        carbon_emissions.append(metrics['carbon_emissions_kg_total'])
        cumulative_carbon_emissions.append(total_carbon_emissions)
        co_emissions.append(metrics['co_emissions_kg_total'])
        cumulative_co_emissions.append(total_co_emissions)
        nox_emissions.append(metrics['nox_emissions_kg_total'])
        cumulative_nox_emissions.append(total_nox_emissions)
        so2_emissions.append(metrics['so2_emissions_kg_total'])
        cumulative_so2_emissions.append(total_so2_emissions)
        weights.append(weight)

        time += time_step

    results = pd.DataFrame({
        'Time (s)': times,
        'Distance (m)': distances,
        'Velocity (m/s)': velocities,
        'Acceleration (m/s^2)': accelerations,
        'Power (W)': powers,
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
        'Altitude (m)': altitudes,
        'Weight (N)': weights,
        'True Airspeed (m/s)': velocities,
        'Groundspeed (m/s)': velocities,
        'Total Power (W)': powers
    })

    print(f"End Taxi Phase: Final Cumulative Fuel = {cumulative_fuel_consumed}")

    engine_power_kW_per_engine = idle_power_kw  # Adjust this if necessary

    # Plot results for checking
    plt.figure(figsize=(14, 8))

    plt.subplot(2, 2, 1)
    plt.plot(results['Time (s)'], results['Velocity (m/s)'], label='Velocity')
    plt.xlabel('Time (s)')
    plt.ylabel('Velocity (m/s)')
    plt.title('Velocity over Time')
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
    plt.plot(results['Time (s)'], results['Power (W)'], label='Power', color='green')
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

    return (
        results, 
        weights[-1], 
        time, 
        distance, 
        engine_power_kW_per_engine * 1000, 
        cumulative_fuel_consumed, 
        total_carbon_emissions, 
        total_co_emissions, 
        total_nox_emissions, 
        total_so2_emissions
    )
