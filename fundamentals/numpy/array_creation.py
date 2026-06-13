import numpy as np
import sys

def arrange():
    size = 10000
    # Numpy Storage:
    array  = np.arange(size)

    array_storage = array.itemsize * array.size

    print('size of numpy array = {}'.format(array_storage))

    # list Storage
    lst = range(size)
    list_storage = sys.getsizeof(1)* len(lst)
    print('size of List = {}'.format(list_storage))


def difference_data():
    #find match and mismatch position
    source_qty = np.array([1000, 1500, 1300, 1800, 2500])
    target_qty = np.array([1000, 1500, 1550, 1800, 2300])

    difference_qty = source_qty - target_qty
    print("difference : ", difference_qty)

    mismatch_index_msk = difference_qty != 0
    print(mismatch_index_msk)
    result = np.where(mismatch_index_msk)
    print("Mismatch position", result)

    print("Match position : ", np.where(difference_qty == 0))





def add_value_in_array():
    source = np.array([100,13,45,56])
    print("original array :", source)
    result = source*2
    print("after multi" ,result)

    result = source>20
    print("after multi" ,source[result])

    qty = np.array([90, 70, -80, 0, 100, 45, 50])
    invalid_mask = qty <= 0
    print(invalid_mask)
    print(qty[invalid_mask])

def main():
   # arrange()
    #add_value_in_array()
    difference_data()




if __name__=="__main__":
    main()