def makeArrayConsecutive2(statues):
    return((max(statues)-min(statues)+1)-(len(statues)))

#max - min + 1 will help you find the total number in the consectuive list
#then minusing the length of list will give you the number that is missing