from PIL import Image, ImageFilter

img = Image.open('./pokedek/pikachu.jpg')
print(img)
print(img.size)
print(img.format)
print(dir(img))


# convert the images by applying the filters.
filtered_image = img.convert('L')
filtered_image.save("grey.png", 'png')
filtered_image.show()

# make the pikachu sharp
filtered_image1 = img.filter(ImageFilter.BLUR)
filtered_image1.save("blur.png", 'png')

# find the edges.
filtered_image2 = img.filter(ImageFilter.FIND_EDGES)
filtered_image2.rotate(180)
filtered_image2.save("edge.png", 'png')
