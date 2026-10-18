import _random

import numpy as np
import inspect
import random

def student():
    pass

def student():
    name = input("enter student name : ")
    print(name," add successfully")
    print(np.array)





def noraml_python():
    arr1 = [1, 2, 3]
    arr2 = [4, 5, 6]

    result = []

    for i in range(len(arr1)):
        result.append(arr1[i] + arr2[i])

    arr4 = arr1 + arr2
    print(arr4)
    print(result)

def using_lib_numpy():
    arr1 = np.array([1, 2, 3])
    arr2 = np.array([4, 5, 6])
    result = arr1 + arr2

    print(result)

class MyRandom(_random.Random):
    def _randbelow_with_getrandbits(self, n):
     pass


def main():
    print(inspect.getsource(random.choice))
    print(inspect.getsource(random.Random._randbelow))
    print(type(random.Random.getrandbits))
    print(inspect.getsource(random.Random.getrandbits))
   # print(type(np.array))
    #print(np.array.__module__)
   # help(np.array)
    #print(inspect.getsource(np.array))


if __name__=="__main__":
    main()
