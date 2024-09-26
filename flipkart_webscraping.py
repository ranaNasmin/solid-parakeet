import numpy as np
from bs4 import BeautifulSoup
import requests
import pandas as pd
import csv
# Function to extract product title
def product_title(soup):
    title = soup.find('span',class_='VU-ZEz').text
    return title
# Function to extract product price
def product_price(soup):
    try:
        price = soup.find('div', class_="Nx9bqj CxhGGd").text

    except AttributeError:
        price = " "
    return price

def product_rating (product):
    try:
        rating = product.find('div', class_='XQDdHH').text

    except AttributeError:
        rating = " "
    return rating

def product_review (product):
    try:
        review = product.find('span', class_='Wphh3N').find('span').text

    except AttributeError:
        review = " "

    return review


# The main block of the code
if __name__ == '__main__':
    # Get the url.
    url = "https://www.flipkart.com/search?q=ps4&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as" \
          "=off"

    # Header for the url
    HEADER = ({'UserAgent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:130.0) Gecko/20100101 Firefox/130.0',
               'Accept-Language': 'en-US, en;q=0.5'})

    # HTTP request
    webpage = requests.get(url, headers=HEADER)
    # creating soup obj
    soup = BeautifulSoup(webpage.content, 'html.parser')

    # Fetch list as List of Tag objects.
    links = soup.find_all('a', class_= 'wjcEIp')

    # Stores the links
    links_list = []

    # Loops for extracting links from tag objects.
    for link in links:
        links_list.append(link.get('href'))

    product_dict = {"title": [], "price": [], "ratings": [], "reviews": []}

    # Loop for extracting product link from each link
    for link in links_list:
        new_webpage = requests.get("https://flipkart.com" + link, headers=HEADER)
        new_soup=BeautifulSoup(new_webpage.content, 'html.parser')

        product_dict['title'].append(product_title(new_soup))
        product_dict['price'].append(product_price(new_soup))
        product_dict['ratings'].append(product_rating(new_soup))
        product_dict['reviews'].append(product_review(new_soup))

    # print(product_dict[10])
    flipkart_df = pd.DataFrame.from_dict(product_dict)
    flipkart_df['title'] = flipkart_df['title'].replace('', np.nan)
    flipkart_df = flipkart_df.dropna(subset=['title'])
    flipkart_df.to_csv("flipkart_data.csv", header = True, index = False, encoding='utf-8-sig', errors='replace')






