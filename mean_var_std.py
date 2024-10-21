import numpy as np

def calculate(lst):
    if len(lst) != 9:
        raise ValueError("List must contain nine numbers.")
    else:
        answer_list = []
        my_arr = np.array(lst)
        my_arr = np.reshape(my_arr, (3, 3))
        myDict = {}
        myDict["mean"] = [my_arr.mean(axis=0).tolist(), my_arr.mean(axis=1).tolist(),my_arr.mean().tolist()]
        myDict["variance"] = [my_arr.var(axis=0).tolist(), my_arr.var(axis=1).tolist(),my_arr.var().tolist()]
        myDict["standard deviation"] = [my_arr.std(axis=0).tolist(), my_arr.std(axis=1).tolist(),my_arr.std().tolist()]
        myDict["max"] = [my_arr.max(axis=0).tolist(), my_arr.max(axis=1).tolist(),my_arr.max().tolist()]
        myDict["min"] = [my_arr.min(axis=0).tolist(), my_arr.min(axis=1).tolist(),my_arr.min().tolist()]
        myDict["sum"] = [my_arr.sum(axis=0).tolist(), my_arr.sum(axis=1).tolist(),my_arr.sum().tolist()]

        """#mean
        mean_response = {}
        mean_response["axis1"] = my_arr.mean(axis=0)
        mean_response["axis2"] = my_arr.mean(axis=1)
        mean_response["flattened"] = my_arr.mean()
        # variance
        var_response = {}
        var_response["axis1"] = my_arr.var(axis=0)
        var_response["axis2"] = my_arr.var(axis=1)
        var_response["flattened"] = my_arr.var()

        # standard dev
        std_response = {}
        std_response["axis1"] = my_arr.std(axis=0)
        std_response["axis2"] = my_arr.std(axis=1)
        std_response["flattened"] = my_arr.std()
        # max
        max_response = {}
        max_response["axis1"] = my_arr.max(axis=0)
        max_response["axis2"] = my_arr.max(axis=1)
        max_response["flattened"] = my_arr.max()
        # min
        min_response = {}
        min_response["axis1"] = my_arr.min(axis=0)
        min_response["axis2"] = my_arr.min(axis=1)
        min_response["flattened"] = my_arr.min()
        # sum
        sum_response = {}
        sum_response["axis1"] = my_arr.sum(axis=0)
        sum_response["axis2"] = my_arr.sum(axis=1)
        sum_response["flattened"] = my_arr.sum()
        print(sum_response)"""
        
    return myDict
#    return calculations

