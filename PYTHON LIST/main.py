# List -> Array
# str, number, bool, func,

# oziq_ovqatlar = ["Non","Tuxum","Yog'","Gruch","Sabzi","Go'sht"]
# print(oziq_ovqatlar[3]) # Gruch

# raqamlar = [4,5,12,7]
# print(raqamlar[2]) # 12

# aralash_savat = ["Olma", 12, "Non", True, -5, 0.2]
# print(aralash_savat[3]) # True

mevalar = ["2kg Olma", "2kg Nok"]

mevalar[0] = "2 ta Banan"
mevalar.append("2 ta Apelsin")
mevalar.append("4 ta kevi")
mevalar.remove("2kg Nok")
nimani_chopding = mevalar.pop(2)
mevalar.append(nimani_chopding)
mevalar.insert(2, "5 ta Nok")
del mevalar[0]

print(mevalar)
# print(nimani_chopding)