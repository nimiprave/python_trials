import os as os
import google.generativeai as genai

apikey = os.environ["API_KEY"]
print(apikey)
print(os.environ["API_KEY"])
genai.configure(api_key=apikey)

model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("Write a hello world program in c.")
print(response.text)


##reading the inputs from the input in loop mode.
