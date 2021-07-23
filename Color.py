import numpy as np


def HEXtoRGB(HexCode):
    if isinstance(HexCode, list):
        result = []
        for hex in HexCode:
            result.append(HEXtoRGB(hex))
        return result
    if isinstance(HexCode, str):
        HexCode = HexCode.lstrip('#')
        return [int(HexCode[i:i + 2], 16) for i in (0, 2, 4)]
    raise Exception


def RGBtoHSV(rgbList, limit100=False):
    if type(rgbList) is np.ndarray:
        rgbList = rgbList.tolist()
    if isinstance(rgbList[0], list):
        result = []
        for rgb in rgbList:
            result.append(RGBtoHSV(rgb, limit100))
        return result

    nMax = max(rgbList)
    nMin = min(rgbList)
    H, S, V = None, None, None,

    if rgbList[0] == rgbList[1] == rgbList[2]:
        H = 0
    elif nMax == rgbList[0]:
        H = 60 * ((rgbList[1] - rgbList[2]) / (nMax - nMin))
    elif nMax == rgbList[1]:
        H = 60 * ((rgbList[2] - rgbList[0]) / (nMax - nMin)) + 120
    else:
        H = 60 * ((rgbList[0] - rgbList[1]) / (nMax - nMin)) + 240

    if limit100:
        S = (nMax - nMin) / nMax * 100
        V = nMax / 255 * 100
    else:
        try:
            S = (nMax - nMin) / nMax * 255
        except ZeroDivisionError:
            S = 0

        V = nMax

    return [H + 360 if H < 0 else H, S, V]


def HEXtoHSV(HexCode, limit100=False):
    return RGBtoHSV(HEXtoRGB(HexCode), limit100)


def HSVtoRGB(hsvList):
    if type(hsvList) is np.ndarray:
        hsvList = hsvList.tolist()
    if isinstance(hsvList[0], list):
        result = []
        for hsv in hsvList:
            result.append(HSVtoRGB(hsv))
        return result
    H, S, V = hsvList[0], hsvList[1], hsvList[2]
    if H > 360:
        H = H - int(H / 360) * 360

    nMax = V
    nMin = nMax - (S / 255 * nMax)

    R, G, B = None, None, None

    if 0 <= H < 60:
        R = nMax
        G = H / 60 * (nMax - nMin) + nMin
        B = nMin
    elif 60 <= H < 120:
        R = (120 - H) / 60 * (nMax - nMin) + nMin
        G = nMax
        B = nMin
    elif 120 <= H < 180:
        R = nMin
        G = nMax
        B = (H - 120) / 60 * (nMax - nMin) + nMin
    elif 180 <= H < 240:
        R = nMin
        G = (240 - H) / 60 * (nMax - nMin) + nMin
        B = nMax
    elif 240 <= H < 300:
        R = (H - 240) / 60 * (nMax - nMin) + nMin
        G = nMin
        B = nMax
    elif 300 <= H < 360:
        R = nMax
        G = nMin
        B = (360 - H) / 60 * (nMax - nMin) + nMin

    return [R, G, B]


def RGBtoHEX(rgbList):
    if type(rgbList) is np.ndarray:
        rgbList = rgbList.tolist()
    if isinstance(rgbList[0], list):
        result = []
        for rgb in rgbList:
            result.append(RGBtoHEX(rgb))
        return result
    return "#" + "".join([hex(int(r))[2:4] if len(hex(int(r))) == 4 else "0" + hex(int(r))[-1] for r in rgbList])


def HSVtoHEX(hsvList):
    return RGBtoHEX(HSVtoRGB(hsvList))

