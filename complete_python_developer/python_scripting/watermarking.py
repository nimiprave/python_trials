import PyPDF2

template = PyPDF2.PdfReader(open("wtr.pdf", 'rb'))
template_pages = template.pages
output = PyPDF2.PdfWriter()
super = PyPDF2.PdfReader(open("super.pdf", 'rb'))
for page in super.pages:
    page.merge_page(template_pages[0])
    output.add_page(page)

with open("watermarkedfile.pdf", 'wb') as file:
    output.write(file)
