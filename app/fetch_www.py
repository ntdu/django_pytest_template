import requests

def fetch_net():
    r = requests.get('https://www.mockaroo.com/')
    if r.status_code == 200:
        return "abc"
    
    return "bcd"

def parse():
    answer = fetch_net() + str("123")
    return answer

print(parse())