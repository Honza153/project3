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

#print(soup.p)
#print(soup.a)
print("-"*25)
lst=list()

for i in range(0,len(soup.body.div.contents)):
    wrd = str(soup.body.div.contents[i]).replace('\n', ' ').replace('\r', '')
    lst.append(wrd)

print("-"*25,"lst")

for i,prvek in enumerate(lst):
    if prvek == " ":
        lst.remove(prvek)

print(lst)
print("-"*25,"lst -children")
for child in soup.body.children:
    print(child)

print("-"*25,"lst - descendant")
for i,descendant in enumerate(soup.div.descendants):
    print('DESCENDANT {}: {}'.format(i,descendant))

print("-"*25,"lst - find all")
print(soup.find_all('p'), '\n')
print(soup.find_all(charset="utf-8"))


