# class Inson:
#     x = 12

# print(Inson.x)
# print(Inson.__name__) # <class '__main__.Inson'>

#-------------------------------------------

# class Inson:
#     inson_nomi = "Sardor"
#     inson_yoshi = 14

# print(Inson.inson_nomi)
# print(Inson.inson_yoshi)

#-------------------------------------------

# class Inson:
#     def __init__(self, nomi, yoshi):
#         self.nomi = nomi
#         self.yoshi = yoshi

#     def salomlash(self):
#         return f"Salom {self.nomi}"

#     def yoshini_oshir(self):
#         return self.yoshi + 1

#     def yoshini_aniqla(self):
#         if self.yoshi < 18:
#             return f"{self.nomi} siz hali yoshsiz!"
#         else:
#             return f"{self.nomi} siz ro'yxatdan o'tdingiz!"
    
#     def nomini_alishtir(self,yangi_nomi):
#         self.nomi = yangi_nomi 
#         return yangi_nomi

# Sardor = Inson("Sardor",14)
# Umid = Inson("Umid",22)

# print(Sardor.nomini_alishtir('Sarik'))
# print(Sardor.salomlash())
# print(Sardor.salomlash())
# print(Sardor.yoshini_oshir())
# print(Sardor.yoshini_aniqla()) 

# print(Umid.salomlash())
# print(Umid.yoshini_oshir())
# print(Umid.yoshini_aniqla())

#-------------------------------------------

# class Calc:
#     def __init__(self, a,b) -> None:
#         self.a = a
#         self.b = b

#     def yigindi(self, natija):
#         self.natija = natija
#         natija = self.a + self.b
#         return

#     def ayirish(self):
#         return self.a - self.b

#     def kupaytma(self):
#         return self.a * self.b

#     def bulish(self):
#         return self.a / self.b

# natija = Calc.yigindi()

# print(natija)

#-------------------------------------------

# class Inson:
#     pass

# class Kitob:
#     pass

# print(id(Inson))
# print(id(Kitob))

# x = 10

# print(id(x))

#-------------------------------------------

# class Inson:
#     nomi = "Ali"
#     yoshi = 22

# print(Inson.nomi)
# print(Inson.yoshi)
# print(Inson.kasbi) # AttributeError: type object 'Inson' has no attribute 'kasbi'

#-------------------------------------------

# class Inson:
#     nomi = "Ali"
#     yoshi = 22

# print(getattr(Inson, 'nomi'))
# print(getattr(Inson, 'yoshi'))

#-------------------------------------------
#-------------------------------------------

# class Inson:
#     nomi = "Ali"
#     yoshi = 22

# # Inson.nomi = "Sardor"
# setattr(Inson, 'nomi', 'Umid')

# print(Inson.nomi)

#-------------------------------------------

# class Inson:
#     nomi = "Ali"
#     yoshi = 22

# delattr(Inson, 'nomi')

# print(Inson.nomi)

#-------------------------------------------

