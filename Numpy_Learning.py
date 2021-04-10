import numpy as np

msg1 = "\nsingle dimentional array"
print(msg1)
n1 = np.array([10, 20, 30, 40, 50])
print(type(n1))
print(n1)

msg2 = "\nmulti dimentional array"
print(msg2)
n2 = np.array([[10, 20, 30, 40, 50],
               [1, 2, 3, 4, 5]])
print(type(n2))
print(n2)

msg3 = "\ninitializing numpy array as zeroes"
print(msg3)
n3 = np.zeros((1, 5))
print(type(n3))
print(n3)
print("Once more...")
n4 = np.zeros((5, 5))
print(type(n4))
print(n4)

msg4 = "\ninitialize numpy with same number"
n5 = np.full((5, 2), '$')
print(type(n5))
print(n5)

msg5 = "\ninitialize numpy array within a range"
n6 = np.arange(10, 20)
print(msg5)
print(n6)
msg6 = "\ninitialize numpy array within range but with step"
n7 = np.arange(10, 50, 5)
print(msg6)
print(n7)

msg7 = "\ninitialize numpy array with random numbers"
n8 = np.random.randint(low=1, high=100, size=6)
print(msg7)
print(n8)

msg8 = "\nchecking the shape of numpy array"
print(msg8)
n9 = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]]])
n10 = np.array([[1, 2, 3, 4], [5, 6, 7, 9]])
print(n9.shape)
print(n10.shape)

msg9 = "\nJoining numpy arrays\n1.vstack\t2.hstack\t3.column_stack"
print(msg9)
n11 = np.array([10, 20, 30, 40])
n12 = np.array([90, 80, 70, 60])
print("example of joining using vstack")
nv = np.vstack((n11, n12))
print(nv)
print("example of joining using hstack")
nh = np.hstack((n11, n12))
print(nh)
print("example of joining using column_stack")
nc = np.column_stack((n11, n12))
print(nc)

msg10 = "\nNumpy Intersaction & Difference"
n13 = np.array([1, 5, 9, 4, 7, 3, ])
n14 = np.array([15, 1, 5, 9, 8, 2, ])
print("intersaction")
n15 = np.intersect1d(n13, n14)
print(n15)
print("first_array - second_array ; here - means exclude the elements")
n16 = np.setdiff1d(n13, n14)
print(n16)

msg11 = "\nAddition of numpy arrays - n17,n18"
print(msg11)
n17 = np.array([10, 20, 30, 40, 50])
n18 = np.array([5, 7, 9, 11, 13])
sum1 = np.sum([n17, n18])
print(sum1)
sum2 = np.sum([n17, n18], axis=0)  # elements number must be same
print(f"When axis = 0\n {sum2}")
sum3 = np.sum([n17, n18], axis=1)  # elements number must be same
print("When axis = 1\n", sum3)

msg12 = "\nNumpy Mathematics"
arr = np.array([10, 20, 30, 40, 50])
print("Basic Addition")
arr = arr + 5
print(arr)
print("Basic Subtraction")
arr = arr - 5
print(arr)
print("Basic Multiplication")
arr = arr * 2
print(arr)
print("Basic Division")
arr = arr / 5
print(arr)

msg13 = "\nNumpy Math Functions"
print(msg13)
arr1 = np.mean(arr)
print(f"Median of arr: {arr1}")
arr2 = np.median(arr)
print(f"Median of arr: {arr2}")
arr3 = np.std(arr)
print(f"Standard Deviation of arr : {arr3}")

msg14 = "\nSave & Load Numpy Array"
print(msg14)
n19 = np.random.randint(low=1,high=100,size=10)
print("Now i want to save this array for performing operation later")
np.save('i_will_use_later',n19)
print("Okay,saved it")
print("Now i want to Load that saved array")
use_it = np.load('i_will_use_later.npy')
print(use_it)




