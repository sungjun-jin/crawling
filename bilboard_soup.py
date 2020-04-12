import requests
import csv

from bs4 import BeautifulSoup

def bilboard_crawl() :
	
	URL = "https://www.billboard.com/charts/hot-100"
	req = requests.get(URL)
	html = req.text
	soup = BeautifulSoup(html, 'html.parser')

	file = open('bilboard_soup.csv',mode='w',encoding='UTF-8',newline='')
	writer = csv.writer(file)
	writer.writerow(['rank','title','artist','last_week','peak','duration'])

	song_lists = soup.find_all('li',{'class': 'chart-list__element'})

	for song in song_lists:
		rank = song.find('span',{'class' : 'chart-element__rank__number'}).string
		title = song.find('span',{'class' : 'chart-element__information__song'}).string
		artist = song.find('span',{'class': 'chart-element__information__artist'}).string
		last_week = song.find('span',{'class' : 'chart-element__meta text--center color--secondary text--last'}).string
		peak = song.find('span',{'class' : 'chart-element__meta text--center color--secondary text--peak'}).string
		duration = song.find('span',{'class' : 'chart-element__meta text--center color--secondary text--week'}).string
		
		writer.writerow((rank,title,artist,last_week,peak,duration))

bilboard_crawl()
