import requests
import bs4

response = requests.get('https://httpbin.org')
print(response.status_code)
# print(response.text)
print(response.json)

response1 = requests.post('http://httpbin.org/post', data = {'my_message':'Hello'})
print(response1.json)

getr = requests.get('http://example.com/')
# print(getr.text)
soup = bs4.BeautifulSoup(getr.text, "html.parser")

print(soup.p)
print(soup.a)