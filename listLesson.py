# create
# num = list((2, 5, 6, 7, 4, 1, 3, 2))
num = [2, 5, 6, 7, 4, 1, 3, 2]

#print("{} - {} - {}".format(num, len(num), type(num)))
#print(num1)

strings = ["city", "river", "country"]

mixed = [2, 3.414, "string", True]

#print(strings)

#print(mixed)

# read
#for el in mixed:
#    print("{} - {}".format(el, type(el)))

# print(mixed[0])
if len(mixed) >= 5:
    print(mixed[4])

# print(mixed[-2])

# num = [2, 5, 6, 7, 4, 1, 3, 2]
num.sort(reverse=True)
#print(num)

num.sort()
#print(num[2:-2])

#print(num[3:])

#print(num[:3])

# strings = ["city", "river", "country"]
strings.sort()
#print(strings)

#if "city" in strings:
#    print("Yes the list has an city element!!")

#if 3 in num:
#    print("Yes the number '3' is an element!!")

# update
strings.append("names")

strings[0] = "CITY"
# print(strings)

num1 = list((2, 5, 6, 7, 4, 1, 3, 2))

num1[0] = 9
print(num1)

num1[1:3] = (8,2)
print(num1)

# delete
# del num1[0]
num1.pop(0)
print(num1)

# num1.pop(-1)
num1.pop()
print(num1)


num1.clear()
print(num1)