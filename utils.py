import numpy as np
import pandas as pd
import pickle

def calculate_fuel_consumption(energy_consumed_MJ_total, num_engines):
    energy_content_MJ_per_kg = 43.0  # MJ per kg
    fuel_density_kg_per_L = 0.8  # kg per L

    # Calculate the fuel consumed in kg for one engine
    fuel_consumed_kg_per_engine = energy_consumed_MJ_total / (energy_content_MJ_per_kg * num_engines)

    # Convert the fuel consumed to liters for one engine
    fuel_consumed_L_per_engine = fuel_consumed_kg_per_engine / fuel_density_kg_per_L

    # Calculate the total fuel consumed in kg and liters for both engines
    fuel_consumed_kg_total = fuel_consumed_kg_per_engine * num_engines
    fuel_consumed_L_total = fuel_consumed_L_per_engine * num_engines

    return fuel_consumed_kg_per_engine, fuel_consumed_L_per_engine, fuel_consumed_kg_total, fuel_consumed_L_total

def calculate_emissions(fuel_consumed_kg_total):
    # Emission factors for Jet A (kg per kg of fuel)
    carbon_emission_factor_kg_per_kg = 3.16  # kg CO2 per kg of fuel
    co_emission_factor_kg_per_kg = 0.002  # kg CO per kg of fuel
    nox_emission_factor_kg_per_kg = 0.015  # kg NOx per kg of fuel
    so2_emission_factor_kg_per_kg = 0.0008  # kg SO2 per kg of fuel

    # Calculate the emissions for both engines
    carbon_emissions_kg_total = fuel_consumed_kg_total * carbon_emission_factor_kg_per_kg
    co_emissions_kg_total = fuel_consumed_kg_total * co_emission_factor_kg_per_kg
    nox_emissions_kg_total = fuel_consumed_kg_total * nox_emission_factor_kg_per_kg
    so2_emissions_kg_total = fuel_consumed_kg_total * so2_emission_factor_kg_per_kg

    return carbon_emissions_kg_total, co_emissions_kg_total, nox_emissions_kg_total, so2_emissions_kg_total

def calculate_metrics(power_output_kW_per_engine, duration_seconds, spline_function, num_engines=2):
    duration_hours = duration_seconds / 3600.0  # Convert seconds to hours
    efficiency = spline_function(power_output_kW_per_engine)

    if efficiency == 0:
        return {
            "power_output_kW_per_engine": power_output_kW_per_engine,
            "efficiency": efficiency,
            "energy_consumed_kWh_per_engine": 0,
            "energy_consumed_kWh_total": 0,
            "fuel_consumed_L_per_engine": 0,
            "fuel_consumed_L_total": 0,
            "fuel_consumed_kg_per_engine": 0,
            "fuel_consumed_kg_total": 0,
            "carbon_emissions_kg_total": 0,
            "co_emissions_kg_total": 0,
            "nox_emissions_kg_total": 0,
            "so2_emissions_kg_total": 0
        }

    actual_power_required_kW_per_engine = power_output_kW_per_engine / (efficiency / 100)
    energy_consumed_kWh_per_engine = actual_power_required_kW_per_engine * duration_hours
    energy_consumed_kWh_total = energy_consumed_kWh_per_engine * num_engines
    energy_consumed_MJ_total = energy_consumed_kWh_total * 3.6

    fuel_consumed_kg_per_engine, fuel_consumed_L_per_engine, fuel_consumed_kg_total, fuel_consumed_L_total = calculate_fuel_consumption(energy_consumed_MJ_total, num_engines)
    carbon_emissions_kg_total, co_emissions_kg_total, nox_emissions_kg_total, so2_emissions_kg_total = calculate_emissions(fuel_consumed_kg_total)

    return {
        "power_output_kW_per_engine": power_output_kW_per_engine,
        "efficiency": efficiency,
        "energy_consumed_kWh_per_engine": energy_consumed_kWh_per_engine,
        "energy_consumed_kWh_total": energy_consumed_kWh_total,
        "fuel_consumed_L_per_engine": fuel_consumed_L_per_engine,
        "fuel_consumed_L_total": fuel_consumed_L_total,
        "fuel_consumed_kg_per_engine": fuel_consumed_kg_per_engine,
        "fuel_consumed_kg_total": fuel_consumed_kg_total,
        "carbon_emissions_kg_total": carbon_emissions_kg_total,
        "co_emissions_kg_total": co_emissions_kg_total,
        "nox_emissions_kg_total": nox_emissions_kg_total,
        "so2_emissions_kg_total": so2_emissions_kg_total
    }

def calculate_metrics_m(power_output_kW_per_motor, duration_seconds, motor_efficiency_spline, gearbox_efficiency, inverter_efficiency, num_motors=2):
    duration_hours = duration_seconds / 3600.0  # Convert seconds to hours
    efficiency_m = motor_efficiency_spline(power_output_kW_per_motor)

    # Actual power required = Output power / (efficiency of motor * gearbox * inverter)
    actual_power_required_kW_per_motor = power_output_kW_per_motor / (efficiency_m * gearbox_efficiency * inverter_efficiency)
    energy_consumed_kWh_total_m = actual_power_required_kW_per_motor * duration_hours * num_motors

    return {
        "power_output_kW_per_motor": power_output_kW_per_motor,
        "efficiency": efficiency_m,
        "energy_consumed_kWh_total_m": energy_consumed_kWh_total_m,
    }

def calculate_drag_coefficient(C_D0, k, C_L):
    return C_D0 + k * C_L**2

def calculate_lift_coefficient_climb(weight, climb_angle, rho, true_airspeed, wing_area):
    return 2 * weight * np.cos(climb_angle) / (rho * true_airspeed**2 * wing_area)

def calculate_lift_coefficient_descent(weight, descent_angle, rho, true_airspeed, wing_area):
    return 2 * weight * np.cos(descent_angle) / (rho * true_airspeed**2 * wing_area)

# Example wind speed scenario function with smooth transitions
def simple_wind_speed_scenario(time):
    if time < 30:
        return 0  # No wind for the first 30 seconds
    elif 30 <= time < 35:
        return (time - 30) * (5 * 0.51444 / 5)  # Linearly increase to 5 knots tailwind over 5 seconds
    elif 35 <= time < 90:
        return 5 * 0.51444  # Maintain 5 knots tailwind
    elif 90 <= time < 95:
        return (5 - (time - 90) * (5 / 5)) * 0.51444  # Linearly decrease back to 0 knots over 5 seconds
    else:
        return 0  # No wind after 95 seconds

# Example crosswind speed scenario function with smooth transitions
def simple_crosswind_speed_scenario(time):
    if time < 60:
        return 0  # No crosswind for the first 60 seconds
    elif 60 <= time < 65:
        return (time - 60) * (3 * 0.51444 / 5)  # Linearly increase to 3 knots crosswind over 5 seconds
    elif 65 <= time < 120:
        return 3 * 0.51444  # Maintain 3 knots crosswind
    elif 120 <= time < 125:
        return (3 - (time - 120) * (3 / 5)) * 0.51444  # Linearly decrease back to 0 knots over 5 seconds
    else:
        return 0  # No crosswind after 125 seconds

def enforce_power_limits(total_power, max_power_kw, idle_power_kw, num_engines):
    max_power_w = max_power_kw * 1000  # Convert kW to W
    idle_power_w = idle_power_kw * 1000  # Convert kW to W

    power_per_engine = total_power / num_engines
    power_per_engine = max(min(power_per_engine, max_power_w), idle_power_w)
    
    return power_per_engine * num_engines