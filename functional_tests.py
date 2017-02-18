from selenium import webdriver

browser = webdriver.Chrome('/Users/rico/Downloads/chromedriver')

#judith has heard about a cool new online todo app
#she goes to check it out
browser.get('http://localhost:8000')

#she notices the page titel and header mention to-do lists
assert 'To-Do' in browser.title

#she is invited to enter a to-do item straight away

#she types "buy some feathers" into a text box

#when she hits enter the page updates and now the page lists
#"1: Buy some feathers" as an item on her todo list

#there is still another text box inviting her to add
#she enters something else

#the page updates again and now shows both items

#she wonders whether the site will remember her list
#then she sees that the site has generated a unique url for her
#there is some explanatory text to that effect

#she visits that url her to-do list is still there

#satisfied she goes back to sleep

browser.quit()
