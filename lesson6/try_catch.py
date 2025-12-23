# # List Comprehension ve Try-Catch


# numbers = [1,2,3,4,5,6,7,8,9]

# list2 = []

# # for number in numbers:
# #     list2.append(number)

# # print(list2)

# # # yukaradki işlemi daha optimize yazmak
# # lise3 = [number for number in numbers]


# # print(lise3)

# # liste3 = [number * number for number in numbers]
# # print(liste3)

# # # Listedeki çift sayılar 
# # liste3 = [number for number in numbers if number % 2 == 0]
# # print(liste3)

# # # çift sayıların karelerinden oluşan
# # liste4 = [number * number for number in numbers if number % 2 == 0]
# # print(liste4)

# # liste4 = [number * number  for number in numbers if number % 2 == 0 and number > 4]

# # print(liste4)


# numbers2 = [1, 2, 3, 4]
# letters = ['a', 'b', 'c', 'd']
# letters2 =["abcd"]
# list2 = []

# # for number, letter in zip(numbers2, letters):
# #     print(number, letter)
# #     list2.append((number, letter))

# # liste5 = [f"{number},{letter}" for number, letter in zip(numbers2, letters)]

# # print(list2)
# # print(liste5)



# liist6 = [(number , letter ) for number in numbers2 for letter in letters2]

# print(liist6)



numbers = [1,2,3,4,5,6,7,8,9]
numbers2 = [2,5,6,7]


numbers3 =[]

for number in numbers:
    if number not in numbers2:
        numbers3.append(number * number)

print(numbers3)


list4 = [number * number for number in numbers if number not in numbers2]

print(list4)

list = [[1,2,3],[4,5,6],[7,8,9]]
list6 = []
for i in list:
    for j in i:
        list6.append(j)

print(list6)

list5 = [j for i in list for j in i]

print(list5)


list_methods = []

for method in dir(list):
    if "__" not in method:
        continue

    list_methods.append(method)

print(list_methods)

