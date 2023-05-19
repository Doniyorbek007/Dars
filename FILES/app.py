from PIL import Image

img = Image.open("photo.jpg")

# print(img.format, img.size, img.mode)

new_img = img.rotate(180)

new_img .save('rotate_180,png')

# img.show()
