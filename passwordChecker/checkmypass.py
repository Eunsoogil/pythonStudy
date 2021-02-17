import requests  # 브라우저 없이 request 가능

# https://haveibeenpwned.com/ 의 api
# password123 -> sha1 -> CBFDAC6008F9CAB4083784CBD1874F76618D2A97
url = 'https://api.pwnedpasswords.com/range/' + 'CBFDA'
res = requests.get(url)