from selenium import webdriver
import time
import os
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException as NoElement
from selenium.common.exceptions import \
    StaleElementReferenceException as NoElement2
from selenium.common.exceptions import ElementNotVisibleException as NotVisible

MAIN_PAGE = 'https://shop.miratorg.ru/'
PATH = 'D:\python\miratorg\\'

class Parser:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get(MAIN_PAGE)
        self.categories = []
        self.hrefs = []


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




    def get_links(self, category):
        self.driver.get(category)
        self.open_all_page()
        self.find_products()
        for product in self.products:
            self.get_link(product)
        filename = category.split('/')[-2]
        if (filename+'.txt') not in os.listdir(PATH+'txt/'):
            with open(PATH+'txt/'+filename+'.txt', 'w') as file:
                for link in self.hrefs:
                    file.write(link+'\n')
        else:
            with open(PATH+'txt/'+filename+'.txt', 'a') as file:
                for link in self.hrefs:
                    file.write(link+'\n')

        self.hrefs = []


        #self.driver.find_element('data-entity', 'items-row')

    def open_all_page(self):
        multipl = 1
        while True:
            self.driver.execute_script("window.scrollTo(0, {})".format(3000 * multipl))
            try:
                shows = self.driver.find_elements_by_xpath('//a[@data-use="show-more-2"]')
                if len(shows) > 0:
                    self.driver.find_element_by_xpath('//a[@data-use="show-more-2"]').click()
                    multipl *= 2
                    time.sleep(1)
                else:
                    break
            except Exception as e:
                pass

    def find_products(self):
        self.products = self.driver.find_elements_by_xpath('//div[@class="cat-item product-block-js"]')

    def get_link(self, product):
        href = product.find_element_by_class_name('card-link-js').get_attribute('href')
        self.hrefs.append(href)

    def start(self):
        self.get_categories()
        for category in self.categories:
            self.get_links(category)

parser = Parser()
parser.start()