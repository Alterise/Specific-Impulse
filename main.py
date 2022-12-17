import numpy as np
import matplotlib.pyplot as plt

heights = np.linspace(0, 28000, 1000)

# engine_thrust_sea_level_value = 654000
# engine_thurst_vacuum_value = 742400

standard_gravity_value = 9.80665
mass_flow_rate_value = 236.6
exit_velocity_value = 2570
standard_atmospheric_pressure_value = 101325
exit_pressure_value = standard_atmospheric_pressure_value * 1.5
nozzle_area_value = 0.9

L = 0.00976
Cp = 1004.685
T0 = 288.16
M = 0.0289697
R0 = 8.31446


def ambient_air_pressure(height):
    return standard_atmospheric_pressure_value * (1 - standard_gravity_value * height / (Cp * T0)) ** (Cp * M / R0)


def engine_thrust(mass_flow_rate, exit_velocity, exit_pressure, nozzle_area, height):
    return mass_flow_rate * exit_velocity + (exit_pressure - ambient_air_pressure(height)) * nozzle_area


def specific_impulse(standard_gravity, mass_flow_rate, exit_velocity, exit_pressure, nozzle_area, height):
    return engine_thrust(mass_flow_rate, exit_velocity, exit_pressure, nozzle_area, height) / (
                standard_gravity * mass_flow_rate)


def specific_impulse_merlin(height):
    return specific_impulse(standard_gravity_value, mass_flow_rate_value, exit_velocity_value, exit_pressure_value,
                            nozzle_area_value, height)


values = np.apply_along_axis(specific_impulse_merlin, 0, heights)

h1 = 0
h2 = 28000

print("Impulse in", h1, "meters:", specific_impulse_merlin(h1))

print("Impulse in", h1, "meters:", specific_impulse_merlin(h2))

fig, ax = plt.subplots()
line, = ax.plot(heights, values)
ax.set_xlabel('Height [m]')
ax.set_ylabel('Specific Impulse [s]')

plt.show()
