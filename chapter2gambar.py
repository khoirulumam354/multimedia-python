from PIL import Image

# Memuat gambar
image = Image.open('gambar/gambar.jpeg')

# Menyimpan gambar
image.save('hasilgambar/result.jpg')

#Cropping image
cropped_image = image.crop((2337, 1769, 6847, 3481))
cropped_image.save('hasilgambar/cropped_result.jpg')

#resize image
resized_image = cropped_image.resize((2840 , 1160))
resized_image.save('hasilgambar/resized_result.jpg')

#filter image
from PIL import ImageFilter

filtered_image = resized_image.filter(ImageFilter.BLUR)
filtered_image.save('hasilgambar/filtered_result.jpg')