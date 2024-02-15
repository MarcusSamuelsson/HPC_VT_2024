import array
from sys import getsizeof as sizeof
from objsize import get_deep_size, get_exclusive_deep_size

array_a = array.array('d',[])
array_b = array.array('d',[0])
array_c = array.array('d',[0,0])

list_a = []
list_b = [0]
list_c = [0,0]

print(sizeof(array.array))
print(sizeof(array_a))
print(sizeof(array_b))
print(sizeof(array_c))
print(sizeof(array_b)-sizeof(array_a))

print("-----------------")

print(sizeof(list_a))
print(sizeof(list_b))
print(sizeof(list_c))
print(sizeof(list_b)-sizeof(list_a))

print("-----------------")

print(get_deep_size(array.array))
print(get_deep_size(array_a))
print(get_deep_size(array_b))
print(get_deep_size(list_a))
print(get_deep_size(list_b))

print("-----------------")

print(get_exclusive_deep_size(array.array))
print(get_exclusive_deep_size(array_a))
print(get_exclusive_deep_size(array_b))
print(get_exclusive_deep_size(list_a))
print(get_exclusive_deep_size(list_b))