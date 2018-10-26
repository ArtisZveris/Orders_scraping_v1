import requests
from bs4 import BeautifulSoup as soup

URL = 'https://orders.koivunen.lt/tklt/login'

postdict = {'BAUser':'Arturas',
	    'BAPass':'guolis26',
	    'cmd':' login '}
fd = requests.post(URL, data=postdict)

URL = 'https://orders.koivunen.lt/tklt/src?'
postdict = {'kood':'CT1028K3'}
fd1 = requests.post(URL, data=postdict, cookies=fd.cookies)

page_soup = soup(fd1.text, "html.parser")

containers = page_soup.findAll("tbody", {"id":"G_307"})

filename = "products.csv"
f = open(filename, "w")
headers = "Gamintojas, Gamintojo_kodas, KOIV_KODAS\n"
f.write(headers)

for container in containers:
    brandas_container = container.findAll("td", {"class":"brhdr"})
    brandas = brandas_container[0].text

    gamintojo_kodas_container = container.findAll("td", {"class":"ali"})
    gamintojo_kodas = gamintojo_kodas_container[0].text

    koiv_kodas_container = container.findAll("b")
    koiv_kodas = koiv_kodas_container[0].text

    f.write(brandas + "," + gamintojo_kodas + "," + koiv_kodas + "\n")
f.close()