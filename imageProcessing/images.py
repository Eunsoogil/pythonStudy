from PIL import Image, ImageFilter

img = Image.open('./Pokedex/pikachu.jpg')

print(img)
print(dir(img))
print(img.format)
print(img.size)
print(img.mode)

filtered_img1 = img.filter(ImageFilter.BLUR)
filtered_img2 = img.filter(ImageFilter.SMOOTH_MORE)
filtered_img3 = img.filter(ImageFilter.SHARPEN)
filtered_img4 = img.convert("L")

filtered_img1.save("./Pokedex/blur.png", 'png')
filtered_img2.save("./Pokedex/smooth_more.png", 'png')
filtered_img3.save("./Pokedex/sharpen.png", 'png')
filtered_img4.save("./Pokedex/grey.png", 'png')

rotateImg = filtered_img4.rotate(90)
rotateImg.show()
# rotateImg.save("./Pokedex/grey.png", 'png')  # 저장 가능

resizeImg = filtered_img4.resize((300, 300))
resizeImg.show()

box = (100, 100, 400, 400)
cropImg = filtered_img4.crop(box)
cropImg.show()

img2 = Image.open('./Pokedex/astro.jpg')
img2.thumbnail((400, 200))  # 비율유지함, return없음
img2.save("./Pokedex/thumbnail_astro.png", 'png')
img2.show()
print(img2.size)