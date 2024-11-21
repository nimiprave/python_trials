# program to translate the text
# take input from the keyboard and spit out the translated text.

from translate import Translator
translator = Translator(to_lang='ja')
while True:
    text = input("Please enter the text to be traslated to Japanese: ")
    if text == 'exit':
        break
    print("Translated Text:")
    print(translator.translate(text))
