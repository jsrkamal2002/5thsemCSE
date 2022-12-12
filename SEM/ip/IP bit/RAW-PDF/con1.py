# import module
from pdf2image import convert_from_path


# Store Pdf with convert_from_path function
print("started!!!")
images = convert_from_path('XML XSLT.pdf')
print(images)

for i in range(len(images)):

	# Save pages as images in the pdf
	images[i].save('page'+ str(i) +'.jpg', 'JPEG')

print("Done")