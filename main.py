# # # # import pandas as pd
# # # # from run_simulation import run_all_phases, calculate_total_distance_excluding_cruise
# # # # from prints_and_plots import plot_results, print_totals

# # # # # Define aircraft-specific parameters
# # # # C_D0 = 0.02  # Zero-lift drag coefficient
# # # # k = 0.045  # Induced drag factor
# # # # S = 54.5  # Wing area in m²

# # # # # Aircraft take-off params
# # # # wing_area = 54.5  # Wing area in m²
# # # # mass = 16500  # kg
# # # # C_T = 0.15  # coefficient of Thrust
# # # # n = 20.2  # RPS
# # # # D = 3.96  # meters
# # # # C_D = 0.05  # example drag coefficient with landing gear
# # # # C_L_MAX = 1.8  # maximum lift coefficient for stall speed calculation
# # # # C_L_AVG = 0.7  # average lift coefficient for takeoff roll
# # # # mu = 0.02  # example coefficient of friction
# # # # propeller_efficiency = 0.80  # propeller efficiency during takeoff
# # # # idle_power_kw = 74.57  # kW per engine
# # # # max_power_kw = 1602  # kW per engine
# # # # initial_angle = 0  # degrees
# # # # final_angle = 10  # degrees
# # # # warmup_duration = 10  # seconds
# # # # time_step = 0.1  # time step for simulation

# # # # # Aircraft climb params
# # # # propeller_efficiency_C = 0.85
# # # # propeller_efficiency_Cr = 0.85

# # # # # Hybrid system parameters
# # # # gearbox_efficiency = 0.99
# # # # inverter_efficiency = 0.93
# # # # battery_capacity_kWh = 5  # Total capacity of one battery in kWh
# # # # usable_capacity_factor = 0.8  # 80% of the battery can be used
# # # # steady_state_motor_power_kW = 150  # Steady state motor power per motor
# # # # num_motors = 2  # Number of electric motors
# # # # num_engines = 2  # Number of engines

# # # # # Get user input for aircraft mass
# # # # mass = 16500


# # # # # Step 2: Adjust the cruise distance based on the total desired distance
# # # # total_flight_distance = 250 * 1000  # Example total flight distance in meters

# # # # # Parameters for the engine turn-on phase
# # # # engine_turn_on_params = {
# # # #     'idle_power_kw': idle_power_kw,
# # # #     'time_step': time_step,
# # # #     'turn_on_duration': 15,  # Example duration in seconds
# # # #     'initial_weight': mass  # kg
# # # # }

# # # # taxi_params = {
# # # #     'taxi_duration': 300,  # taxi duration in seconds
# # # #     'max_taxi_speed': 17.5,  # maximum taxi speed in knots
# # # #     'acceleration_time': 30,  # time to accelerate to taxi speed in seconds
# # # #     'deceleration_time': 30,  # time to decelerate from taxi speed in seconds
# # # #     'idle_power_kw': idle_power_kw,
# # # #     'time_step': time_step,
# # # #     'initial_weight': mass,  # initial weight in kg
# # # # }

# # # # # Add parameters for the take-off phase
# # # # takeoff_params = {
# # # #     'initial_altitude': 0,
# # # #     'C_T': C_T,
# # # #     'n': n,
# # # #     'D': D,
# # # #     'S': S,
# # # #     'C_D': C_D,
# # # #     'C_L_MAX': C_L_MAX,
# # # #     'C_L_AVG': C_L_AVG,
# # # #     'mu': mu,
# # # #     'propeller_efficiency': propeller_efficiency,
# # # #     'idle_power_kW': idle_power_kw,
# # # #     'max_power_kW': max_power_kw,
# # # #     'initial_angle': initial_angle,
# # # #     'final_angle': final_angle,
# # # #     'time_step': time_step,
# # # #     'gearbox_efficiency': gearbox_efficiency,
# # # #     'inverter_efficiency': inverter_efficiency,
# # # #     'battery_capacity_kWh': battery_capacity_kWh,
# # # #     'usable_capacity_factor': usable_capacity_factor,
# # # #     'warmup_duration': warmup_duration,
# # # #     'initial_weight': mass,  # kg
# # # #     'turn_on_duration': engine_turn_on_params['turn_on_duration'],  # Include turn-on duration
# # # #     'max_motor_power_kW': steady_state_motor_power_kW,
# # # #     'DOH': 0
# # # # }

# # # # # Parameters for the additional climb phase
# # # # take_off_C_params = {
# # # #     'initial_altitude': 0,  # in feet
# # # #     'target_altitude': 50,  # in feet
# # # #     'initial_airspeed': 120,  # in knots
# # # #     'final_airspeed': 120,  # in knots
# # # #     'roc': 1800,  # rate of climb in feet per minute
# # # #     'initial_weight': None,  # in kg, to be updated based on the end of takeoff phase
# # # #     'time_step': 0.001,  # in seconds
# # # #     'C_D0': C_D0,
# # # #     'k': k,
# # # #     'S': S,
# # # #     'num_motors': num_motors,
# # # #     'num_engines': num_engines,
# # # #     'gearbox_efficiency': gearbox_efficiency,
# # # #     'inverter_efficiency': inverter_efficiency,
# # # #     'battery_capacity_kWh': battery_capacity_kWh,
# # # #     'usable_capacity_factor': usable_capacity_factor,
# # # #     'max_power_kw': max_power_kw,
# # # #     'propeller_efficiency': propeller_efficiency_C,
# # # #     'idle_power_kw': idle_power_kw,
# # # #     'max_motor_power_kW': steady_state_motor_power_kW,
# # # #     'DOH': 0
# # # # }

# # # # # Parameters for the first phase of climb
# # # # phase1_params = {
# # # #     'initial_altitude': 50,  # in feet
# # # #     'target_altitude': 5000,  # in feet
# # # #     'initial_airspeed': 120,  # in knots
# # # #     'final_airspeed': 130,  # in knots
# # # #     'roc': 1800,  # rate of climb in feet per minute
# # # #     'initial_weight': None,  # in kg, to be updated based on the end of takeoff phase
# # # #     'time_step': 1,  # in seconds
# # # #     'C_D0': C_D0,
# # # #     'k': k,
# # # #     'S': S,
# # # #     'num_motors': num_motors,
# # # #     'num_engines': num_engines,
# # # #     'gearbox_efficiency': gearbox_efficiency,
# # # #     'inverter_efficiency': inverter_efficiency,
# # # #     'battery_capacity_kWh': battery_capacity_kWh,
# # # #     'usable_capacity_factor': usable_capacity_factor,
# # # #     'steady_state_motor_power_kW': steady_state_motor_power_kW,
# # # #     'max_power_kw': max_power_kw,
# # # #     'idle_power_kw': idle_power_kw,
# # # #     'propeller_efficiency': propeller_efficiency_C,
# # # #     'max_motor_power_kW': steady_state_motor_power_kW,
# # # #     'DOH': 0
# # # # }

# # # # # Parameters for the new climb phase between phase1 and phase2
# # # # between_1_2_climb = {
# # # #     'initial_altitude': 5000,  # in feet (starting from the end of phase 1)
# # # #     'initial_airspeed': 130,  # in knots (starting from the end of phase 1)
# # # #     'final_airspeed': 140,  # in knots
# # # #     'initial_roc': 1800,  # initial rate of climb in feet per minute
# # # #     'final_roc': 1500,  # final rate of climb in feet per minute
# # # #     'roc_transition_duration': 100,  # duration for ROC transition in seconds
# # # #     'initial_weight': None,  # to be updated based on the end of phase 1
# # # #     'time_step': 1,  # in seconds
# # # #     'C_D0': C_D0,
# # # #     'k': k,
# # # #     'S': S,
# # # #     'num_motors': num_motors,
# # # #     'num_engines': num_engines,
# # # #     'gearbox_efficiency': gearbox_efficiency,
# # # #     'inverter_efficiency': inverter_efficiency,
# # # #     'battery_capacity_kWh': battery_capacity_kWh,
# # # #     'usable_capacity_factor': usable_capacity_factor,
# # # #     'steady_state_motor_power_kW': steady_state_motor_power_kW,
# # # #     'max_power_kw': max_power_kw,
# # # #     'idle_power_kw': idle_power_kw,
# # # #     'propeller_efficiency': propeller_efficiency_C,
# # # #     'idle_power_kw': idle_power_kw,
# # # #     'max_motor_power_kW': steady_state_motor_power_kW,
# # # #     'DOH': 0
# # # # }

# # # # # Parameters for the second phase of climb
# # # # phase2_params = {
# # # #     'initial_altitude': None,  # will be updated after between_1_2_climb
# # # #     'target_altitude': 15000,  # in feet
# # # #     'initial_airspeed': 130,  # in knots
# # # #     'final_airspeed': 200,  # in knots
# # # #     'roc': 1500,  # rate of climb in feet per minute
# # # #     'initial_weight': None,  # to be updated based on the end of previous phase
# # # #     'time_step': 1,  # in seconds
# # # #     'C_D0': C_D0,
# # # #     'k': k,
# # # #     'S': S,
# # # #     'num_motors': num_motors,
# # # #     'num_engines': num_engines,
# # # #     'gearbox_efficiency': gearbox_efficiency,
# # # #     'inverter_efficiency': inverter_efficiency,
# # # #     'battery_capacity_kWh': battery_capacity_kWh,
# # # #     'usable_capacity_factor': usable_capacity_factor,
# # # #     'steady_state_motor_power_kW': steady_state_motor_power_kW,
# # # #     'max_power_kw': max_power_kw,
# # # #     'idle_power_kw': idle_power_kw,
# # # #     'propeller_efficiency': propeller_efficiency_C,
# # # #     'max_motor_power_kW': steady_state_motor_power_kW,
# # # #     'DOH': 0
# # # # }
# # # # between_2_3_climb = {
# # # #     'initial_altitude': 15000,  # in feet (starting from the end of phase 1)
# # # #     'initial_airspeed': 200,  # in knots (starting from the end of phase 1)
# # # #     'final_airspeed': 200,  # in knots
# # # #     'initial_roc': 1500,  # initial rate of climb in feet per minute
# # # #     'final_roc': 1000,  # final rate of climb in feet per minute
# # # #     'roc_transition_duration': 100,  # duration for ROC transition in seconds
# # # #     'initial_weight': None,  # to be updated based on the end of phase 1
# # # #     'time_step': 1,  # in seconds
# # # #     'C_D0': C_D0,
# # # #     'k': k,
# # # #     'S': S,
# # # #     'num_motors': num_motors,
# # # #     'num_engines': num_engines,
# # # #     'gearbox_efficiency': gearbox_efficiency,
# # # #     'inverter_efficiency': inverter_efficiency,
# # # #     'battery_capacity_kWh': battery_capacity_kWh,
# # # #     'usable_capacity_factor': usable_capacity_factor,
# # # #     'steady_state_motor_power_kW': steady_state_motor_power_kW,
# # # #     'max_power_kw': max_power_kw,
# # # #     'idle_power_kw': idle_power_kw,
# # # #     'propeller_efficiency': propeller_efficiency_C,
# # # #     'idle_power_kw': idle_power_kw,
# # # #     'max_motor_power_kW': steady_state_motor_power_kW,
# # # #     'DOH': 0

# # # # }

# # # # # Parameters for the third phase of climb
# # # # phase3_params = {
# # # #     'initial_altitude': None,  # in feet (starting from the end of phase 2)
# # # #     'target_altitude': 24000,  # in feet
# # # #     'initial_airspeed': 200,  # in knots (starting from the end of phase 2)
# # # #     'final_airspeed': 200,  # in knots
# # # #     'roc': 1000,  # rate of climb in feet per minute
# # # #     'initial_weight': None,  # to be updated based on the end of phase 2
# # # #     'time_step': 1,  # in seconds
# # # #     'C_D0': C_D0,
# # # #     'k': k,
# # # #     'S': S,
# # # #     'num_motors': num_motors,
# # # #     'num_engines': num_engines,
# # # #     'gearbox_efficiency': gearbox_efficiency,
# # # #     'inverter_efficiency': inverter_efficiency,
# # # #     'battery_capacity_kWh': battery_capacity_kWh,
# # # #     'usable_capacity_factor': usable_capacity_factor,
# # # #     'steady_state_motor_power_kW': steady_state_motor_power_kW,
# # # #     'max_power_kw': max_power_kw,
# # # #     'idle_power_kw': idle_power_kw,
# # # #     'propeller_efficiency': propeller_efficiency_C,
# # # #     'max_motor_power_kW': steady_state_motor_power_kW,
# # # #     'DOH': 0
# # # # }

# # # # # Parameters for the cruise phase
# # # # cruise_params = {
# # # #     'initial_altitude': 24000,  # in feet
# # # #     'initial_airspeed': 200,  # in knots
# # # #     'final_airspeed': 250,  # in knots
# # # #     'acceleration_duration': 180,  # in seconds 
# # # #     'cruise_distance': None,  # in km
# # # #     'time_step': 1,  # in seconds
# # # #     'C_D0': C_D0,
# # # #     'k': k,
# # # #     'S': S,
# # # #     'num_motors': num_motors,
# # # #     'num_engines': num_engines,
# # # #     'gearbox_efficiency': gearbox_efficiency,
# # # #     'inverter_efficiency': inverter_efficiency,
# # # #     'battery_capacity_kWh': battery_capacity_kWh,
# # # #     'usable_capacity_factor': usable_capacity_factor,
# # # #     'steady_state_motor_power_kW': steady_state_motor_power_kW,
# # # #     'max_power_kw': max_power_kw,
# # # #     'idle_power_kw': idle_power_kw,
# # # #     'propeller_efficiency': propeller_efficiency_Cr,
# # # #     'max_motor_power_kW': steady_state_motor_power_kW,
# # # #     'DOH': 0
# # # # }

# # # # # Parameters for the descent phase
# # # # descent_params = {
# # # #     'initial_altitude': 24000,  # in feet
# # # #     'target_altitude': 10000,  # in feet
# # # #     'airspeed': 250,  # in knots
# # # #     'rate_of_descent': 1500,  # in feet per minute
# # # #     'time_step': 1,  # in seconds
# # # #     'C_D0': C_D0,
# # # #     'k': k,
# # # #     'S': S,
# # # #     'num_motors': num_motors,
# # # #     'num_engines': num_engines,
# # # #     'gearbox_efficiency': gearbox_efficiency,
# # # #     'inverter_efficiency': inverter_efficiency,
# # # #     'battery_capacity_kWh': battery_capacity_kWh,
# # # #     'usable_capacity_factor': usable_capacity_factor,
# # # #     'steady_state_motor_power_kW': steady_state_motor_power_kW,
# # # #     'max_power_kw': max_power_kw,
# # # #     'idle_power_kw': idle_power_kw
# # # # }

# # # # # Parameters for the approach and landing phase
# # # # approach_and_landing_params = {
# # # #     'initial_altitude': 10000,  # in feet (start of approach)
# # # #     'target_altitude': 0,  # in feet (ground level)
# # # #     'initial_airspeed': 250,  # in knots (initial approach speed)
# # # #     'final_airspeed': 100,  # in knots (final approach speed before landing)
# # # #     'rate_of_descent': 1500,  # in feet per minute
# # # #     'landing_airspeed': 100,  # in knots (landing speed)
# # # #     'landing_distance': 900,  # in meters
# # # #     'time_step': 1,  # in seconds
# # # #     'C_D0': C_D0,
# # # #     'k': k,
# # # #     'S': S,
# # # #     'num_motors': num_motors,
# # # #     'num_engines': num_engines,
# # # #     'gearbox_efficiency': gearbox_efficiency,
# # # #     'inverter_efficiency': inverter_efficiency,
# # # #     'battery_capacity_kWh': battery_capacity_kWh,
# # # #     'usable_capacity_factor': usable_capacity_factor,
# # # #     'steady_state_motor_power_kW': steady_state_motor_power_kW,
# # # #     'max_power_kw': max_power_kw,
# # # #     'idle_power_kw': idle_power_kw
# # # # }

# # # # taxi_params2 = {
# # # #     'taxi_duration': 300,  # taxi duration in seconds
# # # #     'max_taxi_speed': 17.5,  # maximum taxi speed in knots
# # # #     'acceleration_time': 30,  # time to accelerate to taxi speed in seconds
# # # #     'deceleration_time': 30,  # time to decelerate from taxi speed in seconds
# # # #     'idle_power_kw': idle_power_kw,
# # # #     'time_step': time_step,
# # # #     'initial_weight': mass,  # initial weight in kg
# # # # }

# # # # # Step 1: Calculate the total distance excluding the cruise phase
# # # # total_distance_excluding_cruise = calculate_total_distance_excluding_cruise(
# # # #     engine_turn_on_params, taxi_params, takeoff_params, take_off_C_params, 
# # # #     phase1_params, between_1_2_climb, phase2_params, between_2_3_climb, 
# # # #     phase3_params, descent_params, approach_and_landing_params, taxi_params2
# # # # )

# # # # # Step 2: Adjust the cruise distance based on the total desired distance
# # # # cruise_distance = (total_flight_distance - total_distance_excluding_cruise) / 1000  # Convert to km

# # # # # Update cruise_params with the calculated cruise distance
# # # # cruise_params['cruise_distance'] = cruise_distance

# # # # cruise_distance = (total_flight_distance - total_distance_excluding_cruise) / 1000  # Convert to km

# # # # # Update cruise_params with the calculated cruise distance
# # # # cruise_params['cruise_distance'] = cruise_distance
# # # # print(f'cruise distance {cruise_distance:2f}')

# # # # # Run the simulation for all phases with the updated cruise distance
# combined_results = run_all_phases(
#     engine_turn_on_params, taxi_params, takeoff_params, take_off_C_params, 
#     phase1_params, between_1_2_climb, phase2_params, between_2_3_climb, 
#     phase3_params, cruise_params, descent_params, approach_and_landing_params, 
#     taxi_params2, num_engines
# )

# # # # # Print and plot results
# # # # print_totals(combined_results)
# # # # plot_results(combined_results)

# # import pandas as pd
# # import numpy as np
# # import random
# # from deap import base, creator, tools, algorithms
# # from run_simulation import run_all_phases, calculate_total_distance_excluding_cruise
# # from prints_and_plots import plot_results, print_totals

# # # Define aircraft-specific parameters
# # C_D0 = 0.02  # Zero-lift drag coefficient
# # k = 0.045  # Induced drag factor
# # S = 54.5  # Wing area in m²

# # # Aircraft take-off params
# # wing_area = 54.5  # Wing area in m²
# # mass = 16500  # kg
# # C_T = 0.15  # coefficient of Thrust
# # n = 20.2  # RPS
# # D = 3.96  # meters
# # C_D = 0.05  # example drag coefficient with landing gear
# # C_L_MAX = 1.8  # maximum lift coefficient for stall speed calculation
# # C_L_AVG = 0.7  # average lift coefficient for takeoff roll
# # mu = 0.02  # example coefficient of friction
# # propeller_efficiency = 0.80  # propeller efficiency during takeoff
# # idle_power_kw = 74.57  # kW per engine
# # max_power_kw = 1602  # kW per engine
# # initial_angle = 0  # degrees
# # final_angle = 10  # degrees
# # warmup_duration = 10  # seconds
# # time_step = 0.1  # time step for simulation

# # # Aircraft climb params
# # propeller_efficiency_C = 0.85
# # propeller_efficiency_Cr = 0.85

# # # Hybrid system parameters
# # gearbox_efficiency = 0.99
# # inverter_efficiency = 0.93
# # battery_capacity_kWh = 5  # Total capacity of one battery in kWh
# # usable_capacity_factor = 0.8  # 80% of the battery can be used
# # steady_state_motor_power_kW = 150  # Steady state motor power per motor
# # num_motors = 2  # Number of electric motors
# # num_engines = 2  # Number of engines

# # # Genetic Algorithm parameters
# # POP_SIZE = 50
# # GENS = 40
# # MUTPB = 0.2
# # CXPB = 0.5

# # # Define the problem space
# # ALT_MIN = 10000  # Minimum altitude for climb phases (example value)
# # ALT_MAX = 18000  # Maximum altitude for climb phases (example value)

# # # Define climb parameters (rate of climb and initial weights for each phase)
# # roc1 = 1800  # Rate of climb in feet per minute for phase 1
# # roc2 = 1500  # Rate of climb in feet per minute for phase 2
# # roc3 = 1000  # Rate of climb in feet per minute for phase 3
# # initial_weight = mass  # Initial weight of the aircraft

# # engine_turn_on_params = {
# #     'idle_power_kw': idle_power_kw,
# #     'time_step': time_step,
# #     'turn_on_duration': 15,  # Example duration in seconds
# #     'initial_weight': mass  # kg
# # }

# # taxi_params = {
# #     'taxi_duration': 300,  # taxi duration in seconds
# #     'max_taxi_speed': 17.5,  # maximum taxi speed in knots
# #     'acceleration_time': 30,  # time to accelerate to taxi speed in seconds
# #     'deceleration_time': 30,  # time to decelerate from taxi speed in seconds
# #     'idle_power_kw': idle_power_kw,
# #     'time_step': time_step,
# #     'initial_weight': mass,  # initial weight in kg
# # }

# # # Add parameters for the take-off phase
# # takeoff_params = {
# #     'initial_altitude': 0,
# #     'C_T': C_T,
# #     'n': n,
# #     'D': D,
# #     'S': S,
# #     'C_D': C_D,
# #     'C_L_MAX': C_L_MAX,
# #     'C_L_AVG': C_L_AVG,
# #     'mu': mu,
# #     'propeller_efficiency': propeller_efficiency,
# #     'idle_power_kW': idle_power_kw,
# #     'max_power_kW': max_power_kw,
# #     'initial_angle': initial_angle,
# #     'final_angle': final_angle,
# #     'time_step': time_step,
# #     'gearbox_efficiency': gearbox_efficiency,
# #     'inverter_efficiency': inverter_efficiency,
# #     'battery_capacity_kWh': battery_capacity_kWh,
# #     'usable_capacity_factor': usable_capacity_factor,
# #     'warmup_duration': warmup_duration,
# #     'initial_weight': mass,  # kg
# #     'turn_on_duration': engine_turn_on_params['turn_on_duration'],  # Include turn-on duration
# #     'max_motor_power_kW': steady_state_motor_power_kW,
# #     'DOH': 0
# # }

# # # Parameters for the additional climb phase
# # take_off_C_params = {
# #     'initial_altitude': 0,  # in feet
# #     'target_altitude': 50,  # in feet
# #     'initial_airspeed': 120,  # in knots
# #     'final_airspeed': 120,  # in knots
# #     'roc': 1800,  # rate of climb in feet per minute
# #     'initial_weight': None,  # in kg, to be updated based on the end of takeoff phase
# #     'time_step': 0.001,  # in seconds
# #     'C_D0': C_D0,
# #     'k': k,
# #     'S': S,
# #     'num_motors': num_motors,
# #     'num_engines': num_engines,
# #     'gearbox_efficiency': gearbox_efficiency,
# #     'inverter_efficiency': inverter_efficiency,
# #     'battery_capacity_kWh': battery_capacity_kWh,
# #     'usable_capacity_factor': usable_capacity_factor,
# #     'max_power_kw': max_power_kw,
# #     'propeller_efficiency': propeller_efficiency_C,
# #     'idle_power_kw': idle_power_kw,
# #     'max_motor_power_kW': steady_state_motor_power_kW,
# #     'DOH': 0
# # }


# # # Initialize phase parameters
# # phase1_params = {
# #     'initial_altitude': 50,  # in feet
# #     'target_altitude': 5000,  # in feet
# #     'initial_airspeed': 120,  # in knots
# #     'final_airspeed': 130,  # in knots
# #     'roc': roc1,  # rate of climb in feet per minute
# #     'initial_weight': None,  # in kg, to be updated based on the end of takeoff phase
# #     'time_step': 1,  # in seconds
# #     'C_D0': C_D0,
# #     'k': k,
# #     'S': S,
# #     'num_motors': num_motors,
# #     'num_engines': num_engines,
# #     'gearbox_efficiency': gearbox_efficiency,
# #     'inverter_efficiency': inverter_efficiency,
# #     'battery_capacity_kWh': battery_capacity_kWh,
# #     'usable_capacity_factor': usable_capacity_factor,
# #     'steady_state_motor_power_kW': steady_state_motor_power_kW,
# #     'max_power_kw': max_power_kw,
# #     'idle_power_kw': idle_power_kw,
# #     'propeller_efficiency': propeller_efficiency_C,
# #     'max_motor_power_kW': steady_state_motor_power_kW,
# #     'DOH': 0
# # }

# # between_1_2_climb = {
# #     'initial_altitude': 5000,  # in feet (starting from the end of phase 1)
# #     'initial_airspeed': 130,  # in knots (starting from the end of phase 1)
# #     'final_airspeed': 140,  # in knots
# #     'initial_roc': roc1,  # initial rate of climb in feet per minute
# #     'final_roc': roc2,  # final rate of climb in feet per minute
# #     'roc_transition_duration': 100,  # duration for ROC transition in seconds
# #     'initial_weight': None,  # to be updated based on the end of phase 1
# #     'time_step': 1,  # in seconds
# #     'C_D0': C_D0,
# #     'k': k,
# #     'S': S,
# #     'num_motors': num_motors,
# #     'num_engines': num_engines,
# #     'gearbox_efficiency': gearbox_efficiency,
# #     'inverter_efficiency': inverter_efficiency,
# #     'battery_capacity_kWh': battery_capacity_kWh,
# #     'usable_capacity_factor': usable_capacity_factor,
# #     'steady_state_motor_power_kW': steady_state_motor_power_kW,
# #     'max_power_kw': max_power_kw,
# #     'idle_power_kw': idle_power_kw,
# #     'propeller_efficiency': propeller_efficiency_C,
# #     'idle_power_kw': idle_power_kw,
# #     'max_motor_power_kW': steady_state_motor_power_kW,
# #     'DOH': 0
# # }

# # phase2_params = {
# #     'initial_altitude': None,  # will be updated after between_1_2_climb
# #     'target_altitude': 15000,  # in feet
# #     'initial_airspeed': 130,  # in knots
# #     'final_airspeed': 200,  # in knots
# #     'roc': roc2,  # rate of climb in feet per minute
# #     'initial_weight': None,  # to be updated based on the end of previous phase
# #     'time_step': 1,  # in seconds
# #     'C_D0': C_D0,
# #     'k': k,
# #     'S': S,
# #     'num_motors': num_motors,
# #     'num_engines': num_engines,
# #     'gearbox_efficiency': gearbox_efficiency,
# #     'inverter_efficiency': inverter_efficiency,
# #     'battery_capacity_kWh': battery_capacity_kWh,
# #     'usable_capacity_factor': usable_capacity_factor,
# #     'steady_state_motor_power_kW': steady_state_motor_power_kW,
# #     'max_power_kw': max_power_kw,
# #     'idle_power_kw': idle_power_kw,
# #     'propeller_efficiency': propeller_efficiency_C,
# #     'max_motor_power_kW': steady_state_motor_power_kW,
# #     'DOH': 0
# # }

# # between_2_3_climb = {
# #     'initial_altitude': 15000,  # in feet (starting from the end of phase 1)
# #     'initial_airspeed': 200,  # in knots (starting from the end of phase 1)
# #     'final_airspeed': 200,  # in knots
# #     'initial_roc': roc2,  # initial rate of climb in feet per minute
# #     'final_roc': roc3,  # final rate of climb in feet per minute
# #     'roc_transition_duration': 100,  # duration for ROC transition in seconds
# #     'initial_weight': None,  # to be updated based on the end of phase 1
# #     'time_step': 1,  # in seconds
# #     'C_D0': C_D0,
# #     'k': k,
# #     'S': S,
# #     'num_motors': num_motors,
# #     'num_engines': num_engines,
# #     'gearbox_efficiency': gearbox_efficiency,
# #     'inverter_efficiency': inverter_efficiency,
# #     'battery_capacity_kWh': battery_capacity_kWh,
# #     'usable_capacity_factor': usable_capacity_factor,
# #     'steady_state_motor_power_kW': steady_state_motor_power_kW,
# #     'max_power_kw': max_power_kw,
# #     'idle_power_kw': idle_power_kw,
# #     'propeller_efficiency': propeller_efficiency_C,
# #     'idle_power_kw': idle_power_kw,
# #     'max_motor_power_kW': steady_state_motor_power_kW,
# #     'DOH': 0
# # }

# # phase3_params = {
# #     'initial_altitude': None,  # in feet (starting from the end of phase 2)
# #     'target_altitude': 24000,  # in feet
# #     'initial_airspeed': 200,  # in knots (starting from the end of phase 2)
# #     'final_airspeed': 200,  # in knots
# #     'roc': roc3,  # rate of climb in feet per minute
# #     'initial_weight': None,  # to be updated based on the end of phase 2
# #     'time_step': 1,  # in seconds
# #     'C_D0': C_D0,
# #     'k': k,
# #     'S': S,
# #     'num_motors': num_motors,
# #     'num_engines': num_engines,
# #     'gearbox_efficiency': gearbox_efficiency,
# #     'inverter_efficiency': inverter_efficiency,
# #     'battery_capacity_kWh': battery_capacity_kWh,
# #     'usable_capacity_factor': usable_capacity_factor,
# #     'steady_state_motor_power_kW': steady_state_motor_power_kW,
# #     'max_power_kw': max_power_kw,
# #     'idle_power_kw': idle_power_kw,
# #     'propeller_efficiency': propeller_efficiency_C,
# #     'max_motor_power_kW': steady_state_motor_power_kW,
# #     'DOH': 0
# # }

# # cruise_params = {
# #     'initial_altitude': 24000,  # in feet
# #     'initial_airspeed': 200,  # in knots
# #     'final_airspeed': 250,  # in knots
# #     'acceleration_duration': 180,  # in seconds 
# #     'cruise_distance': None,  # in km
# #     'time_step': 1,  # in seconds
# #     'C_D0': C_D0,
# #     'k': k,
# #     'S': S,
# #     'num_motors': num_motors,
# #     'num_engines': num_engines,
# #     'gearbox_efficiency': gearbox_efficiency,
# #     'inverter_efficiency': inverter_efficiency,
# #     'battery_capacity_kWh': battery_capacity_kWh,
# #     'usable_capacity_factor': usable_capacity_factor,
# #     'steady_state_motor_power_kW': steady_state_motor_power_kW,
# #     'max_power_kw': max_power_kw,
# #     'idle_power_kw': idle_power_kw,
# #     'propeller_efficiency': propeller_efficiency_Cr,
# #     'max_motor_power_kW': steady_state_motor_power_kW,
# #     'DOH': 0
# # }

# # descent_params = {
# #     'initial_altitude': 24000,  # in feet
# #     'target_altitude': 10000,  # in feet
# #     'airspeed': 250,  # in knots
# #     'rate_of_descent': 1500,  # in feet per minute
# #     'time_step': 1,  # in seconds
# #     'C_D0': C_D0,
# #     'k': k,
# #     'S': S,
# #     'num_motors': num_motors,
# #     'num_engines': num_engines,
# #     'gearbox_efficiency': gearbox_efficiency,
# #     'inverter_efficiency': inverter_efficiency,
# #     'battery_capacity_kWh': battery_capacity_kWh,
# #     'usable_capacity_factor': usable_capacity_factor,
# #     'steady_state_motor_power_kW': steady_state_motor_power_kW,
# #     'max_power_kw': max_power_kw,
# #     'idle_power_kw': idle_power_kw
# # }

# # approach_and_landing_params = {
# #     'initial_altitude': 10000,  # in feet (start of approach)
# #     'target_altitude': 0,  # in feet (ground level)
# #     'initial_airspeed': 250,  # in knots (initial approach speed)
# #     'final_airspeed': 100,  # in knots (final approach speed before landing)
# #     'rate_of_descent': 1500,  # in feet per minute
# #     'landing_airspeed': 100,  # in knots (landing speed)
# #     'landing_distance': 900,  # in meters
# #     'time_step': 1,  # in seconds
# #     'C_D0': C_D0,
# #     'k': k,
# #     'S': S,
# #     'num_motors': num_motors,
# #     'num_engines': num_engines,
# #     'gearbox_efficiency': gearbox_efficiency,
# #     'inverter_efficiency': inverter_efficiency,
# #     'battery_capacity_kWh': battery_capacity_kWh,
# #     'usable_capacity_factor': usable_capacity_factor,
# #     'steady_state_motor_power_kW': steady_state_motor_power_kW,
# #     'max_power_kw': max_power_kw,
# #     'idle_power_kw': idle_power_kw
# # }

# # taxi_params2 = {
# #     'taxi_duration': 300,  # taxi duration in seconds
# #     'max_taxi_speed': 17.5,  # maximum taxi speed in knots
# #     'acceleration_time': 30,  # time to accelerate to taxi speed in seconds
# #     'deceleration_time': 30,  # time to decelerate from taxi speed in seconds
# #     'idle_power_kw': idle_power_kw,
# #     'time_step': time_step,
# #     'initial_weight': mass,  # initial weight in kg
# # }

# # # Create the fitness and individual classes
# # creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
# # creator.create("Individual", list, fitness=creator.FitnessMin)

# # toolbox = base.Toolbox()
# # toolbox.register("attr_alt", np.random.uniform, ALT_MIN, ALT_MAX)
# # toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_alt, n=5)
# # toolbox.register("population", tools.initRepeat, list, toolbox.individual)

# # def eval_individual(individual):
# #     # Ensure altitude order constraint
# #     individual.sort()

# #     phase1_params['target_altitude'] = individual[0]
# #     between_1_2_climb['target_altitude'] = individual[1]
# #     phase2_params['target_altitude'] = individual[2]
# #     between_2_3_climb['target_altitude'] = individual[3]
# #     phase3_params['target_altitude'] = individual[4]

# #     # Calculate the total distance excluding the cruise phase
# #     total_distance_excluding_cruise = calculate_total_distance_excluding_cruise(
# #         engine_turn_on_params, taxi_params, takeoff_params, take_off_C_params, 
# #         phase1_params, between_1_2_climb, phase2_params, between_2_3_climb, 
# #         phase3_params, descent_params, approach_and_landing_params, taxi_params2
# #     )

# #     # Adjust the cruise distance based on the total desired distance
# #     cruise_distance = (total_flight_distance - total_distance_excluding_cruise) / 1000  # Convert to km
# #     cruise_params['cruise_distance'] = cruise_distance

# #     # Run the simulation for all phases with the updated cruise distance
# #     combined_results = run_all_phases(
# #         engine_turn_on_params, taxi_params, takeoff_params, take_off_C_params, 
# #         phase1_params, between_1_2_climb, phase2_params, between_2_3_climb, 
# #         phase3_params, cruise_params, descent_params, approach_and_landing_params, 
# #         taxi_params2, num_engines
# #     )

# #     total_fuel_consumed = combined_results['Cumulative Fuel Consumption (kg)'].iloc[-1]
# #     return (total_fuel_consumed,)

# # toolbox.register("evaluate", eval_individual)
# # toolbox.register("mate", tools.cxBlend, alpha=0.5)
# # toolbox.register("mutate", tools.mutGaussian, mu=0, sigma=1, indpb=0.2)
# # toolbox.register("select", tools.selTournament, tournsize=3)

# # def constrain_altitudes(individual):
# #     individual.sort()
# #     return individual

# # def optimize_for_distance(total_flight_distance_km):
# #     global total_flight_distance
# #     total_flight_distance = total_flight_distance_km * 1000  # Convert to meters
# #     population = toolbox.population(n=POP_SIZE)
# #     halloffame = tools.HallOfFame(1)
# #     stats = tools.Statistics(lambda ind: ind.fitness.values)
# #     stats.register("avg", np.mean)
# #     stats.register("std", np.std)
# #     stats.register("min", np.min)
# #     stats.register("max", np.max)

# #     # Apply constraints
# #     for ind in population:
# #         constrain_altitudes(ind)

# #     population, logbook = algorithms.eaSimple(population, toolbox, cxpb=CXPB, mutpb=MUTPB, ngen=GENS, 
# #                         stats=stats, halloffame=halloffame, verbose=True)

# #     best = halloffame[0]
# #     print(f"Best individual for {total_flight_distance_km} km:", best)
# #     print("Best fitness:", best.fitness.values)

# #     # Update the climb parameters with the best individual
# #     phase1_params['target_altitude'] = best[0]
# #     between_1_2_climb['target_altitude'] = best[1]
# #     phase2_params['target_altitude'] = best[2]
# #     between_2_3_climb['target_altitude'] = best[3]
# #     phase3_params['target_altitude'] = best[4]

# #     # Run the simulation with the best individual
# #     total_distance_excluding_cruise = calculate_total_distance_excluding_cruise(
# #         engine_turn_on_params, taxi_params, takeoff_params, take_off_C_params, 
# #         phase1_params, between_1_2_climb, phase2_params, between_2_3_climb, 
# #         phase3_params, descent_params, approach_and_landing_params, taxi_params2
# #     )

# #     cruise_distance = (total_flight_distance - total_distance_excluding_cruise) / 1000
# #     cruise_params['cruise_distance'] = cruise_distance

# #     combined_results = run_all_phases(
# #         engine_turn_on_params, taxi_params, takeoff_params, take_off_C_params, 
# #         phase1_params, between_1_2_climb, phase2_params, between_2_3_climb, 
# #         phase3_params, cruise_params, descent_params, approach_and_landing_params, 
# #         taxi_params2, num_engines
# #     )

# #     # Print and plot results
# #     print_totals(combined_results)
# #     plot_results(combined_results)

# #     # Save results to CSV
# #     combined_results.to_csv(f'results_{total_flight_distance_km}_km.csv', index=False)
# #     return logbook

# # if __name__ == "__main__":
# #     for total_flight_distance_km in range(200, 201, 100):  # Debugging for 200 km
# #         print(f"Optimizing for total flight distance: {total_flight_distance_km} km")
# #         logbook = optimize_for_distance(total_flight_distance_km)


# import pandas as pd
# import numpy as np
# import random
# from deap import base, creator, tools, algorithms
# from run_simulation import run_all_phases, calculate_total_distance_excluding_cruise
# from prints_and_plots import plot_results, print_totals

# # Define aircraft-specific parameters
# C_D0 = 0.02  # Zero-lift drag coefficient
# k = 0.045  # Induced drag factor
# S = 54.5  # Wing area in m²

# # Aircraft take-off params
# wing_area = 54.5  # Wing area in m²
# mass = 16500  # kg
# C_T = 0.15  # coefficient of Thrust
# n = 20.2  # RPS
# D = 3.96  # meters
# C_D = 0.05  # example drag coefficient with landing gear
# C_L_MAX = 1.8  # maximum lift coefficient for stall speed calculation
# C_L_AVG = 0.7  # average lift coefficient for takeoff roll
# mu = 0.02  # example coefficient of friction
# propeller_efficiency = 0.80  # propeller efficiency during takeoff
# idle_power_kw = 74.57  # kW per engine
# max_power_kw = 1602  # kW per engine
# initial_angle = 0  # degrees
# final_angle = 10  # degrees
# warmup_duration = 10  # seconds
# time_step = 0.1  # time step for simulation

# # Aircraft climb params
# propeller_efficiency_C = 0.85
# propeller_efficiency_Cr = 0.85

# # Hybrid system parameters
# gearbox_efficiency = 0.99
# inverter_efficiency = 0.93
# battery_capacity_kWh = 5  # Total capacity of one battery in kWh
# usable_capacity_factor = 0.8  # 80% of the battery can be used
# steady_state_motor_power_kW = 150  # Steady state motor power per motor
# num_motors = 2  # Number of electric motors
# num_engines = 2  # Number of engines

# # Genetic Algorithm parameters
# POP_SIZE = 50
# GENS = 40
# MUTPB = 0.2
# CXPB = 0.5
# EARLY_STOPPING_THRESHOLD = 10  # Number of generations with no improvement to trigger early stopping

# # Define the problem space
# ALT_MIN = 10000  # Minimum altitude for climb phases (example value)
# ALT_MAX = 22000  # Maximum altitude for climb phases (example value)

# # Define climb parameters (rate of climb and initial weights for each phase)
# roc1 = 1800  # Rate of climb in feet per minute for phase 1
# roc2 = 1500  # Rate of climb in feet per minute for phase 2
# roc3 = 1000  # Rate of climb in feet per minute for phase 3
# initial_weight = mass  # Initial weight of the aircraft

# engine_turn_on_params = {
#     'idle_power_kw': idle_power_kw,
#     'time_step': time_step,
#     'turn_on_duration': 15,  # Example duration in seconds
#     'initial_weight': mass  # kg
# }

# taxi_params = {
#     'taxi_duration': 300,  # taxi duration in seconds
#     'max_taxi_speed': 17.5,  # maximum taxi speed in knots
#     'acceleration_time': 30,  # time to accelerate to taxi speed in seconds
#     'deceleration_time': 30,  # time to decelerate from taxi speed in seconds
#     'idle_power_kw': idle_power_kw,
#     'time_step': time_step,
#     'initial_weight': mass,  # initial weight in kg
# }

# # Add parameters for the take-off phase
# takeoff_params = {
#     'initial_altitude': 0,
#     'C_T': C_T,
#     'n': n,
#     'D': D,
#     'S': S,
#     'C_D': C_D,
#     'C_L_MAX': C_L_MAX,
#     'C_L_AVG': C_L_AVG,
#     'mu': mu,
#     'propeller_efficiency': propeller_efficiency,
#     'idle_power_kW': idle_power_kw,
#     'max_power_kW': max_power_kw,
#     'initial_angle': initial_angle,
#     'final_angle': final_angle,
#     'time_step': time_step,
#     'gearbox_efficiency': gearbox_efficiency,
#     'inverter_efficiency': inverter_efficiency,
#     'battery_capacity_kWh': battery_capacity_kWh,
#     'usable_capacity_factor': usable_capacity_factor,
#     'warmup_duration': warmup_duration,
#     'initial_weight': mass,  # kg
#     'turn_on_duration': engine_turn_on_params['turn_on_duration'],  # Include turn-on duration
#     'max_motor_power_kW': steady_state_motor_power_kW,
#     'DOH': 0
# }

# # Parameters for the additional climb phase
# take_off_C_params = {
#     'initial_altitude': 0,  # in feet
#     'target_altitude': 50,  # in feet
#     'initial_airspeed': 120,  # in knots
#     'final_airspeed': 120,  # in knots
#     'roc': 1800,  # rate of climb in feet per minute
#     'initial_weight': None,  # in kg, to be updated based on the end of takeoff phase
#     'time_step': 0.001,  # in seconds
#     'C_D0': C_D0,
#     'k': k,
#     'S': S,
#     'num_motors': num_motors,
#     'num_engines': num_engines,
#     'gearbox_efficiency': gearbox_efficiency,
#     'inverter_efficiency': inverter_efficiency,
#     'battery_capacity_kWh': battery_capacity_kWh,
#     'usable_capacity_factor': usable_capacity_factor,
#     'max_power_kw': max_power_kw,
#     'propeller_efficiency': propeller_efficiency_C,
#     'idle_power_kw': idle_power_kw,
#     'max_motor_power_kW': steady_state_motor_power_kW,
#     'DOH': 0
# }


# # Initialize phase parameters
# phase1_params = {
#     'initial_altitude': 50,  # in feet
#     'target_altitude': 5000,  # in feet
#     'initial_airspeed': 120,  # in knots
#     'final_airspeed': 130,  # in knots
#     'roc': roc1,  # rate of climb in feet per minute
#     'initial_weight': None,  # in kg, to be updated based on the end of takeoff phase
#     'time_step': 1,  # in seconds
#     'C_D0': C_D0,
#     'k': k,
#     'S': S,
#     'num_motors': num_motors,
#     'num_engines': num_engines,
#     'gearbox_efficiency': gearbox_efficiency,
#     'inverter_efficiency': inverter_efficiency,
#     'battery_capacity_kWh': battery_capacity_kWh,
#     'usable_capacity_factor': usable_capacity_factor,
#     'steady_state_motor_power_kW': steady_state_motor_power_kW,
#     'max_power_kw': max_power_kw,
#     'idle_power_kw': idle_power_kw,
#     'propeller_efficiency': propeller_efficiency_C,
#     'max_motor_power_kW': steady_state_motor_power_kW,
#     'DOH': 0
# }

# between_1_2_climb = {
#     'initial_altitude': 5000,  # in feet (starting from the end of phase 1)
#     'initial_airspeed': 130,  # in knots (starting from the end of phase 1)
#     'final_airspeed': 140,  # in knots
#     'initial_roc': roc1,  # initial rate of climb in feet per minute
#     'final_roc': roc2,  # final rate of climb in feet per minute
#     'roc_transition_duration': 100,  # duration for ROC transition in seconds
#     'initial_weight': None,  # to be updated based on the end of phase 1
#     'time_step': 1,  # in seconds
#     'C_D0': C_D0,
#     'k': k,
#     'S': S,
#     'num_motors': num_motors,
#     'num_engines': num_engines,
#     'gearbox_efficiency': gearbox_efficiency,
#     'inverter_efficiency': inverter_efficiency,
#     'battery_capacity_kWh': battery_capacity_kWh,
#     'usable_capacity_factor': usable_capacity_factor,
#     'steady_state_motor_power_kW': steady_state_motor_power_kW,
#     'max_power_kw': max_power_kw,
#     'idle_power_kw': idle_power_kw,
#     'propeller_efficiency': propeller_efficiency_C,
#     'idle_power_kw': idle_power_kw,
#     'max_motor_power_kW': steady_state_motor_power_kW,
#     'DOH': 0
# }

# phase2_params = {
#     'initial_altitude': None,  # will be updated after between_1_2_climb
#     'target_altitude': 15000,  # in feet
#     'initial_airspeed': 130,  # in knots
#     'final_airspeed': 200,  # in knots
#     'roc': roc2,  # rate of climb in feet per minute
#     'initial_weight': None,  # to be updated based on the end of previous phase
#     'time_step': 1,  # in seconds
#     'C_D0': C_D0,
#     'k': k,
#     'S': S,
#     'num_motors': num_motors,
#     'num_engines': num_engines,
#     'gearbox_efficiency': gearbox_efficiency,
#     'inverter_efficiency': inverter_efficiency,
#     'battery_capacity_kWh': battery_capacity_kWh,
#     'usable_capacity_factor': usable_capacity_factor,
#     'steady_state_motor_power_kW': steady_state_motor_power_kW,
#     'max_power_kw': max_power_kw,
#     'idle_power_kw': idle_power_kw,
#     'propeller_efficiency': propeller_efficiency_C,
#     'max_motor_power_kW': steady_state_motor_power_kW,
#     'DOH': 0
# }

# between_2_3_climb = {
#     'initial_altitude': 15000,  # in feet (starting from the end of phase 1)
#     'initial_airspeed': 200,  # in knots (starting from the end of phase 1)
#     'final_airspeed': 200,  # in knots
#     'initial_roc': roc2,  # initial rate of climb in feet per minute
#     'final_roc': roc3,  # final rate of climb in feet per minute
#     'roc_transition_duration': 100,  # duration for ROC transition in seconds
#     'initial_weight': None,  # to be updated based on the end of phase 1
#     'time_step': 1,  # in seconds
#     'C_D0': C_D0,
#     'k': k,
#     'S': S,
#     'num_motors': num_motors,
#     'num_engines': num_engines,
#     'gearbox_efficiency': gearbox_efficiency,
#     'inverter_efficiency': inverter_efficiency,
#     'battery_capacity_kWh': battery_capacity_kWh,
#     'usable_capacity_factor': usable_capacity_factor,
#     'steady_state_motor_power_kW': steady_state_motor_power_kW,
#     'max_power_kw': max_power_kw,
#     'idle_power_kw': idle_power_kw,
#     'propeller_efficiency': propeller_efficiency_C,
#     'idle_power_kw': idle_power_kw,
#     'max_motor_power_kW': steady_state_motor_power_kW,
#     'DOH': 0
# }

# phase3_params = {
#     'initial_altitude': None,  # in feet (starting from the end of phase 2)
#     'target_altitude': 24000,  # in feet
#     'initial_airspeed': 200,  # in knots (starting from the end of phase 2)
#     'final_airspeed': 200,  # in knots
#     'roc': roc3,  # rate of climb in feet per minute
#     'initial_weight': None,  # to be updated based on the end of phase 2
#     'time_step': 1,  # in seconds
#     'C_D0': C_D0,
#     'k': k,
#     'S': S,
#     'num_motors': num_motors,
#     'num_engines': num_engines,
#     'gearbox_efficiency': gearbox_efficiency,
#     'inverter_efficiency': inverter_efficiency,
#     'battery_capacity_kWh': battery_capacity_kWh,
#     'usable_capacity_factor': usable_capacity_factor,
#     'steady_state_motor_power_kW': steady_state_motor_power_kW,
#     'max_power_kw': max_power_kw,
#     'idle_power_kw': idle_power_kw,
#     'propeller_efficiency': propeller_efficiency_C,
#     'max_motor_power_kW': steady_state_motor_power_kW,
#     'DOH': 0
# }

# cruise_params = {
#     'initial_altitude': 24000,  # in feet
#     'initial_airspeed': 200,  # in knots
#     'final_airspeed': 250,  # in knots
#     'acceleration_duration': 180,  # in seconds 
#     'cruise_distance': None,  # in km
#     'time_step': 1,  # in seconds
#     'C_D0': C_D0,
#     'k': k,
#     'S': S,
#     'num_motors': num_motors,
#     'num_engines': num_engines,
#     'gearbox_efficiency': gearbox_efficiency,
#     'inverter_efficiency': inverter_efficiency,
#     'battery_capacity_kWh': battery_capacity_kWh,
#     'usable_capacity_factor': usable_capacity_factor,
#     'steady_state_motor_power_kW': steady_state_motor_power_kW,
#     'max_power_kw': max_power_kw,
#     'idle_power_kw': idle_power_kw,
#     'propeller_efficiency': propeller_efficiency_Cr,
#     'max_motor_power_kW': steady_state_motor_power_kW,
#     'DOH': 0
# }

# descent_params = {
#     'initial_altitude': 24000,  # in feet
#     'target_altitude': 6000,  # in feet
#     'airspeed': 250,  # in knots
#     'rate_of_descent': 1500,  # in feet per minute
#     'time_step': 1,  # in seconds
#     'C_D0': C_D0,
#     'k': k,
#     'S': S,
#     'num_motors': num_motors,
#     'num_engines': num_engines,
#     'gearbox_efficiency': gearbox_efficiency,
#     'inverter_efficiency': inverter_efficiency,
#     'battery_capacity_kWh': battery_capacity_kWh,
#     'usable_capacity_factor': usable_capacity_factor,
#     'steady_state_motor_power_kW': steady_state_motor_power_kW,
#     'max_power_kw': max_power_kw,
#     'idle_power_kw': idle_power_kw
# }

# approach_and_landing_params = {
#     'initial_altitude': 6000,  # in feet (start of approach)
#     'target_altitude': 0,  # in feet (ground level)
#     'initial_airspeed': 250,  # in knots (initial approach speed)
#     'final_airspeed': 100,  # in knots (final approach speed before landing)
#     'rate_of_descent': 1500,  # in feet per minute
#     'landing_airspeed': 100,  # in knots (landing speed)
#     'landing_distance': 900,  # in meters
#     'time_step': 1,  # in seconds
#     'C_D0': C_D0,
#     'k': k,
#     'S': S,
#     'num_motors': num_motors,
#     'num_engines': num_engines,
#     'gearbox_efficiency': gearbox_efficiency,
#     'inverter_efficiency': inverter_efficiency,
#     'battery_capacity_kWh': battery_capacity_kWh,
#     'usable_capacity_factor': usable_capacity_factor,
#     'steady_state_motor_power_kW': steady_state_motor_power_kW,
#     'max_power_kw': max_power_kw,
#     'idle_power_kw': idle_power_kw
# }

# taxi_params2 = {
#     'taxi_duration': 300,  # taxi duration in seconds
#     'max_taxi_speed': 17.5,  # maximum taxi speed in knots
#     'acceleration_time': 30,  # time to accelerate to taxi speed in seconds
#     'deceleration_time': 30,  # time to decelerate from taxi speed in seconds
#     'idle_power_kw': idle_power_kw,
#     'time_step': time_step,
#     'initial_weight': mass,  # initial weight in kg
# }

# # Create the fitness and individual classes
# creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
# creator.create("Individual", list, fitness=creator.FitnessMin)

# toolbox = base.Toolbox()
# toolbox.register("attr_alt", np.random.uniform, ALT_MIN, ALT_MAX)
# toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_alt, n=5)
# toolbox.register("population", tools.initRepeat, list, toolbox.individual)

# def eval_individual(individual):
#     # Ensure altitude order constraint
#     individual.sort()

#     phase1_params['target_altitude'] = individual[0]
#     between_1_2_climb['target_altitude'] = individual[1]
#     phase2_params['target_altitude'] = individual[2]
#     between_2_3_climb['target_altitude'] = individual[3]
#     phase3_params['target_altitude'] = individual[4]

#     # Calculate the total distance excluding the cruise phase
#     total_distance_excluding_cruise = calculate_total_distance_excluding_cruise(
#         engine_turn_on_params, taxi_params, takeoff_params, take_off_C_params, 
#         phase1_params, between_1_2_climb, phase2_params, between_2_3_climb, 
#         phase3_params, descent_params, approach_and_landing_params, taxi_params2
#     )

#     # Adjust the cruise distance based on the total desired distance
#     cruise_distance = (total_flight_distance - total_distance_excluding_cruise) / 1000  # Convert to km
#     cruise_params['cruise_distance'] = cruise_distance

#     # Run the simulation for all phases with the updated cruise distance
#     combined_results = run_all_phases(
#         engine_turn_on_params, taxi_params, takeoff_params, take_off_C_params, 
#         phase1_params, between_1_2_climb, phase2_params, between_2_3_climb, 
#         phase3_params, cruise_params, descent_params, approach_and_landing_params, 
#         taxi_params2, num_engines
#     )

#     total_fuel_consumed = combined_results['Cumulative Fuel Consumption (kg)'].iloc[-1]
#     return (total_fuel_consumed,)

# toolbox.register("evaluate", eval_individual)
# toolbox.register("mate", tools.cxBlend, alpha=0.5)
# toolbox.register("mutate", tools.mutGaussian, mu=0, sigma=1, indpb=0.2)
# toolbox.register("select", tools.selTournament, tournsize=3)

# def constrain_altitudes(individual):
#     individual.sort()
#     return individual

# # def optimize_for_distance(total_flight_distance_km):
# #     global total_flight_distance
# #     total_flight_distance = total_flight_distance_km * 1000  # Convert to meters
# #     population = toolbox.population(n=POP_SIZE)
# #     halloffame = tools.HallOfFame(1)
# #     stats = tools.Statistics(lambda ind: ind.fitness.values)
# #     stats.register("avg", np.mean)
# #     stats.register("std", np.std)
# #     stats.register("min", np.min)
# #     stats.register("max", np.max)

# #     # Apply constraints
# #     for ind in population:
# #         constrain_altitudes(ind)

# #     population, logbook = algorithms.eaSimple(population, toolbox, cxpb=CXPB, mutpb=MUTPB, ngen=GENS, 
# #                         stats=stats, halloffame=halloffame, verbose=True)

# #     best = halloffame[0]
# #     print(f"Best individual for {total_flight_distance_km} km:", best)
# #     print("Best fitness:", best.fitness.values)

# #     # Update the climb parameters with the best individual
# #     phase1_params['target_altitude'] = best[0]
# #     between_1_2_climb['target_altitude'] = best[1]
# #     phase2_params['target_altitude'] = best[2]
# #     between_2_3_climb['target_altitude'] = best[3]
# #     phase3_params['target_altitude'] = best[4]

# #     # Run the simulation with the best individual
# #     total_distance_excluding_cruise = calculate_total_distance_excluding_cruise(
# #         engine_turn_on_params, taxi_params, takeoff_params, take_off_C_params, 
# #         phase1_params, between_1_2_climb, phase2_params, between_2_3_climb, 
# #         phase3_params, descent_params, approach_and_landing_params, taxi_params2
# #     )

# #     cruise_distance = (total_flight_distance - total_distance_excluding_cruise) / 1000
# #     cruise_params['cruise_distance'] = cruise_distance

# #     combined_results = run_all_phases(
# #         engine_turn_on_params, taxi_params, takeoff_params, take_off_C_params, 
# #         phase1_params, between_1_2_climb, phase2_params, between_2_3_climb, 
# #         phase3_params, cruise_params, descent_params, approach_and_landing_params, 
# #         taxi_params2, num_engines
# #     )

# #     # Print and plot results
# #     print_totals(combined_results)
# #     plot_results(combined_results)

# #     # Save results to CSV
# #     combined_results.to_csv(f'results_{total_flight_distance_km}_km.csv', index=False)
# #     # Save best individual values to a separate CSV
# #     best_individual_df = pd.DataFrame([best], columns=['Phase1', 'Between1_2', 'Phase2', 'Between2_3', 'Phase3'])
# #     best_individual_df.to_csv(f'best_individual_{total_flight_distance_km}_km.csv', index=False)
    
# #     return logbook

# # if __name__ == "__main__":
# #     for total_flight_distance_km in range(150, 501, 50):  # Range from 150 km to 500 km with step of 50 km
# #         print(f"Optimizing for total flight distance: {total_flight_distance_km} km")
# #         logbook = optimize_for_distance(total_flight_distance_km)

# def optimize_for_distance(total_flight_distance_km):
#     global total_flight_distance
#     total_flight_distance = total_flight_distance_km * 1000  # Convert to meters
#     population = toolbox.population(n=POP_SIZE)
#     halloffame = tools.HallOfFame(1)
#     stats = tools.Statistics(lambda ind: ind.fitness.values)
#     stats.register("avg", np.mean)
#     stats.register("std", np.std)
#     stats.register("min", np.min)
#     stats.register("max", np.max)

#     # Apply constraints
#     for ind in population:
#         constrain_altitudes(ind)

#     best_fitness = float('inf')
#     generations_without_improvement = 0

#     for gen in range(GENS):
#         population, logbook = algorithms.eaSimple(population, toolbox, cxpb=CXPB, mutpb=MUTPB, ngen=1, 
#                                                   stats=stats, halloffame=halloffame, verbose=True)

#         current_best_fitness = halloffame[0].fitness.values[0]

#         if current_best_fitness < best_fitness:
#             best_fitness = current_best_fitness
#             generations_without_improvement = 0
#         else:
#             generations_without_improvement += 1

#         if generations_without_improvement >= EARLY_STOPPING_THRESHOLD:
#             print(f"Early stopping at generation {gen} due to no improvement in the last {EARLY_STOPPING_THRESHOLD} generations.")
#             break

#     best = halloffame[0]
#     print(f"Best individual for {total_flight_distance_km} km:", best)
#     print("Best fitness:", best.fitness.values)

#     # Update the climb parameters with the best individual
#     phase1_params['target_altitude'] = best[0]
#     between_1_2_climb['target_altitude'] = best[1]
#     phase2_params['target_altitude'] = best[2]
#     between_2_3_climb['target_altitude'] = best[3]
#     phase3_params['target_altitude'] = best[4]

#     # Run the simulation with the best individual
#     total_distance_excluding_cruise = calculate_total_distance_excluding_cruise(
#         engine_turn_on_params, taxi_params, takeoff_params, take_off_C_params, 
#         phase1_params, between_1_2_climb, phase2_params, between_2_3_climb, 
#         phase3_params, descent_params, approach_and_landing_params, taxi_params2
#     )

#     cruise_distance = (total_flight_distance - total_distance_excluding_cruise) / 1000
#     cruise_params['cruise_distance'] = cruise_distance

#     combined_results = run_all_phases(
#         engine_turn_on_params, taxi_params, takeoff_params, take_off_C_params, 
#         phase1_params, between_1_2_climb, phase2_params, between_2_3_climb, 
#         phase3_params, cruise_params, descent_params, approach_and_landing_params, 
#         taxi_params2, num_engines
#     )

#     # Print and plot results
#     print_totals(combined_results)
#     plot_results(combined_results)

#     # Save results to CSV
#     combined_results.to_csv(f'results_{total_flight_distance_km}_km.csv', index=False)
#     # Save best individual values to a separate CSV
#     best_individual_df = pd.DataFrame([best], columns=['Phase1', 'Between1_2', 'Phase2', 'Between2_3', 'Phase3'])
#     best_individual_df.to_csv(f'best_individual_{total_flight_distance_km}_km.csv', index=False)
    
#     return logbook

# if __name__ == "__main__":
#     for total_flight_distance_km in range(150, 501, 50):  # Range from 150 km to 500 km with step of 50 km
#         print(f"Optimizing for total flight distance: {total_flight_distance_km} km")
#         logbook = optimize_for_distance(total_flight_distance_km)

import pandas as pd
import numpy as np
import random
from deap import base, creator, tools, algorithms
from run_simulation import run_all_phases, calculate_total_distance_excluding_cruise
from prints_and_plots import plot_results, print_totals

# Define aircraft-specific parameters
C_D0 = 0.02  # Zero-lift drag coefficient
k = 0.045  # Induced drag factor
S = 54.5  # Wing area in m²

# Aircraft take-off params
wing_area = 54.5  # Wing area in m²
mass = 16500  # kg
C_T = 0.15  # coefficient of Thrust
n = 20.2  # RPS
D = 3.96  # meters
C_D = 0.05  # example drag coefficient with landing gear
C_L_MAX = 1.8  # maximum lift coefficient for stall speed calculation
C_L_AVG = 0.7  # average lift coefficient for takeoff roll
mu = 0.02  # example coefficient of friction
propeller_efficiency = 0.80  # propeller efficiency during takeoff
idle_power_kw = 74.57  # kW per engine
max_power_kw = 1602  # kW per engine
initial_angle = 0  # degrees
final_angle = 10  # degrees
warmup_duration = 10  # seconds
time_step = 0.1  # time step for simulation

# Aircraft climb params
propeller_efficiency_C = 0.85
propeller_efficiency_Cr = 0.85

# Hybrid system parameters
gearbox_efficiency = 0.99
inverter_efficiency = 0.93
battery_capacity_kWh = 5  # Total capacity of one battery in kWh
usable_capacity_factor = 0.8  # 80% of the battery can be used
steady_state_motor_power_kW = 150  # Steady state motor power per motor
num_motors = 2  # Number of electric motors
num_engines = 2  # Number of engines
total_flight_distance = 250 * 1000  # Example total flight distance in meters
# Genetic Algorithm parameters
POP_SIZE = 50
GENS = 40
MUTPB = 0.2
CXPB = 0.5
EARLY_STOPPING_THRESHOLD = 5  # Number of generations with no improvement to trigger early stopping

# Define the problem space
ALT_MIN = 10000  # Minimum altitude for climb phases (example value)
ALT_MAX = 24000  # Maximum altitude for climb phases (example value)

# Define climb parameters (rate of climb and initial weights for each phase)
roc1 = 1800  # Rate of climb in feet per minute for phase 1
roc2 = 1500  # Rate of climb in feet per minute for phase 2
roc3 = 1000  # Rate of climb in feet per minute for phase 3
initial_weight = mass  # Initial weight of the aircraft

engine_turn_on_params = {
    'idle_power_kw': idle_power_kw,
    'time_step': time_step,
    'turn_on_duration': 15,  # Example duration in seconds
    'initial_weight': mass  # kg
}

taxi_params = {
    'taxi_duration': 300,  # taxi duration in seconds
    'max_taxi_speed': 17.5,  # maximum taxi speed in knots
    'acceleration_time': 30,  # time to accelerate to taxi speed in seconds
    'deceleration_time': 30,  # time to decelerate from taxi speed in seconds
    'idle_power_kw': idle_power_kw,
    'time_step': time_step,
    'initial_weight': mass,  # initial weight in kg
}

# Add parameters for the take-off phase
takeoff_params = {
    'initial_altitude': 0,
    'C_T': C_T,
    'n': n,
    'D': D,
    'S': S,
    'C_D': C_D,
    'C_L_MAX': C_L_MAX,
    'C_L_AVG': C_L_AVG,
    'mu': mu,
    'propeller_efficiency': propeller_efficiency,
    'idle_power_kW': idle_power_kw,
    'max_power_kW': max_power_kw,
    'initial_angle': initial_angle,
    'final_angle': final_angle,
    'time_step': time_step,
    'gearbox_efficiency': gearbox_efficiency,
    'inverter_efficiency': inverter_efficiency,
    'battery_capacity_kWh': battery_capacity_kWh,
    'usable_capacity_factor': usable_capacity_factor,
    'warmup_duration': warmup_duration,
    'initial_weight': mass,  # kg
    'turn_on_duration': engine_turn_on_params['turn_on_duration'],  # Include turn-on duration
    'max_motor_power_kW': steady_state_motor_power_kW,
    'DOH': 0
}

# Parameters for the additional climb phase
take_off_C_params = {
    'initial_altitude': 0,  # in feet
    'target_altitude': 50,  # in feet
    'initial_airspeed': 120,  # in knots
    'final_airspeed': 120,  # in knots
    'roc': 1800,  # rate of climb in feet per minute
    'initial_weight': None,  # in kg, to be updated based on the end of takeoff phase
    'time_step': 0.001,  # in seconds
    'C_D0': C_D0,
    'k': k,
    'S': S,
    'num_motors': num_motors,
    'num_engines': num_engines,
    'gearbox_efficiency': gearbox_efficiency,
    'inverter_efficiency': inverter_efficiency,
    'battery_capacity_kWh': battery_capacity_kWh,
    'usable_capacity_factor': usable_capacity_factor,
    'max_power_kw': max_power_kw,
    'propeller_efficiency': propeller_efficiency_C,
    'idle_power_kw': idle_power_kw,
    'max_motor_power_kW': steady_state_motor_power_kW,
    'DOH': 0
}


# Initialize phase parameters
phase1_params = {
    'initial_altitude': 50,  # in feet
    'target_altitude': 7936,  # in feet
    'initial_airspeed': 120,  # in knots
    'final_airspeed': 130,  # in knots
    'roc': roc1,  # rate of climb in feet per minute
    'initial_weight': None,  # in kg, to be updated based on the end of takeoff phase
    'time_step': 0.1,  # in seconds
    'C_D0': C_D0,
    'k': k,
    'S': S,
    'num_motors': num_motors,
    'num_engines': num_engines,
    'gearbox_efficiency': gearbox_efficiency,
    'inverter_efficiency': inverter_efficiency,
    'battery_capacity_kWh': battery_capacity_kWh,
    'usable_capacity_factor': usable_capacity_factor,
    'steady_state_motor_power_kW': steady_state_motor_power_kW,
    'max_power_kw': max_power_kw,
    'idle_power_kw': idle_power_kw,
    'propeller_efficiency': propeller_efficiency_C,
    'max_motor_power_kW': steady_state_motor_power_kW,
    'DOH': 0
}

between_1_2_climb = {
    'initial_altitude': 7936,  # in feet (starting from the end of phase 1)
    'initial_airspeed': 130,  # in knots (starting from the end of phase 1)
    'final_airspeed': 130,  # in knots
    'initial_roc': roc1,  # initial rate of climb in feet per minute
    'final_roc': roc2,  # final rate of climb in feet per minute
    'roc_transition_duration': 60,  # duration for ROC transition in seconds
    'initial_weight': None,  # to be updated based on the end of phase 1
    'time_step': 1,  # in seconds
    'C_D0': C_D0,
    'k': k,
    'S': S,
    'num_motors': num_motors,
    'num_engines': num_engines,
    'gearbox_efficiency': gearbox_efficiency,
    'inverter_efficiency': inverter_efficiency,
    'battery_capacity_kWh': battery_capacity_kWh,
    'usable_capacity_factor': usable_capacity_factor,
    'steady_state_motor_power_kW': steady_state_motor_power_kW,
    'max_power_kw': max_power_kw,
    'idle_power_kw': idle_power_kw,
    'propeller_efficiency': propeller_efficiency_C,
    'idle_power_kw': idle_power_kw,
    'max_motor_power_kW': steady_state_motor_power_kW,
    'DOH': 0
}
phase2_params = {
    'initial_altitude': None,  # will be updated after phase 1
    'target_altitude': 9200,  # in feet
    'initial_airspeed': 130,  # in knots
    'final_airspeed': 200,  # in knots
    'roc': roc2,  # rate of climb in feet per minute
    'initial_weight': None,  # to be updated based on the end of previous phase
    'time_step': 1,  # in seconds
    'C_D0': C_D0,
    'k': k,
    'S': S,
    'num_motors': num_motors,
    'num_engines': num_engines,
    'gearbox_efficiency': gearbox_efficiency,
    'inverter_efficiency': inverter_efficiency,
    'battery_capacity_kWh': battery_capacity_kWh,
    'usable_capacity_factor': usable_capacity_factor,
    'steady_state_motor_power_kW': steady_state_motor_power_kW,
    'max_power_kw': max_power_kw,
    'idle_power_kw': idle_power_kw,
    'propeller_efficiency': propeller_efficiency_C,
    'max_motor_power_kW': steady_state_motor_power_kW,
    'DOH': 0
}
between_2_3_climb = {
    'initial_altitude': 9200,  # in feet (starting from the end of phase 1)
    'initial_airspeed': 200,  # in knots (starting from the end of phase 1)
    'final_airspeed': 200,  # in knots
    'initial_roc': roc2,  # initial rate of climb in feet per minute
    'final_roc': roc3,  # final rate of climb in feet per minute
    'roc_transition_duration': 100,  # duration for ROC transition in seconds
    'initial_weight': None,  # to be updated based on the end of phase 1
    'time_step': 1,  # in seconds
    'C_D0': C_D0,
    'k': k,
    'S': S,
    'num_motors': num_motors,
    'num_engines': num_engines,
    'gearbox_efficiency': gearbox_efficiency,
    'inverter_efficiency': inverter_efficiency,
    'battery_capacity_kWh': battery_capacity_kWh,
    'usable_capacity_factor': usable_capacity_factor,
    'steady_state_motor_power_kW': steady_state_motor_power_kW,
    'max_power_kw': max_power_kw,
    'idle_power_kw': idle_power_kw,
    'propeller_efficiency': propeller_efficiency_C,
    'idle_power_kw': idle_power_kw,
    'max_motor_power_kW': steady_state_motor_power_kW,
    'DOH': 0
}

phase3_params = {
    'initial_altitude': None,  # in feet (starting from the end of phase 2)
    'target_altitude': 17000,  # in feet
    'initial_airspeed': 200,  # in knots (starting from the end of phase 2)
    'final_airspeed': 200,  # in knots
    'roc': roc3,  # rate of climb in feet per minute
    'initial_weight': None,  # to be updated based on the end of phase 2
    'time_step': 1,  # in seconds
    'C_D0': C_D0,
    'k': k,
    'S': S,
    'num_motors': num_motors,
    'num_engines': num_engines,
    'gearbox_efficiency': gearbox_efficiency,
    'inverter_efficiency': inverter_efficiency,
    'battery_capacity_kWh': battery_capacity_kWh,
    'usable_capacity_factor': usable_capacity_factor,
    'steady_state_motor_power_kW': steady_state_motor_power_kW,
    'max_power_kw': max_power_kw,
    'idle_power_kw': idle_power_kw,
    'propeller_efficiency': propeller_efficiency_C,
    'max_motor_power_kW': steady_state_motor_power_kW,
    'DOH': 0
}

cruise_params = {
    'initial_altitude': 19000,  # in feet
    'initial_airspeed': 200,  # in knots
    'final_airspeed': 250,  # in knots
    'acceleration_duration': 180,  # in seconds 
    'cruise_distance': None,  # in km
    'time_step': 1,  # in seconds
    'C_D0': C_D0,
    'k': k,
    'S': S,
    'num_motors': num_motors,
    'num_engines': num_engines,
    'gearbox_efficiency': gearbox_efficiency,
    'inverter_efficiency': inverter_efficiency,
    'battery_capacity_kWh': battery_capacity_kWh,
    'usable_capacity_factor': usable_capacity_factor,
    'steady_state_motor_power_kW': steady_state_motor_power_kW,
    'max_power_kw': max_power_kw,
    'idle_power_kw': idle_power_kw,
    'propeller_efficiency': propeller_efficiency_Cr,
    'max_motor_power_kW': steady_state_motor_power_kW,
    'DOH': 0
}

descent_params = {
    'initial_altitude': 17000,  # in feet
    'target_altitude': 3000,  # in feet
    'airspeed': 250,  # in knots
    'rate_of_descent': 1500,  # in feet per minute
    'time_step': 1,  # in seconds
    'C_D0': C_D0,
    'k': k,
    'S': S,
    'num_motors': num_motors,
    'num_engines': num_engines,
    'gearbox_efficiency': gearbox_efficiency,
    'inverter_efficiency': inverter_efficiency,
    'battery_capacity_kWh': battery_capacity_kWh,
    'usable_capacity_factor': usable_capacity_factor,
    'steady_state_motor_power_kW': steady_state_motor_power_kW,
    'max_power_kw': max_power_kw,
    'idle_power_kw': idle_power_kw
}

approach_and_landing_params = {
    'initial_altitude': 3000,  # in feet (start of approach)
    'target_altitude': 0,  # in feet (ground level)
    'initial_airspeed': 250,  # in knots (initial approach speed)
    'final_airspeed': 100,  # in knots (final approach speed before landing)
    'rate_of_descent': 1500,  # in feet per minute
    'landing_airspeed': 100,  # in knots (landing speed)
    'landing_distance': 900,  # in meters
    'time_step': 1,  # in seconds
    'C_D0': C_D0,
    'k': k,
    'S': S,
    'num_motors': num_motors,
    'num_engines': num_engines,
    'gearbox_efficiency': gearbox_efficiency,
    'inverter_efficiency': inverter_efficiency,
    'battery_capacity_kWh': battery_capacity_kWh,
    'usable_capacity_factor': usable_capacity_factor,
    'steady_state_motor_power_kW': steady_state_motor_power_kW,
    'max_power_kw': max_power_kw,
    'idle_power_kw': idle_power_kw
}

taxi_params2 = {
    'taxi_duration': 300,  # taxi duration in seconds
    'max_taxi_speed': 17.5,  # maximum taxi speed in knots
    'acceleration_time': 30,  # time to accelerate to taxi speed in seconds
    'deceleration_time': 30,  # time to decelerate from taxi speed in seconds
    'idle_power_kw': idle_power_kw,
    'time_step': time_step,
    'initial_weight': mass,  # initial weight in kg
}

    # Calculate the total distance excluding the cruise phase
# Run the simulation with the best individual
total_distance_excluding_cruise = calculate_total_distance_excluding_cruise(
        engine_turn_on_params, taxi_params, takeoff_params, take_off_C_params, 
        phase1_params, between_1_2_climb, phase2_params, between_2_3_climb, 
        phase3_params, descent_params, approach_and_landing_params, taxi_params2, 
    )
    # Adjust the cruise distance based on the total desired distance
cruise_distance = (total_flight_distance - total_distance_excluding_cruise) / 1000  # Convert to km
cruise_params['cruise_distance'] = cruise_distance

    # Run the simulation for all phases with the updated cruise distance
combined_results = run_all_phases(
    engine_turn_on_params, taxi_params, takeoff_params, take_off_C_params, 
    phase1_params, between_1_2_climb, phase2_params, between_2_3_climb, 
    phase3_params, cruise_params, descent_params, approach_and_landing_params, 
    taxi_params2, num_engines
)


# # Create the fitness and individual classes
# creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
# creator.create("Individual", list, fitness=creator.FitnessMin)

# toolbox = base.Toolbox()
# toolbox.register("attr_alt", np.random.uniform, ALT_MIN, ALT_MAX)
# toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_alt, n=3)
# toolbox.register("population", tools.initRepeat, list, toolbox.individual)

# def eval_individual(individual):
#     # Ensure altitude order constraint
#     individual.sort()

#     phase1_params['target_altitude'] = individual[0]
#     phase2_params['target_altitude'] = individual[1]
#     phase3_params['target_altitude'] = individual[2]

#     # Update intermediate phases to link altitudes correctly
#     phase2_params['initial_altitude'] = phase1_params['target_altitude']
#     phase3_params['initial_altitude'] = phase2_params['target_altitude']
#     descent_params['initial_altitude'] = phase3_params['target_altitude']

#     # Calculate the total distance excluding the cruise phase
# # Run the simulation with the best individual
#     total_distance_excluding_cruise = calculate_total_distance_excluding_cruise(
#         engine_turn_on_params, taxi_params, takeoff_params, take_off_C_params, 
#         phase1_params, between_1_2_climb, phase2_params, between_2_3_climb, 
#         phase3_params, descent_params, approach_and_landing_params, taxi_params2, 
#     )
#     # Adjust the cruise distance based on the total desired distance
#     cruise_distance = (total_flight_distance - total_distance_excluding_cruise) / 1000  # Convert to km
#     cruise_params['cruise_distance'] = cruise_distance

#     # Run the simulation for all phases with the updated cruise distance
#     combined_results = run_all_phases(
#     engine_turn_on_params, taxi_params, takeoff_params, take_off_C_params, 
#     phase1_params, between_1_2_climb, phase2_params, between_2_3_climb, 
#     phase3_params, cruise_params, descent_params, approach_and_landing_params, 
#     taxi_params2, num_engines
# )

#     total_fuel_consumed = combined_results['Cumulative Fuel Consumption (kg)'].iloc[-1]
#     return (total_fuel_consumed,)

# toolbox.register("evaluate", eval_individual)
# toolbox.register("mate", tools.cxBlend, alpha=0.5)
# toolbox.register("mutate", tools.mutGaussian, mu=0, sigma=1, indpb=0.2)
# toolbox.register("select", tools.selTournament, tournsize=3)

# def constrain_altitudes(individual):
#     individual.sort()
#     return individual

# def optimize_for_distance(total_flight_distance_km):
#     global total_flight_distance
#     total_flight_distance = total_flight_distance_km * 1000  # Convert to meters
#     population = toolbox.population(n=POP_SIZE)
#     halloffame = tools.HallOfFame(1)
#     stats = tools.Statistics(lambda ind: ind.fitness.values)
#     stats.register("avg", np.mean)
#     stats.register("std", np.std)
#     stats.register("min", np.min)
#     stats.register("max", np.max)

#     # Apply constraints
#     for ind in population:
#         constrain_altitudes(ind)

#     # Variables for early stopping
#     best_fitness = float('inf')
#     no_improvement_gens = 0

#     # Run the genetic algorithm with early stopping
#     for gen in range(GENS):
#         population, logbook = algorithms.eaSimple(population, toolbox, cxpb=CXPB, mutpb=MUTPB, ngen=1,
#                                                   stats=stats, halloffame=halloffame, verbose=True)
        
#         current_best_fitness = halloffame[0].fitness.values[0]
#         print(f"Generation {gen + 1}, Best Fitness: {current_best_fitness}")

#         if current_best_fitness < best_fitness:
#             best_fitness = current_best_fitness
#             no_improvement_gens = 0
#         else:
#             no_improvement_gens += 1
        
#         if no_improvement_gens >= EARLY_STOPPING_THRESHOLD:
#             print(f"Early stopping at generation {gen + 1} due to no improvement in {EARLY_STOPPING_THRESHOLD} generations.")
#             break

#     best = halloffame[0]
#     print(f"Best individual for {total_flight_distance_km} km:", best)
#     print("Best fitness:", best.fitness.values)

#     # Update the climb parameters with the best individual
#     phase1_params['target_altitude'] = best[0]
#     phase2_params['target_altitude'] = best[1]
#     phase3_params['target_altitude'] = best[2]

#     # Update intermediate phases to link altitudes correctly
#     phase2_params['initial_altitude'] = phase1_params['target_altitude']
#     phase3_params['initial_altitude'] = phase2_params['target_altitude']
#     descent_params['initial_altitude'] = phase3_params['target_altitude']

#     # Calculate the total distance excluding the cruise phase
#     total_distance_excluding_cruise = calculate_total_distance_excluding_cruise(
#     engine_turn_on_params, taxi_params, takeoff_params, take_off_C_params, 
#     phase1_params, between_1_2_climb, phase2_params, between_2_3_climb, 
#     phase3_params, descent_params, approach_and_landing_params, taxi_params2
#         )
#     cruise_distance = (total_flight_distance - total_distance_excluding_cruise) / 1000
#     cruise_params['cruise_distance'] = cruise_distance

    

#     # Run the simulation for all phases with the updated cruise distance
#     combined_results = run_all_phases(
#     engine_turn_on_params, taxi_params, takeoff_params, take_off_C_params, 
#     phase1_params, between_1_2_climb, phase2_params, between_2_3_climb, 
#     phase3_params, cruise_params, descent_params, approach_and_landing_params, 
#     taxi_params2, num_engines
# )

#     # Print and plot results
#     print_totals(combined_results)
#     plot_results(combined_results)

#     # Save results to CSV
#     combined_results.to_csv(f'results_{total_flight_distance_km}_km.csv', index=False)
#     best_individual_df = pd.DataFrame([best], columns=['Phase 1 Altitude', 'Phase 2 Altitude', 'Phase 3 Altitude'])
#     best_individual_df.to_csv(f'best_individual_{total_flight_distance_km}_km.csv', index=False)

#     print(f"Cruise distance for {total_flight_distance_km} km: {cruise_distance} km")
#     return logbook

# if __name__ == "__main__":
#     for total_flight_distance_km in range(250, 501, 50):  # Adjust range as needed
#         print(f"Optimizing for total flight distance: {total_flight_distance_km} km")
#         logbook = optimize_for_distance(total_flight_distance_km)
