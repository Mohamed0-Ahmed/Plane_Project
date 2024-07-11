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
#     'gearbox_efficiency': gearbox_efficiency,
#     'inverter_efficiency': inverter_efficiency,
#     'battery_capacity_kWh': battery_capacity_kWh,
#     'usable_capacity_factor': usable_capacity_factor,
#     'warmup_duration': warmup_duration,
#     'initial_weight': mass,  # kg
#     'turn_on_duration': engine_turn_on_params['turn_on_duration'],  # Include turn-on duration
#     'max_motor_power_kW': steady_state_motor_power_kW,
#     'DOH': 0.15
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
#     'DOH': 0.15
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
#     'idle_power_kw': idle_power_kw,
#     'propeller_efficiency': propeller_efficiency_C,
#     'max_motor_power_kW': steady_state_motor_power_kW,
#     'DOH': 0.15
# }

# # Parameters for the new climb phase between phase1 and phase2
# between_1_2_climb = {
#     'initial_altitude': 5000,  # in feet (starting from the end of phase 1)
#     'initial_airspeed': 130,  # in knots (starting from the end of phase 1)
#     'final_airspeed': 140,  # in knots
#     'initial_roc': 1800,  # initial rate of climb in feet per minute
#     'final_roc': 1500,  # final rate of climb in feet per minute
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
#     'DOH': 0.15
# }

# # Parameters for the second phase of climb
# phase2_params = {
#     'initial_altitude': None,  # will be updated after between_1_2_climb
#     'target_altitude': 15000,  # in feet
#     'initial_airspeed': 130,  # in knots
#     'final_airspeed': 200,  # in knots
#     'roc': 1500,  # rate of climb in feet per minute
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
#     'DOH': 0.15
# }
# between_2_3_climb = {
#     'initial_altitude': 15000,  # in feet (starting from the end of phase 1)
#     'initial_airspeed': 200,  # in knots (starting from the end of phase 1)
#     'final_airspeed': 200,  # in knots
#     'initial_roc': 1500,  # initial rate of climb in feet per minute
#     'final_roc': 1000,  # final rate of climb in feet per minute
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
#     'DOH': 0.15

# }

# # Parameters for the third phase of climb
# phase3_params = {
#     'initial_altitude': None,  # in feet (starting from the end of phase 2)
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
#     'idle_power_kw': idle_power_kw,
#     'propeller_efficiency': propeller_efficiency_C,
#     'max_motor_power_kW': steady_state_motor_power_kW,
#     'DOH': 0
# }

# # Parameters for the cruise phase
# cruise_params = {
#     'initial_altitude': 24000,  # in feet
#     'initial_airspeed': 200,  # in knots
#     'final_airspeed': 250,  # in knots
#     'acceleration_duration': 180,  # in seconds 
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
#     'idle_power_kw': idle_power_kw,
#     'propeller_efficiency': propeller_efficiency_Cr,
#     'max_motor_power_kW': steady_state_motor_power_kW,
#     'DOH': 0
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
# combined_results = run_all_phases(engine_turn_on_params, taxi_params, takeoff_params, take_off_C_params, phase1_params, between_1_2_climb, phase2_params,between_2_3_climb, phase3_params, cruise_params, descent_params, approach_and_landing_params, taxi_params2, num_engines)

# # Print and plot results
# print_totals(combined_results)
# plot_results(combined_results)

import pandas as pd
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

# Get user input for aircraft mass
mass = 16500


# Step 2: Adjust the cruise distance based on the total desired distance
total_flight_distance = 250 * 1000  # Example total flight distance in meters

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
    'idle_power_kw': idle_power_kw,
    'propeller_efficiency': propeller_efficiency_C,
    'max_motor_power_kW': steady_state_motor_power_kW,
    'DOH': 0
}

# Parameters for the new climb phase between phase1 and phase2
between_1_2_climb = {
    'initial_altitude': 5000,  # in feet (starting from the end of phase 1)
    'initial_airspeed': 130,  # in knots (starting from the end of phase 1)
    'final_airspeed': 140,  # in knots
    'initial_roc': 1800,  # initial rate of climb in feet per minute
    'final_roc': 1500,  # final rate of climb in feet per minute
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
    'idle_power_kw': idle_power_kw,
    'propeller_efficiency': propeller_efficiency_C,
    'max_motor_power_kW': steady_state_motor_power_kW,
    'DOH': 0
}
between_2_3_climb = {
    'initial_altitude': 8300,  # in feet (starting from the end of phase 1)
    'initial_airspeed': 200,  # in knots (starting from the end of phase 1)
    'final_airspeed': 200,  # in knots
    'initial_roc': 1500,  # initial rate of climb in feet per minute
    'final_roc': 1000,  # final rate of climb in feet per minute
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

# Parameters for the third phase of climb
phase3_params = {
    'initial_altitude': None,  # in feet (starting from the end of phase 2)
    'target_altitude': 17000,  # in feet
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
    'idle_power_kw': idle_power_kw,
    'propeller_efficiency': propeller_efficiency_C,
    'max_motor_power_kW': steady_state_motor_power_kW,
    'DOH': 0
}

# Parameters for the cruise phase
cruise_params = {
    'initial_altitude': 17000,  # in feet
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

# Parameters for the descent phase
descent_params = {
    'initial_altitude': 17000,  # in feet
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

# Step 1: Calculate the total distance excluding the cruise phase
total_distance_excluding_cruise = calculate_total_distance_excluding_cruise(
    engine_turn_on_params, taxi_params, takeoff_params, take_off_C_params, 
    phase1_params, between_1_2_climb, phase2_params, between_2_3_climb, 
    phase3_params, descent_params, approach_and_landing_params, taxi_params2
)

# Step 2: Adjust the cruise distance based on the total desired distance
cruise_distance = (total_flight_distance - total_distance_excluding_cruise) / 1000  # Convert to km

# Update cruise_params with the calculated cruise distance
cruise_params['cruise_distance'] = cruise_distance

cruise_distance = (total_flight_distance - total_distance_excluding_cruise) / 1000  # Convert to km
print(f'cruise distance {cruise_distance}')
# Update cruise_params with the calculated cruise distance
cruise_params['cruise_distance'] = cruise_distance
print(f'cruise distance {cruise_distance:2f}')

# Run the simulation for all phases with the updated cruise distance
combined_results = run_all_phases(
    engine_turn_on_params, taxi_params, takeoff_params, take_off_C_params, 
    phase1_params, between_1_2_climb, phase2_params, between_2_3_climb, 
    phase3_params, cruise_params, descent_params, approach_and_landing_params, 
    taxi_params2, num_engines
)

# Print and plot results
print_totals(combined_results)
plot_results(combined_results)
