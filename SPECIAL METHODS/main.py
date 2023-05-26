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

class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    def __eq__(self, other):
        return self.age == other.age 

john = Person('John', 'Doe', 26)
jane = Person('John', 'Doe', 25)

print(john == jane) # True ✅
print(john is jane) # True ✅