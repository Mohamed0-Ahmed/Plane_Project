import pandas as pd
from simulations.takeoff_phase import simulate_takeoff_phase
from simulations.climb_phase import simulate_climb_phase
from simulations.cruise_phase import simulate_cruise_phase
from simulations.descent_phase import simulate_descent_phase
from simulations.approach_and_landing_phase import simulate_approach_and_landing
from utils import simple_wind_speed_scenario, simple_crosswind_speed_scenario

def run_all_phases(takeoff_params, phase1_params, phase2_params, phase3_params, cruise_params, descent_params, approach_and_landing_params, num_engines=2):
    # Run the take-off phase
    results_takeoff, final_weight_takeoff, final_time_takeoff, final_horizontal_distance_takeoff, final_engine_power_takeoff, cumulative_fuel_consumed_takeoff, total_carbon_emissions_takeoff, total_co_emissions_takeoff, total_nox_emissions_takeoff, total_so2_emissions_takeoff = simulate_takeoff_phase(
        takeoff_params,
        simple_wind_speed_scenario,
        simple_crosswind_speed_scenario,
        takeoff_params['initial_weight'],  # Starting weight
        0,
        0,
        cumulative_fuel_consumed=0,
        total_carbon_emissions=0,
        total_co_emissions=0,
        total_nox_emissions=0,
        total_so2_emissions=0
    )

    # Update initial conditions for the first climb phase based on the take-off phase
    phase1_params['initial_weight'] = final_weight_takeoff / 9.81  # Convert N to kg
    initial_time = final_time_takeoff
    initial_horizontal_distance = final_horizontal_distance_takeoff

    # Run the first phase of climb
    results_phase1, final_weight_phase1, final_time_phase1, final_horizontal_distance_phase1, final_engine_power_phase1, total_fuel_consumed_phase1, total_carbon_emissions_phase1, total_co_emissions_phase1, total_nox_emissions_phase1, total_so2_emissions_phase1 = simulate_climb_phase(
        phase1_params,
        simple_wind_speed_scenario,
        simple_crosswind_speed_scenario,
        phase1_params['initial_weight'],
        initial_time,
        initial_horizontal_distance,
        num_engines,
        cumulative_fuel_consumed=cumulative_fuel_consumed_takeoff,
        total_carbon_emissions=total_carbon_emissions_takeoff,
        total_co_emissions=total_co_emissions_takeoff,
        total_nox_emissions=total_nox_emissions_takeoff,
        total_so2_emissions=total_so2_emissions_takeoff
    )

    # Update initial conditions for the second climb phase based on the first climb phase
    phase2_params['initial_weight'] = final_weight_phase1 / 9.81  # Convert N to kg
    initial_time = final_time_phase1
    initial_horizontal_distance = final_horizontal_distance_phase1

    # Run the second phase of climb
    results_phase2, final_weight_phase2, final_time_phase2, final_horizontal_distance_phase2, final_engine_power_phase2, total_fuel_consumed_phase2, total_carbon_emissions_phase2, total_co_emissions_phase2, total_nox_emissions_phase2, total_so2_emissions_phase2 = simulate_climb_phase(
        phase2_params,
        simple_wind_speed_scenario,
        simple_crosswind_speed_scenario,
        phase2_params['initial_weight'],
        initial_time,
        initial_horizontal_distance,
        num_engines,
        cumulative_fuel_consumed=total_fuel_consumed_phase1,
        total_carbon_emissions=total_carbon_emissions_phase1,
        total_co_emissions=total_co_emissions_phase1,
        total_nox_emissions=total_nox_emissions_phase1,
        total_so2_emissions=total_so2_emissions_phase1
    )

    # Update initial conditions for the third climb phase based on the second climb phase
    phase3_params['initial_weight'] = final_weight_phase2 / 9.81  # Convert N to kg
    initial_time = final_time_phase2
    initial_horizontal_distance = final_horizontal_distance_phase2

    # Run the third phase of climb
    results_phase3, final_weight_phase3, final_time_phase3, final_horizontal_distance_phase3, _, total_fuel_consumed_phase3, total_carbon_emissions_phase3, total_co_emissions_phase3, total_nox_emissions_phase3, total_so2_emissions_phase3 = simulate_climb_phase(
        phase3_params,
        simple_wind_speed_scenario,
        simple_crosswind_speed_scenario,
        phase3_params['initial_weight'],
        initial_time,
        initial_horizontal_distance,
        num_engines,
        cumulative_fuel_consumed=total_fuel_consumed_phase2,
        total_carbon_emissions=total_carbon_emissions_phase2,
        total_co_emissions=total_co_emissions_phase2,
        total_nox_emissions=total_nox_emissions_phase2,
        total_so2_emissions=total_so2_emissions_phase2
    )

    # Run the cruise phase
    results_cruise, final_weight_cruise, final_time_cruise, final_horizontal_distance_cruise, total_fuel_consumed_cruise, total_carbon_emissions_cruise, total_co_emissions_cruise, total_nox_emissions_cruise, total_so2_emissions_cruise = simulate_cruise_phase(
        cruise_params,
        simple_wind_speed_scenario,
        simple_crosswind_speed_scenario,
        final_weight_phase3 / 9.81,  # Convert N to kg
        final_time_phase3,
        final_horizontal_distance_phase3,
        num_engines,
        cumulative_fuel_consumed=total_fuel_consumed_phase3,
        total_carbon_emissions=total_carbon_emissions_phase3,
        total_co_emissions=total_co_emissions_phase3,
        total_nox_emissions=total_nox_emissions_phase3,
        total_so2_emissions=total_so2_emissions_phase3
    )

    # Run the descent phase
    results_descent, final_weight_descent, final_time_descent, final_horizontal_distance_descent, total_fuel_consumed_descent, total_carbon_emissions_descent, total_co_emissions_descent, total_nox_emissions_descent, total_so2_emissions_descent = simulate_descent_phase(
        descent_params,
        simple_wind_speed_scenario,
        simple_crosswind_speed_scenario,
        final_weight_cruise / 9.81,  # Convert N to kg
        final_time_cruise,
        final_horizontal_distance_cruise,
        num_engines,
        cumulative_fuel_consumed=total_fuel_consumed_cruise,
        total_carbon_emissions=total_carbon_emissions_cruise,
        total_co_emissions=total_co_emissions_cruise,
        total_nox_emissions=total_nox_emissions_cruise,
        total_so2_emissions=total_so2_emissions_cruise
    )

    # Run the approach and landing phase
    results_approach_and_landing, final_weight_landing, final_time_landing, final_horizontal_distance_landing, total_fuel_consumed_landing, total_carbon_emissions_landing, total_co_emissions_landing, total_nox_emissions_landing, total_so2_emissions_landing = simulate_approach_and_landing(
        approach_and_landing_params,
        simple_wind_speed_scenario,
        simple_crosswind_speed_scenario,
        final_weight_descent / 9.81,  # Convert N to kg
        final_time_descent,
        final_horizontal_distance_descent,
        num_engines,
        cumulative_fuel_consumed=total_fuel_consumed_descent,
        total_carbon_emissions=total_carbon_emissions_descent,
        total_co_emissions=total_co_emissions_descent,
        total_nox_emissions=total_nox_emissions_descent,
        total_so2_emissions=total_so2_emissions_descent
    )

    # Combine the results of all phases
    combined_results = pd.concat([results_takeoff, results_phase1, results_phase2, results_phase3, results_cruise, results_descent, results_approach_and_landing], ignore_index=True)

    return combined_results
