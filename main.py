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
inverter_efficiency = 0.92
battery_capacity_kWh = 5  # Total capacity of one battery in kWh
usable_capacity_factor = 0.8  # 80% of the battery can be used
steady_state_motor_power_kW = 150  # Steady state motor power per motor
num_motors = 2  # Number of electric motors
num_engines = 2  # Number of engines

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
    'initial_weight': mass  # kg
}

take_off_C_params = {
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

# Parameters for the second phase of climb
phase2_params = {
    'initial_altitude': 5000,  # in feet (starting from the end of phase 1)
    'target_altitude': 15000,  # in feet
    'initial_airspeed': 130,  # in knots (starting from the end of phase 1)
    'final_airspeed': 200,  # in knots
    'roc': 1500,  # rate of climb in feet per minute
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
    'initial_altitude': 15000,  # in feet (starting from the end of phase 2)
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

# Run the simulation for all phases
combined_results = run_all_phases(takeoff_params, take_off_C_params, phase1_params, phase2_params, phase3_params, cruise_params, descent_params, approach_and_landing_params, num_engines)

# Print and plot results
print_totals(combined_results)
plot_results(combined_results)