# my_list = [1,2,3,4,5,6,7]

# new_list = []

# for i in my_list:
#     new_list.append(i*2)

# print(new_list) # [2, 4, 6, 8, 10, 12, 14]

# #--------------------------------------------------

# my_list = [1,2,3,4,5,6,7]

# new_items = map(lambda i: i * 2, my_list)

# print(list(new_items))

# #--------------------------------------------------

# my_list = [1,2,3,4,5,6,7] # input

# new_list = []

# for i in my_list:
#     if i > 5:
#       new_list.append(i)
    

# print(new_list) # [6, 7]

# #--------------------------------------------------

# new_items = filter(lambda i: i > 5, my_list)

# print(list(new_items))

# #--------------------------------------------------

# print(list(filter(lambda i: i > 5, my_list)))

# #--------------------------------------------------

# from functools import reduce

# def sum(a, b):
#     print(f"a={a}, b={b}, {a} * {b} ={a*b}")
#     return a * b

# scores = [75, 65, 80, 95, 50]
# total = reduce(sum, scores)
# print(total)
# #--------------------------------------------------
# print(reduce(lambda a, b: a * b, scores))

# #--------------------------------------------------

# numbers = [1, 2, 3, 4, 5]
# squares = [number**2 for number in numbers]

# print(squares)  
# #--------------------------------------------------
# print(list(number**2 for number in numbers))

# #--------------------------------------------------

