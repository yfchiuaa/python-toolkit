from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


class SeleniumSetup:
    def __init__(self):

        # Driver options
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--ignore-ssl-errors')
        options.add_experimental_option('w3c')      # Resolve cannot call non-w3c standard command

        # Set up the driver
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

        # The `Implicit Waits` method (https://selenium-python.readthedocs.io/waits.html)
        self.driver.implicitly_wait(10)

    def __del__(self):

        self.driver.close()

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
