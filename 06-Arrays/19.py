'''19.	Try to create the following arrays. Then, display the created array content.
a.	arr1 = [3,7,1,0,4]
b.	arr2 = [[2,3],[7,1],[0,4]]
c.	arr3 = [7 for i in range(5)]
d.	arr4 = [i for i in range(1,10)]
e.	arr5 = [i*2 for i in range(1,10)]
f.	arr6 = [random.randint(1,20) for i in range(10)]
g.	arr7 = [[] for i in range(5)]
h.	arr8 = [[1 for i in range(2)] for j in range(4)]
i.	arr9 = [[random.randint(1,20) for i in range(3)] for j in range(5)]
j.	an array with values: 4,0,3
k.	15-element array filled with zeros
l.	an array with integer values in the range of <1,30>
m.	20-element array filled with 0 or 1 randomly
n.	two dimensional array with five rows and two columns filled with False
'''
import random
arr1 = [3,7,1,0,4]
print("a: ",arr1)
arr2 = [[2,3],[7,1],[0,4]]
print("b: ",arr2)
arr3 = [7 for i in range(5)]
print("c: ",arr3)
arr4 = [i for i in range(1,10)]
print("d: ",arr4)
arr5 = [i*2 for i in range(1,10)]
print("e: ",arr5)
arr6 = [random.randint(1,20) for i in range(10)]
print("f: ",arr6)
arr7 = [[] for i in range(5)]
print("g: ",arr7)
arr8 = [[1 for i in range(2)] for j in range(4)]
print("h: ",arr8)
arr9 = [[random.randint(1,20) for i in range(3)] for j in range(5)]
print("i: ",arr9)
'''j.	an array with values: 4,0,3
k.	15-element array filled with zeros
l.	an array with integer values in the range of <1,30>
m.	20-element array filled with 0 or 1 randomly
n.	two dimensional array with five rows and two columns filled with False'''
arr10 = [4,0,3]
print("j: ", arr10)
arr11 = [0 for i in range(15)]
print("k: ",arr11)
arr12 = [i for i in range(1,31)]
print("l: ",arr12)
arr13 = [random.randrange(0,2) for i in range(20)]
print("m: ",arr13)
arr14 = [[False for i in range(2)] for j in range(5)]
print("n: ",arr14)