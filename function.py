from tkinter import messagebox
import numpy as np
from tkinter import *
import matplotlib.pyplot as plt
import random
import math
from collections import Counter
import plotly.graph_objects as go
import tkinter.font as font

def getCntNew(a):
    elems = np.unique(a)
    res = []
    for i in range(len(elems)):
        res.append([elems[i], a.count(elems[i])])
    return res


def getCnt(a):
    elems = np.unique(a)
    cnts = [a.count(elem) for elem in elems]
    return [elems, cnts]


def getIntervalCnt(a):
    r = 1
    for i in range(10000):
        if 2 ** i < len(a) <= 2 ** (i + 1):
            r = i
            break
    intervalCnt = r
    mn = min(a)
    mx = max(a)
    intervalLen = (mx - mn) / intervalCnt
    intervals = []
    cnts = []
    for i in range(intervalCnt):
        l = mn + i * intervalLen
        r = mn + (i + 1) * intervalLen
        l = round(l, 2)
        r = round(r, 2)
        curInterval = [l, r]
        if i == 0:
            cnt = sum(1 for k in a if l <= k <= r)
        else:
            cnt = sum(1 for k in a if l < k <= r)
        intervals.append(curInterval)
        cnts.append(cnt)
    return [[str(elem) for elem in intervals], cnts]


def getIntervalCntNew(a):
    r = 1
    for i in range(10000):
        if 2 ** i < len(a) <= 2 ** (i + 1):
            r = i
            break
    intervalCnt = r
    mn = min(a)
    mx = max(a)
    intervalLen = (mx - mn) / intervalCnt
    res = []
    for i in range(intervalCnt):
        l = mn + i * intervalLen
        r = mn + (i + 1) * intervalLen
        l = round(l, 2)
        r = round(r, 2)
        curInterval = [l, r]
        if i == 0:
            cnt = sum(1 for k in a if l <= k <= r)
        else:
            cnt = sum(1 for k in a if l < k <= r)
        res.append([curInterval, round(mn + (i+0.5) * intervalLen,2), cnt])

    return res


def show_bar(inputList):
    inp = getCnt(inputList)
    plt.figure()
    plt.ylabel('count')
    plt.xlabel('x')
    plt.bar(inp[0], inp[1], width=0.2)
    plt.show()


def show_plot(inputList):
    inp = getCnt(inputList)
    plt.figure()
    plt.ylabel('count')
    plt.xlabel('x')
    plt.plot(inp[0], inp[1])
    plt.show()


def show_hist(inputList):
    inp = getIntervalCnt(inputList)
    plt.figure()
    plt.ylabel('count')
    plt.xlabel('x')
    plt.bar(inp[0], inp[1], width=0.99)
    plt.show()


def show_emp(inputList):
    t = getCnt(inputList)
    elems = [t[0][0] - 5]
    elems.extend(t[0])
    elems.append(elems[-1] + 5)
    cnts = [0]
    cnts.extend(t[1])
    cnts.append(cnts[-1])
    g = []
    cntSum = 0
    for i in range(len(elems) - 1):
        cntSum += cnts[i]
        g.append([[elems[i], cntSum], [elems[i + 1], cntSum]])
        plt.plot((elems[i], elems[i+1]), ((cntSum-cnts[i]) / len(inputList), (cntSum) / len(inputList)), color='green')
    plt.show()

def show_emp2(inputList):
    t = getCnt(inputList)
    elems = [t[0][0] - 5]
    elems.extend(t[0])
    elems.append(elems[-1] + 5)
    cnts = [0]
    cnts.extend(t[1])
    cnts.append(cnts[-1])
    g = []
    cntSum = 0
    for i in range(len(elems) - 1):
        cntSum += cnts[i]
        g.append([[elems[i], cntSum], [elems[i + 1], cntSum]])
        plt.plot((elems[i], elems[i + 1]), (cntSum / len(inputList), cntSum / len(inputList)), color='green')
    plt.show()


def getQuant(a):
    n = len(a)
    res = []
    if n % 4 == 0:
        for i in range(1, 4):
            res.append(["Q" + str(i), str(a[(n // 4) * i - 1])])
        res.append(["Q3 - Q1", str(a[(3 * n) // 4 - 1] - a[n // 4 - 1])])
    if n % 10 == 0:
        for i in range(1, 10):
            res.append(["D" + str(i), str(a[(n // 10) * i - 1])])
        res.append(["D9 - D1", str(a[(9 * n) // 10 - 1] - a[n // 10 - 1])])
    if n % 100 == 0:
        for i in range(1, 100):
            res.append(["C" + str(i), str(a[(n // 100) * i - 1])])
        res.append(["C99 - C1", str(a[(99 * n) // 100 - 1] - a[n // 100 - 1])])
    if n % 1000 == 0:
        for i in range(1, 1000):
            res.append(["M" + str(i / 10), str(a[(n // 1000) * i - 1])])
        res.append(["M99,9 - M0,1", str(a[(999 * n) // 1000 - 1] - a[n // 1000 - 1])])
    return res


def getMomentums(a):
    n = len(a)
    res = []
    for i in range(0, 5):
        res.append(["Momentum(" + str(i) + ")", sum([elem ** i for elem in a]) / n])
    return res


def getCentralMomentums(a, mean):
    n = len(a)
    res = []
    for i in range(1, 5):
        res.append(["Central Momentum(" + str(i) + ")", sum([(elem - mean) ** i for elem in a]) / n])
    res.append(["Asymetry", res[2][1] / (res[1][1] ** 1.5)])
    res.append(["Excess", res[3][1] / (res[1][1] ** 2) - 3])
    return res


def getInfo(inputList):
    inputList.sort()
    n = len(inputList)
    lst = np.array(inputList)
    res = []
    res.append(["Median", np.median(lst)])
    res.append(["Mode", Counter(lst).most_common(1)[0][0]])
    lstMean = np.mean(lst)
    res.append(["Mean", lstMean])
    res.append(["Scope", lst.max() - lst.min()])
    lstDev = sum([(x - lstMean) ** 2 for x in lst])
    res.append(["Deviation", lstDev])
    lstVariance = lstDev / (n - 1)
    res.append(["Variance", lstVariance])
    lstStd = math.sqrt(lstVariance)
    res.append(["Standart", lstStd])
    res.append(["Dispersion", lstDev / n])
    res.append(["Variation", lstStd / lstMean])
    res.extend(getQuant(inputList))
    res.extend(getMomentums(inputList))
    res.extend(getCentralMomentums(inputList, lstMean))
    return res


def getIntervalMode(a):
    ind = 0
    mx = 0
    for i in range(len(a)):
        if a[i][2]>mx:
            mx = a[i][2]
            ind = i
    prevCnt = 0
    if ind != 0:
        prevCnt = a[ind-1][2]
    nextCnt = 0
    if ind != len(a)-1:
        nextCnt = a[ind+1][2]
    res = a[ind][0][0] + (a[ind][0][1]-a[ind][0][0]) * (a[ind][2] - prevCnt) / (a[ind][2] - prevCnt + a[ind][2]+nextCnt)
    return res

def getIntervalMedian(a):
    ind = 0
    mx = 0
    sumCnt = 0
    sumToMax = 0
    print(a)
    for i in range(len(a)):
        if a[i][2]>mx:
            mx = a[i][2]
            ind = i
        sumCnt += a[i][2]
    for i in range(ind):
        sumToMax += a[i][2]
    res = a[ind][0][0] + (a[ind][0][1]-a[ind][0][0]) * (sumCnt/2 - sumToMax) / a[ind][2]
    return res

def getIntervalMomentums(a,allCnt):
    n = len(a)
    res = []
    for i in range(0, 5):
        res.append(["Momentum(" + str(i) + ")", sum([a[j][2] * (a[j][1] ** i) for j in range(n)]) / allCnt])
    return res


def getIntervalCentralMomentums(a, mean, allCnt):
    n = len(a)
    res = []
    for i in range(1, 5):
        res.append(["Central Momentum(" + str(i) + ")", sum([a[j][2] * ((a[j][1] - mean) ** i) for j in range(n)]) / allCnt])
    res.append(["Asymetry", res[2][1] / (res[1][1] ** 1.5)])
    res.append(["Excess", res[3][1] / (res[1][1] ** 2) - 3])
    return res


def getIntervalInfo(inputList):
    n = len(inputList)
    Zi = []
    allCnt = 0
    Ni = []
    for i in range(n):
        Zi.append(inputList[i][1])
        Ni.append(inputList[i][2])
        allCnt += Ni[i]
    res = []
    res.append(["Median", getIntervalMedian(inputList)])
    res.append(["Mode", getIntervalMode(inputList)])
    lstMean = sum([Zi[u]*Ni[u] for u in range(n)])/allCnt
    res.append(["Mean", lstMean])
    lstDev = sum([Ni[j] *((Zi[j] - lstMean)** 2)  for j in range(n)])
    res.append(["Deviation", lstDev])
    lstVariance = lstDev / (allCnt - 1)
    res.append(["Variance", lstVariance])
    lstStd = math.sqrt(lstVariance)
    res.append(["Standart", lstStd])
    res.append(["Dispersion", lstDev / allCnt])
    res.append(["Variation", lstStd / lstMean])
    res.extend(getIntervalMomentums(inputList, allCnt))
    res.extend(getIntervalCentralMomentums(inputList, lstMean, allCnt))
    return res

def generate(mn, mx, cnt):
    return [math.floor(random.uniform(mn, mx)) for i in range(cnt)]


def readFromFile(fileName):
    try:
        result = []
        file = open(fileName)
        inp = file.readlines()
        for line in inp:
            x, n = map(int, line.split())
            result.extend([x for i in range(n)])
        return result
    except:
        print('ERROR')
        messagebox.showerror("ERROR", "Invalid file")


