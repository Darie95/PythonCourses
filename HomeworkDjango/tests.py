from time import sleep

from django.test import TestCase
from selenium import webdriver
import random
import string


class ItemTests(TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(
            executable_path='C:\chromedriver')

    def test_item_search(self):
        self.driver.get('http://localhost:8000/search/')
        self.driver.find_element_by_id('id_min_price').send_keys('10')
        self.driver.find_element_by_id('id_max_price').send_keys('500')
        self.driver.find_element_by_name('is_sold').click()
        self.driver.find_element_by_tag_name('button').click()
        sleep(10)

        rows = self.driver.find_elements_by_tag_name('tr')
        result_id = [int(row.get_attribute('data-item-id')) for row in rows[1:]]
        self.assertEqual([1, 6], result_id)

    def test_item_create(self):
        self.driver.get('http://localhost:8000/item_create/')
        new_name = ''.join(random.choice(string.ascii_lowercase) for _ in range(10))
        self.driver.find_element_by_id('id_name').send_keys(new_name)
        self.driver.find_element_by_id('id_price').send_keys('100')
        self.driver.find_element_by_xpath("//select/option[@value='1']").click()
        self.driver.find_element_by_tag_name('button').click()
        sleep(10)
        self.assertTrue(new_name in self.driver.page_source)


