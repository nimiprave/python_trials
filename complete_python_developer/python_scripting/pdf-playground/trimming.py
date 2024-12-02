import PyPDF2


source = PyPDF2.PdfReader(open("citizenshipCertificates.pdf", "rb"))
output = PyPDF2.PdfWriter()
output.add_page(source.pages[0])
output.add_page(source.pages[1])
output.write(open("nirmalCitizenCertificate.pdf", "wb"))
