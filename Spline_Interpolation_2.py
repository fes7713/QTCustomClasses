import numpy as np
import collections
from KClass.Color import *
import colorsys as cs

def Spline_Interpolation(x, y, precision, nested_index=False):
    x = np.array(x).astype(float)
    y = np.array(y).astype(float)

    a = np.unique(x, return_index=True)
    x = a[0]
    y = y[a[1]]

    x_1 = np.roll(x, -1)
    x_1[-1] = np.NaN
    x_2 = np.roll(x_1, -1)
    x_2[-1] = np.NaN

    h = x_1 - x
    h_1 = x_2 - x_1
    h__1 = np.roll(h, 1)
    h__1[0] = np.NaN

    y_1 = np.roll(y, -1)
    y__1 = np.roll(y, 1)
    y__1[0] = np.NaN

    v = 6 * ((y_1 - y) / h - (y - y__1) / h__1)
    v = v[1:-1]

    h_mat = np.diag(h)
    h_1_mat = np.diag(h_1)
    h_1_up_mat = np.roll(h_mat, -1, axis=0)
    h_1_up_mat[-1] = 0
    h_1_left_mat = np.roll(h_mat, -1, axis=1)
    h_1_left_mat[:, -1] = 0
    hh_1_mat = 2 * (h_mat + h_1_mat)

    fMat = (hh_1_mat + h_1_left_mat + h_1_up_mat)[:-2, :-2]
    fMat_inv = np.linalg.inv(fMat)

    u_1 = np.dot(fMat_inv, v)
    u_1 = np.hstack((u_1, np.array([0, 0])))
    u = np.roll(u_1, 1)
    u_1[-1] = np.NaN

    a = (u_1 - u) / (6 * (x_1 - x))
    b = u / 2
    c = ((y_1 - y) / h) - (1 / 6) * h * (2 * u + u_1)
    d = y

    sample_x = np.linspace(np.min(x), np.max(x), precision)
    data = np.array([x, y, a, b, c, d, u])
    bins = data[0]

    index = np.digitize(sample_x, bins=bins[0:-1]) - 1
    index_counter = collections.Counter(index)
    index_counter = list(dict(sorted(index_counter.items())).values())
    result = np.zeros((1 + np.size(data, 0), np.size(sample_x)), float)
    result[0, :] = sample_x

    for i in range(len(index_counter)):
        sample_tile = np.tile(data[:, i], index_counter[i])
        sample_tile_reshape = sample_tile.reshape(index_counter[i], np.size(data, 0))
        sample_tile_T = sample_tile_reshape.T

        result[1:, sum(index_counter[0:i]):sum(index_counter[0:i + 1])] = sample_tile_T

    data_dict = {"sample_x": result[0], "x": result[1], "y": result[2], "a": result[3], "b": result[4],
                 "c": result[5], "d": result[6], "u": result[7]}

    y_height = data_dict["a"] * (data_dict["sample_x"] - data_dict["x"]) ** 3 + data_dict["b"] * \
               (data_dict["sample_x"] - data_dict["x"]) ** 2 + data_dict["c"] * \
               (data_dict["sample_x"] - data_dict["x"]) + data_dict["d"]

    if nested_index:
        return data_dict["sample_x"], y_height, index_counter

    return data_dict["sample_x"], y_height


def Angle_3D_Interpolation(x, angleList, nSteps, nested_index=False):
    angle_x = np.cos(np.radians(angleList))
    angle_y = np.sin(np.radians(angleList))
    ragged_index_info = None
    if nested_index:
        x_values, angle_x_values, ragged_index_info = Spline_Interpolation(x, angle_x, nSteps, nested_index=True)
        x_values, angle_y_values, ragged_index_info = Spline_Interpolation(x, angle_y, nSteps, nested_index=True)
    else:
        x_values, angle_x_values = Spline_Interpolation(x, angle_x, nSteps)
        x_values, angle_y_values = Spline_Interpolation(x, angle_y, nSteps)

    angle_values = np.degrees(np.arctan2(angle_y_values, angle_x_values))
    angle_values[angle_values < 0] = angle_values[angle_values < 0] + 360

    if ragged_index_info:
        # print(sum(ragged_index_info))
        # data_x_2d = []
        # data_y_2d = []
        # nSum = 0
        # for n in ragged_index_info:
        #     data_x_2d.append(list(x_values[nSum:nSum + n]))
        #     data_y_2d.append(list(angle_values[nSum:nSum + n]))
        #     nSum += n
        return x_values, angle_values, ragged_index_info
    return x_values, angle_values


def Color_Interpolation(hexList, nSteps):
    hsvList = None
    h_list = []
    s_list = []
    v_list = []

    if isinstance(hexList[0], str):
        # hsvList = HEXtoHSV(hexList)
        for code in hexList:
            # print(code)
            h, s, v = cs.rgb_to_hsv(int(code[1:3], 16), int(code[3:5], 16), int(code[5:7], 16))
            h_list.append(h * 360)
            s_list.append(s * 255)
            v_list.append(v)

    elif isinstance(hexList[0], float) or isinstance(hexList[0], int):
        hsvList = RGBtoHSV(hexList)

        h_list = [hsv[0] for hsv in hsvList]
        s_list = [hsv[1] for hsv in hsvList]
        v_list = [hsv[2] for hsv in hsvList]
    # print(h_list)
    # print(s_list)
    # print(v_list)
    x = np.array(range(len(h_list)))

    x_values, h_values, nested_index = Angle_3D_Interpolation(x, h_list, nSteps, nested_index=True)
    x_values, s_values = Spline_Interpolation(x, s_list, nSteps)
    x_values, v_values = Spline_Interpolation(x, v_list, nSteps)

    h_values[h_values > 360] = h_values[h_values > 360] - 360
    h_values[h_values < 0] = h_values[h_values > 360] + 360
    s_values[s_values > 255] = 255
    s_values[s_values < 0] = 0
    v_values[v_values > 255] = 255
    v_values[v_values < 0] = 0

    hsv_values = np.array([h_values, s_values, v_values]).T
    # print(nested_index)
    return HSVtoHEX(hsv_values)


def Color_Interpolation_2D(topLeftColor, topRightColor, bottomLeftColor, bottomRightColor, steps):
    rightEdgeColors = Color_Interpolation([topRightColor, bottomRightColor], steps)
    leftEdgeColors = Color_Interpolation([topLeftColor, bottomLeftColor], steps)
    colorList_2D = []
    for i in range(steps):
        colorList_2D.append(Color_Interpolation([rightEdgeColors[i], leftEdgeColors[i]], steps))

    return colorList_2D


if __name__ == '__main__':
    print(Color_Interpolation(["#ff0000", "#ff7b00", "#ffea00", "#99ff00", "#00ff00"], 10))
    print(Color_Interpolation_2D())
