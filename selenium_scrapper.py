from selenium import webdriver
from selenium.webdriver.chrome.options import  Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
import time
import sys


url = "https://www.brainyquote.com/"
driver_path="D:\\chromedriver_win32\\chromedriver.exe"
chrome_options = Options()
chrome_options.add_argument("--ignore-certificate-errors")

webdriver = webdriver.Chrome( driver_path ,options=chrome_options)

#default search query
search_query = "life"

if(len(sys.argv))>=2:
	search_query = sys.argv[1]
	print(search_query)

with webdriver as driver:
	#timeout
	wait = WebDriverWait(driver,10)

	#retrive data
	driver.get(url)

	#find searchbox
	search = driver.find_element_by_id("hmSearch")
	search.send_keys(search_query + Keys.RETURN)

	#wait
	wait.until(presence_of_element_located((By.ID,"quotesList")))
	results = driver.find_elements_by_class_name("m-brick")
	for quote in results:
		q_array = quote.text
		print(q_array)
		with open("contents.txt", "a") as f:
		    f.write(">> "+q_array+"\n\n")


	driver.close()
