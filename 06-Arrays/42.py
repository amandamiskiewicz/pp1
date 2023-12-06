'''42.	Define a function rand_elem(array) that returns a randomly selected array element. 
Using the function, display a few randomly selected array elements.'''


arr = [42, 17, 93, 55, 30, 85, 10, 68, 27, 77]


def rand_elem(array):
    import random
    ind=random.randint(0,len(array)-1)
    return array[ind]

print(rand_elem(arr))
print(rand_elem(arr))
print(rand_elem(arr))
print(rand_elem(arr))