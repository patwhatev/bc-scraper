# -*- coding: utf-8 -*-
from __future__ import print_function
from selenium import webdriver
import requests
import random
from bs4 import BeautifulSoup
import shutil
import os
import re
from urls import urlArr
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

print('$$\       $$$$$$$$\  $$$$$$\  $$$$$$$\     $$$$$\ ')
print('$$ |      $$  _____|$$  __$$\ $$  __$$\    \__$$ |')
print('$$ |      $$ |      $$ /  \__|$$ |  $$ |      $$ |')
print('$$ |      $$$$$\    \$$$$$$\  $$ |  $$ |      $$ |')
print('$$ |      $$  __|    \____$$\ $$ |  $$ |$$\   $$ |')
print('$$ |      $$ |      $$\   $$ |$$ |  $$ |$$ |  $$ |')
print('$$$$$$$$\ $$$$$$$$\ \$$$$$$  |$$$$$$$  |\$$$$$$  |')
print('\________|\________| \______/ \_______/  \______/ ')


#PhantomJS
driver = webdriver.PhantomJS(executable_path='/Users/temp/Documents/phantomjs/bin/phantomjs')

for collection in urlArr:
	name = collection["name"]
	url = collection["url"]
	os.mkdir(f'saved/{name}')

	print("scraping from: " + url)
	driver.get(url)
	current_url = driver.current_url 
	r = requests.get(url)
	soup = BeautifulSoup(r.content, "html.parser")
	page = soup.find("section", {"class" : "Main-content"})
	to_write = []

	# store images in array
	for image in page.findAll('img',{"src":True}):
		src = image['src']
		if not src in to_write:
			to_write.append(src)

	count = 0
	for file in to_write:
		r = requests.get(file, stream=True)

		if r.status_code == 200:                     #200 status code = OK
			with open(f"saved/{name}/{count}.JPG", 'wb') as f: 
				r.raw.decode_content = True
				shutil.copyfileobj(r.raw, f)
		
		count +=1
