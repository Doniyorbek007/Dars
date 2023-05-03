# def sum(a = 50, b = 80):
#     c = a + b
#     return c


# print(sum(140, 80))
# print(sum(100))
# print(sum())

# #-----------------------------------------------------

# def salomlash(ism = "Ali"):
#     """ Ism kiritiladi va unga salom beriladi! """

#     return f"Salom {ism}!"

# print(salomlash("Sardor"))

# print(salomlash.__doc__)

# #-----------------------------------------------------

# def S(a,b):
#     s = a * b
#     return s

# print("To'rtbuchak yuzi:", S(3,3))

# def P(a,b):
#     p = (a + b) * 2
#     return p

# print("To'rtbuchak perimetri:", P(2, 5))

# #-----------------------------------------------------

# # Devorni bo'yi = 4m, eni = 6  2ta deraza bo'yi = 2m, eni = 1.5m  1m 25000

# def devor_yuzi(a = int(input("Devor bo'yi: ")), b = int(input("Devor eni: ")), c = int(input("Deraza bo'yi: ")), d = float(input("Deraza eni: ")), e = int(input("Derazalar soni: "))):
#     S = (a * b)-((c * d)* e)

#     return S

# print(devor_yuzi())

# def Summ(): 

# #-----------------------------------------------------

#  def devor_yuzi(devor_eni, devor_uzunligi, oyna_eni, oyna_uzunligi, oynalar_soni):
#         devor_yuzi_oynasi_bilan = devor_eni * devor_uzunligi
#         oynalar_yuzi = (oyna_eni * oyna_uzunligi) * oynalar_soni
#         devor_yuzi_oynalarsiz = (devor_yuzi_oynasi_bilan - oynalar_yuzi)

#         return devor_yuzi_oynalarsiz

# def narxi(narxi, devor_yuzi):
#     aboy_narxi = narxi * devor_yuzi

#     return aboy_narxi

# nateja = narxi(25000, devor_yuzi(4, 6, 1.5, 2, 3))

# print(nateja)

# #-----------------------------------------------------

# def toq_sonlar():
#     nateja = []

#     for i in range(1, 11, 2):
#         nateja.append(i)
#     return nateja

# print(toq_sonlar())

# #-----------------------------------------------------

# def daraja(a, b):
#     natija = a ** b
#     return natija

# print(daraja(2,3))

# def a(a):
#     if (a % 2 == 0):
#         return("juft")
#     else:
#         return("toq")

# print(a(2))

# #-----------------------------------------------------

# for i in range(1, 101):
#     if i % 12 == 0:
#         print(i)

# for i in range(1, 101):
#     if i % 5 ==0 and i % 6 == 0:
#         print(i)
