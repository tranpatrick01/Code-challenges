def adjacentElementsProduct(inputArray):
    largest = -1000
    for numbers in range(len(inputArray)-1):
        numbers = inputArray[numbers] * inputArray[numbers+1]
        if numbers > largest:
            largest = numbers
    return largest
        
        
        
        

