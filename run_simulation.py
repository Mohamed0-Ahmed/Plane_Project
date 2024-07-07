# import pandas as pd
# from simulations.takeoff_phase import simulate_takeoff_phase
# from simulations.taxi_phase import simulate_taxi_phase
# from simulations.climb_phase import simulate_climb_phase
# from simulations.cruise_phase import simulate_cruise_phase
# from simulations.descent_phase import simulate_descent_phase
# from simulations.approach_and_landing_phase import simulate_approach_and_landing
# from simulations.engine_turn_on_phase import engine_turn_on_phase
# from prints_and_plots import plot_results, print_totals
# from utils import simple_wind_speed_scenario, simple_crosswind_speed_scenario

# def run_all_phases(engine_turn_on_params, taxi_params, takeoff_params, take_off_C_params, phase1_params, phase2_params, phase3_params, cruise_params, descent_params, approach_and_landing_params, num_engines=2):
#     # Run the engine turn-on phase
#     turn_on_results, final_weight_turn_on, final_time_turn_on, final_horizontal_distance_turn_on, final_engine_power_turn_on, cumulative_fuel_consumed_turn_on, total_carbon_emissions_turn_on, total_co_emissions_turn_on, total_nox_emissions_turn_on, total_so2_emissions_turn_on = engine_turn_on_phase(
#         engine_turn_on_params,
#         0,  # Starting time
#         0,  # Starting horizontal distance
#         num_engines,
#         cumulative_fuel_consumed_turn_on=0,
#         total_carbon_emissions_turn_on=0,
#         total_co_emissions_turn_on=0,
#         total_nox_emissions_turn_on=0,
#         total_so2_emissions_turn_on=0
#     )

#     results_taxi, final_weight_taxi, final_time_taxi, final_horizontal_distance_taxi, final_engine_power_takeoff, cumulative_fuel_consumed_taxi, total_carbon_emissions_taxi, total_co_emissions_taxi, total_nox_emissions_taxi, total_so2_emissions_taxi = simulate_taxi_phase(
#         taxi_params,
#         simple_wind_speed_scenario,
#         simple_crosswind_speed_scenario,
#         takeoff_params['initial_weight'],
#         initial_time,
#         initial_horizontal_distance,
#         cumulative_fuel_consumed=cumulative_fuel_consumed_turn_on,
#         total_carbon_emissions=total_carbon_emissions_turn_on,
#         total_co_emissions=total_co_emissions_turn_on,
#         total_nox_emissions=total_nox_emissions_turn_on,
#         total_so2_emissions=total_so2_emissions_turn_on
#     )


#     # Update initial conditions for the takeoff phase
#     takeoff_params['initial_weight'] = final_weight_turn_on  # Convert N to kg
#     initial_time = final_time_turn_on
#     initial_horizontal_distance = final_horizontal_distance_turn_on

#     # Run the take-off phase
#     results_takeoff, final_weight_takeoff, final_time_takeoff, final_horizontal_distance_takeoff, final_engine_power_takeoff, cumulative_fuel_consumed_takeoff, total_carbon_emissions_takeoff, total_co_emissions_takeoff, total_nox_emissions_takeoff, total_so2_emissions_takeoff = simulate_takeoff_phase(
#         takeoff_params,
#         simple_wind_speed_scenario,
#         simple_crosswind_speed_scenario,
#         takeoff_params['initial_weight'],
#         initial_time,
#         initial_horizontal_distance,
#         cumulative_fuel_consumed=cumulative_fuel_consumed_turn_on,
#         total_carbon_emissions=total_carbon_emissions_turn_on,
#         total_co_emissions=total_co_emissions_turn_on,
#         total_nox_emissions=total_nox_emissions_turn_on,
#         total_so2_emissions=total_so2_emissions_turn_on
#     )

#     # Update initial conditions for the additional climb phase (take_off_C_params)
#     take_off_C_params['initial_weight'] = final_weight_takeoff / 9.81  # Convert N to kg
#     initial_time = final_time_takeoff
#     initial_horizontal_distance = final_horizontal_distance_takeoff

#     # Run the additional climb phase (take_off_C_params)
#     results_take_off_C, final_weight_take_off_C, final_time_take_off_C, final_horizontal_distance_take_off_C, final_engine_power_take_off_C, cumulative_fuel_consumed_take_off_C, total_carbon_emissions_take_off_C, total_co_emissions_take_off_C, total_nox_emissions_take_off_C, total_so2_emissions_take_off_C = simulate_climb_phase(
#         take_off_C_params,
#         simple_wind_speed_scenario,
#         simple_crosswind_speed_scenario,
#         take_off_C_params['initial_weight'],
#         initial_time,
#         initial_horizontal_distance,
#         num_engines,
#         cumulative_fuel_consumed=cumulative_fuel_consumed_takeoff,
#         total_carbon_emissions=total_carbon_emissions_takeoff,
#         total_co_emissions=total_co_emissions_takeoff,
#         total_nox_emissions=total_nox_emissions_takeoff,
#         total_so2_emissions=total_so2_emissions_takeoff
#     )

#     # Update initial conditions for the first climb phase
#     phase1_params['initial_weight'] = final_weight_take_off_C / 9.81  # Convert N to kg
#     initial_time = final_time_take_off_C
#     initial_horizontal_distance = final_horizontal_distance_take_off_C

#     # Run the first phase of climb
#     results_phase1, final_weight_phase1, final_time_phase1, final_horizontal_distance_phase1, final_engine_power_phase1, cumulative_fuel_consumed_phase1, total_carbon_emissions_phase1, total_co_emissions_phase1, total_nox_emissions_phase1, total_so2_emissions_phase1 = simulate_climb_phase(
#         phase1_params,
#         simple_wind_speed_scenario,
#         simple_crosswind_speed_scenario,
#         phase1_params['initial_weight'],
#         initial_time,
#         initial_horizontal_distance,
#         num_engines,
#         cumulative_fuel_consumed=cumulative_fuel_consumed_take_off_C,
#         total_carbon_emissions=total_carbon_emissions_take_off_C,
#         total_co_emissions=total_co_emissions_take_off_C,
#         total_nox_emissions=total_nox_emissions_take_off_C,
#         total_so2_emissions=total_so2_emissions_take_off_C
#     )

#     # Update initial conditions for the second climb phase
#     phase2_params['initial_weight'] = final_weight_phase1 / 9.81  # Convert N to kg
#     initial_time = final_time_phase1
#     initial_horizontal_distance = final_horizontal_distance_phase1

#     # Run the second phase of climb
#     results_phase2, final_weight_phase2, final_time_phase2, final_horizontal_distance_phase2, final_engine_power_phase2, cumulative_fuel_consumed_phase2, total_carbon_emissions_phase2, total_co_emissions_phase2, total_nox_emissions_phase2, total_so2_emissions_phase2 = simulate_climb_phase(
#         phase2_params,
#         simple_wind_speed_scenario,
#         simple_crosswind_speed_scenario,
#         phase2_params['initial_weight'],
#         initial_time,
#         initial_horizontal_distance,
#         num_engines,
#         cumulative_fuel_consumed=cumulative_fuel_consumed_phase1,
#         total_carbon_emissions=total_carbon_emissions_phase1,
#         total_co_emissions=total_co_emissions_phase1,
#         total_nox_emissions=total_nox_emissions_phase1,
#         total_so2_emissions=total_so2_emissions_phase1
#     )

#     # Update initial conditions for the third climb phase
#     phase3_params['initial_weight'] = final_weight_phase2 / 9.81  # Convert N to kg
#     initial_time = final_time_phase2
#     initial_horizontal_distance = final_horizontal_distance_phase2

#     # Run the third phase of climb
#     results_phase3, final_weight_phase3, final_time_phase3, final_horizontal_distance_phase3,final_engine_power_phase3, cumulative_fuel_consumed_phase3, total_carbon_emissions_phase3, total_co_emissions_phase3, total_nox_emissions_phase3, total_so2_emissions_phase3 = simulate_climb_phase(
#         phase3_params,
#         simple_wind_speed_scenario,
#         simple_crosswind_speed_scenario,
#         phase3_params['initial_weight'],
#         initial_time,
#         initial_horizontal_distance,
#         num_engines,
#         cumulative_fuel_consumed=cumulative_fuel_consumed_phase2,
#         total_carbon_emissions=total_carbon_emissions_phase2,
#         total_co_emissions=total_co_emissions_phase2,
#         total_nox_emissions=total_nox_emissions_phase2,
#         total_so2_emissions=total_so2_emissions_phase2
#     )

#     # Update initial conditions for the cruise phase
#     cruise_params['initial_weight'] = final_weight_phase3 / 9.81  # Convert N to kg
#     initial_time = final_time_phase3
#     initial_horizontal_distance = final_horizontal_distance_phase3

#     # Run the cruise phase
#     results_cruise, final_weight_cruise, final_time_cruise, final_horizontal_distance_cruise, cumulative_fuel_consumed_cruise, total_carbon_emissions_cruise, total_co_emissions_cruise, total_nox_emissions_cruise, total_so2_emissions_cruise = simulate_cruise_phase(
#         cruise_params,
#         simple_wind_speed_scenario,
#         simple_crosswind_speed_scenario,
#         cruise_params['initial_weight'],
#         initial_time,
#         initial_horizontal_distance,
#         num_engines,
#         cumulative_fuel_consumed=cumulative_fuel_consumed_phase3,
#         total_carbon_emissions=total_carbon_emissions_phase3,
#         total_co_emissions=total_co_emissions_phase3,
#         total_nox_emissions=total_nox_emissions_phase3,
#         total_so2_emissions=total_so2_emissions_phase3
#     )

#     # Update initial conditions for the descent phase
#     descent_params['initial_weight'] = final_weight_cruise / 9.81  # Convert N to kg
#     initial_time = final_time_cruise
#     initial_horizontal_distance = final_horizontal_distance_cruise

#     # Run the descent phase
#     results_descent, final_weight_descent, final_time_descent, final_horizontal_distance_descent, cumulative_fuel_consumed_descent, total_carbon_emissions_descent, total_co_emissions_descent, total_nox_emissions_descent, total_so2_emissions_descent = simulate_descent_phase(
#         descent_params,
#         simple_wind_speed_scenario,
#         simple_crosswind_speed_scenario,
#         descent_params['initial_weight'],
#         initial_time,
#         initial_horizontal_distance,
#         num_engines,
#         cumulative_fuel_consumed=cumulative_fuel_consumed_cruise,
#         total_carbon_emissions=total_carbon_emissions_cruise,
#         total_co_emissions=total_co_emissions_cruise,
#         total_nox_emissions=total_nox_emissions_cruise,
#         total_so2_emissions=total_so2_emissions_cruise
#     )

#     # Update initial conditions for the approach and landing phase
#     approach_and_landing_params['initial_weight'] = final_weight_descent / 9.81  # Convert N to kg
#     initial_time = final_time_descent
#     initial_horizontal_distance = final_horizontal_distance_descent

#     # Run the approach and landing phase
#     results_approach_and_landing, final_weight_landing, final_time_landing, final_horizontal_distance_landing, cumulative_fuel_consumed_landing, total_carbon_emissions_landing, total_co_emissions_landing, total_nox_emissions_landing, total_so2_emissions_landing = simulate_approach_and_landing(
#         approach_and_landing_params,
#         simple_wind_speed_scenario,
#         simple_crosswind_speed_scenario,
#         approach_and_landing_params['initial_weight'],
#         initial_time,
#         initial_horizontal_distance,
#         num_engines,
#         cumulative_fuel_consumed=cumulative_fuel_consumed_descent,
#         total_carbon_emissions=total_carbon_emissions_descent,
#         total_co_emissions=total_co_emissions_descent,
#         total_nox_emissions=total_nox_emissions_descent,
#         total_so2_emissions=total_so2_emissions_descent
#     )

#     # Combine the results of all phases
#     combined_results = pd.concat([turn_on_results, results_taxi, results_takeoff, results_take_off_C, results_phase1, results_phase2, results_phase3, results_cruise, results_descent, results_approach_and_landing], ignore_index=True)
#     take_off_full_results = pd.concat([results_takeoff, results_take_off_C])
#     climb_full_results = pd.concat([results_phase1, results_phase2, results_phase3])

#     plot_results(take_off_full_results)

#     return combined_results

import pandas as pd
from simulations.takeoff_phase import simulate_takeoff_phase
from simulations.taxi_phase import simulate_taxi_phase
from simulations.climb_phase import simulate_climb_phase
from simulations.cruise_phase import simulate_cruise_phase
from simulations.descent_phase import simulate_descent_phase
from simulations.approach_and_landing_phase import simulate_approach_and_landing
from simulations.engine_turn_on_phase import engine_turn_on_phase
from utils import simple_wind_speed_scenario, simple_crosswind_speed_scenario

def run_all_phases(engine_turn_on_params, taxi_params, takeoff_params, take_off_C_params, phase1_params, phase2_params, phase3_params, cruise_params, descent_params, approach_and_landing_params, num_engines=2):
    # Run the engine turn-on phase
    turn_on_results, final_weight_turn_on, final_time_turn_on, final_horizontal_distance_turn_on, final_engine_power_turn_on, cumulative_fuel_consumed_turn_on, total_carbon_emissions_turn_on, total_co_emissions_turn_on, total_nox_emissions_turn_on, total_so2_emissions_turn_on = engine_turn_on_phase(
        engine_turn_on_params,
        0,  # Starting time
        0,  # Starting horizontal distance
        num_engines,
        cumulative_fuel_consumed_turn_on=0,
        total_carbon_emissions_turn_on=0,
        total_co_emissions_turn_on=0,
        total_nox_emissions_turn_on=0,
        total_so2_emissions_turn_on=0
    )

    # Update initial conditions for the taxi phase
    taxi_params['initial_weight'] = final_weight_turn_on  # Convert N to kg
    initial_time = final_time_turn_on
    initial_horizontal_distance = final_horizontal_distance_turn_on

    results_taxi, final_weight_taxi, final_time_taxi, final_horizontal_distance_taxi, final_engine_power_taxi, cumulative_fuel_consumed_taxi, total_carbon_emissions_taxi, total_co_emissions_taxi, total_nox_emissions_taxi, total_so2_emissions_taxi = simulate_taxi_phase(
        taxi_params,
        simple_wind_speed_scenario,
        simple_crosswind_speed_scenario,
        taxi_params['initial_weight'],
        initial_time,
        initial_horizontal_distance,
        cumulative_fuel_consumed=cumulative_fuel_consumed_turn_on,
        total_carbon_emissions=total_carbon_emissions_turn_on,
        total_co_emissions=total_co_emissions_turn_on,
        total_nox_emissions=total_nox_emissions_turn_on,
        total_so2_emissions=total_so2_emissions_turn_on
    )

    # Update initial conditions for the takeoff phase
    takeoff_params['initial_weight'] = final_weight_taxi/9.81  # Convert N to kg
    initial_time = final_time_taxi
    initial_horizontal_distance = final_horizontal_distance_taxi

    # Run the take-off phase
    results_takeoff, final_weight_takeoff, final_time_takeoff, final_horizontal_distance_takeoff, final_engine_power_takeoff, cumulative_fuel_consumed_takeoff, total_carbon_emissions_takeoff, total_co_emissions_takeoff, total_nox_emissions_takeoff, total_so2_emissions_takeoff = simulate_takeoff_phase(
        takeoff_params,
        simple_wind_speed_scenario,
        simple_crosswind_speed_scenario,
        takeoff_params['initial_weight'],
        initial_time,
        initial_horizontal_distance,
        cumulative_fuel_consumed=cumulative_fuel_consumed_taxi,
        total_carbon_emissions=total_carbon_emissions_taxi,
        total_co_emissions=total_co_emissions_taxi,
        total_nox_emissions=total_nox_emissions_taxi,
        total_so2_emissions=total_so2_emissions_taxi
    )

    # Update initial conditions for the additional climb phase (take_off_C_params)
    take_off_C_params['initial_weight'] = final_weight_takeoff / 9.81  # Convert N to kg
    initial_time = final_time_takeoff
    initial_horizontal_distance = final_horizontal_distance_takeoff

    # Run the additional climb phase (take_off_C_params)
    results_take_off_C, final_weight_take_off_C, final_time_take_off_C, final_horizontal_distance_take_off_C, final_engine_power_take_off_C, cumulative_fuel_consumed_take_off_C, total_carbon_emissions_take_off_C, total_co_emissions_take_off_C, total_nox_emissions_take_off_C, total_so2_emissions_take_off_C = simulate_climb_phase(
        take_off_C_params,
        simple_wind_speed_scenario,
        simple_crosswind_speed_scenario,
        take_off_C_params['initial_weight'],
        initial_time,
        initial_horizontal_distance,
        num_engines,
        cumulative_fuel_consumed=cumulative_fuel_consumed_takeoff,
        total_carbon_emissions=total_carbon_emissions_takeoff,
        total_co_emissions=total_co_emissions_takeoff,
        total_nox_emissions=total_nox_emissions_takeoff,
        total_so2_emissions=total_so2_emissions_takeoff
    )

    # Update initial conditions for the first climb phase
    phase1_params['initial_weight'] = final_weight_take_off_C / 9.81  # Convert N to kg
    initial_time = final_time_take_off_C
    initial_horizontal_distance = final_horizontal_distance_take_off_C

    # Run the first phase of climb
    results_phase1, final_weight_phase1, final_time_phase1, final_horizontal_distance_phase1, final_engine_power_phase1, cumulative_fuel_consumed_phase1, total_carbon_emissions_phase1, total_co_emissions_phase1, total_nox_emissions_phase1, total_so2_emissions_phase1 = simulate_climb_phase(
        phase1_params,
        simple_wind_speed_scenario,
        simple_crosswind_speed_scenario,
        phase1_params['initial_weight'],
        initial_time,
        initial_horizontal_distance,
        num_engines,
        cumulative_fuel_consumed=cumulative_fuel_consumed_take_off_C,
        total_carbon_emissions=total_carbon_emissions_take_off_C,
        total_co_emissions=total_co_emissions_take_off_C,
        total_nox_emissions=total_nox_emissions_take_off_C,
        total_so2_emissions=total_so2_emissions_take_off_C
    )

    # Update initial conditions for the second climb phase
    phase2_params['initial_weight'] = final_weight_phase1 / 9.81  # Convert N to kg
    initial_time = final_time_phase1
    initial_horizontal_distance = final_horizontal_distance_phase1

    # Run the second phase of climb
    results_phase2, final_weight_phase2, final_time_phase2, final_horizontal_distance_phase2, final_engine_power_phase2, cumulative_fuel_consumed_phase2, total_carbon_emissions_phase2, total_co_emissions_phase2, total_nox_emissions_phase2, total_so2_emissions_phase2 = simulate_climb_phase(
        phase2_params,
        simple_wind_speed_scenario,
        simple_crosswind_speed_scenario,
        phase2_params['initial_weight'],
        initial_time,
        initial_horizontal_distance,
        num_engines,
        cumulative_fuel_consumed=cumulative_fuel_consumed_phase1,
        total_carbon_emissions=total_carbon_emissions_phase1,
        total_co_emissions=total_co_emissions_phase1,
        total_nox_emissions=total_nox_emissions_phase1,
        total_so2_emissions=total_so2_emissions_phase1
    )

    # Update initial conditions for the third climb phase
    phase3_params['initial_weight'] = final_weight_phase2 / 9.81  # Convert N to kg
    initial_time = final_time_phase2
    initial_horizontal_distance = final_horizontal_distance_phase2

    # Run the third phase of climb
    results_phase3, final_weight_phase3, final_time_phase3, final_horizontal_distance_phase3, final_engine_power_phase3, cumulative_fuel_consumed_phase3, total_carbon_emissions_phase3, total_co_emissions_phase3, total_nox_emissions_phase3, total_so2_emissions_phase3 = simulate_climb_phase(
        phase3_params,
        simple_wind_speed_scenario,
        simple_crosswind_speed_scenario,
        phase3_params['initial_weight'],
        initial_time,
        initial_horizontal_distance,
        num_engines,
        cumulative_fuel_consumed=cumulative_fuel_consumed_phase2,
        total_carbon_emissions=total_carbon_emissions_phase2,
        total_co_emissions=total_co_emissions_phase2,
        total_nox_emissions=total_nox_emissions_phase2,
        total_so2_emissions=total_so2_emissions_phase2
    )

    # Update initial conditions for the cruise phase
    cruise_params['initial_weight'] = final_weight_phase3 / 9.81  # Convert N to kg
    initial_time = final_time_phase3
    initial_horizontal_distance = final_horizontal_distance_phase3

    # Run the cruise phase
    results_cruise, final_weight_cruise, final_time_cruise, final_horizontal_distance_cruise, cumulative_fuel_consumed_cruise, total_carbon_emissions_cruise, total_co_emissions_cruise, total_nox_emissions_cruise, total_so2_emissions_cruise = simulate_cruise_phase(
        cruise_params,
        simple_wind_speed_scenario,
        simple_crosswind_speed_scenario,
        cruise_params['initial_weight'],
        initial_time,
        initial_horizontal_distance,
        num_engines,
        cumulative_fuel_consumed=cumulative_fuel_consumed_phase3,
        total_carbon_emissions=total_carbon_emissions_phase3,
        total_co_emissions=total_co_emissions_phase3,
        total_nox_emissions=total_nox_emissions_phase3,
        total_so2_emissions=total_so2_emissions_phase3
    )

    # Update initial conditions for the descent phase
    descent_params['initial_weight'] = final_weight_cruise / 9.81  # Convert N to kg
    initial_time = final_time_cruise
    initial_horizontal_distance = final_horizontal_distance_cruise

    # Run the descent phase
    results_descent, final_weight_descent, final_time_descent, final_horizontal_distance_descent, cumulative_fuel_consumed_descent, total_carbon_emissions_descent, total_co_emissions_descent, total_nox_emissions_descent, total_so2_emissions_descent = simulate_descent_phase(
        descent_params,
        simple_wind_speed_scenario,
        simple_crosswind_speed_scenario,
        descent_params['initial_weight'],
        initial_time,
        initial_horizontal_distance,
        num_engines,
        cumulative_fuel_consumed=cumulative_fuel_consumed_cruise,
        total_carbon_emissions=total_carbon_emissions_cruise,
        total_co_emissions=total_co_emissions_cruise,
        total_nox_emissions=total_nox_emissions_cruise,
        total_so2_emissions=total_so2_emissions_cruise
    )

    # Update initial conditions for the approach and landing phase
    approach_and_landing_params['initial_weight'] = final_weight_descent / 9.81  # Convert N to kg
    initial_time = final_time_descent
    initial_horizontal_distance = final_horizontal_distance_descent

    # Run the approach and landing phase
    results_approach_and_landing, final_weight_landing, final_time_landing, final_horizontal_distance_landing, cumulative_fuel_consumed_landing, total_carbon_emissions_landing, total_co_emissions_landing, total_nox_emissions_landing, total_so2_emissions_landing = simulate_approach_and_landing(
        approach_and_landing_params,
        simple_wind_speed_scenario,
        simple_crosswind_speed_scenario,
        approach_and_landing_params['initial_weight'],
        initial_time,
        initial_horizontal_distance,
        num_engines,
        cumulative_fuel_consumed=cumulative_fuel_consumed_descent,
        total_carbon_emissions=total_carbon_emissions_descent,
        total_co_emissions=total_co_emissions_descent,
        total_nox_emissions=total_nox_emissions_descent,
        total_so2_emissions=total_so2_emissions_descent
    )

    # Combine the results of all phases
    combined_results = pd.concat([turn_on_results, results_taxi, results_takeoff, results_take_off_C, results_phase1, results_phase2, results_phase3, results_cruise, results_descent, results_approach_and_landing], ignore_index=True)
    take_off_full_results = pd.concat([results_takeoff, results_take_off_C])
    climb_full_results = pd.concat([results_phase1, results_phase2, results_phase3])

    return combined_results

# import pandas as pd
# from simulations.takeoff_phase import simulate_takeoff_phase
# from simulations.taxi_phase import simulate_taxi_phase
# from simulations.climb_phase import simulate_climb_phase
# from simulations.cruise_phase import simulate_cruise_phase
# from simulations.descent_phase import simulate_descent_phase
# from simulations.approach_and_landing_phase import simulate_approach_and_landing
# from simulations.engine_turn_on_phase import engine_turn_on_phase
# from utils import simple_wind_speed_scenario, simple_crosswind_speed_scenario

# def run_all_phases(engine_turn_on_params, taxi_params, takeoff_params, phase1_params, phase2_params, phase3_params, cruise_params, descent_params, approach_and_landing_params, num_engines=2):
#     print("Starting engine turn-on phase...")
#     turn_on_results, final_weight_turn_on, final_time_turn_on, final_horizontal_distance_turn_on, final_engine_power_turn_on, cumulative_fuel_consumed_turn_on, total_carbon_emissions_turn_on, total_co_emissions_turn_on, total_nox_emissions_turn_on, total_so2_emissions_turn_on = engine_turn_on_phase(
#         engine_turn_on_params,
#         0,  # Starting time
#         0,  # Starting horizontal distance
#         num_engines,
#         cumulative_fuel_consumed_turn_on=0,
#         total_carbon_emissions_turn_on=0,
#         total_co_emissions_turn_on=0,
#         total_nox_emissions_turn_on=0,
#         total_so2_emissions_turn_on=0
#     )

#     print("Completed engine turn-on phase. Starting taxi phase...")
#     # Update initial conditions for the taxi phase
#     taxi_params['initial_weight'] = final_weight_turn_on  # Convert N to kg
#     initial_time = final_time_turn_on
#     initial_horizontal_distance = final_horizontal_distance_turn_on

#     results_taxi, final_weight_taxi, final_time_taxi, final_horizontal_distance_taxi, final_engine_power_taxi, cumulative_fuel_consumed_taxi, total_carbon_emissions_taxi, total_co_emissions_taxi, total_nox_emissions_taxi, total_so2_emissions_taxi = simulate_taxi_phase(
#         taxi_params,
#         simple_wind_speed_scenario,
#         simple_crosswind_speed_scenario,
#         taxi_params['initial_weight'],
#         initial_time,
#         initial_horizontal_distance,
#         num_engines
#     )

#     print("Completed taxi phase. Starting takeoff phase...")
#     # Update initial conditions for the takeoff phase
#     takeoff_params['initial_weight'] = final_weight_taxi  # Convert N to kg
#     initial_time = final_time_taxi
#     initial_horizontal_distance = final_horizontal_distance_taxi

#     # Run the take-off phase
#     results_takeoff, final_weight_takeoff, final_time_takeoff, final_horizontal_distance_takeoff, final_engine_power_takeoff, cumulative_fuel_consumed_takeoff, total_carbon_emissions_takeoff, total_co_emissions_takeoff, total_nox_emissions_takeoff, total_so2_emissions_takeoff = simulate_takeoff_phase(
#         takeoff_params,
#         simple_wind_speed_scenario,
#         simple_crosswind_speed_scenario,
#         takeoff_params['initial_weight'],
#         initial_time,
#         initial_horizontal_distance,
#         warm_up_duration=takeoff_params['warmup_duration'],
#         previous_engine_power=final_engine_power_taxi,
#         cumulative_fuel_consumed=cumulative_fuel_consumed_taxi,
#         total_carbon_emissions=total_carbon_emissions_taxi,
#         total_co_emissions=total_co_emissions_taxi,
#         total_nox_emissions=total_nox_emissions_taxi,
#         total_so2_emissions=total_so2_emissions_taxi
#     )

#     print("Completed takeoff phase. Starting additional climb phase...")

#     # Update initial conditions for the additional climb phase (phase1_params)
#     phase1_params['initial_weight'] = final_weight_takeoff / 9.81  # Convert N to kg
#     initial_time = final_time_takeoff
#     initial_horizontal_distance = final_horizontal_distance_takeoff

#     # Run the additional climb phase (phase1_params)
#     results_phase1, final_weight_phase1, final_time_phase1, final_horizontal_distance_phase1, final_engine_power_phase1, cumulative_fuel_consumed_phase1, total_carbon_emissions_phase1, total_co_emissions_phase1, total_nox_emissions_phase1, total_so2_emissions_phase1 = simulate_climb_phase(
#         phase1_params,
#         simple_wind_speed_scenario,
#         simple_crosswind_speed_scenario,
#         phase1_params['initial_weight'],
#         initial_time,
#         initial_horizontal_distance,
#         num_engines,
#         cumulative_fuel_consumed=cumulative_fuel_consumed_takeoff,
#         total_carbon_emissions=total_carbon_emissions_takeoff,
#         total_co_emissions=total_co_emissions_takeoff,
#         total_nox_emissions=total_nox_emissions_takeoff,
#         total_so2_emissions=total_so2_emissions_takeoff
#     )

#     print("Completed additional climb phase. Starting second climb phase...")

#     # Update initial conditions for the second climb phase (phase2_params)
#     phase2_params['initial_weight'] = final_weight_phase1 / 9.81  # Convert N to kg
#     initial_time = final_time_phase1
#     initial_horizontal_distance = final_horizontal_distance_phase1

#     # Run the second climb phase (phase2_params)
#     results_phase2, final_weight_phase2, final_time_phase2, final_horizontal_distance_phase2, final_engine_power_phase2, cumulative_fuel_consumed_phase2, total_carbon_emissions_phase2, total_co_emissions_phase2, total_nox_emissions_phase2, total_so2_emissions_phase2 = simulate_climb_phase(
#         phase2_params,
#         simple_wind_speed_scenario,
#         simple_crosswind_speed_scenario,
#         phase2_params['initial_weight'],
#         initial_time,
#         initial_horizontal_distance,
#         num_engines,
#         cumulative_fuel_consumed=cumulative_fuel_consumed_phase1,
#         total_carbon_emissions=total_carbon_emissions_phase1,
#         total_co_emissions=total_co_emissions_phase1,
#         total_nox_emissions=total_nox_emissions_phase1,
#         total_so2_emissions=total_so2_emissions_phase1
#     )

#     print("Completed second climb phase. Starting third climb phase...")

#     # Update initial conditions for the third climb phase (phase3_params)
#     phase3_params['initial_weight'] = final_weight_phase2 / 9.81  # Convert N to kg
#     initial_time = final_time_phase2
#     initial_horizontal_distance = final_horizontal_distance_phase2

#     # Run the third climb phase (phase3_params)
#     results_phase3, final_weight_phase3, final_time_phase3, final_horizontal_distance_phase3, final_engine_power_phase3, cumulative_fuel_consumed_phase3, total_carbon_emissions_phase3, total_co_emissions_phase3, total_nox_emissions_phase3, total_so2_emissions_phase3 = simulate_climb_phase(
#         phase3_params,
#         simple_wind_speed_scenario,
#         simple_crosswind_speed_scenario,
#         phase3_params['initial_weight'],
#         initial_time,
#         initial_horizontal_distance,
#         num_engines,
#         cumulative_fuel_consumed=cumulative_fuel_consumed_phase2,
#         total_carbon_emissions=total_carbon_emissions_phase2,
#         total_co_emissions=total_co_emissions_phase2,
#         total_nox_emissions=total_nox_emissions_phase2,
#         total_so2_emissions=total_so2_emissions_phase2
#     )

#     print("Completed third climb phase. Starting cruise phase...")

#     # Update initial conditions for the cruise phase
#     cruise_params['initial_weight'] = final_weight_phase3 / 9.81  # Convert N to kg
#     initial_time = final_time_phase3
#     initial_horizontal_distance = final_horizontal_distance_phase3

#     # Run the cruise phase
#     results_cruise, final_weight_cruise, final_time_cruise, final_horizontal_distance_cruise, cumulative_fuel_consumed_cruise, total_carbon_emissions_cruise, total_co_emissions_cruise, total_nox_emissions_cruise, total_so2_emissions_cruise = simulate_cruise_phase(
#         cruise_params,
#         simple_wind_speed_scenario,
#         simple_crosswind_speed_scenario,
#         cruise_params['initial_weight'],
#         initial_time,
#         initial_horizontal_distance,
#         num_engines,
#         cumulative_fuel_consumed=cumulative_fuel_consumed_phase3,
#         total_carbon_emissions=total_carbon_emissions_phase3,
#         total_co_emissions=total_co_emissions_phase3,
#         total_nox_emissions=total_nox_emissions_phase3,
#         total_so2_emissions=total_so2_emissions_phase3
#     )

#     print("Completed cruise phase. Starting descent phase...")

#     # Update initial conditions for the descent phase
#     descent_params['initial_weight'] = final_weight_cruise / 9.81  # Convert N to kg
#     initial_time = final_time_cruise
#     initial_horizontal_distance = final_horizontal_distance_cruise

#     # Run the descent phase
#     results_descent, final_weight_descent, final_time_descent, final_horizontal_distance_descent, cumulative_fuel_consumed_descent, total_carbon_emissions_descent, total_co_emissions_descent, total_nox_emissions_descent, total_so2_emissions_descent = simulate_descent_phase(
#         descent_params,
#         simple_wind_speed_scenario,
#         simple_crosswind_speed_scenario,
#         descent_params['initial_weight'],
#         initial_time,
#         initial_horizontal_distance,
#         num_engines,
#         cumulative_fuel_consumed=cumulative_fuel_consumed_cruise,
#         total_carbon_emissions=total_carbon_emissions_cruise,
#         total_co_emissions=total_co_emissions_cruise,
#         total_nox_emissions=total_nox_emissions_cruise,
#         total_so2_emissions=total_so2_emissions_cruise
#     )

#     print("Completed descent phase. Starting approach and landing phase...")

#     # Update initial conditions for the approach and landing phase
#     approach_and_landing_params['initial_weight'] = final_weight_descent / 9.81  # Convert N to kg
#     initial_time = final_time_descent
#     initial_horizontal_distance = final_horizontal_distance_descent

#     # Run the approach and landing phase
#     results_approach_and_landing, final_weight_landing, final_time_landing, final_horizontal_distance_landing, cumulative_fuel_consumed_landing, total_carbon_emissions_landing, total_co_emissions_landing, total_nox_emissions_landing, total_so2_emissions_landing = simulate_approach_and_landing(
#         approach_and_landing_params,
#         simple_wind_speed_scenario,
#         simple_crosswind_speed_scenario,
#         approach_and_landing_params['initial_weight'],
#         initial_time,
#         initial_horizontal_distance,
#         num_engines,
#         cumulative_fuel_consumed=cumulative_fuel_consumed_descent,
#         total_carbon_emissions=total_carbon_emissions_descent,
#         total_co_emissions=total_co_emissions_descent,
#         total_nox_emissions=total_nox_emissions_descent,
#         total_so2_emissions=total_so2_emissions_descent
#     )

#     # Combine the results of all phases
#     combined_results = pd.concat([turn_on_results, results_taxi, results_takeoff, results_phase1, results_phase2, results_phase3, results_cruise, results_descent, results_approach_and_landing], ignore_index=True)

#     return combined_results
