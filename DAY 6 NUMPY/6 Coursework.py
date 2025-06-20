import numpy

import numpy as np


print(np.__version__)

arr=np.array([1,2,3]) #1 dimensional array
print(arr)

print("Type of array",type(arr))
print("Dimension",arr.ndim)
print("Shape",arr.shape)


#2D array


array2=np.array([[1,2],[3,4]])
print(array2)
print("Dimension",array2.ndim)
print("Shape",array2.shape)
print("Data type",array2.dtype)

matrix=np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
print(matrix)
matrix[:,3]=[5,3]
print(matrix)
print("type",type(matrix))
print('Dimenion',matrix.ndim)
print('Shape ',matrix.shape)
print(matrix[1,5])


#Indexing in Numpy Array

print(matrix[0,:])  # colon : represent all values
print(matrix[:,3])
print(matrix[0,1:6:2])  #Start_index: stop idex-1: step index


#3D Array

b=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(b)


#Special Arrays initialization

print(np.zeros(3))
print(np.zeros((2,3)))
print(np.zeros((2,3,3)))

print(np.ones(4))
print(np.ones((2,3)))
print(np.random.rand(4,2))

print(np.identity(5))

a=np.array([1,2,3])
print(a+2) #Broadcasting
print(a-1)
print(a*3)
print(a/2)
print(a%2)

#Element wise arthmeytic

arr1=np.array([1,2,3])
arr2=np.array([4,5,6])

print(arr1+arr2)
print(arr2-arr2)
print(arr1*arr2)

#Aggregation function (min,max,sum,mean)

numbers=np.array([10,20,30,40,50])
print(np.mean(numbers))
print(np.sum(numbers))
print(np.max(numbers))

# Matrix MUltiplication 

A=np.array([[1,2],[3,4]])
B=np.array([[5,6],[7,8]])
C=np.matmul(A,B)    #dot and matmul are same
print(C)

print(A.T)

#Wap to create a numpy array to do arithmetic calculation

arr1=np.array([[10,6,14,20],[1,2,3,4]])
arr2=np.array([[2,6,1,5],[1,1,1,1]])

print("Sum is ")
print(arr1+arr2)
print("Difference is")
print(arr1-arr2)
print("Multiply is")
print(arr1*arr2)
print("Division is")
print(arr1/arr2)
print("Remainder is")
print(arr1%arr2)
