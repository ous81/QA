import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
import threading
import sys
import os

# Add the parent directory to the system path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app  # Assuming `app` is your Flask app instance

class TestProductExceptSelfE2E(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Start the Flask app in a separate thread
        cls.app_thread = threading.Thread(target=app.run, kwargs={'debug': False, 'use_reloader': False})
        cls.app_thread.daemon = True
        cls.app_thread.start()
        time.sleep(1)  # Give the server a second to ensure it's up

        # Initialize the Selenium WebDriver
        cls.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        cls.driver.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        self.driver.get('http://127.0.0.1:5000/')

    def test_product_except_self_valid_input(self):
        driver = self.driver
        nums_input = driver.find_element(By.ID, 'nums')
        nums_input.clear()
        nums_input.send_keys('1,2,3,4')
        driver.find_element(By.TAG_NAME, 'button').click()
        time.sleep(1)
        result = driver.find_element(By.ID, 'result').text
        self.assertEqual(result, 'Result: 24, 12, 8, 6')

    def test_product_except_self_invalid_input(self):
        driver = self.driver
        nums_input = driver.find_element(By.ID, 'nums')
        nums_input.clear()
        nums_input.send_keys('a,b,c')
        driver.find_element(By.TAG_NAME, 'button').click()
        time.sleep(1)
        result = driver.find_element(By.ID, 'result').text
        self.assertIn('Error:', result)

if __name__ == '__main__':
    unittest.main()
