from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, InvalidArgumentException


class SeleniumSetup:
    def __init__(self, url: str):

        # The base url for opening
        self.url = url

        # The driver to use
        self.driver = None

    def __del__(self):

        if self.driver:
            self.driver.close()

    def chrome_driver_setup(self):

        # Chome driver options
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--ignore-ssl-errors')
        options.add_experimental_option('w3c', False)      # Resolve cannot call non-w3c standard command

        # Set up the driver
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

        # The `Implicit Waits` method (https://selenium-python.readthedocs.io/waits.html)
        self.driver.implicitly_wait(10)

    def start_driver(self):

        try:
            self.driver.get(self.url)
        except InvalidArgumentException:
            print("Please check your url if it is valid")

    def get_driver(self) -> webdriver:

        return self.driver

    def is_page_loaded_js(self) -> bool:
        """ Check page finish loading by check readystate (Not reliable) """

        page_state = self.driver.execute_script('return document.readyState;')
        return page_state == 'complete'

    def is_page_loaded_element(self, id_of_element: str) -> bool:
        """ The `Explicit Waits` method check page finish loading by wait for expected element  """

        try:
            is_element_present = EC.presence_of_element_located((By.ID, id_of_element))
            WebDriverWait(self.driver, 60).until(is_element_present)
        except TimeoutException:
            print("The page is taking too long to load")


if __name__ == "__main__":
    url = input("Please enter the url you wanna go to: ")
    selenium_setup = SeleniumSetup(url)
    selenium_setup.chrome_driver_setup()
    selenium_setup.start_driver()
