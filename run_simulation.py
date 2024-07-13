# # import pandas as pd
# # from simulations.takeoff_phase import simulate_takeoff_phase
# # from simulations.taxi_phase import simulate_taxi_phase
# # from simulations.climb_phase import simulate_climb_phase
# # from simulations.interpolated_climb_phase import simulate_climb_phase_int
# # from simulations.cruise_phase import simulate_cruise_phase
# # from simulations.descent_phase import simulate_descent_phase
# # from simulations.approach_and_landing_phase import simulate_approach_and_landing
# # from simulations.engine_turn_on_phase import engine_turn_on_phase
# # from utils import simple_wind_speed_scenario, simple_crosswind_speed_scenario

# # def run_all_phases(engine_turn_on_params, taxi_params, takeoff_params, take_off_C_params, phase1_params, between_1_2_climb, phase2_params, between_2_3_climb, phase3_params, cruise_params, descent_params, approach_and_landing_params, taxi_params2, num_engines=2):
# #     # Run the engine turn-on phase
# #     initial_cumulative_battery_energy_consumed = 0
# #     total_required_batteries = 0

# #     turn_on_results, final_weight_turn_on, final_time_turn_on, final_horizontal_distance_turn_on, final_engine_power_turn_on, cumulative_fuel_consumed_turn_on, total_carbon_emissions_turn_on, total_co_emissions_turn_on, total_nox_emissions_turn_on, total_so2_emissions_turn_on = engine_turn_on_phase(
# #         engine_turn_on_params,
# #         0,  # Starting time
# #         0,  # Starting horizontal distance
# #         num_engines,
# #         cumulative_fuel_consumed_turn_on=0,
# #         total_carbon_emissions_turn_on=0,
# #         total_co_emissions_turn_on=0,
# #         total_nox_emissions_turn_on=0,
# #         total_so2_emissions_turn_on=0
# #     )
# #     print(f"After Turn-On Phase: Cumulative Fuel = {cumulative_fuel_consumed_turn_on}")

# #     # Update initial conditions for the taxi phase
# #     taxi_params['initial_weight'] = final_weight_turn_on  # Convert N to kg
# #     initial_time = final_time_turn_on
# #     initial_horizontal_distance = final_horizontal_distance_turn_on

# #     results_taxi, final_weight_taxi, final_time_taxi, final_horizontal_distance_taxi, final_engine_power_taxi, cumulative_fuel_consumed_taxi, total_carbon_emissions_taxi, total_co_emissions_taxi, total_nox_emissions_taxi, total_so2_emissions_taxi = simulate_taxi_phase(
# #         taxi_params,
# #         simple_wind_speed_scenario,
# #         simple_crosswind_speed_scenario,
# #         taxi_params['initial_weight'],
# #         initial_time,
# #         initial_horizontal_distance,
# #         cumulative_fuel_consumed=cumulative_fuel_consumed_turn_on,
# #         total_carbon_emissions=total_carbon_emissions_turn_on,
# #         total_co_emissions=total_co_emissions_turn_on,
# #         total_nox_emissions=total_nox_emissions_turn_on,
# #         total_so2_emissions=total_so2_emissions_turn_on
# #     )

# #     print(f"After Taxi Phase: Cumulative Fuel = {cumulative_fuel_consumed_taxi}")

# #     # Update initial conditions for the takeoff phase
# #     takeoff_params['initial_weight'] = final_weight_taxi / 9.81  # Convert N to kg
# #     initial_time = final_time_taxi
# #     initial_horizontal_distance = final_horizontal_distance_taxi

# #     # Run the take-off phase
# #     results_takeoff, final_weight_takeoff, final_time_takeoff, final_horizontal_distance_takeoff, final_engine_power_takeoff, cumulative_battery_energy_consumed_takeoff, cumulative_fuel_consumed_takeoff, total_carbon_emissions_takeoff, total_co_emissions_takeoff, total_nox_emissions_takeoff, total_so2_emissions_takeoff, required_batteries_takeoff = simulate_takeoff_phase(
# #         takeoff_params,
# #         simple_wind_speed_scenario,
# #         simple_crosswind_speed_scenario,
# #         takeoff_params['initial_weight'],
# #         initial_time,
# #         initial_horizontal_distance,
# #         cumulative_fuel_consumed=cumulative_fuel_consumed_taxi,
# #         total_carbon_emissions=total_carbon_emissions_taxi,
# #         total_co_emissions=total_co_emissions_taxi,
# #         total_nox_emissions=total_nox_emissions_taxi,
# #         total_so2_emissions=total_so2_emissions_taxi
# #     )

# #     # Update initial conditions for the additional climb phase (take_off_C_params)
# #     take_off_C_params['initial_weight'] = final_weight_takeoff / 9.81  # Convert N to kg
# #     initial_time = final_time_takeoff
# #     initial_horizontal_distance = final_horizontal_distance_takeoff
# #     total_required_batteries += required_batteries_takeoff

# #     print(f"battery count after take-off{required_batteries_takeoff}")

# #     # Run the additional climb phase (take_off_C_params)
# #     #results_takeoff, final_weight_takeoff, final_time_takeoff, final_horizontal_distance_takeoff, final_engine_power_takeoff, cumulative_battery_energy_consumed_takeoff, cumulative_fuel_consumed_takeoff, total_carbon_emissions_takeoff, total_co_emissions_takeoff, total_nox_emissions_takeoff, total_so2_emissions_takeoff, required_batteries_takeoff
# #     results_take_off_C, final_weight_take_off_C, final_time_take_off_C, final_horizontal_distance_take_off_C, final_engine_power_take_off_C, cumulative_battery_energy_consumed_takeoff_C, cumulative_fuel_consumed_take_off_C, total_carbon_emissions_take_off_C, total_co_emissions_take_off_C, total_nox_emissions_take_off_C, total_so2_emissions_take_off_C, required_batteries_takeoff_C= simulate_climb_phase(
# #         take_off_C_params,
# #         simple_wind_speed_scenario,
# #         simple_crosswind_speed_scenario,
# #         take_off_C_params['initial_weight'],
# #         initial_time,
# #         initial_horizontal_distance,
# #         num_engines,
# #         cumulative_fuel_consumed=cumulative_fuel_consumed_takeoff,
# #         total_carbon_emissions=total_carbon_emissions_takeoff,
# #         total_co_emissions=total_co_emissions_takeoff,
# #         total_nox_emissions=total_nox_emissions_takeoff,
# #         total_so2_emissions=total_so2_emissions_takeoff
# #     )

# #     # Update initial conditions for the first climb phase
# #     phase1_params['initial_weight'] = final_weight_take_off_C / 9.81  # Convert N to kg
# #     initial_time = final_time_take_off_C
# #     initial_horizontal_distance = final_horizontal_distance_take_off_C

# #     # Run the first phase of climb
# #     results_phase1, final_weight_phase1, final_time_phase1, final_horizontal_distance_phase1, final_engine_power_phase1, cumulative_battery_energy_consumed_takeoff_C, cumulative_fuel_consumed_phase1, total_carbon_emissions_phase1, total_co_emissions_phase1, total_nox_emissions_phase1, total_so2_emissions_phase1, required_batteries_phase1 = simulate_climb_phase(
# #         phase1_params,
# #         simple_wind_speed_scenario,
# #         simple_crosswind_speed_scenario,
# #         phase1_params['initial_weight'],
# #         initial_time,
# #         initial_horizontal_distance,
# #         num_engines,
# #         cumulative_fuel_consumed=cumulative_fuel_consumed_take_off_C,
# #         total_carbon_emissions=total_carbon_emissions_take_off_C,
# #         total_co_emissions=total_co_emissions_take_off_C,
# #         total_nox_emissions=total_nox_emissions_take_off_C,
# #         total_so2_emissions=total_so2_emissions_take_off_C
# #     )

# #     # Update initial conditions for the interpolated climb phase between the first and second climb phases
# #     between_1_2_climb['initial_weight'] = final_weight_phase1 / 9.81  # Convert N to kg
# #     initial_time = final_time_phase1
# #     initial_horizontal_distance = final_horizontal_distance_phase1

# #     # Run the interpolated climb phase between the first and second climb phases
# #     results_between_1_2_climb, final_weight_between_1_2_climb, final_time_between_1_2_climb, final_horizontal_distance_between_1_2_climb, final_engine_power_between_1_2_climb, cumulative_battery_energy_consumed_1_2_climb, cumulative_fuel_consumed_between_1_2_climb, total_carbon_emissions_between_1_2_climb, total_co_emissions_between_1_2_climb, total_nox_emissions_between_1_2_climb, total_so2_emissions_between_1_2_climb, final_altitude_between_1_2_climb, required_batteries_1_2_climb = simulate_climb_phase_int(
# #         between_1_2_climb,
# #         simple_wind_speed_scenario,
# #         simple_crosswind_speed_scenario,
# #         between_1_2_climb['initial_weight'],
# #         initial_time,
# #         initial_horizontal_distance,
# #         between_1_2_climb['initial_roc'],
# #         between_1_2_climb['final_roc'],
# #         between_1_2_climb['roc_transition_duration'],
# #         num_engines,
# #         cumulative_fuel_consumed=cumulative_fuel_consumed_phase1,
# #         total_carbon_emissions=total_carbon_emissions_phase1,
# #         total_co_emissions=total_co_emissions_phase1,
# #         total_nox_emissions=total_nox_emissions_phase1,
# #         total_so2_emissions=total_so2_emissions_phase1
# #     )

# #     # Update initial conditions for the second climb phase
# #     phase2_params['initial_weight'] = final_weight_between_1_2_climb / 9.81  # Convert N to kg
# #     initial_time = final_time_between_1_2_climb
# #     phase2_params['initial_altitude'] = final_altitude_between_1_2_climb * 3.281  # Update initial altitude
# #     initial_horizontal_distance = final_horizontal_distance_between_1_2_climb

# #     # Run the second phase of climb
# #     results_phase2, final_weight_phase2, final_time_phase2, final_horizontal_distance_phase2, final_engine_power_phase2,cumulative_battery_energy_consumed_takeoff_C, cumulative_fuel_consumed_phase2, total_carbon_emissions_phase2, total_co_emissions_phase2, total_nox_emissions_phase2, total_so2_emissions_phase2, required_batteries_takeoff_C = simulate_climb_phase(
# #         phase2_params,
# #         simple_wind_speed_scenario,
# #         simple_crosswind_speed_scenario,
# #         phase2_params['initial_weight'],
# #         initial_time,
# #         initial_horizontal_distance,
# #         num_engines,
# #         cumulative_fuel_consumed=cumulative_fuel_consumed_between_1_2_climb,
# #         total_carbon_emissions=total_carbon_emissions_between_1_2_climb,
# #         total_co_emissions=total_co_emissions_between_1_2_climb,
# #         total_nox_emissions=total_nox_emissions_between_1_2_climb,
# #         total_so2_emissions=total_so2_emissions_between_1_2_climb
# #     )

# #     # Update initial conditions for the interpolation phase between the second and third climb phases
# #     between_2_3_climb['initial_weight'] = final_weight_phase2 / 9.81  # Convert N to kg
# #     initial_time = final_time_phase2
# #     initial_horizontal_distance = final_horizontal_distance_phase2

# #     # Run the interpolation phase between the second and third climb phases
# #     results_between_2_3_climb, final_weight_between_2_3_climb, final_time_between_2_3_climb, final_horizontal_distance_between_2_3_climb, final_engine_power_between_2_3_climb, cumulative_battery_energy_consumed_2_3_climb, cumulative_fuel_consumed_between_2_3_climb, total_carbon_emissions_between_2_3_climb, total_co_emissions_between_2_3_climb, total_nox_emissions_between_2_3_climb, total_so2_emissions_between_2_3_climb, final_altitude_between_2_3_climb, required_batteries_2_3_climb = simulate_climb_phase_int(
# #         between_2_3_climb,
# #         simple_wind_speed_scenario,
# #         simple_crosswind_speed_scenario,
# #         between_2_3_climb['initial_weight'],
# #         initial_time,
# #         initial_horizontal_distance,
# #         between_2_3_climb['initial_roc'],
# #         between_2_3_climb['final_roc'],
# #         between_2_3_climb['roc_transition_duration'],
# #         num_engines,
# #         cumulative_fuel_consumed=cumulative_fuel_consumed_phase2,
# #         total_carbon_emissions=total_carbon_emissions_phase2,
# #         total_co_emissions=total_co_emissions_phase2,
# #         total_nox_emissions=total_nox_emissions_phase2,
# #         total_so2_emissions=total_so2_emissions_phase2
# #     )

# #     # Update initial conditions for the third climb phase
# #     phase3_params['initial_weight'] = final_weight_between_2_3_climb / 9.81  # Convert N to kg
# #     phase3_params['initial_altitude'] = final_altitude_between_2_3_climb * 3.281  # Update initial altitude
# #     initial_time = final_time_between_2_3_climb
# #     initial_horizontal_distance = final_horizontal_distance_between_2_3_climb

# #     # Run the third phase of climb
# #     results_phase3, final_weight_phase3, final_time_phase3, final_horizontal_distance_phase3, final_engine_power_phase3, cumulative_battery_energy_consumed_takeoff_C, cumulative_fuel_consumed_phase3, total_carbon_emissions_phase3, total_co_emissions_phase3, total_nox_emissions_phase3, total_so2_emissions_phase3, required_batteries_takeoff_C = simulate_climb_phase(
# #         phase3_params,
# #         simple_wind_speed_scenario,
# #         simple_crosswind_speed_scenario,
# #         phase3_params['initial_weight'],
# #         initial_time,
# #         initial_horizontal_distance,
# #         num_engines,
# #         cumulative_fuel_consumed=cumulative_fuel_consumed_between_2_3_climb,
# #         total_carbon_emissions=total_carbon_emissions_between_2_3_climb,
# #         total_co_emissions=total_co_emissions_between_2_3_climb,
# #         total_nox_emissions=total_nox_emissions_between_2_3_climb,
# #         total_so2_emissions=total_so2_emissions_between_2_3_climb
# #     )

# #     # Update initial conditions for the cruise phase
# #     cruise_params['initial_weight'] = final_weight_phase3 / 9.81  # Convert N to kg
# #     initial_time = final_time_phase3
# #     initial_horizontal_distance = final_horizontal_distance_phase3

# #     # Run the cruise phase
# #     results_cruise, final_weight_cruise, final_time_cruise, final_horizontal_distance_cruise, cumulative_battery_energy_consumed_cruise, cumulative_fuel_consumed_cruise, total_carbon_emissions_cruise, total_co_emissions_cruise, total_nox_emissions_cruise, total_so2_emissions_cruise, required_batteries_cruise = simulate_cruise_phase(
# #         cruise_params,
# #         simple_wind_speed_scenario,
# #         simple_crosswind_speed_scenario,
# #         cruise_params['initial_weight'],
# #         initial_time,
# #         initial_horizontal_distance,
# #         num_engines,
# #         cumulative_fuel_consumed=cumulative_fuel_consumed_phase3,
# #         total_carbon_emissions=total_carbon_emissions_phase3,
# #         total_co_emissions=total_co_emissions_phase3,
# #         total_nox_emissions=total_nox_emissions_phase3,
# #         total_so2_emissions=total_so2_emissions_phase3
# #     )

# #     # Update initial conditions for the descent phase
# #     descent_params['initial_weight'] = final_weight_cruise / 9.81  # Convert N to kg
# #     initial_time = final_time_cruise
# #     initial_horizontal_distance = final_horizontal_distance_cruise

# #     # Run the descent phase
# #     results_descent, final_weight_descent, final_time_descent, final_horizontal_distance_descent, cumulative_fuel_consumed_descent, total_carbon_emissions_descent, total_co_emissions_descent, total_nox_emissions_descent, total_so2_emissions_descent = simulate_descent_phase(
# #         descent_params,
# #         simple_wind_speed_scenario,
# #         simple_crosswind_speed_scenario,
# #         descent_params['initial_weight'],
# #         initial_time,
# #         initial_horizontal_distance,
# #         num_engines,
# #         cumulative_fuel_consumed=cumulative_fuel_consumed_cruise,
# #         total_carbon_emissions=total_carbon_emissions_cruise,
# #         total_co_emissions=total_co_emissions_cruise,
# #         total_nox_emissions=total_nox_emissions_cruise,
# #         total_so2_emissions=total_so2_emissions_cruise
# #     )

# #     # Update initial conditions for the approach and landing phase
# #     approach_and_landing_params['initial_weight'] = final_weight_descent / 9.81  # Convert N to kg
# #     initial_time = final_time_descent
# #     initial_horizontal_distance = final_horizontal_distance_descent

# #     # Run the approach and landing phase
# #     results_approach_and_landing, final_weight_landing, final_time_landing, final_horizontal_distance_landing, cumulative_fuel_consumed_landing, total_carbon_emissions_landing, total_co_emissions_landing, total_nox_emissions_landing, total_so2_emissions_landing = simulate_approach_and_landing(
# #         approach_and_landing_params,
# #         simple_wind_speed_scenario,
# #         simple_crosswind_speed_scenario,
# #         approach_and_landing_params['initial_weight'],
# #         initial_time,
# #         initial_horizontal_distance,
# #         num_engines,
# #         cumulative_fuel_consumed=cumulative_fuel_consumed_descent,
# #         total_carbon_emissions=total_carbon_emissions_descent,
# #         total_co_emissions=total_co_emissions_descent,
# #         total_nox_emissions=total_nox_emissions_descent,
# #         total_so2_emissions=total_so2_emissions_descent
# #     )
# #     print(f"After Approach and Landing Phase: Cumulative Fuel = {cumulative_fuel_consumed_landing}")

# #     taxi_params2['initial_weight'] = final_weight_landing / 9.81  # Convert N to kg
# #     initial_time = final_time_landing
# #     initial_horizontal_distance = final_horizontal_distance_landing


# #     #Update initial conditions for the taxi phase
# #     results_taxi2, final_weight_taxi2, final_time_taxi2, final_horizontal_distance_taxi2, final_engine_power_taxi, cumulative_fuel_consumed_taxi2, total_carbon_emissions_taxi2, total_co_emissions_taxi2, total_nox_emissions_taxi2, total_so2_emissions_taxi2 = simulate_taxi_phase(
# #         taxi_params2,
# #         simple_wind_speed_scenario,
# #         simple_crosswind_speed_scenario,
# #         taxi_params2['initial_weight'],
# #         initial_time,
# #         initial_horizontal_distance,
# #         cumulative_fuel_consumed=cumulative_fuel_consumed_landing,
# #         total_carbon_emissions=total_carbon_emissions_landing,
# #         total_co_emissions=total_co_emissions_landing,
# #         total_nox_emissions=total_nox_emissions_landing,
# #         total_so2_emissions=total_so2_emissions_landing
# #     )
# #     print(f"After Second Taxi Phase: Cumulative Fuel = {cumulative_fuel_consumed_taxi2}")


# #     # Combine the results of all phases
# #     combined_results = pd.concat([turn_on_results, results_taxi, results_takeoff, results_take_off_C, results_phase1, results_between_1_2_climb, results_phase2, results_between_2_3_climb, results_phase3, results_cruise, results_descent, results_approach_and_landing, results_taxi2], ignore_index=True)
# #     take_off_full_results = pd.concat([results_takeoff, results_take_off_C])
# #     climb_full_results = pd.concat([results_phase1, results_between_1_2_climb, results_phase2, results_between_2_3_climb, results_phase3])

# #     return combined_results

# import pandas as pd
# from simulations.takeoff_phase import simulate_takeoff_phase
# from simulations.taxi_phase import simulate_taxi_phase
# from simulations.climb_phase import simulate_climb_phase
# from simulations.interpolated_climb_phase import simulate_climb_phase_int
# from simulations.cruise_phase import simulate_cruise_phase
# from simulations.descent_phase import simulate_descent_phase
# from simulations.approach_and_landing_phase import simulate_approach_and_landing
# from simulations.engine_turn_on_phase import engine_turn_on_phase
# from utils import simple_wind_speed_scenario, simple_crosswind_speed_scenario

# def calculate_total_distance_excluding_cruise(engine_turn_on_params, taxi_params, takeoff_params, take_off_C_params, phase1_params, between_1_2_climb, phase2_params, between_2_3_climb, phase3_params, descent_params, approach_and_landing_params, taxi_params2, num_engines=2):
#     # Run the engine turn-on phase
#     turn_on_results, final_weight_turn_on, final_time_turn_on, final_horizontal_distance_turn_on, _, _, _, _, _, _ = engine_turn_on_phase(
#         engine_turn_on_params,
#         0,  # Starting time
#         0,  # Starting horizontal distance
#         num_engines
#     )

#     # Update initial conditions for the taxi phase
#     taxi_params['initial_weight'] = final_weight_turn_on  # Convert N to kg
#     initial_time = final_time_turn_on
#     #initial_horizontal_distance = final_horizontal_distance_turn_on

#     results_taxi, final_weight_taxi, final_time_taxi, final_horizontal_distance_taxi, _, _, _, _, _, _ = simulate_taxi_phase(
#         taxi_params,
#         simple_wind_speed_scenario,
#         simple_crosswind_speed_scenario,
#         taxi_params['initial_weight'],
#         initial_time,
#         0,
#         cumulative_fuel_consumed=0,
#         total_carbon_emissions=0,
#         total_co_emissions=0,
#         total_nox_emissions=0,
#         total_so2_emissions=0
#     )

#     # Update initial conditions for the takeoff phase
#     takeoff_params['initial_weight'] = final_weight_taxi / 9.81  # Convert N to kg
#     initial_time = final_time_taxi
#     #initial_horizontal_distance = final_horizontal_distance_taxi

#     # Run the take-off phase
#     results_takeoff, final_weight_takeoff, final_time_takeoff, final_horizontal_distance_takeoff, _, _, _, _, _, _, _, _ = simulate_takeoff_phase(
#         takeoff_params,
#         simple_wind_speed_scenario,
#         simple_crosswind_speed_scenario,
#         takeoff_params['initial_weight'],
#         initial_time,
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
#     #initial_horizontal_distance = final_horizontal_distance_takeoff

#     # Run the additional climb phase (take_off_C_params)
#     results_take_off_C, final_weight_take_off_C, final_time_take_off_C, final_horizontal_distance_take_off_C, _, _, _, _, _, _, _, _ = simulate_climb_phase(
#         take_off_C_params,
#         simple_wind_speed_scenario,
#         simple_crosswind_speed_scenario,
#         take_off_C_params['initial_weight'],
#         initial_time,
#         0,
#         num_engines,
#         cumulative_fuel_consumed=0,
#         total_carbon_emissions=0,
#         total_co_emissions=0,
#         total_nox_emissions=0,
#         total_so2_emissions=0
#     )

#     # Update initial conditions for the first climb phase
#     phase1_params['initial_weight'] = final_weight_take_off_C / 9.81  # Convert N to kg
#     initial_time = final_time_take_off_C
#     #initial_horizontal_distance = final_horizontal_distance_take_off_C

#     # Run the first phase of climb
#     results_phase1, final_weight_phase1, final_time_phase1, final_horizontal_distance_phase1, _, _, _, _, _, _, _, _ = simulate_climb_phase(
#         phase1_params,
#         simple_wind_speed_scenario,
#         simple_crosswind_speed_scenario,
#         phase1_params['initial_weight'],
#         initial_time,
#         0,
#         num_engines,
#         cumulative_fuel_consumed=0,
#         total_carbon_emissions=0,
#         total_co_emissions=0,
#         total_nox_emissions=0,
#         total_so2_emissions=0
#     )

#     # Update initial conditions for the interpolated climb phase between the first and second climb phases
#     between_1_2_climb['initial_weight'] = final_weight_phase1 / 9.81  # Convert N to kg
#     initial_time = final_time_phase1
#     #initial_horizontal_distance = final_horizontal_distance_phase1

#     # Run the interpolated climb phase between the first and second climb phases
#     results_between_1_2_climb, final_weight_between_1_2_climb, final_time_between_1_2_climb, final_horizontal_distance_between_1_2_climb, _, _, _, _, _, _,_, final_altitude_between_1_2_climb, _ = simulate_climb_phase_int(
#         between_1_2_climb,
#         simple_wind_speed_scenario,
#         simple_crosswind_speed_scenario,
#         between_1_2_climb['initial_weight'],
#         initial_time,
#         0,
#         between_1_2_climb['initial_roc'],
#         between_1_2_climb['final_roc'],
#         between_1_2_climb['roc_transition_duration'],
#         num_engines,
#         cumulative_fuel_consumed=0,
#         total_carbon_emissions=0,
#         total_co_emissions=0,
#         total_nox_emissions=0,
#         total_so2_emissions=0
#     )

#     # Update initial conditions for the second climb phase
#     phase2_params['initial_weight'] = final_weight_between_1_2_climb / 9.81  # Convert N to kg
#     initial_time = final_time_between_1_2_climb
#     phase2_params['initial_altitude'] = final_altitude_between_1_2_climb * 3.281  # Update initial altitude
#     #initial_horizontal_distance = final_horizontal_distance_between_1_2_climb

#     # Run the second phase of climb
#     results_phase2, final_weight_phase2, final_time_phase2, final_horizontal_distance_phase2, _, _, _, _, _, _, _, _ = simulate_climb_phase(
#         phase2_params,
#         simple_wind_speed_scenario,
#         simple_crosswind_speed_scenario,
#         phase2_params['initial_weight'],
#         initial_time,
#         0,
#         num_engines,
#         cumulative_fuel_consumed=0,
#         total_carbon_emissions=0,
#         total_co_emissions=0,
#         total_nox_emissions=0,
#         total_so2_emissions=0
#     )

#     # Update initial conditions for the interpolation phase between the second and third climb phases
#     between_2_3_climb['initial_weight'] = final_weight_phase2 / 9.81  # Convert N to kg
#     initial_time = final_time_phase2
#     #initial_horizontal_distance = final_horizontal_distance_phase2

#     # Run the interpolation phase between the second and third climb phases
#     results_between_2_3_climb, final_weight_between_2_3_climb, final_time_between_2_3_climb, final_horizontal_distance_between_2_3_climb, _, _, _, _, _, _,_, final_altitude_between_2_3_climb, _ = simulate_climb_phase_int(
#         between_2_3_climb,
#         simple_wind_speed_scenario,
#         simple_crosswind_speed_scenario,
#         between_2_3_climb['initial_weight'],
#         initial_time,
#         0,
#         between_2_3_climb['initial_roc'],
#         between_2_3_climb['final_roc'],
#         between_2_3_climb['roc_transition_duration'],
#         num_engines,
#         cumulative_fuel_consumed=0,
#         total_carbon_emissions=0,
#         total_co_emissions=0,
#         total_nox_emissions=0,
#         total_so2_emissions=0
#     )

#     # Update initial conditions for the third climb phase
#     phase3_params['initial_weight'] = final_weight_between_2_3_climb / 9.81  # Convert N to kg
#     phase3_params['initial_altitude'] = final_altitude_between_2_3_climb * 3.281  # Update initial altitude
#     initial_time = final_time_between_2_3_climb
#     #initial_horizontal_distance = final_horizontal_distance_between_2_3_climb

#     # Run the third phase of climb
#     results_phase3, final_weight_phase3, final_time_phase3, final_horizontal_distance_phase3, _, _, _, _, _, _, _, _ = simulate_climb_phase(
#         phase3_params,
#         simple_wind_speed_scenario,
#         simple_crosswind_speed_scenario,
#         phase3_params['initial_weight'],
#         initial_time,
#         0,
#         num_engines,
#         cumulative_fuel_consumed=0,
#         total_carbon_emissions=0,
#         total_co_emissions=0,
#         total_nox_emissions=0,
#         total_so2_emissions=0
#     )

#     # Update initial conditions for the descent phase
#     descent_params['initial_weight'] = final_weight_phase3 / 9.81  # Convert N to kg
#     initial_time = final_time_phase3
#     #initial_horizontal_distance = final_horizontal_distance_phase3

#     # Run the descent phase
#     results_descent, final_weight_descent, final_time_descent, final_horizontal_distance_descent, _, _, _, _, _ = simulate_descent_phase(
#         descent_params,
#         simple_wind_speed_scenario,
#         simple_crosswind_speed_scenario,
#         descent_params['initial_weight'],
#         initial_time,
#         0,
#         num_engines,
#         cumulative_fuel_consumed=0,
#         total_carbon_emissions=0,
#         total_co_emissions=0,
#         total_nox_emissions=0,
#         total_so2_emissions=0
#     )

#     # Update initial conditions for the approach and landing phase
#     approach_and_landing_params['initial_weight'] = final_weight_descent / 9.81  # Convert N to kg
#     initial_time = final_time_descent
#     #initial_horizontal_distance = final_horizontal_distance_descent

#     # Run the approach and landing phase
#     results_approach_and_landing, final_weight_landing, final_time_landing, final_horizontal_distance_landing, _, _, _, _,_ = simulate_approach_and_landing(
#         approach_and_landing_params,
#         simple_wind_speed_scenario,
#         simple_crosswind_speed_scenario,
#         approach_and_landing_params['initial_weight'],
#         initial_time,
#         0,
#         num_engines,
#         cumulative_fuel_consumed=0,
#         total_carbon_emissions=0,
#         total_co_emissions=0,
#         total_nox_emissions=0,
#         total_so2_emissions=0
#     )

#     # Update initial conditions for the second taxi phase
#     taxi_params2['initial_weight'] = final_weight_landing / 9.81  # Convert N to kg
#     initial_time = final_time_landing
#     #initial_horizontal_distance = final_horizontal_distance_landing

#     # Run the second taxi phase
#     results_taxi2, final_weight_taxi2, final_time_taxi2, final_horizontal_distance_taxi2, _, _, _, _, _, _  = simulate_taxi_phase(
#         taxi_params2,
#         simple_wind_speed_scenario,
#         simple_crosswind_speed_scenario,
#         taxi_params2['initial_weight'],
#         initial_time,
#         0,
#         cumulative_fuel_consumed=0,
#         total_carbon_emissions=0,
#         total_co_emissions=0,
#         total_nox_emissions=0,
#         total_so2_emissions=0
#     )

#     # Sum the total horizontal distance excluding the cruise phase
#     total_distance_excluding_cruise = (  
#                                        final_horizontal_distance_takeoff + final_horizontal_distance_take_off_C + 
#                                        final_horizontal_distance_phase1 + final_horizontal_distance_between_1_2_climb + 
#                                        final_horizontal_distance_phase2 + final_horizontal_distance_between_2_3_climb + 
#                                        final_horizontal_distance_phase3 + final_horizontal_distance_descent 
#                                        )

#     return total_distance_excluding_cruise

# def run_all_phases(engine_turn_on_params, taxi_params, takeoff_params, take_off_C_params, phase1_params, between_1_2_climb, phase2_params, between_2_3_climb, phase3_params, cruise_params, descent_params, approach_and_landing_params, taxi_params2, total_flight_distance, num_engines=2):
#     # Calculate the total distance excluding the cruise phase
#     # total_distance_excluding_cruise = calculate_total_distance_excluding_cruise(
#     #     engine_turn_on_params, taxi_params, takeoff_params, take_off_C_params, phase1_params, 
#     #     between_1_2_climb, phase2_params, between_2_3_climb, phase3_params, descent_params, 
#     #     approach_and_landing_params, taxi_params2, num_engines
#     # )

#     # # Calculate the required cruise distance
#     # required_cruise_distance = total_flight_distance - total_distance_excluding_cruise
#     # cruise_params['cruise_distance'] = required_cruise_distance / 1000  # Convert to km

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

#     print(f"After Turn-On Phase: Cumulative Fuel = {cumulative_fuel_consumed_turn_on}")

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
#         cumulative_fuel_consumed=cumulative_fuel_consumed_turn_on,
#         total_carbon_emissions=total_carbon_emissions_turn_on,
#         total_co_emissions=total_co_emissions_turn_on,
#         total_nox_emissions=total_nox_emissions_turn_on,
#         total_so2_emissions=total_so2_emissions_turn_on
#     )

#     print(f"After Taxi Phase: Cumulative Fuel = {cumulative_fuel_consumed_taxi}")

#     # Update initial conditions for the takeoff phase
#     takeoff_params['initial_weight'] = final_weight_taxi / 9.81  # Convert N to kg
#     initial_time = final_time_taxi
#     initial_horizontal_distance = final_horizontal_distance_taxi

#     # Run the take-off phase
#     results_takeoff, final_weight_takeoff, final_time_takeoff, final_horizontal_distance_takeoff, final_engine_power_takeoff, cumulative_battery_energy_consumed_takeoff, cumulative_fuel_consumed_takeoff, total_carbon_emissions_takeoff, total_co_emissions_takeoff, total_nox_emissions_takeoff, total_so2_emissions_takeoff, required_batteries_takeoff = simulate_takeoff_phase(
#         takeoff_params,
#         simple_wind_speed_scenario,
#         simple_crosswind_speed_scenario,
#         takeoff_params['initial_weight'],
#         initial_time,
#         initial_horizontal_distance,
#         cumulative_fuel_consumed=cumulative_fuel_consumed_taxi,
#         total_carbon_emissions=total_carbon_emissions_taxi,
#         total_co_emissions=total_co_emissions_taxi,
#         total_nox_emissions=total_nox_emissions_taxi,
#         total_so2_emissions=total_so2_emissions_taxi
#     )

#     # Update initial conditions for the additional climb phase (take_off_C_params)
#     take_off_C_params['initial_weight'] = final_weight_takeoff / 9.81  # Convert N to kg
#     initial_time = final_time_takeoff
#     initial_horizontal_distance = final_horizontal_distance_takeoff
#     total_required_batteries = required_batteries_takeoff

#     print(f"Battery count after take-off: {required_batteries_takeoff}")

#     # Run the additional climb phase (take_off_C_params)
#     results_take_off_C, final_weight_take_off_C, final_time_take_off_C, final_horizontal_distance_take_off_C, final_engine_power_take_off_C, cumulative_battery_energy_consumed_takeoff_C, cumulative_fuel_consumed_take_off_C, total_carbon_emissions_take_off_C, total_co_emissions_take_off_C, total_nox_emissions_take_off_C, total_so2_emissions_take_off_C, required_batteries_takeoff_C = simulate_climb_phase(
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
#     results_phase1, final_weight_phase1, final_time_phase1, final_horizontal_distance_phase1, final_engine_power_phase1, cumulative_battery_energy_consumed_takeoff_C, cumulative_fuel_consumed_phase1, total_carbon_emissions_phase1, total_co_emissions_phase1, total_nox_emissions_phase1, total_so2_emissions_phase1, required_batteries_phase1 = simulate_climb_phase(
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

#     # Update initial conditions for the interpolated climb phase between the first and second climb phases
#     between_1_2_climb['initial_weight'] = final_weight_phase1 / 9.81  # Convert N to kg
#     initial_time = final_time_phase1
#     initial_horizontal_distance = final_horizontal_distance_phase1

#     # Run the interpolated climb phase between the first and second climb phases
#     results_between_1_2_climb, final_weight_between_1_2_climb, final_time_between_1_2_climb, final_horizontal_distance_between_1_2_climb, final_engine_power_between_1_2_climb, cumulative_battery_energy_consumed_1_2_climb, cumulative_fuel_consumed_between_1_2_climb, total_carbon_emissions_between_1_2_climb, total_co_emissions_between_1_2_climb, total_nox_emissions_between_1_2_climb, total_so2_emissions_between_1_2_climb, final_altitude_between_1_2_climb, required_batteries_1_2_climb = simulate_climb_phase_int(
#         between_1_2_climb,
#         simple_wind_speed_scenario,
#         simple_crosswind_speed_scenario,
#         between_1_2_climb['initial_weight'],
#         initial_time,
#         initial_horizontal_distance,
#         between_1_2_climb['initial_roc'],
#         between_1_2_climb['final_roc'],
#         between_1_2_climb['roc_transition_duration'],
#         num_engines,
#         cumulative_fuel_consumed=cumulative_fuel_consumed_phase1,
#         total_carbon_emissions=total_carbon_emissions_phase1,
#         total_co_emissions=total_co_emissions_phase1,
#         total_nox_emissions=total_nox_emissions_phase1,
#         total_so2_emissions=total_so2_emissions_phase1
#     )

#     # Update initial conditions for the second climb phase
#     phase2_params['initial_weight'] = final_weight_between_1_2_climb / 9.81  # Convert N to kg
#     initial_time = final_time_between_1_2_climb
#     phase2_params['initial_altitude'] = final_altitude_between_1_2_climb * 3.281  # Update initial altitude
#     initial_horizontal_distance = final_horizontal_distance_between_1_2_climb

#     # Run the second phase of climb
#     results_phase2, final_weight_phase2, final_time_phase2, final_horizontal_distance_phase2, final_engine_power_phase2,cumulative_battery_energy_consumed_takeoff_C, cumulative_fuel_consumed_phase2, total_carbon_emissions_phase2, total_co_emissions_phase2, total_nox_emissions_phase2, total_so2_emissions_phase2, required_batteries_takeoff_C = simulate_climb_phase(
#         phase2_params,
#         simple_wind_speed_scenario,
#         simple_crosswind_speed_scenario,
#         phase2_params['initial_weight'],
#         initial_time,
#         initial_horizontal_distance,
#         num_engines,
#         cumulative_fuel_consumed=cumulative_fuel_consumed_between_1_2_climb,
#         total_carbon_emissions=total_carbon_emissions_between_1_2_climb,
#         total_co_emissions=total_co_emissions_between_1_2_climb,
#         total_nox_emissions=total_nox_emissions_between_1_2_climb,
#         total_so2_emissions=total_so2_emissions_between_1_2_climb
#     )

#     # Update initial conditions for the interpolation phase between the second and third climb phases
#     between_2_3_climb['initial_weight'] = final_weight_phase2 / 9.81  # Convert N to kg
#     initial_time = final_time_phase2
#     initial_horizontal_distance = final_horizontal_distance_phase2

#     # Run the interpolation phase between the second and third climb phases
#     results_between_2_3_climb, final_weight_between_2_3_climb, final_time_between_2_3_climb, final_horizontal_distance_between_2_3_climb, final_engine_power_between_2_3_climb, cumulative_battery_energy_consumed_2_3_climb, cumulative_fuel_consumed_between_2_3_climb, total_carbon_emissions_between_2_3_climb, total_co_emissions_between_2_3_climb, total_nox_emissions_between_2_3_climb, total_so2_emissions_between_2_3_climb, final_altitude_between_2_3_climb, required_batteries_2_3_climb = simulate_climb_phase_int(
#         between_2_3_climb,
#         simple_wind_speed_scenario,
#         simple_crosswind_speed_scenario,
#         between_2_3_climb['initial_weight'],
#         initial_time,
#         initial_horizontal_distance,
#         between_2_3_climb['initial_roc'],
#         between_2_3_climb['final_roc'],
#         between_2_3_climb['roc_transition_duration'],
#         num_engines,
#         cumulative_fuel_consumed=cumulative_fuel_consumed_phase2,
#         total_carbon_emissions=total_carbon_emissions_phase2,
#         total_co_emissions=total_co_emissions_phase2,
#         total_nox_emissions=total_nox_emissions_phase2,
#         total_so2_emissions=total_so2_emissions_phase2
#     )

#     # Update initial conditions for the third climb phase
#     phase3_params['initial_weight'] = final_weight_between_2_3_climb / 9.81  # Convert N to kg
#     phase3_params['initial_altitude'] = final_altitude_between_2_3_climb * 3.281  # Update initial altitude
#     initial_time = final_time_between_2_3_climb
#     initial_horizontal_distance = final_horizontal_distance_between_2_3_climb

#     # Run the third phase of climb
#     results_phase3, final_weight_phase3, final_time_phase3, final_horizontal_distance_phase3, final_engine_power_phase3, cumulative_battery_energy_consumed_takeoff_C, cumulative_fuel_consumed_phase3, total_carbon_emissions_phase3, total_co_emissions_phase3, total_nox_emissions_phase3, total_so2_emissions_phase3, required_batteries_takeoff_C = simulate_climb_phase(
#         phase3_params,
#         simple_wind_speed_scenario,
#         simple_crosswind_speed_scenario,
#         phase3_params['initial_weight'],
#         initial_time,
#         initial_horizontal_distance,
#         num_engines,
#         cumulative_fuel_consumed=cumulative_fuel_consumed_between_2_3_climb,
#         total_carbon_emissions=total_carbon_emissions_between_2_3_climb,
#         total_co_emissions=total_co_emissions_between_2_3_climb,
#         total_nox_emissions=total_nox_emissions_between_2_3_climb,
#         total_so2_emissions=total_so2_emissions_between_2_3_climb
#     )

#     # Update initial conditions for the cruise phase
#     cruise_params['initial_weight'] = final_weight_phase3 / 9.81  # Convert N to kg
#     initial_time = final_time_phase3
#     initial_horizontal_distance = final_horizontal_distance_phase3

#     # Run the cruise phase
#     results_cruise, final_weight_cruise, final_time_cruise, final_horizontal_distance_cruise, cumulative_battery_energy_consumed_cruise, cumulative_fuel_consumed_cruise, total_carbon_emissions_cruise, total_co_emissions_cruise, total_nox_emissions_cruise, total_so2_emissions_cruise, required_batteries_cruise = simulate_cruise_phase(
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
#     print(f"After Approach and Landing Phase: Cumulative Fuel = {cumulative_fuel_consumed_landing}")

#     taxi_params2['initial_weight'] = final_weight_landing / 9.81  # Convert N to kg
#     initial_time = final_time_landing
#     initial_horizontal_distance = final_horizontal_distance_landing

#     #Update initial conditions for the taxi phase
#     results_taxi2, final_weight_taxi2, final_time_taxi2, final_horizontal_distance_taxi2, final_engine_power_taxi, cumulative_fuel_consumed_taxi2, total_carbon_emissions_taxi2, total_co_emissions_taxi2, total_nox_emissions_taxi2, total_so2_emissions_taxi2 = simulate_taxi_phase(
#         taxi_params2,
#         simple_wind_speed_scenario,
#         simple_crosswind_speed_scenario,
#         taxi_params2['initial_weight'],
#         initial_time,
#         initial_horizontal_distance,
#         cumulative_fuel_consumed=cumulative_fuel_consumed_landing,
#         total_carbon_emissions=total_carbon_emissions_landing,
#         total_co_emissions=total_co_emissions_landing,
#         total_nox_emissions=total_nox_emissions_landing,
#         total_so2_emissions=total_so2_emissions_landing
#     )
#     print(f"After Second Taxi Phase: Cumulative Fuel = {cumulative_fuel_consumed_taxi2}")

#     # Combine the results of all phases
#     combined_results = pd.concat([turn_on_results, results_taxi, results_takeoff, results_take_off_C, results_phase1, results_between_1_2_climb, results_phase2, results_between_2_3_climb, results_phase3, results_cruise, results_descent, results_approach_and_landing, results_taxi2], ignore_index=True)
#     take_off_full_results = pd.concat([results_takeoff, results_take_off_C])
#     climb_full_results = pd.concat([results_phase1, results_between_1_2_climb, results_phase2, results_between_2_3_climb, results_phase3])

#     return combined_results

import pandas as pd
from simulations.takeoff_phase import simulate_takeoff_phase
from simulations.taxi_phase import simulate_taxi_phase
from simulations.climb_phase import simulate_climb_phase
from simulations.interpolated_climb_phase import simulate_climb_phase_int
from simulations.cruise_phase import simulate_cruise_phase
from simulations.descent_phase import simulate_descent_phase
from simulations.approach_and_landing_phase import simulate_approach_and_landing
from simulations.engine_turn_on_phase import engine_turn_on_phase
from utils import simple_wind_speed_scenario, simple_crosswind_speed_scenario

def calculate_total_distance_excluding_cruise(engine_turn_on_params, taxi_params, takeoff_params, take_off_C_params, climb_params, descent_params, approach_and_landing_params, taxi_params2, num_engines=2):
    # Run the engine turn-on phase
    turn_on_results, final_weight_turn_on, final_time_turn_on, final_horizontal_distance_turn_on, _, _, _, _, _, _ = engine_turn_on_phase(
        engine_turn_on_params,
        0,  # Starting time
        0,  # Starting horizontal distance
        num_engines
    )

    # Update initial conditions for the taxi phase
    taxi_params['initial_weight'] = final_weight_turn_on  # Convert N to kg
    initial_time = final_time_turn_on

    results_taxi, final_weight_taxi, final_time_taxi, final_horizontal_distance_taxi, _, _, _, _, _, _ = simulate_taxi_phase(
        taxi_params,
        simple_wind_speed_scenario,
        simple_crosswind_speed_scenario,
        taxi_params['initial_weight'],
        initial_time,
        0,
        cumulative_fuel_consumed=0,
        total_carbon_emissions=0,
        total_co_emissions=0,
        total_nox_emissions=0,
        total_so2_emissions=0
    )

    # Update initial conditions for the takeoff phase
    takeoff_params['initial_weight'] = final_weight_taxi / 9.81  # Convert N to kg
    initial_time = final_time_taxi

    # Run the take-off phase
    results_takeoff, final_weight_takeoff, final_time_takeoff, final_horizontal_distance_takeoff, _, _, _, _, _, _, _, _ = simulate_takeoff_phase(
        takeoff_params,
        simple_wind_speed_scenario,
        simple_crosswind_speed_scenario,
        takeoff_params['initial_weight'],
        initial_time,
        0,
        cumulative_fuel_consumed=0,
        total_carbon_emissions=0,
        total_co_emissions=0,
        total_nox_emissions=0,
        total_so2_emissions=0
    )

    # Update initial conditions for the additional climb phase (take_off_C_params)
    take_off_C_params['initial_weight'] = final_weight_takeoff / 9.81  # Convert N to kg
    initial_time = final_time_takeoff

    # Run the additional climb phase (take_off_C_params)
    results_take_off_C, final_weight_take_off_C, final_time_take_off_C, final_horizontal_distance_take_off_C, _, _, _, _, _, _, _, _ = simulate_climb_phase(
        take_off_C_params,
        simple_wind_speed_scenario,
        simple_crosswind_speed_scenario,
        take_off_C_params['initial_weight'],
        initial_time,
        0,
        num_engines,
        cumulative_fuel_consumed=0,
        total_carbon_emissions=0,
        total_co_emissions=0,
        total_nox_emissions=0,
        total_so2_emissions=0
    )

    # Update initial conditions for the single long climb phase
    climb_params['initial_weight'] = final_weight_take_off_C / 9.81  # Convert N to kg
    initial_time = final_time_take_off_C

    # Run the single long climb phase
    results_climb, final_weight_climb, final_time_climb, final_horizontal_distance_climb, _, _, _, _, _, _, _, _ = simulate_climb_phase(
        climb_params,
        simple_wind_speed_scenario,
        simple_crosswind_speed_scenario,
        climb_params['initial_weight'],
        initial_time,
        0,
        num_engines,
        cumulative_fuel_consumed=0,
        total_carbon_emissions=0,
        total_co_emissions=0,
        total_nox_emissions=0,
        total_so2_emissions=0
    )

    # Update initial conditions for the descent phase
    descent_params['initial_weight'] = final_weight_climb / 9.81  # Convert N to kg
    initial_time = final_time_climb

    # Run the descent phase
    results_descent, final_weight_descent, final_time_descent, final_horizontal_distance_descent, _, _, _, _, _ = simulate_descent_phase(
        descent_params,
        simple_wind_speed_scenario,
        simple_crosswind_speed_scenario,
        descent_params['initial_weight'],
        initial_time,
        0,
        num_engines,
        cumulative_fuel_consumed=0,
        total_carbon_emissions=0,
        total_co_emissions=0,
        total_nox_emissions=0,
        total_so2_emissions=0
    )

    # Update initial conditions for the approach and landing phase
    approach_and_landing_params['initial_weight'] = final_weight_descent / 9.81  # Convert N to kg
    initial_time = final_time_descent

    # Run the approach and landing phase
    results_approach_and_landing, final_weight_landing, final_time_landing, final_horizontal_distance_landing, _, _, _, _, _ = simulate_approach_and_landing(
        approach_and_landing_params,
        simple_wind_speed_scenario,
        simple_crosswind_speed_scenario,
        approach_and_landing_params['initial_weight'],
        initial_time,
        0,
        num_engines,
        cumulative_fuel_consumed=0,
        total_carbon_emissions=0,
        total_co_emissions=0,
        total_nox_emissions=0,
        total_so2_emissions=0
    )

    # Update initial conditions for the second taxi phase
    taxi_params2['initial_weight'] = final_weight_landing / 9.81  # Convert N to kg
    initial_time = final_time_landing

    # Run the second taxi phase
    results_taxi2, final_weight_taxi2, final_time_taxi2, final_horizontal_distance_taxi2, _, _, _, _, _, _  = simulate_taxi_phase(
        taxi_params2,
        simple_wind_speed_scenario,
        simple_crosswind_speed_scenario,
        taxi_params2['initial_weight'],
        initial_time,
        0,
        cumulative_fuel_consumed=0,
        total_carbon_emissions=0,
        total_co_emissions=0,
        total_nox_emissions=0,
        total_so2_emissions=0
    )

    # Sum the total horizontal distance excluding the cruise phase
    total_distance_excluding_cruise = (
                                       final_horizontal_distance_takeoff + final_horizontal_distance_take_off_C + 
                                       final_horizontal_distance_climb + final_horizontal_distance_descent + final_horizontal_distance_landing
                                       )

    return total_distance_excluding_cruise


def run_all_phases(engine_turn_on_params, taxi_params, takeoff_params, take_off_C_params, climb_params, cruise_params, descent_params, approach_and_landing_params, taxi_params2, num_engines=2):
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

    print(f"After Turn-On Phase: Cumulative Fuel = {cumulative_fuel_consumed_turn_on}")

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

    print(f"After Taxi Phase: Cumulative Fuel = {cumulative_fuel_consumed_taxi}")

    # Update initial conditions for the takeoff phase
    takeoff_params['initial_weight'] = final_weight_taxi / 9.81  # Convert N to kg
    initial_time = final_time_taxi
    initial_horizontal_distance = final_horizontal_distance_taxi

    # Run the take-off phase
    results_takeoff, final_weight_takeoff, final_time_takeoff, final_horizontal_distance_takeoff, final_engine_power_takeoff, cumulative_battery_energy_consumed_takeoff, cumulative_fuel_consumed_takeoff, total_carbon_emissions_takeoff, total_co_emissions_takeoff, total_nox_emissions_takeoff, total_so2_emissions_takeoff, required_batteries_takeoff = simulate_takeoff_phase(
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
    total_required_batteries = required_batteries_takeoff

    print(f"Battery count after take-off: {required_batteries_takeoff}")

    # Run the additional climb phase (take_off_C_params)
    results_take_off_C, final_weight_take_off_C, final_time_take_off_C, final_horizontal_distance_take_off_C, final_engine_power_take_off_C, cumulative_battery_energy_consumed_takeoff_C, cumulative_fuel_consumed_take_off_C, total_carbon_emissions_take_off_C, total_co_emissions_take_off_C, total_nox_emissions_take_off_C, total_so2_emissions_take_off_C, required_batteries_takeoff_C = simulate_climb_phase(
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

    # Update initial conditions for the single long climb phase
    climb_params['initial_weight'] = final_weight_take_off_C / 9.81  # Convert N to kg
    initial_time = final_time_take_off_C
    initial_horizontal_distance = final_horizontal_distance_take_off_C

    # Run the single long climb phase
    results_climb, final_weight_climb, final_time_climb, final_horizontal_distance_climb, final_engine_power_climb, cumulative_battery_energy_consumed_climb, cumulative_fuel_consumed_climb, total_carbon_emissions_climb, total_co_emissions_climb, total_nox_emissions_climb, total_so2_emissions_climb, required_batteries_climb = simulate_climb_phase(
        climb_params,
        simple_wind_speed_scenario,
        simple_crosswind_speed_scenario,
        climb_params['initial_weight'],
        initial_time,
        initial_horizontal_distance,
        num_engines,
        cumulative_fuel_consumed=cumulative_fuel_consumed_take_off_C,
        total_carbon_emissions=total_carbon_emissions_take_off_C,
        total_co_emissions=total_co_emissions_take_off_C,
        total_nox_emissions=total_nox_emissions_take_off_C,
        total_so2_emissions=total_so2_emissions_take_off_C
    )

    # Update initial conditions for the cruise phase
    cruise_params['initial_weight'] = final_weight_climb / 9.81  # Convert N to kg
    initial_time = final_time_climb
    initial_horizontal_distance = final_horizontal_distance_climb

    # Run the cruise phase
    results_cruise, final_weight_cruise, final_time_cruise, final_horizontal_distance_cruise, cumulative_battery_energy_consumed_cruise, cumulative_fuel_consumed_cruise, total_carbon_emissions_cruise, total_co_emissions_cruise, total_nox_emissions_cruise, total_so2_emissions_cruise, required_batteries_cruise = simulate_cruise_phase(
        cruise_params,
        simple_wind_speed_scenario,
        simple_crosswind_speed_scenario,
        cruise_params['initial_weight'],
        initial_time,
        initial_horizontal_distance,
        num_engines,
        cumulative_fuel_consumed=cumulative_fuel_consumed_climb,
        total_carbon_emissions=total_carbon_emissions_climb,
        total_co_emissions=total_co_emissions_climb,
        total_nox_emissions=total_nox_emissions_climb,
        total_so2_emissions=total_so2_emissions_climb
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
    print(f"After Approach and Landing Phase: Cumulative Fuel = {cumulative_fuel_consumed_landing}")

    taxi_params2['initial_weight'] = final_weight_landing / 9.81  # Convert N to kg
    initial_time = final_time_landing
    initial_horizontal_distance = final_horizontal_distance_landing

    #Update initial conditions for the taxi phase
    results_taxi2, final_weight_taxi2, final_time_taxi2, final_horizontal_distance_taxi2, final_engine_power_taxi, cumulative_fuel_consumed_taxi2, total_carbon_emissions_taxi2, total_co_emissions_taxi2, total_nox_emissions_taxi2, total_so2_emissions_taxi2 = simulate_taxi_phase(
        taxi_params2,
        simple_wind_speed_scenario,
        simple_crosswind_speed_scenario,
        taxi_params2['initial_weight'],
        initial_time,
        initial_horizontal_distance,
        cumulative_fuel_consumed=cumulative_fuel_consumed_landing,
        total_carbon_emissions=total_carbon_emissions_landing,
        total_co_emissions=total_co_emissions_landing,
        total_nox_emissions=total_nox_emissions_landing,
        total_so2_emissions=total_so2_emissions_landing
    )
    print(f"After Second Taxi Phase: Cumulative Fuel = {cumulative_fuel_consumed_taxi2}")

    # Combine the results of all phases
    combined_results = pd.concat([turn_on_results, results_taxi, results_takeoff, results_take_off_C, results_climb, results_cruise, results_descent, results_approach_and_landing, results_taxi2], ignore_index=True)
    take_off_full_results = pd.concat([results_takeoff, results_take_off_C])
    climb_full_results = pd.concat([results_climb])

    return combined_results
