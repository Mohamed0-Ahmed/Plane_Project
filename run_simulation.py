# import pandas as pd
# from simulations.takeoff_phase import simulate_takeoff_phase
# from simulations.climb_phase import simulate_climb_phase
# from simulations.cruise_phase import simulate_cruise_phase
# from simulations.descent_phase import simulate_descent_phase
# from simulations.approach_and_landing_phase import simulate_approach_and_landing
# from utils import simple_wind_speed_scenario, simple_crosswind_speed_scenario

# def run_all_phases(takeoff_params, take_off_C_params, phase1_params, phase2_params, phase3_params, cruise_params, descent_params, approach_and_landing_params, num_engines=2):
#     # Run the take-off phase
#     results_takeoff, final_weight_takeoff, final_time_takeoff, final_horizontal_distance_takeoff, final_engine_power_takeoff, cumulative_fuel_consumed_takeoff, total_carbon_emissions_takeoff, total_co_emissions_takeoff, total_nox_emissions_takeoff, total_so2_emissions_takeoff = simulate_takeoff_phase(
#         takeoff_params,
#         simple_wind_speed_scenario,
#         simple_crosswind_speed_scenario,
#         takeoff_params['initial_weight'],  # Starting weight
#         0,
#         0,
#         cumulative_fuel_consumed=0,
#         total_carbon_emissions=0,
#         total_co_emissions=0,
#         total_nox_emissions=0,
#         total_so2_emissions=0
#     )

#     # Update initial conditions for the additional climb phase (take_off_C_params)
#     take_off_C_params['initial_weight'] = final_weight_takeoff / 9.81  # Convert N to kg
#     initial_time = final_time_takeoff
#     initial_horizontal_distance = final_horizontal_distance_takeoff

#     # Run the additional climb phase (take_off_C_params)
#     # results_take_off_C, final_weight_take_off_C, final_time_take_off_C, final_horizontal_distance_take_off_C, final_engine_power_take_off_C, total_fuel_consumed_take_off_C, total_carbon_emissions_take_off_C, total_co_emissions_take_off_C, total_nox_emissions_take_off_C, total_so2_emissions_take_off_C = simulate_climb_phase(
#     #     take_off_C_params,
#     #     simple_wind_speed_scenario,
#     #     simple_crosswind_speed_scenario,
#     #     take_off_C_params['initial_weight'],
#     #     initial_time,
#     #     initial_horizontal_distance,
#     #     num_engines,
#     #     cumulative_fuel_consumed=cumulative_fuel_consumed_takeoff,
#     #     total_carbon_emissions=total_carbon_emissions_takeoff,
#     #     total_co_emissions=total_co_emissions_takeoff,
#     #     total_nox_emissions=total_nox_emissions_takeoff,
#     #     total_so2_emissions=total_so2_emissions_takeoff
#     # )

#         # Run the additional climb phase (take_off_C_params)
#     results_take_off_C, final_weight_take_off_C, final_time_take_off_C, final_horizontal_distance_take_off_C, final_engine_power_take_off_C, total_fuel_consumed_take_off_C, total_carbon_emissions_take_off_C, total_co_emissions_take_off_C, total_nox_emissions_take_off_C, total_so2_emissions_take_off_C = simulate_climb_phase(
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

#     # Update initial conditions for the first climb phase based on the additional climb phase
#     phase1_params['initial_weight'] = final_weight_take_off_C / 9.81  # Convert N to kg
#     initial_time = final_time_take_off_C
#     initial_horizontal_distance = final_horizontal_distance_take_off_C

#     # Run the first phase of climb
#     results_phase1, final_weight_phase1, final_time_phase1, final_horizontal_distance_phase1, final_engine_power_phase1, total_fuel_consumed_phase1, total_carbon_emissions_phase1, total_co_emissions_phase1, total_nox_emissions_phase1, total_so2_emissions_phase1 = simulate_climb_phase(
#         phase1_params,
#         simple_wind_speed_scenario,
#         simple_crosswind_speed_scenario,
#         phase1_params['initial_weight'],
#         initial_time,
#         initial_horizontal_distance,
#         num_engines,
#         cumulative_fuel_consumed=total_fuel_consumed_take_off_C,
#         total_carbon_emissions=total_carbon_emissions_take_off_C,
#         total_co_emissions=total_co_emissions_take_off_C,
#         total_nox_emissions=total_nox_emissions_take_off_C,
#         total_so2_emissions=total_so2_emissions_take_off_C
#     )

#     # Update initial conditions for the second climb phase based on the first climb phase
#     phase2_params['initial_weight'] = final_weight_phase1 / 9.81  # Convert N to kg
#     initial_time = final_time_phase1
#     initial_horizontal_distance = final_horizontal_distance_phase1

#     # Run the second phase of climb
#     results_phase2, final_weight_phase2, final_time_phase2, final_horizontal_distance_phase2, final_engine_power_phase2, total_fuel_consumed_phase2, total_carbon_emissions_phase2, total_co_emissions_phase2, total_nox_emissions_phase2, total_so2_emissions_phase2 = simulate_climb_phase(
#         phase2_params,
#         simple_wind_speed_scenario,
#         simple_crosswind_speed_scenario,
#         phase2_params['initial_weight'],
#         initial_time,
#         initial_horizontal_distance,
#         num_engines,
#         cumulative_fuel_consumed=total_fuel_consumed_phase1,
#         total_carbon_emissions=total_carbon_emissions_phase1,
#         total_co_emissions=total_co_emissions_phase1,
#         total_nox_emissions=total_nox_emissions_phase1,
#         total_so2_emissions=total_so2_emissions_phase1
#     )

#     # Update initial conditions for the third climb phase based on the second climb phase
#     phase3_params['initial_weight'] = final_weight_phase2 / 9.81  # Convert N to kg
#     initial_time = final_time_phase2
#     initial_horizontal_distance = final_horizontal_distance_phase2

#     # Run the third phase of climb
#     results_phase3, final_weight_phase3, final_time_phase3, final_horizontal_distance_phase3, _, total_fuel_consumed_phase3, total_carbon_emissions_phase3, total_co_emissions_phase3, total_nox_emissions_phase3, total_so2_emissions_phase3 = simulate_climb_phase(
#         phase3_params,
#         simple_wind_speed_scenario,
#         simple_crosswind_speed_scenario,
#         phase3_params['initial_weight'],
#         initial_time,
#         initial_horizontal_distance,
#         num_engines,
#         cumulative_fuel_consumed=total_fuel_consumed_phase2,
#         total_carbon_emissions=total_carbon_emissions_phase2,
#         total_co_emissions=total_co_emissions_phase2,
#         total_nox_emissions=total_nox_emissions_phase2,
#         total_so2_emissions=total_so2_emissions_phase2
#     )

#     # Run the cruise phase
#     results_cruise, final_weight_cruise, final_time_cruise, final_horizontal_distance_cruise, total_fuel_consumed_cruise, total_carbon_emissions_cruise, total_co_emissions_cruise, total_nox_emissions_cruise, total_so2_emissions_cruise = simulate_cruise_phase(
#         cruise_params,
#         simple_wind_speed_scenario,
#         simple_crosswind_speed_scenario,
#         final_weight_phase3 / 9.81,  # Convert N to kg
#         final_time_phase3,
#         final_horizontal_distance_phase3,
#         num_engines,
#         cumulative_fuel_consumed=total_fuel_consumed_phase3,
#         total_carbon_emissions=total_carbon_emissions_phase3,
#         total_co_emissions=total_co_emissions_phase3,
#         total_nox_emissions=total_nox_emissions_phase3,
#         total_so2_emissions=total_so2_emissions_phase3
#     )

#     # Run the descent phase
#     results_descent, final_weight_descent, final_time_descent, final_horizontal_distance_descent, total_fuel_consumed_descent, total_carbon_emissions_descent, total_co_emissions_descent, total_nox_emissions_descent, total_so2_emissions_descent = simulate_descent_phase(
#         descent_params,
#         simple_wind_speed_scenario,
#         simple_crosswind_speed_scenario,
#         final_weight_cruise / 9.81,  # Convert N to kg
#         final_time_cruise,
#         final_horizontal_distance_cruise,
#         num_engines,
#         cumulative_fuel_consumed=total_fuel_consumed_cruise,
#         total_carbon_emissions=total_carbon_emissions_cruise,
#         total_co_emissions=total_co_emissions_cruise,
#         total_nox_emissions=total_nox_emissions_cruise,
#         total_so2_emissions=total_so2_emissions_cruise
#     )

#     # Run the approach and landing phase
#     results_approach_and_landing, final_weight_landing, final_time_landing, final_horizontal_distance_landing, total_fuel_consumed_landing, total_carbon_emissions_landing, total_co_emissions_landing, total_nox_emissions_landing, total_so2_emissions_landing = simulate_approach_and_landing(
#         approach_and_landing_params,
#         simple_wind_speed_scenario,
#         simple_crosswind_speed_scenario,
#         final_weight_descent / 9.81,  # Convert N to kg
#         final_time_descent,
#         final_horizontal_distance_descent,
#         num_engines,
#         cumulative_fuel_consumed=total_fuel_consumed_descent,
#         total_carbon_emissions=total_carbon_emissions_descent,
#         total_co_emissions=total_co_emissions_descent,
#         total_nox_emissions=total_nox_emissions_descent,
#         total_so2_emissions=total_so2_emissions_descent
#     )

#     # Combine the results of all phases
#     combined_results = pd.concat([results_takeoff, results_take_off_C, results_phase1, results_phase2, results_phase3, results_cruise, results_descent, results_approach_and_landing], ignore_index=True)

#     return combined_results

# import pandas as pd
# from simulations.takeoff_phase import simulate_takeoff_phase
# from simulations.climb_phase import simulate_climb_phase
# from simulations.cruise_phase import simulate_cruise_phase
# from simulations.descent_phase import simulate_descent_phase
# from simulations.approach_and_landing_phase import simulate_approach_and_landing
# from simulations.engine_turn_on_phase import engine_turn_on_phase
# from utils import simple_wind_speed_scenario, simple_crosswind_speed_scenario

# def run_all_phases(engine_turn_on_params, takeoff_params, take_off_C_params, phase1_params, phase2_params, phase3_params, cruise_params, descent_params, approach_and_landing_params, num_engines=2):
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

#     # Update initial conditions for the takeoff phase
#     takeoff_params['initial_weight'] = final_weight_turn_on / 9.81  # Convert N to kg
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

#     # Run the climb phases (phase1, phase2, phase3)
#     results_phase1, final_weight_phase1, final_time_phase1, final_horizontal_distance_phase1, cumulative_fuel_consumed_phase1, total_carbon_emissions_phase1, total_co_emissions_phase1, total_nox_emissions_phase1, total_so2_emissions_phase1 = simulate_climb_phase(
#         phase1_params,
#         simple_wind_speed_scenario,
#         simple_crosswind_speed_scenario,
#         final_weight_take_off_C,
#         final_time_take_off_C,
#         final_horizontal_distance_take_off_C,
#         num_engines,
#         cumulative_fuel_consumed=cumulative_fuel_consumed_take_off_C,
#         total_carbon_emissions=total_carbon_emissions_take_off_C,
#         total_co_emissions=total_co_emissions_take_off_C,
#         total_nox_emissions=total_nox_emissions_take_off_C,
#         total_so2_emissions=total_so2_emissions_take_off_C
#     )

#     results_phase2, final_weight_phase2, final_time_phase2, final_horizontal_distance_phase2, cumulative_fuel_consumed_phase2, total_carbon_emissions_phase2, total_co_emissions_phase2, total_nox_emissions_phase2, total_so2_emissions_phase2 = simulate_climb_phase(
#         phase2_params,
#         simple_wind_speed_scenario,
#         simple_crosswind_speed_scenario,
#         final_weight_phase1,
#         final_time_phase1,
#         final_horizontal_distance_phase1,
#         num_engines,
#         cumulative_fuel_consumed=cumulative_fuel_consumed_phase1,
#         total_carbon_emissions=total_carbon_emissions_phase1,
#         total_co_emissions=total_co_emissions_phase1,
#         total_nox_emissions=total_nox_emissions_phase1,
#         total_so2_emissions=total_so2_emissions_phase1
#     )

#     results_phase3, final_weight_phase3, final_time_phase3, final_horizontal_distance_phase3, cumulative_fuel_consumed_phase3, total_carbon_emissions_phase3, total_co_emissions_phase3, total_nox_emissions_phase3, total_so2_emissions_phase3 = simulate_climb_phase(
#         phase3_params,
#         simple_wind_speed_scenario,
#         simple_crosswind_speed_scenario,
#         final_weight_phase2,
#         final_time_phase2,
#         final_horizontal_distance_phase2,
#         num_engines,
#         cumulative_fuel_consumed=cumulative_fuel_consumed_phase2,
#         total_carbon_emissions=total_carbon_emissions_phase2,
#         total_co_emissions=total_co_emissions_phase2,
#         total_nox_emissions=total_nox_emissions_phase2,
#         total_so2_emissions=total_so2_emissions_phase2
#     )

#     # Run the cruise phase
#     results_cruise, final_weight_cruise, final_time_cruise, final_horizontal_distance_cruise, cumulative_fuel_consumed_cruise, total_carbon_emissions_cruise, total_co_emissions_cruise, total_nox_emissions_cruise, total_so2_emissions_cruise = simulate_cruise_phase(
#         cruise_params,
#         simple_wind_speed_scenario,
#         simple_crosswind_speed_scenario,
#         final_weight_phase3 / 9.81,  # Convert N to kg
#         final_time_phase3,
#         final_horizontal_distance_phase3,
#         num_engines,
#         cumulative_fuel_consumed=cumulative_fuel_consumed_phase3,
#         total_carbon_emissions=total_carbon_emissions_phase3,
#         total_co_emissions=total_co_emissions_phase3,
#         total_nox_emissions=total_nox_emissions_phase3,
#         total_so2_emissions=total_so2_emissions_phase3
#     )

#     # Run the descent phase
#     results_descent, final_weight_descent, final_time_descent, final_horizontal_distance_descent, cumulative_fuel_consumed_descent, total_carbon_emissions_descent, total_co_emissions_descent, total_nox_emissions_descent, total_so2_emissions_descent = simulate_descent_phase(
#         descent_params,
#         simple_wind_speed_scenario,
#         simple_crosswind_speed_scenario,
#         final_weight_cruise / 9.81,  # Convert N to kg
#         final_time_cruise,
#         final_horizontal_distance_cruise,
#         num_engines,
#         cumulative_fuel_consumed=cumulative_fuel_consumed_cruise,
#         total_carbon_emissions=total_carbon_emissions_cruise,
#         total_co_emissions=total_co_emissions_cruise,
#         total_nox_emissions=total_nox_emissions_cruise,
#         total_so2_emissions=total_so2_emissions_cruise
#     )

#     # Run the approach and landing phase
#     results_approach_and_landing, final_weight_landing, final_time_landing, final_horizontal_distance_landing, cumulative_fuel_consumed_landing, total_carbon_emissions_landing, total_co_emissions_landing, total_nox_emissions_landing, total_so2_emissions_landing = simulate_approach_and_landing(
#         approach_and_landing_params,
#         simple_wind_speed_scenario,
#         simple_crosswind_speed_scenario,
#         final_weight_descent / 9.81,  # Convert N to kg
#         final_time_descent,
#         final_horizontal_distance_descent,
#         num_engines,
#         cumulative_fuel_consumed=cumulative_fuel_consumed_descent,
#         total_carbon_emissions=total_carbon_emissions_descent,
#         total_co_emissions=total_co_emissions_descent,
#         total_nox_emissions=total_nox_emissions_descent,
#         total_so2_emissions=total_so2_emissions_descent
#     )

#     # Combine the results of all phases
#     combined_results = pd.concat([turn_on_results, results_takeoff, results_take_off_C, results_phase1, results_phase2, results_phase3, results_cruise, results_descent, results_approach_and_landing], ignore_index=True)

#     return combined_results

import pandas as pd
from simulations.takeoff_phase import simulate_takeoff_phase
from simulations.climb_phase import simulate_climb_phase
from simulations.cruise_phase import simulate_cruise_phase
from simulations.descent_phase import simulate_descent_phase
from simulations.approach_and_landing_phase import simulate_approach_and_landing
from simulations.engine_turn_on_phase import engine_turn_on_phase
from utils import simple_wind_speed_scenario, simple_crosswind_speed_scenario

def run_all_phases(engine_turn_on_params, takeoff_params, take_off_C_params, phase1_params, phase2_params, phase3_params, cruise_params, descent_params, approach_and_landing_params, num_engines=2):
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

    # Update initial conditions for the takeoff phase
    takeoff_params['initial_weight'] = final_weight_turn_on / 9.81  # Convert N to kg
    initial_time = final_time_turn_on
    initial_horizontal_distance = final_horizontal_distance_turn_on

    # Run the take-off phase
    results_takeoff, final_weight_takeoff, final_time_takeoff, final_horizontal_distance_takeoff, final_engine_power_takeoff, cumulative_fuel_consumed_takeoff, total_carbon_emissions_takeoff, total_co_emissions_takeoff, total_nox_emissions_takeoff, total_so2_emissions_takeoff = simulate_takeoff_phase(
        takeoff_params,
        simple_wind_speed_scenario,
        simple_crosswind_speed_scenario,
        takeoff_params['initial_weight'],
        initial_time,
        initial_horizontal_distance,
        cumulative_fuel_consumed=cumulative_fuel_consumed_turn_on,
        total_carbon_emissions=total_carbon_emissions_turn_on,
        total_co_emissions=total_co_emissions_turn_on,
        total_nox_emissions=total_nox_emissions_turn_on,
        total_so2_emissions=total_so2_emissions_turn_on
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
    results_phase3, final_weight_phase3, final_time_phase3, final_horizontal_distance_phase3,final_engine_power_phase3, cumulative_fuel_consumed_phase3, total_carbon_emissions_phase3, total_co_emissions_phase3, total_nox_emissions_phase3, total_so2_emissions_phase3 = simulate_climb_phase(
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
    combined_results = pd.concat([turn_on_results, results_takeoff, results_take_off_C, results_phase1, results_phase2, results_phase3, results_cruise, results_descent, results_approach_and_landing], ignore_index=True)

    return combined_results
