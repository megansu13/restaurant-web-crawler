# restaurant-web-crawler

## Introduction
I'm an indecisive person. With Ann Arbor's myriad of restaurants and my busy schedule during the school year, there is no way of choosing which restaurant to eat at. This program lists a particular number of restaurants from [Yelp](https://www.yelp.com), as well as their ratings (out of 5 stars) and price range. If you are still unable to decide where to eat, the program will randomly select one for you.

## Requirements
- [Python](https://www.python.org/downloads/)
- Pip
- Beautifulsoup 4

## Crawling and Parsing
Our generation relies on Yelp for crowd-sources reviews, so it only feels natural to derive a list of restaurants based on a website popular among millions of users. This program utilizes bs4 and urllib.request to extract the restaurant name, rating, and price range by scraping the webpage.

The [ten restaurants](https://github.com/megansu13/restaurant-web-crawler/blob/main/ten-restaurants.py) code lists ten restaurants in Ann Arbor.

The [fifty restaurants](https://github.com/megansu13/restaurant-web-crawler/blob/main/fifty-restaurants.py) code lists fifty restaurants in Ann Arbor. After extracting information for the ten restaurants listed on the first page, the program crawls to the second page, continuously doing so until writing a list of fifty restaurants. The code executes a while loop for the number of restaurants on each page within another while loop responsible for keeping count of the number of pages that have been parsed.

## Random
After displaying the restaurant names, ratings, and price range on the terminal and writing a table in a [csv](https://github.com/megansu13/restaurant-web-crawler/blob/main/fifty-restaurants.py) file, the code asks if the user is still unable to decide which restaurant to visit. If the user, like me, still can't decide, the program uses the Random module to randomly select a place to eat from the list of restaurants.

## Improvements
Although UMich is the best college, I suppose there are other cities to explore. I plan to create an improved version of this program, which allows the user to type in any city they want.

Happy dining, Wolverines!
