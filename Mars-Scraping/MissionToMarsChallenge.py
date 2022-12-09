
# ### NASA Mars Exploration Scraping

# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


# set up browser for scraping
execPath = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **execPath, headless = False)

# set up url to scrape
url = 'https://redplanetscience.com'
browser.visit(url)

# if you wanted to delay opening the url
browser.is_element_present_by_css('div.list_text', wait_time = 1)

# set up html parser
html = browser.html
newSoup = soup(html, 'html.parser')

# set up elem holder and get article title
slideElem = newSoup.select_one('div.list_text')
slideElem.find('div', class_ = 'content_title')

# how to scrape but just get text, no html
Title = slideElem.find('div', class_ = 'content_title').get_text()
Title

Summary = slideElem.find('div', class_ = 'article_teaser_body').get_text()
Summary

# ### Featured Images

# Space images URL scraping
urll = 'https://spaceimages-mars.com'
browser.visit(urll)

# find and select button to make image full screen
fullscreen = browser.find_by_tag('button')[1]
fullscreen.click()

# parsing the HTML w/ Soup
html = browser.html
imgSoup = soup(html, 'html.parser')

# want to get newest photo, not same one so have to pull based off of prev code
newImage = imgSoup.find('img', class_ = 'fancybox-image').get('src')
newImage

# add base of URL to image to ensure proper load
imageURL = f'https://spaceimages-mars.com/{newImage}'
imageURL

# ### Mars Fact Scraping

# use a dataframe to store entire tables values 
df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace = True)
df

# convert a dataframe to html
df.to_html()

# # D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles
# 
# ### Hemispheres

# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'

browser.visit(url)

# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

# 3. Write code to retrieve the image urls and titles for each hemisphere.
html = browser.html
hemiList = soup(html, 'html.parser')
items = hemiList.find_all('div', class_='item')
baseURL = 'https://marshemispheres.com/'

#for loop updates the url each time it loops to get to the next image and title
for i in items:
    url = i.find('a')['href']
    browser.visit(baseURL + url)

    hemiHTML = browser.html
    hemiSoup = soup(hemiHTML, 'html.parser')

    title = hemiSoup.find('h2', class_='title').text
    images = hemiSoup.find('img', class_='wide-image').get('src')

    hemisphere_image_urls.append({"title": title, "img url": baseURL+images})

# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls

# 5. Quit the browser
browser.quit()


