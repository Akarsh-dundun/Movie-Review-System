from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import requests #needed to load the page for BS4
from bs4 import BeautifulSoup
import pandas as pd #Using panda to create our dataframe

import numpy as np
import pandas as pd

import os

def getting_reviews(movie):

    os.environ['WDM_LOG_LEVEL'] = '0'

    #path to the webdriver file
    PATH = r"C:\chromedriver.exe"
    #tell selenium to use Chrome and find the webdriver file in this location
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    driver.maximize_window()
    url = 'https://www.imdb.com/'
    driver.get(url)

    # Typing the movie name in the search input
    search_tab = wait.until(ec.element_to_be_clickable((By.XPATH, '//*[@id="suggestion-search"]')))
    search_tab.send_keys(movie)

    # Searching the movie name
    search_button = driver.find_element(By.ID, 'suggestion-search-button')
    search_button.click()

    # Clicking on the first result that pops up
    search_result = wait.until(ec.element_to_be_clickable((By.XPATH, f'/html/body/div[2]/main/div[2]/div[3]/section/div/div[1]/section[2]/div[2]/ul/li[1]/div[2]/div/a')))
    search_result.click()

    # Getting the poster of the movie
    going_img = driver.find_element(By.XPATH, f'/html/body/div[2]/main/div/section[1]/section/div[3]/section/section/div[3]/div[1]/div[1]/div/a')
    going_img.click()
    img = driver.find_element(By.XPATH, f'/html/body/div[2]/main/div[2]/div[3]/div[4]/img').get_attribute('src')
    driver.back()

    movie_name = driver.find_element(By.XPATH, f'/html/body/div[2]/main/div/section[1]/section/div[3]/section/section/div[2]/div[1]/h1/span')
    url = driver.current_url

    # Getting Director Name and Stuff
    director_name = driver.find_element(By.XPATH, f'/html/body/div[2]/main/div/section[1]/section/div[3]/section/section/div[3]/div[2]/div[1]/section/div[2]/div/ul/li[1]/div/ul/li/a').text
    movie_name = driver.find_element(By.XPATH, f'/html/body/div[2]/main/div/section[1]/section/div[3]/section/section/div[2]/div[1]/h1/span').text
    description = driver.find_element(By.XPATH, f'/html/body/div[2]/main/div/section[1]/section/div[3]/section/section/div[3]/div[2]/div[1]/section/p/span[2]').get_attribute('innerText')
    stars = driver.find_element(By.XPATH, f'/html/body/div[2]/main/div/section[1]/section/div[3]/section/section/div[2]/div[2]/div/div[1]/a/span/div/div[2]/div[1]/span[1]').get_attribute('innerText')

    print(director_name)

    Actors = []
    #Actors_link = WebDriverWait(driver, 2).until(ec.presence_of_all_elements_located(('By.XPATH,f/html/body/div[2]/main/div/section[1]/section/div[3]/section/section/div[3]/div[2]/div[1]/section/div[2]/div/ul/li[3]/div/ul')))
    #for Actor in Actors_link:
    #    actor = Actor.find_element(By,XPATH, f'//*[@id="__next"]').text 
    #    Actors.append(actor)

    try:
        for i in range(3):
            html_element = '/html/body/div[2]/main/div/section[1]/section/div[3]/section/section/div[3]/div[2]/div[1]/section/div[2]/div/ul/li[3]/div/ul/li[%s]/a'%(i+1)
            actor_name = driver.find_element(By.XPATH, html_element).text
            Actors.append(actor_name)

    except:
        print('We have reached the limit of cast members')

    
    
    # Going to the User Review Page
    user_review_link = wait.until(ec.element_to_be_clickable((By.XPATH, f'/html/body/div[2]/main/div/section[1]/section/div[3]/section/section/div[1]/div/div[2]/ul/li[2]/a')))
    user_review_link.click()

    page = 1
    #We want at least 1000 review, so get 50 at a safe number
    while page<2:  
        try:
            #find the load more button on the webpage
            load_more = driver.find_element(By.ID, "load-more-trigger")
            #click on that button
            load_more.click()
            time.sleep(3)
            page+=1
        except:
            #If couldn't find any more button to click, stop
            print("we reached here")
            break
            
    all_movie_reviews = WebDriverWait(driver, 2).until(ec.presence_of_all_elements_located((By.XPATH,'//div[@class="lister-item-content"]'))) # locate all loaded reviews
    all_reviews = [] # we'll store all reviews in this list
    for review in all_movie_reviews:
        # this will get actual rating from user
        try:
            rating = review.find_element(By.XPATH, './/div[@class="ipl-ratings-bar"]').text
        except:
            rating = np.nan

        # this will get headline/title of review
        try:
            headline = review.find_element(By.XPATH, './/a[@class="title"]').get_attribute('text')
        except:
            headline = np.nan

        # date when the review was posted
        try:
            date = review.find_element(By.XPATH, './/span[@class="review-date"]').text
        except:
            date = np.nan

        # username of person who wrote the review
        try:
            username = review.find_element(By.XPATH,'.//span[@class="display-name-link"]//a').text
        except: 
            username = np.nan

        try:
            # some reviews are longer then others
            # longer reviews are listed in different class
            # we'll assume that the review is longer, and try to scrape it like that
            review = review.find_element(By.XPATH,'.//div[@class="text show-more__control"]').text
        except:
            # exception will raise if our previous attempt was not successful
            # this means that this is shorter review
            # shorter reviews are listed under the 'content' class
            review = review.find_element(By.XPATH, './/div[@class="content"]').text

        # dictionary to store all scraped elements
        full_review = {
            "rating" : rating,
            "headline" : headline,
            "username" : username,
            "date" : date,
            "review" : review
        }
        all_reviews.append(full_review) # append our dictionary to list

    reviews = pd.DataFrame.from_dict(all_reviews)

    return (img, url, director_name, description, stars, Actors, reviews, movie_name)




    
    
