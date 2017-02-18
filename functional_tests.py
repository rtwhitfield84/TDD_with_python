from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	def test_can_start_a_list_and_retrieve_it_later(self):
		#judith has heard about a cool new online todo app
		#she goes to check it out
		self.browser.get('http://localhost:8000')
		
		#she notices the page title and header mention to-do lists
		self.assertIn('To-Do', self.browser.title)
		self.fail('Finish the test!')

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

if __name__ == '__main__':
	unittest.main(warnings='ignore')