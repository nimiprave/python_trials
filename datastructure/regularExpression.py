# Regex module in python
import re
s = "Geek for Geeks:  A computer science portal for geeks"

match = re.search(r'portal', s)
print(f'Start Index: {match.start()}')
print(f'Start Index: {match.end()}')


# finding all occurance of the text
results = re.findall(r'Geeks', s)
print(f"Entries found: {len(results)}")
for i in results:
    print(i)


# Example to find the digits:

string = """Hello my Number is 123456789 and
            my friend's number is 987654321"""

regex = '\d+'
match = re.findall(regex, string)
for i in match:
    print(i)


# pattern matches:
p = re.compile('[a-e]')
print(p.findall('Aye said Mr. Gibenson Stark'))
