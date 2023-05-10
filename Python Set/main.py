# my_dict = {}

# my_set = set()

# print(type(my_dict))
# print(type(my_set))

# #------------------------------

# kasblar = {'Dasturchi','Dezayner','Loyiha menejeri'}

# kasblar.add('Testlovchi')
# kasblar.remove('DevOps') # KeyError: 'DevOps'
# kasblar.discard('DevOps') # Error not found!
# kasblar.discard('Loyiha menejeri')

# chopilgan_kasb = kasblar.pop()

# kasblar.clear()


# print(chopilgan_kasb)

# print(kasblar)
 
# #------------------------------

# a = 10
# b = 15

# if not a < b:
#     print("Ishladi")
# else:
#     print("Ishlamadi")

# if a != b:
#     print("Ishladi")
# else:
#     print("Ishlamadi")

# #------------------------------

# skills = {'Problem solving', 'Software design', 'Python programming'}

# for index, skills in enumerate(skills):
#     print(f"{index}.{skills}")

# print(enumarate(skills)) # <enumarete objects at 0x00000239AA6A5350>

# #------------------------------

# skills = {'Problem solving', 'Software design', 'Python programming'}

# for index, skills in enumerate(skills, 1):
#     print(f"{index}.{skills}")

# #------------------------------

# tags = {'Django', 'Pandas', 'Numpy'}
# new_tags = {tag.lower() for tag in tags if tag != 'Numpy'}

# print(new_tags)

# print(set(tag.lower() for tag in tags if tag != 'Numpy'))

# #------------------------------

# s1 = {'Python', 'Java'}
# s2 = {'C#', 'Java'}

# s = s1.union(s2)

# print(s)

# #------------------------------

# s1 = {'Python', 'Java'}
# s2 = {'C#', 'Java'}

# s = s1.union(s2)

# #------------------------------

# s1 = {'Python', 'Java'}
# s2 = {'C#', 'Java'}

# s = s1 | s2

# print(s)

# #------------------------------

# numbers = {1, 2, 3}
# scores = [2, 3, 4]

# numbers = numbers & scores

# print(numbers) # TypeError: unsupported operand type(s) for &: 'set' and 'list'

# #------------------------------

