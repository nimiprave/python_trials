from translate import Translator
import pdb

translator = Translator(to_lang='ja')

try:
    # reader = open('payload.txt', 'r', encoding='utf-8').read()
    # print(reader)

    # This construct resolves the cursur and the closing of the file issue.
    with open('payload.txt', 'r') as file:

        content = file.read()
       # pdb.set_trace()
        print(content)
        with open('translatedText.txt', 'w', encoding='utf-8') as file1:
            print(file1.write(translator.translate(content)))
except FileNotFoundError as err:
    print(err)
