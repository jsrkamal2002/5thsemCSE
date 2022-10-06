# import module
from pdf2image import convert_from_path


# Store Pdf with convert_from_path function
images = convert_from_path('PDF Gallery_20221005_233628.pdf')
# print(images)
print("started!!!")

for i in range(len(images)):

	# Save pages as images in the pdf
	# print the number of times the loop is running
	print(i)
	images[i].save('page'+ str(i) +'.jpg', 'JPEG')

print("Done")