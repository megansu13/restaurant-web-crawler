import bs4 as bs
import urllib.request as url
from random import choice

source = url.urlopen('https://www.yelp.com/search?find_desc=restaurants&find_loc=Ann+Arbor%2C+MI')
page_soup = bs.BeautifulSoup(source, 'html.parser')
attributes = page_soup.find_all("div", {"class": "padding-t3__09f24__TMrIW padding-r3__09f24__eaF7p padding-b3__09f24__S8R2d padding-l3__09f24__IOjKY border-color--default__09f24__NPAKY"})

filename = "restaurants.csv"
f = open(filename, "w")
header = "name, ratings, price"
f.write(header)

names = []
for attribute in attributes:
    try: 
        name = attribute.find("span", {"class": "css-1egxyvc"}).a.get('name')
        print("Name: " + name)
    except:
        print(None)
    try: 
        ratings = attribute.find("span", {"class": "display--inline__09f24__c6N_k border-color--default__09f24__NPAKY"}).div.get('aria-label')
        print("Ratings: " + ratings)
    except: 
        print(None)
    try: 
        price = attribute.find("span", {"class": "priceRange__09f24__mmOuH css-1s7bx9e"}).text
        print("Price: " + price)
    except:
        print(None)
    names.append(name)
    f.write("\n" + name + "," + ratings + "," + price)

print("still can't decide? (y/n)")
help = input()
if help == 'y':
    print(choice(names))
elif help == 'n':
    print("enjoy! dont blame me if u dont like it")
else:
    print("if ur dumb and cant decide, type y. if ur good, type n.")
    help = input()
    if help == 'y':
        print(choice(names))
    elif help == 'n':
        print("enjoy! dont blame me if u dont like it")
    else:
        print("ur on ur own buddy")
f.close()
