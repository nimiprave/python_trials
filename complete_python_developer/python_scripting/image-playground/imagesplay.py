from PIL import Image, ImageFilter

img = Image.open('./pokedek/pikachu.jpg')
filter_image = img.filter(ImageFilter.EDGE_ENHANCE)
filter_image.resize((100, 100))
filter_image.save('./output/resized.png', 'png')
