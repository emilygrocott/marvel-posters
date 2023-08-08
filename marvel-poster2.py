from PIL import Image

import check2_helper

im = Image.new('RGB', (512, 512), (255, 255, 255))

image1 = "1.jpg"
image2 = "2.jpg"
image3 = "4.jpg"
image4 = "3.jpg"

image1 = Image.open(image1)
image2 = Image.open(image2)
image3 = Image.open(image3)
image4 = Image.open(image4)

image1 = check2_helper.make_square(image1)
image2 = check2_helper.make_square(image2)
image3 = check2_helper.make_square(image3)
image4 = check2_helper.make_square(image4)


image1 = image1.resize( (256,256) )
image2 = image2.resize( (256,256) )
image3 = image3.resize( (256,256) )
image4 = image4.resize( (256,256) )

im.paste (image1, (0,0))
im.paste (image2, (256,0))
im.paste (image3, (256,256))
im.paste (image4, (0,256))

im.save('ca-marvel.jpg')
im.show()
