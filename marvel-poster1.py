from PIL import Image

im = Image.new ('RGB', (1000, 360) )

image1 = "1.jpg"
image2 = "2.jpg"
image3 = "3.jpg"
image4 = "4.jpg"
image5 = "5.jpg"
image6 = "6.jpg"


image1 = Image.open(image1)
image2 = Image.open(image2)
image3 = Image.open(image3)
image4 = Image.open(image4)
image5 = Image.open(image5)
image6 = Image.open(image6)

w1, h1 = image1.size
width = int(w1*256/h1)


image1 = image1.resize( (width,256) )
image2 = image2.resize( (width,256) )
image3 = image3.resize( (width,256) )
image4 = image4.resize( (width,256) )
image5 = image5.resize( (width,256) )
image6 = image6.resize( (width,256) )

im.paste (image1, (31, 20))
im.paste (image2, (191, 60))
im.paste (image3, (351, 20))
im.paste (image4, (511, 60))
im.paste (image5, (671, 20))
im.paste (image6, (831, 60))

im.save('ca-marvel.jpg')
im.show()