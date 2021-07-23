import colorsys as cs
import numpy as np


hex = "#fc89a8"

h, s, v = cs.rgb_to_hsv(int("fc", 16), int("89", 16), int("a8", 16))

print("h : " + str(360 * h) + " s : " + str(255 * s) + " v : " + str(v))
r, g, b = cs.hsv_to_rgb(0.5, 1, 250)
print(b)
# # r = 40/255
# # g = 150/255
# # b = 180/255
code_top_left = '#{:02x}{:02x}{:02x}'.format(int(r * 255), int(g * 255), int(b * 255))
code_top_left = '#{:02x}{:02x}{:02x}'.format(int(r), int(g), int(b))
print(code_top_left)

print([1])
print(type(np.array(["hello"]*4)))

print(int(1.1) == 1.1)