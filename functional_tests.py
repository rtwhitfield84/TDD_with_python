from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://localhost:800')

assert 'Django' in browser.title