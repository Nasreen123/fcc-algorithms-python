
def diffArray(arr1,arr2):

    new1 = [item for item in arr1 if item not in arr2]
    new2 = [item for item in arr2 if item not in arr1]

    newArr = new1 + new2

    return newArr


print diffArray([1, 2, 3, 5], [1, 2, 3, 4, 5])
print diffArray(["diorite", "andesite", "grass", "dirt", "pink wool", "dead shrub"], ["diorite", "andesite", "grass", "dirt", "dead shrub"])
print diffArray([1, "calf", 3, "piglet"], [1, "calf", 3, 4])
print diffArray([1, "calf", 3, "piglet"], [7, "filly"])
