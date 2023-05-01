# # Mavzu if ... else

# a = 50
# b = 15

# if a < b:
#     print(f'Katta son {b}')
# elif a == b:
#     print(f'Ikkalasi teng {a} = {b}')
# else:
#     print(f'Katta son {a}')

# #-----------------------------------------------------------------
# # 3ta sondan eng kattasini aniqlovchi dastur

# a = int(input("a sonni kiting: "))
# b = int(input("b sonni kiting: "))
# c = int(input("c sonni kiting: "))

# if a > b > c:
#     print(f'a son eng kattasi {a}')
# elif b > a > c:
#     print(f'a son eng kattasi {b}')
# elif c > b > a:
#     print(f'c son eng kattasi {c}')
# else:
#     print(f'Hamma sonlar teng {a} = {b} = {c}')


# # -----------------------------------------------------------------

# a = 50 
# b = 500

# # Python Ternary Operator
# print(a) if a > b else print(b)

# #-----------------------------------------------------------------

# text = "Salom"

# # print(text[0])
# # print(text[1])
# # print(text[2])
# # print(text[3])
# # print(text[4])

# for harf in text:
#     print(harf)

# #-----------------------------------------------------------------

# # range(start, stop, step)

# for raqam in range(1, 10, 2):
#     print(raqam)

# #-----------------------------------------------------------------
# # Salom beruvchi dastur

# tanishlar = ['Sardor', 'Doniyor', 'Miraziz', 'Xabib']

# for bro in tanishlar:
#     print(f"Salom {bro}")

# #-----------------------------------------------------------------
# # Python While

# a = 2
# b = 5

# # if, for

# # 

# while a < b:
#     print(b)

# #-----------------------------------------------------------------

# tanishlar = ['Sardor','Donyor','Miraziz','Xabib']
# # print(tanishlar[0]) # Sardor

# sanagich = 0

# while sanagich < 4:
#     print(tanishlar[sanagich])

#     sanagich = sanagich + 1

# #-----------------------------------------------------------------

# tanishlar = ['Sardor','Donyor','Miraziz','Xabib']
# # print(tanishlar[0]) # Sardor

# sanagich = 0

# while sanagich <= 3:
#     if tanishlar[sanagich] == "Miraziz":
#         print(f"Qanday {tanishlar[sanagich]}?")
#     else:
#         print(f"Salom {tanishlar[sanagich]}!")

#     sanagich = sanagich + 1

# #-----------------------------------------------------------------

# counter = 1
# while counter <= 5:
#     print(counter)
#     # counter = counter + 1
#     counter += 1

# #-----------------------------------------------------------------

# for raqam in range(0, 10):
#     print(raqam)
#     if raqam == 3:
#         break

# #-----------------------------------------------------------------

# a = int(input("a sonni kiriting: "))
# b = int(input("b sonni kiriting: "))

# if a > b:
#     print(f'{a} soni {b} sonidan katta')
# elif b > a:    
#     print(f'{b} soni {a} sonidan katta')
# else:
#     print(f'{b} sonlari {a} bir-biriga teng!')

# #-----------------------------------------------------------------

# son = int(input("Sonni kiriting: "))

# # if son > 0:
# #     print(son * -1)
# # elif son < 0:
# #     print(son * -1)
# print(son * -1) if son > 0 else print(son * -1)

# #-----------------------------------------------------------------

# son = input("Sonni kiriting: ")

# print(son[::-1])