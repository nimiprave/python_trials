import PyPDF2

template = PyPDF2.PdfReader(open('wtr.pdf', 'rb'))
source = PyPDF2.PdfReader(open('super.pdf', 'rb'))
output = PyPDF2.PdfWriter()
for page in source.pages:
    page.merge_page(template.pages[0])
    output.add_page(page)

output.write(open('watermarkResult.pdf', 'wb'))
