import sys
import numpy as np

#Request user to input a list of numbers, and return error if the list doesn't consist of 9 number
numbers = input("Enter a list of numbers separated by spaces:").split()
count=len(numbers)
if count != 9:
    raise ValueError('List must contain nine numbers.')

# convert the list into 3x3 array
arr = np.array(numbers).reshape(3,3)
arr1 = arr.astype(np.int16) 
print("3x3 array:",arr1)

#Calculate means

mean_axis_0 = arr1.mean(axis=0),  # Mean along columns
mean_axis_1 = arr1.mean(axis=1),  # Mean along rows
mean_flattened = arr1.mean()    # Mean of the flattened array

var_axis_0 = arr1.var(axis=0),  # Var along columns
var_axis_1 = arr1.var(axis=1),  # Var along rows
var_flattened = arr1.var()    # Var of the flattened array

std_axis_0 = arr1.std(axis=0),  # Std along columns
std_axis_1 = arr1.std(axis=1),  # Std along rows
std_flattened = arr1.std()    # Std of the flattened array

max_axis_0 = arr1.max(axis=0),  # max along columns
max_axis_1 = arr1.max(axis=1),  # max along rows
max_flattened = arr1.max()    # max of the flattened array

min_axis_0 = arr1.min(axis=0),  # min along columns
min_axis_1 = arr1.min(axis=1),  # min along rows
min_flattened = arr1.min()    # min of the flattened array

sum_axis_0 = arr1.sum(axis=0),  # sumalong columns
sum_axis_1 = arr1.sum(axis=1),  # sum along rows
sum_flattened = arr1.sum()    # sum of the flattened array

print("mean:",mean_axis_0,mean_axis_1,mean_flattened)
print("var:",var_axis_0,var_axis_1,var_flattened)
print("standard deviation:",std_axis_0,std_axis_1,std_flattened)
print("max:",max_axis_0,max_axis_1,max_flattened)
print("min:",min_axis_0,min_axis_1,min_flattened)
print("sum:",sum_axis_0,sum_axis_1,sum_flattened)
