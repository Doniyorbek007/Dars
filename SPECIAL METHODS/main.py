# class Person:
#     def __init__(self, first_name, last_name, age):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age

#     def __str__(self):
#         return f'Person({self.first_name},{self.last_name},{self.age})'
    
# personcha = Person("Ali","Valiyev",25)

# print(personcha) # Person(Ali,Valiyev,25)

#------------------------------------------------------------------------------

# class Person:
#     def __init__(self, first_name, last_name, age):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
    
# john = Person('John', 'Doe', 25)
# jane = Person('John', 'Doe', 25)

# print(john is jane) # False ❌ id jihatdan
# print(john == jane) # False ❌ id jihatdan

#------------------------------------------------------------------------------

# class Person:
#     def __init__(self, first_name, last_name, age):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
    
#     def __eq__(self, other):
#         return isinstance(other, Person) and self.age == other.age 

# john = Person('John', 'Doe', 26)
# jane = Person('John', 'Doe', 25)

# print(john == jane) # True ✅
# print(john is jane) # True ✅

#------------------------------------------------------------------------------

# class Inson:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __eq__(self, other):
#         return isinstance(other,Inson)  and self.age == other.age
    

# jhone = Person("Jhone",25)
# jane = Person("Jane",25)

# print(jhone == jane) # False

#------------------------------------------------------------------------------

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self._age = age

#     @property
#     def age(self):
#         return self._age

#     def __eq__(self, other):
#         return isinstance(other, Person) and self.age == other.age

#     def __hash__(self):
#         return hash(self.age)
    
# jhone = Person("Jhone",25)
# jane = Person("Jane",25)

# # print(hash(Person))

# print(hash(jhone))
# print(hash(jane))

#------------------------------------------------------------------------------

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __bool__(self):
#         if self.age < 18 or self.age > 65:
#             return False
#         return True


# if __name__ == '__main__':
#     person = Person('Jane', 16)
#     print(bool(person))  # False

#------------------------------------------------------------------------------

# def base_func(lst):
#     new_list = []
#     for i in lst:
#         new_list.append(i + 1)
#     return "".join(str(i) for i in new_list)


# print(base_func([1,2,3])) # [2, 3, 4] => 234