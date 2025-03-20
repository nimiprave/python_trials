import os as os
import google.generativeai as genai

apikey = os.environ["API_KEY"]
# print(apikey)
# print(os.environ["API_KEY"])
genai.configure(api_key=apikey)

model = genai.GenerativeModel("gemini-1.5-flash")

# read the content from the file
with open("abbreviationPayload.txt", "r") as file:
    file_content = file.read()
    response = model.generate_content(file_content)
    print(response.text)


##reading the inputs from the input in loop mode.
