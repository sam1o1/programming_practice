def twoSum(list, target):
    # index list
    ind_list = []
    if len(list) >= 2:
        for i in range(len(list)):
            for j in range(i+1, len(list)):
                if list[i] + list[j] == target:
                    if i not in ind_list and j not in ind_list:
                        ind_list.append(i)
                        ind_list.append(j)
                        break
    return ind_list


def test():
    edge_cases = {"case_1": [[2, 7, 11, 15], 9, [0, 1]], "case_2": [
        [3, 2, 4], 6, [1, 2]], "case_3": [[3, 3], 6, [0, 1]]}
    for key, value in edge_cases.items():
        try:
            assert twoSum(value[0], value[1]) == value[2]
            print("{} Passed".format(key))
        except:
            print("{} failed".format(key))


test()
