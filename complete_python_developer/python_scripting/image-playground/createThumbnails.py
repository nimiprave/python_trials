from PIL import Image, ImageFilter

img = Image.open('./randompics/women.jpg')
img.thumbnail((400, 200))
img.save('./output/womenthumbnail.jpg')
