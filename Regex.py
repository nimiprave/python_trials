#Testing the Regex.py
import re

txt = "The rain in spain"
x = re.search("^The.*spain",txt)
if x:
    print("Found")
else:
    print("Not found")


y = "I have found peace, which is peacful, peace is itself"
matchesfound  = re.findall("peace",y)
print(matchesfound)

matcher =  re.search("peace",y)
print(matcher.start())
print(matcher.span())
print(matcher.string)
print(matcher.group())



print(re.sub("peace","war",y))