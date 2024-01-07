def linearSearch(list,target):
    """ returns value of the target if found, if not returns error"""
    for i in list:
        if list[i] == target:
            print("Target value found")
            return i
    return None

