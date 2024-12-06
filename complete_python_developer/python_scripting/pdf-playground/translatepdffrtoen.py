
from deep_translator import GoogleTranslator
import PyPDF2
import time


translator = GoogleTranslator(source="fr", target="en")
DELAY_IN_SECONDS = 3
# translated_text = translator.translate(text)
# print(translated_text)

# delay function


def introduce_delay(delay_seconds):
    time.sleep(delay_seconds)


text = ''
# read pdf and translate
try:
    file = open('./options.pdf', 'rb')
    writeFile = open('./translated_options.docx', 'a', encoding="utf-8")
    reader = PyPDF2.PdfReader(file)
    output = PyPDF2.PdfWriter()
    page_number = 1
    for page in reader.pages:
        text = page.extract_text()
        translated_text = translator.translate(text)
        writeFile.write(f' Page Number: {page_number} \n')
        writeFile.write(translated_text)
        page_number = page_number + 1
        introduce_delay(DELAY_IN_SECONDS)
        print(translated_text)
except FileExistsError as error:
    print(error)
