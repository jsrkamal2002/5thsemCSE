# import module
from pdf2image import convert_from_path


# Store Pdf with convert_from_path function
images = convert_from_path('World Wide Web and HTTP - FTP - Electronic Mail - Telnet - Secure Shell - Domain Name System.pdf')
print("start")

for i in range(len(images)):

	# Save pages as images in the pdf
	images[i].save('page'+ str(i) +'.jpg', 'JPEG')

print("Done")