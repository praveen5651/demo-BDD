from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
import random
from selenium.webdriver.chrome.options import Options

class Base:
    _instance = None  # Class-level instance variable

    def __new__(cls, *args, **kwargs):
        """ Ensure only one instance of Base is created """
        if cls._instance is None:
            cls._instance = super(Base, cls).__new__(cls)
            cls._instance._initialize()
        return cls._instance

    def _initialize(self):
        """ Initialize the WebDriver only once """
        options = Options()
        # options.add_argument("--headless")  # Run Chrome in headless mode
        # options.add_argument("--no-sandbox")
        # options.add_argument("--disable-dev-shm-usage")

        self.driver = webdriver.Chrome(options=options)
        self.action = ActionChains(self.driver)


    def open_url(self, url):
        self.driver.get(url=url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def close_opened_browser(self):
        self.driver.close()


    def scroll_page(self, x_value, y_value):
        self.driver.execute_script(f'window.scrollBy({x_value}, {y_value})')

    def scroll_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def select_x_path_locator(self, locator):
        return self.driver.find_element(By.XPATH,locator)

    def select_id_locator(self, locator):
        return self.driver.find_element(By.ID,locator)

    def action_class(self, locator):
        self.action.click(locator).release().perform()

    def enter_username_and_emai_id(self):
        user_names = ["praveenKumar3", "kumarPraveen", "PKPraveen", "KUmarPK"]
        user_name = random.choice(user_names)
        rand_nums = random.randint(1, 1000)
        user_mail = user_name + str(rand_nums) + "@gmail.com"
        return user_name,user_mail









