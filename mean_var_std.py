import numpy as np

def calculate(lst):
    if len(lst) != 9:
        raise ValueError("List must contain nine numbers.")
    else:
        answer_list = []
        my_arr = np.array(lst)
        my_arr = np.reshape(my_arr, (3, 3))
        #mean
        mean_response = {}
        mean_response["axis1"] = my_arr.mean(axis=0)
        mean_response["axis2"] = my_arr.mean(axis=1)
        mean_response["flattened"] = my_arr.mean()
        # variance

        # standard dev

        # max

        # min

        # sum
        

    return print("Done running")
#    return calculations
