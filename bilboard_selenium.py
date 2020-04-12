import requests
import csv
import time

from selenium import webdriver
from bs4 import BeautifulSoup

def bilboard_crawl():

	URL = 'https://www.billboard.com/charts/hot-100'
	driver = webdriver.Chrome('/home/sungjunjin/chromedriver')
	driver.get(URL)

	file = open('bilboard_selenium.csv',mode='w',encoding='UTF-8',newline='')
	writer = csv.writer(file)
	writer.writerow(['rank','title','artist','last_week','peak','duration','image-url'])
	
	for i in range(10):
		driver.execute_script(f"window.scrollTo(0, document.body.scrollHeight * {i/10});")
		print(f"scrolling page {i}")
		time.sleep(0.01)

	req = requests.get(URL)
	html = driver.page_source
	soup = BeautifulSoup(html, 'html.parser')
	song_lists = soup.find_all('li',{'class': 'chart-list__element'})
	
	for song in song_lists:
		rank = song.find('span',{'class' : 'chart-element__rank__number'}).string
		title = song.find('span',{'class' : 'chart-element__information__song'}).string
		artist = song.find('span',{'class': 'chart-element__information__artist'}).string
		last_week = song.find('span',{'class' : 'chart-element__information__delta__text text--last'}).string.split(' ')[0]
		peak = song.find('span',{'class' : 'chart-element__information__delta__text text--peak'}).string.split(' ')[0]
		duration = song.find('span',{'class' : 'chart-element__information__delta__text text--week'}).string.split(' ')[0]
		image = song.find('span',{'class' : 'chart-element__image flex--no-shrink'})['style'].split(' ')[1]
		
		writer.writerow((rank,title,artist,last_week,peak,duration,image))	

	driver.close()

bilboard_crawl()	
