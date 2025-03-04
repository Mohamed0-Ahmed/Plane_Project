# import pandas as pd
# from run_simulation import run_all_phases
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

# # Hybrid system parameters
# gearbox_efficiency = 0.99
# inverter_efficiency = 0.92
# battery_capacity_kWh = 5  # Total capacity of one battery in kWh
# usable_capacity_factor = 0.8  # 80% of the battery can be used
# steady_state_motor_power_kW = 150  # Steady state motor power per motor
# num_motors = 2  # Number of electric motors
# num_engines = 2  # Number of engines

# # Get user input for aircraft mass
# mass = 16500

# # Parameters for the engine turn-on phase
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
#     'warmup_duration': warmup_duration,
#     'initial_weight': mass,  # kg
#     'turn_on_duration': engine_turn_on_params['turn_on_duration']  # Include turn-on duration
# }

# # Parameters for the additional climb phase
# take_off_C_params = {
#     'initial_altitude': 0,  # in feet
#     'target_altitude': 50,  # in feet
#     'initial_airspeed': 120,  # in knots
#     'final_airspeed': 130,  # in knots
#     'roc': 300,  # rate of climb in feet per minute
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
#     'idle_power_kw': idle_power_kw
# }

# # Parameters for the first phase of climb
# phase1_params = {
#     'initial_altitude': 50,  # in feet
#     'target_altitude': 5000,  # in feet
#     'initial_airspeed': 120,  # in knots
#     'final_airspeed': 130,  # in knots
#     'roc': 1800,  # rate of climb in feet per minute
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
#     'idle_power_kw': idle_power_kw
# }

# # Parameters for the first phase of climb
# phase1_params = {
#     'initial_altitude': 50,  # in feet
#     'target_altitude': 5000,  # in feet
#     'initial_airspeed': 120,  # in knots
#     'final_airspeed': 130,  # in knots
#     'roc': 1800,  # rate of climb in feet per minute
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
#     'idle_power_kw': idle_power_kw
# }

# between_1_2_climb = {
#     'initial_altitude': 5000,  # in feet (starting from the end of phase 1)
#     'initial_airspeed': 130,  # in knots (starting from the end of phase 1)
#     'final_airspeed': 130,  # in knots
#     'roc': 1500,  # rate of climb in feet per minute
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
#     'idle_power_kw': idle_power_kw
# }

# # Parameters for the second phase of climb
# phase2_params = {
#     'initial_altitude': 5000,  # in feet (starting from the end of phase 1)
#     'target_altitude': 15000,  # in feet
#     'initial_airspeed': 130,  # in knots (starting from the end of phase 1)
#     'final_airspeed': 200,  # in knots
#     'roc': 1500,  # rate of climb in feet per minute
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
#     'idle_power_kw': idle_power_kw
# }

# # Parameters for the third phase of climb
# phase3_params = {
#     'initial_altitude': 15000,  # in feet (starting from the end of phase 2)
#     'target_altitude': 24000,  # in feet
#     'initial_airspeed': 200,  # in knots (starting from the end of phase 2)
#     'final_airspeed': 200,  # in knots
#     'roc': 1000,  # rate of climb in feet per minute
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
#     'idle_power_kw': idle_power_kw
# }

# # Parameters for the cruise phase
# cruise_params = {
#     'initial_altitude': 24000,  # in feet
#     'initial_airspeed': 200,  # in knots
#     'final_airspeed': 250,  # in knots
#     'acceleration_duration': 180,  # in seconds (1 minute)
#     'cruise_distance': 100,  # in km
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

# # Parameters for the descent phase
# descent_params = {
#     'initial_altitude': 24000,  # in feet
#     'target_altitude': 10000,  # in feet
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

# # Parameters for the approach and landing phase
# approach_and_landing_params = {
#     'initial_altitude': 10000,  # in feet (start of approach)
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


# # Run the simulation for all phases
# combined_results = run_all_phases(engine_turn_on_params, taxi_params, takeoff_params, take_off_C_params, phase1_params, phase2_params, phase3_params, cruise_params, descent_params, approach_and_landing_params, taxi_params2, num_engines)
# # combined_results_take_off = run_all_phases(takeoff_params, take_off_C_params)
# # combined_results_climb = run_all_phases(phase1_params, phase2_params, phase3_params)

# # Print and plot results
# print_totals(combined_results)
# plot_results(combined_results)

# # print_totals(combined_results_take_off)
# # print_totals(combined_results_climb)

# # plot_results(combined_results_take_off)
# # plot_results(combined_results_climb)

import pandas as pd
from run_simulation import run_all_phases
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

# Hybrid system parameters
gearbox_efficiency = 0.99
inverter_efficiency = 0.9
battery_capacity_kWh = 5  # Total capacity of one battery in kWh
usable_capacity_factor = 0.8  # 80% of the battery can be used
steady_state_motor_power_kW = 150  # Steady state motor power per motor
num_motors = 2  # Number of electric motors
num_engines = 2  # Number of engines

# Get user input for aircraft mass
mass = 16500

# Parameters for the engine turn-on phase
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
    'warmup_duration': warmup_duration,
    'initial_weight': mass,  # kg
    'turn_on_duration': engine_turn_on_params['turn_on_duration']  # Include turn-on duration
}

# Parameters for the additional climb phase
take_off_C_params = {
    'initial_altitude': 0,  # in feet
    'target_altitude': 50,  # in feet
    'initial_airspeed': 120,  # in knots
    'final_airspeed': 130,  # in knots
    'roc': 300,  # rate of climb in feet per minute
    'initial_weight': None,  # in kg, to be updated based on the end of takeoff phase
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

# Parameters for the first phase of climb
phase1_params = {
    'initial_altitude': 50,  # in feet
    'target_altitude': 5000,  # in feet
    'initial_airspeed': 120,  # in knots
    'final_airspeed': 130,  # in knots
    'roc': 1800,  # rate of climb in feet per minute
    'initial_weight': None,  # in kg, to be updated based on the end of takeoff phase
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

# Parameters for the new climb phase between phase1 and phase2
between_1_2_climb = {
    'initial_altitude': 5000,  # in feet (starting from the end of phase 1)
    'initial_airspeed': 130,  # in knots (starting from the end of phase 1)
    'final_airspeed': 130,  # in knots
    'initial_roc': 1800,  # initial rate of climb in feet per minute
    'final_roc': 1500,  # final rate of climb in feet per minute
    'roc_transition_duration': 30,  # duration for ROC transition in seconds
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
    'idle_power_kw': idle_power_kw
}

# Parameters for the second phase of climb
phase2_params = {
    'initial_altitude': None,  # will be updated after between_1_2_climb
    'target_altitude': 15000,  # in feet
    'initial_airspeed': 130,  # in knots
    'final_airspeed': 200,  # in knots
    'roc': 1500,  # rate of climb in feet per minute
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
    'idle_power_kw': idle_power_kw
}
between_2_3_climb = {
    'initial_altitude': 15000,  # in feet (starting from the end of phase 1)
    'initial_airspeed': 200,  # in knots (starting from the end of phase 1)
    'final_airspeed': 200,  # in knots
    'initial_roc': 1500,  # initial rate of climb in feet per minute
    'final_roc': 1000,  # final rate of climb in feet per minute
    'roc_transition_duration': 30,  # duration for ROC transition in seconds
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
    'idle_power_kw': idle_power_kw

}

# Parameters for the third phase of climb
phase3_params = {
    'initial_altitude': None,  # in feet (starting from the end of phase 2)
    'target_altitude': 24000,  # in feet
    'initial_airspeed': 200,  # in knots (starting from the end of phase 2)
    'final_airspeed': 200,  # in knots
    'roc': 1000,  # rate of climb in feet per minute
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
    'idle_power_kw': idle_power_kw
}

# Parameters for the cruise phase
cruise_params = {
    'initial_altitude': 24000,  # in feet
    'initial_airspeed': 200,  # in knots
    'final_airspeed': 250,  # in knots
    'acceleration_duration': 180,  # in seconds (1 minute)
    'cruise_distance': 100,  # in km
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

# Parameters for the descent phase
descent_params = {
    'initial_altitude': 24000,  # in feet
    'target_altitude': 10000,  # in feet
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

# Parameters for the approach and landing phase
approach_and_landing_params = {
    'initial_altitude': 10000,  # in feet (start of approach)
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

# Run the simulation for all phases
combined_results = run_all_phases(engine_turn_on_params, taxi_params, takeoff_params, take_off_C_params, phase1_params, between_1_2_climb, phase2_params,between_2_3_climb, phase3_params, cruise_params, descent_params, approach_and_landing_params, taxi_params2, num_engines)

# Print and plot results
print_totals(combined_results)
plot_results(combined_results)

