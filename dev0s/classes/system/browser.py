
# imports
from dev0s.classes.config import *

# selenium.
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium import webdriver


# the disks object class.
class Browser(object):
	def __init__(self,
		# the driver.
		driver="chromedriver",
	):

		# docs.
		DOCS = {
			"module":"dev0s.system.Browser", 
			"initialized":False,
			"description":[], 
			"chapter": "System", }
		
		# objects.
		#options = Options()
		#options.binary_location = "C:\\Program Files\\Chrome\\chrome64_55.0.2883.75\\chrome.exe"
		#driver = webdriver.Chrome(chrome_options = options, executable_path=r'C:\path\to\chromedriver.exe')
		if driver in ["chrome", "google chrome", "chromedriver"]:
			#self.driver = webdriver.Chrome(f'{SOURCE_PATH}/classes/browser/drivers/{OS}/chromedriver')
			self.driver = webdriver.Chrome("/usr/local/bin/chromedriver")
		elif driver in ["firefox", "geckodriver"]:
			#self.driver = webdriver.Firefox(executable_path=f'{SOURCE_PATH}/classes/browser/drivers/{OS}/geckodriver')
			self.driver = webdriver.Firefox(executable_path="/usr/local/bin/geckodriver")
		else:
			raise ValueError(f"Unknown driver: {driver}")

		#
	def get(self, url):
		self.driver.get(url)
	def get_element(self,
		# the element type.
		element="input",
		# the attribute name.
		attribute="name",
		# the attributes value.
		value="username",
		# the parent element (default is self.driver).
		parent=None, 
	):
		#search_bar = driver.find_element_by_name("q")
		if parent == None:
			return self.driver.find_element_by_xpath(f"//{element}[@{attribute}='{value}']")
		else:
			return parent.find_element_by_xpath(f".//{element}[@{attribute}='{value}']")