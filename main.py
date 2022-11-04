import numpy as np

mas = np.array([0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0])
mas = mas.reshape(5, 5)


def task1():
    if reflex(mas) and sym(mas) and trans(mas):
        print("Equivalent relation")
    else:
        print("Non-Equivalent relation")
    if reflex(mas) and antisym(mas) and trans(mas):
        print("Partial order relation")
    else:
        print("Non-Partial order relation")
    if antireflex(mas) and antisym(mas) and trans(mas):
        print("Strict order relation")
    else:
        print("Non-Strict order relation")


def task2():
    print("Default relation: ")
    print(mas)
    print("Reflection locked relation: ")
    reflexlock(mas)
    print("Symetric locked relation: ")
    symlock(mas)
    print("Transitition locked relation: ")
    translock(mas)


def task3():
    powers(mas)


def reflex(arr):
    for i in arr.diagonal():
        if i == 1:
            return True
        else:
            return False


def sym(arr):
    s = 0
    for i in range(5):
        for j in range(5):
            if arr[i][j] == arr[j][i] and i != j:
                s += s
    if s == 20:
        return True
    else:
        return False


def trans(arr):
    s = 0
    for i in range(5):
        for j in range(5):
            for k in range(5):
                if arr[i][j] == arr[k][j] == 1 and arr[i][k] == 1:
                    s += s
    if s == 20:
        return True
    else:
        return False


def antisym(arr):
    s = 0
    for i in range(5):
        for j in range(5):
            if arr[i][i] == arr[j][j]:
                s += s
    if s == 5:
        return True
    else:
        return False


def antireflex(arr):
    for i in arr.diagonal():
        if i == 0:
            return True
        else:
            return False


def reflexlock(arr):
    brr = arr
    for i in range(5):
        if arr[i][i] != 1:
            brr[i][i] = 1
        else:
            brr[i][i] = 0
    print(brr)
    return arr


def translock(arr):
    brr = arr
    for i in range(5):
        for j in range(5):
            for k in range(5):
                if arr[i][j] == arr[k][j] == 1 and arr[i][k] == 0 and i != j != k:
                    brr[i][k] = 1
                    if arr[i][k] == 1:
                        brr[i][k] = 0
    print(brr)


def symlock(arr):
    brr = arr
    for i in range(5):
        for j in range(5):
            if arr[i][j] != arr[j][i] and i != j:
                brr[j][i] = brr[i][j]
    print(brr)


def powers(arr):
    brr = arr.dot(arr)
    for i in range(5):
        for t in range(5):
            if brr[i][t] != 1 and brr[i][t] != 0:
                brr[i][t] = 1
    print("Second power")
    print(brr)
    print("----------")
    crr = arr.dot(brr)
    for i in range(5):
        for t in range(5):
            if crr[i][t] != 1 and crr[i][t] != 0:
                crr[i][t] = 1
    print("Third power")
    print(crr)
    print("----------")


task1()
print("=================")
task2()
print("=================")
task3()
