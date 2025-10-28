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

plt.plot(x_values,y_values)
plt.show()