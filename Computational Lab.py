import math
import matplotlib.pyplot as plt

t = 0.0
x = 0.0
y = 0.0
v0 = 12
angle = 50
v0x = 0.0
v0y = 0.0
ax = 0.0
ay = -9.8
delta_t = 0.2

x_values = []
y_values = []
t_values = []

v0x = v0*math.cos(math.radians(angle))
v0y = v0*math.sin(math.radians(angle))
print("v0x = ", v0x)
print("v0y = ", v0y)

while y>=0:
  x = v0x*t + (0.5)*ax*t*t
  y = v0y*t +(0.5)*ay*t*t

  x_values.append(x)
  y_values.append(y)
  t_values.append(t)
  t = t + delta_t

plt.figure(figsize=(12,4))

plt.subplot(1,3,1)
plt.plot(x_values, y_values)
plt.title("Projectile Path (y vs x)")
plt.xlabel("x-position (m)")
plt.ylabel("y-position (m)")

plt.subplot(1,3,2)
plt.plot(t_values, x_values)
plt.title("x-position vs Time")
plt.xlabel("Time (s)")
plt.ylabel("x-position (m)")

plt.subplot(1,3,3)
plt.plot(t_values, y_values)
plt.title("y-position vs Time")
plt.xlabel("Time (s)")
plt.ylabel("y-position (m)")

plt.tight_layout()
plt.show()

range_x = x_values[-1]
time_in_air = t_values[-1]
max_height = max(y_values)

print(f"\nPredicted Range (m): {range_x:.2f}")
print(f"Predicted Time in Air (s): {time_in_air:.2f}")
print(f"Predicted Max Height (m): {max_height:.2f}")

# Example:
experimental_range = float(input("Measured (experimental) range (m): "))

percent_error = abs((experimental_range - range_x) / range_x) * 100
print(f"Percent error: {percent_error:.2f}%")