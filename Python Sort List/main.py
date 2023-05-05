# harflar = ["B","A","C"]
# sonlar = [10, 5, 20]

# # harflar.sort()
# # sonlar.sort()

# harflar.sort(reverse=True)
# sonlar.sort(reverse=True)

# print('Sort list: ', harflar)
# print('Sort list: ', sonlar)

# # ----------------------------------------------------------

# harflar = ["B","A","C"]
# sonlar = [10, 5, 20]

# saralangan_harflar = sorted(harflar)
# saralangan_sonlar = sorted(sonlar)

# # harflar.sort(reverse=True)
# # sonlar.sort(reverse=True)

# print('Sort list: ', saralangan_harflar)
# print('Sort list: ', saralangan_sonlar)

# # ----------------------------------------------------------

# harflar = ["B","A","C","D","Z"]
# sonlar = [10, 5, 20, 40, 12, 25]

# print(harflar[2:4]) # ['C', 'D']
# print(sonlar[-5]) # 5

# print(harflar[::-1]) # ['Z', 'D', 'C', 'A', 'B']

# print(harflar[1:4:2]) # ['A', 'D']

# # ----------------------------------------------------------

# my_list = [1,2,3,100]

# print(my_list[0], end=" ")
# print(my_list[1], end=" ")
# print(my_list[2], end=" ")
# print(my_list[3])

# print(*my_list)

# # ----------------------------------------------------------

# my_list = [1,2,3]

# def my_sum(a,b,c):
#     return a + b + c

# # print(my_sum(1,2,3)) 
# print(my_sum(my_list[0]),(my_list[1]),(my_list[2])) # Qo'lda unpucking qilish
# print(my_sum(*my_list)) # Python yordamida unpucking qilish

# # ----------------------------------------------------------

# my_list = [1,2,3,10,100]

# def my_sum(*value):
#     sum = 0
#     for i in value:
#         sum += i

#     return sum

# print(my_sum(*my_list))

# # ----------------------------------------------------------

# my_list = [1,2,3,4,5,6,7]

# a, b, *c = my_list

# print("a =",a)
# print("b =",b)
# print("c =",c)

# # ----------------------------------------------------------

# cities = ['New York', 'Beijing', 'Cairo', 'Mumbai', 'Mexico']

# result = cities.index('Mumbai')
# print(result)

# my_list = [1,2,3,4,5,6,7]

# index_raqami = my_list.index(5)

# print(index_raqami)

# # ----------------------------------------------------------

# my_list = [1,2,3,4,5,6,7]

# for i in my_list:
#     print(i)

# element = iter(my_list)

# print(next(element)) # 1
# print(next(element)) # 2
# print(next(element)) # 3

# # ----------------------------------------------------------

