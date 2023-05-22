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

class Inson:
    def __init__(self, nomi, yoshi):
        self.nomi = nomi
        self.yoshi = yoshi

    def salomlash(self):
        return f"Salom {self.nomi}"

    def yoshini_oshir(self):
        return self.yoshi + 1

    def yoshini_aniqla(self):
        if self.yoshi < 18:
            return f"{self.nomi} siz hali yoshsiz!"
        else:
            return f"{self.nomi} siz ro'yxatdan o'tdingiz!"
    
    def nomini_alishtir(self,yangi_nomi):
        self.nomi = yangi_nomi 
        return yangi_nomi

Sardor = Inson("Sardor",14)
Umid = Inson("Umid",22)

print(Sardor.nomini_alishtir('Sarik'))
print(Sardor.salomlash())
# print(Sardor.salomlash())
# print(Sardor.yoshini_oshir())
# print(Sardor.yoshini_aniqla())

# print(Umid.salomlash())
# print(Umid.yoshini_oshir())
# print(Umid.yoshini_aniqla())