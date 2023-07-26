"""Complete the function that

accepts two integer arrays of equal length
compares the value each member in one array to the corresponding member in the other
squares the absolute value difference between those two values
and returns the average of those squared absolute value difference between each member pair."""

def solution(array_a, array_b):
    number_order=-1
    f=0
    w=0
    for h in array_a:
        number_order+=1
        f= (h - array_b[number_order])
        w+= f*f
    return w/len(array_a)
    pass
