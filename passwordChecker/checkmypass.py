import requests  # 브라우저 없이 request 가능
import hashlib
import sys


# https://haveibeenpwned.com/ 의 api
# password123 -> sha1 -> CBFDAC6008F9CAB4083784CBD1874F76618D2A97
# 앞 5자리만 잘라서 사용 (K-anonymity)
# python checkmypass.py hello


def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching: {res.status_code}, check API again')
    return res


def get_password_leaks(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0


def pwned_api_check(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5_char)
    return get_password_leaks(response, tail)


def main(args):
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(f'{password} was found {count} times..')
        else:
            print(f'{password} was NOT found!')
    return 'done!'


main(sys.argv[1:])

