import pandas as pd
import matplotlib.pyplot as plt

def print_totals(combined_results):
    total_fuel_consumed = combined_results['Cumulative Fuel Consumption (kg)'].iloc[-1]
    total_carbon_emissions = combined_results['Cumulative Carbon Emissions (kg)'].iloc[-1]
    total_co_emissions = combined_results['Cumulative CO Emissions (kg)'].iloc[-1]
    total_nox_emissions = combined_results['Cumulative NOx Emissions (kg)'].iloc[-1]
    total_so2_emissions = combined_results['Cumulative SO2 Emissions (kg)'].iloc[-1]

    print(f"Total fuel consumed (kg): {total_fuel_consumed:.2f}")
    print(f"Total carbon emissions (kg): {total_carbon_emissions:.2f}")
    print(f"Total CO emissions (kg): {total_co_emissions:.2f}")
    print(f"Total NOx emissions (kg): {total_nox_emissions:.2f}")
    print(f"Total SO2 emissions (kg): {total_so2_emissions:.2f}")

def plot_results(combined_results):
    # Plot the total emissions as bar graphs
    total_emissions = combined_results[['Cumulative Carbon Emissions (kg)', 'Cumulative CO Emissions (kg)', 'Cumulative NOx Emissions (kg)', 'Cumulative SO2 Emissions (kg)']].iloc[-1]

    plt.figure(figsize=(10, 6))
    total_emissions.plot(kind='bar', color=['green', 'blue', 'red', 'purple'])
    plt.title('Total Emissions for the Mission')
    plt.xlabel('Emission Type')
    plt.ylabel('Total Emissions (kg)')
    plt.grid(True)
    plt.show()

    # Plot the results
    plt.figure(figsize=(10, 6))
    plt.plot(combined_results['Time (s)'], combined_results['Groundspeed (m/s)'])
    plt.title('Ground Speed over Time')
    plt.xlabel('Time (s)')
    plt.ylabel('Ground Speed (m/s)')
    plt.grid(True)
    plt.show()

    plt.figure(figsize=(10, 6))
    plt.plot(combined_results['Time (s)'], combined_results['True Airspeed (m/s)'])
    plt.title('True Airspeed over Time')
    plt.xlabel('Time (s)')
    plt.ylabel('True Airspeed (m/s)')
    plt.grid(True)
    plt.show()

    plt.figure(figsize=(10, 6))
    plt.plot(combined_results['Time (s)'], combined_results['Altitude (m)'])
    plt.title('Altitude over Time')
    plt.xlabel('Time (s)')
    plt.ylabel('Altitude (m)')
    plt.grid(True)
    plt.show()

    # plt.figure(figsize=(10, 6))
    # plt.plot(combined_results['Time (s)'], combined_results['Heading (degrees)'])
    # plt.title('Heading over Time')
    # plt.xlabel('Time (s)')
    # plt.ylabel('Heading (degrees)')
    # plt.grid(True)
    # plt.show()

    plt.figure(figsize=(10, 6))
    plt.plot(combined_results['Time (s)'], combined_results['Total Power (W)'], label='Total Power')
    plt.plot(combined_results['Time (s)'], combined_results['Power Drag (W)'], label='Power to Overcome Drag')
    plt.plot(combined_results['Time (s)'], combined_results['Power Climb (W)'], label='Power for Climb')
    plt.title('Power Required over Time')
    plt.xlabel('Time (s)')
    plt.ylabel('Power (W)')
    plt.legend()
    plt.grid(True)
    plt.show()

    plt.figure(figsize=(10, 6))
    plt.plot(combined_results['Time (s)'], combined_results['Engine Power (W)'], label='Engine Power')
    plt.plot(combined_results['Time (s)'], combined_results['Motor Power (W)'], label='Motor Power')
    plt.title('Engine and Motor Power over Time')
    plt.xlabel('Time (s)')
    plt.ylabel('Power (W)')
    plt.legend()
    plt.grid(True)
    plt.show()

    plt.figure(figsize=(10, 6))
    plt.plot(combined_results['Time (s)'], combined_results['Horizontal Distance (m)'])
    plt.title('Horizontal Distance over Time')
    plt.xlabel('Time (s)')
    plt.ylabel('Horizontal Distance (m)')
    plt.grid(True)
    plt.show()

    # plt.figure(figsize=(10, 6))
    # plt.plot(combined_results['Time (s)'], combined_results['Battery Energy Consumption (kWh)'])
    # plt.title('Battery Energy Consumption over Time')
    # plt.xlabel('Time (s)')
    # plt.ylabel('Battery Energy Consumption (kWh)')
    # plt.grid(True)
    # plt.show()

    # plt.figure(figsize=(10, 6))
    # plt.plot(combined_results['Time (s)'], combined_results['Cumulative Battery Energy Consumption (kWh)'])
    # plt.title('Cumulative Battery Energy Consumption over Time')
    # plt.xlabel('Time (s)')
    # plt.ylabel('Cumulative Battery Energy Consumption (kWh)')
    # plt.grid(True)
    # plt.show()

    plt.figure(figsize=(10, 6))
    plt.plot(combined_results['Time (s)'], combined_results['Drag Coefficient'], label='Drag Coefficient')
    plt.plot(combined_results['Time (s)'], combined_results['Climb Angle (degrees)'], label='Climb Angle')
    plt.title('Drag Coefficient and Climb Angle over Time')
    plt.xlabel('Time (s)')
    plt.ylabel('Value')
    plt.legend()
    plt.grid(True)
    plt.show()

    plt.figure(figsize=(10, 6))
    plt.plot(combined_results['Time (s)'], combined_results['Cumulative Fuel Consumption (kg)'])
    plt.title('Cumulative Fuel Consumption over Time')
    plt.xlabel('Time (s)')
    plt.ylabel('Cumulative Fuel Consumption (kg)')
    plt.grid(True)
    plt.show()

    plt.figure(figsize=(10, 6))
    plt.plot(combined_results['Time (s)'], combined_results['Weight (N)'])
    plt.title('Weight over Time')
    plt.xlabel('Time (s)')
    plt.ylabel('Weight (N)')
    plt.grid(True)
    plt.show()

    plt.figure(figsize=(10, 6))
    plt.plot(combined_results['Time (s)'], combined_results['Drag Coefficient'])
    plt.title('Coefficient of Drag over Time')
    plt.xlabel('Time (s)')
    plt.ylabel('Drag Coefficient')
    plt.grid(True)
    plt.show()

    plt.figure(figsize=(10, 6))
    plt.plot(combined_results['Time (s)'], combined_results['Lift Coefficient'])
    plt.title('Coefficient of Lift over Time')
    plt.xlabel('Time (s)')
    plt.ylabel('Lift Coefficient')
    plt.grid(True)
    plt.show()

    plt.figure(figsize=(10, 6))
    plt.plot(combined_results['Time (s)'], combined_results['Pressure (Pa)'])
    plt.title('Atmospheric Pressure over Time')
    plt.xlabel('Time (s)')
    plt.ylabel('Pressure (Pa)')
    plt.grid(True)
    plt.show()
