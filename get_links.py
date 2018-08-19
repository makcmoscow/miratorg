from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException as NoElement
from selenium.common.exceptions import \
    StaleElementReferenceException as NoElement2
from selenium.common.exceptions import ElementNotVisibleException as NotVisible

MAIN_PAGE = 'https://shop.miratorg.ru/'

class Parser:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get(MAIN_PAGE)
        self.categories = []


    def get_categories(self):
        lis = self.driver.find_element_by_xpath('//nav[@class="menu-item first"]').find_elements_by_tag_name('li')
        lis = lis[:-1]

        print(len(lis))
        for li in lis:
            deep = li.find_elements_by_class_name('hidden')
            if len(deep) == 0:
                href = li.find_element_by_tag_name('a').get_attribute('href')
                self.categories.append(href)

            else:
                pass
        print(len(self.categories))



    def get_links(self, category='https://shop.miratorg.ru/catalog/kulinariya/'):
        self.driver.get(category)
        multipl = 1
        while True:
            self.driver.execute_script("window.scrollTo(0, {})".format(3000*multipl))
            try:
                shows = self.driver.find_elements_by_xpath('//a[@data-use="show-more-2"]')
                if len(shows)>0:
                    self.driver.find_element_by_xpath('//a[@data-use="show-more-2"]').click()
                    multipl *=2
                else:
                    break
            except Exception as e:
                pass

        #self.driver.find_element('data-entity', 'items-row')



parser = Parser()
#parser.get_categories()
parser.get_links()