
def function1(list):
    values = list[0],list[-1]
    list[-1], list[0] = values
    return list

def function2(list):
    list[0], list[len(list)-1] = list[len(list)-1], list[0]
    return list

def function3(list):
    first, *middle, end = list
    print('first', first, ' middle ',middle, ' end ',end)
    list = end,*middle,first
    return list

def function4(list):
    first = list.pop(0)
    last = list.pop(-1)
    list.insert(0, last)
    list.append(first)
    return list

def function5(list):
    return list[-1:] + list[1:-1] + list[0:1]

def test_lists(list1, list2):
    return all(x==y for x,y in zip(list1,list2))
if __name__ == '__main__':
    result_list = [5,2,3,4,1]
    result_func = function1([1,2,3,4,5])
    print('The output of function1 {}, matches with expected output ? {}'
          .format(result_func, test_lists(result_list, result_func)))

    result_func = function2([1,2,3,4,5])
    print('The output of function2 {}, matches with expected output ? {}'
          .format(result_func, test_lists(result_list, result_func)))

    result_func = function3([1,2,3,4,5])
    print('The output of function3 {}, matches with expected output ? {}'
          .format(result_func, test_lists(result_list, result_func)))

    result_func = function4([1,2,3,4,5])
    print('The output of function4 {}, matches with expected output ? {}'
          .format(result_func, test_lists(result_list, result_func)))

    result_func = function5([1,2,3,4,5])
    print('The output of function5 {}, matches with expected output ? {}'
          .format(result_func, test_lists(result_list, result_func)))



