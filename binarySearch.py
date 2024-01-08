def binarySearch(list,target):
    first = 0 ## first index in list
    last = len(list) - 1 ## last index in list
    ## executes code as long as first is less than or equal to last
    while first <= last:
        ## floor division to break list in half and round down to nearest whole number 
        midpoint = (first + last)//2
        
        ## returns index if it is equal to target
        if list[midpoint] == target:
            return midpoint
        ## if the target value is greater than the midpoint we make the first index mid point + 1 for the midpoint to be calculated again with a greater first value
        elif list[midpoint] < target:
            first = midpoint + 1
        ## if the target value is less than the midpoint we make last index midpoint - 1 for the mid point to be calculated again with a lesser last value 
        else:
            last = midpoint -1
