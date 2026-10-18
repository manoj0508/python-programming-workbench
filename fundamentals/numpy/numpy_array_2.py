import numpy as np

def main()-> None:
    array_4=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])
    array_reshap= array_4.reshape((4,4))

    print(array_4)

    print(array_reshap)

    extract_array = array_reshap[:,-1]
    print(extract_array)

    array_3 = np.arange(3,61,3)
    print(array_3)
    shaped_array_3= array_3.reshape((5,4))
    print(shaped_array_3)

    print(shaped_array_3[1::2,::2])
    array_3_at = np.transpose(shaped_array_3) #In transpose() and split() what is axes attributes ?
    print(array_3_at.shape)

    print(np.hstack((array_reshap,shaped_array_3)))

    np.split()





if __name__ == "__main__":
    main()
