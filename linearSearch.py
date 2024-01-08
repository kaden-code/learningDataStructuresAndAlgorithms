def linearSearch(list,target):
    """ returns value of the target if found, if not returns error"""
    for i in range(0,len(list)):
      if list[i] == target:
          return i
    return None


def verify(index):
    if index != None:
      print("Target value index:" , index)
    else:
      print("Target not found")

numbers = [1,2,3,4,5,6,7,8,9,10]

## search for number in list
result = linearSearch(numbers,8)
verify(result)


## search for number not in list
result = linearSearch(numbers,12)
verify(result)
