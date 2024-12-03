from PIL import Image
import img2pdf


def convertJpgToPdf(jpgPath, pdfPath):
    # Open the image file
    image = Image.open(jpgPath)
    pdfBytes = img2pdf.convert(image.filename)
    # Write the pdf file
    with open(pdfPath, "wb") as pdfFile:
        pdfFile.write(pdfBytes)


convertJpgToPdf("rental.jpg", "rental.pdf")
