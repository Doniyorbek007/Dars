# f = open('./demo.txt')

# result = f.read()

# print(result)

# f.close()

# print("File yopilgan!")

#---------------------------------------

# with open('./demo.txt', 'wt') as f:
#     f.write("Hello World!")

# with open('./demo.txt') as f:
#    result = f.read()
#    print(result)

# print("Fayil yopilgan!")

#---------------------------------------

# with open('./demo.txt', 'wt') as f:
#     f.write(input('Ismingiz nima? '))
#     f.write('\n')
#     f.write(input('Familiyangiz nima? '))

# with open('./demo.txt') as f:
#     result = f.read()
#     print(result)

#---------------------------------------

# ismi = input("Ismingiz nima: ")
# familiyasi = input("familiyangiz nima: ")

# with open('./demo.txt', 'at') as f:
#     f.write(f"{ismi} {familiyasi}")

#---------------------------------------

# login = input('Login: ')
# parol = input('Parol: ')

# with open('./demo.txt') as f:
#     user_data = (f.readline()[:-1], f.readline())
#     if login == user_data[0] and parol == user_data[1]:
#         print('Wellcome!')
#     else:
#         print('Uyga bor!')

#---------------------------------------

words_count = int(input("Words count: "))

count = 1 
while count <= words_count :
    word = input(f"{count} Word: ")
    with open("./app.txt", "at") as f:
        f.write(word)
        f.write("\n")

    count += 1
    
with open("./app.txt") as f:
    result = f.read()
    print(result)

#---------------------------------------

