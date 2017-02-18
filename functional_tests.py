from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	def check_for_row_in_list_table(self, row_text):
		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertIn(row_text, [row.text for row in rows])

	def test_can_start_a_list_and_retrieve_it_later(self):
		#judith has heard about a cool new online todo app
		#she goes to check it out
		self.browser.get('http://localhost:8000')
		
		#she notices the page title and header mention to-do lists
		self.assertIn('To-Do', self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('To-Do', header_text)

		#she is invited to enter a to-do item straight away
		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertEqual(
				inputbox.get_attribute('placeholder'),
				'Enter a to-do item'
		)

		#she types "buy some feathers" into a text box
		inputbox.send_keys('Buy peacock feathers')

		#when she hits enter the page updates and now the page lists
		#"1: Buy some feathers" as an item on her todo list
		inputbox = self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys('Use peacock feathers to make a fly')
		inputbox.send_keys(Keys.ENTER)
		self.check_for_row_in_list_table('1: Buy peacock feathers')
		self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')

		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertIn('1: Buy peacock feathers', [row.text for row in rows])




		#there is still another text box inviting her to add
		#she enters something else
		self.fail('finish the test')
		#the page updates again and now shows both items

		#she wonders whether the site will remember her list
		#then she sees that the site has generated a unique url for her
		#there is some explanatory text to that effect

		#she visits that url her to-do list is still there

		#satisfied she goes back to sleep

if __name__ == '__main__':
	unittest.main(warnings='ignore')