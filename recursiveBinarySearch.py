def recursiveBinarySearch(list,target):
    ## checks if list is empty if so returns item not found
    if len(list) == 0:
        return False
    else:
        ## calculates mid point of list via floor division
        midpoint = (len(list))//2
        ## checks if the value at midpoint == to target
        if list[midpoint] == target:
            return True
        else:
            ## checks if the value at the midpoint is less than the target 
            if list[midpoint] < target:
                ## if midpoint is less than the target calls function again with smaller list and starts at index one more than previous midpoint
                return recursiveBinarySearch(list[midpoint + 1:], target)
            else:
                ## if midpoint is greater than the target function calls it self with smaller list which ends at the midpoint 
                return recursiveBinarySearch(list[:midpoint],target)
            

def verify(result):
    print("Target found:", result)

numbers = [1,2,3,4,5,6,7,8]

result = recursiveBinarySearch(numbers,12)
verify(result)

result = recursiveBinarySearch(numbers,2)
verify(result)
