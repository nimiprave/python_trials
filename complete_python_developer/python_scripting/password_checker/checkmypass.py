import requests
import hashlib


# password check api to get the hash being passed
def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching: {
                           res.status_code}, check the api and try again')
    return res


# convert the password to hash
def pwned_api_check(password):
    # check password if it exist in api response
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5_char)
    hashes = read_res(response)
    get_password_leaks_count(hashes, tail)


# create dictionary out of response
def read_res(response):
    hashes = {}
    lines = response.text.strip().split('\r')
    for line in lines:
        hash_value, count = line[1:].split(':')
        hashes[hash_value] = count
    return hashes

# get count of the password leaks


def get_password_leaks_count(hashes, hash_to_check):
    count = hashes.get(hash_to_check)
    print(count)
    if count == None or count == 0:
        print(f'Password is not pawned')
    else:
        print(f'Password was pawned: {count} times')


# test
while True:
    pwd = input('Please enter the password to check:   ')
    if pwd.upper() == 'EXIT':
        break
    else:
        pwned_api_check(pwd)
