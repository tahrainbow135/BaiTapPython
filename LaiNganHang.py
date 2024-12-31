def laisuat(sotiengui, sothang):
    if (sothang >= 1) and (sothang <= 2):
        if sotiengui < 10**9:
            return 0.025
        elif sotiengui < 3*10**9:
            return 0.027
        elif sotiengui >= 3*10**9:
            return 0.028
    elif (sothang >= 3) and (sothang <= 6):
        if sotiengui < 10**9:
            return 0.039
        elif sotiengui < 3*10**9:
            return 0.041
        elif sotiengui >= 3*10**9:
            return 0.043
    elif (sothang >= 7) and (sothang <= 12):
        if sotiengui < 10**9:
            return 0.048
        elif sotiengui < 3*10**9:
            return 0.049
        elif sotiengui >= 3*10**9:
            return 0.05
    elif (sothang >= 13) and (sothang <= 36):
        if sotiengui < 10**9:
            return 0.048
        elif sotiengui < 3*10**9:
            return 0.05
        elif sotiengui >= 3*10**9:
            return 0.051
    elif sothang > 36:
        if sotiengui < 10**9:
            return 0.047
        elif sotiengui < 3*10**9:
            return 0.049
        elif sotiengui >= 3*10**9:
            return 0.05
    return 0
sotiengui = int(input())
sothang = int(input())
res = sotiengui * (laisuat(sotiengui, sothang) / 12) * sothang
print('%.0f' %res)