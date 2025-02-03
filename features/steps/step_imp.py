import time

from pages.Base import Base
from selenium.webdriver.common.by import By

import random

class StepImp:
    def __init__(self):
        self.base = Base()

    def launch_page(self):
        self.base.open_url(url='https://www.automationexercise.com/')

    def verify_slider_row(self):
        elements = self.base.driver.find_elements(By.XPATH,'//img[@src="/static/images/home/girl2.jpg" or @class="girl img-responsive"]')
        count = 0
        for item in range(len(elements)):
            print(f"{count+1} Image Loaded")
            self.base.select_x_path_locator(locator='(//i[@class="fa fa-angle-right"])[1]').click()
            self.base.driver.implicitly_wait(5)

    def verify_category_text(self):
        text = self.base.select_x_path_locator(locator='//h2[text()="Category"]')
        print(text.text)
        if text.text == "CATEGORY":
            print("Pass Ayyindi Bro...")
        else:
            assert False, "Poyindi Kaka"

    def verify_brand_text(self):
        self.base.scroll_page(0,300)
        text = self.base.select_x_path_locator(locator='//h2[text()="Brands"]')
        if text.text == "BRANDS":
            print("Pass Ayyindi Bro...")
        else:
            assert False, "Poyindi Kaka"

    def verify_features_item_text(self):
        text = self.base.select_x_path_locator(locator='//h2[text()="Features Items"]')
        if text.text == "FEATURES ITEMS":
            print("Pass Ayyindi Bro...")
        else:
            assert False, "Poyindi Kaka"

    def scroll_to_bottom(self):
        self.base.scroll_to_bottom()


    def verify_subscription_text(self):
        text = self.base.select_x_path_locator(locator='// h2[text() = "Subscription"]')
        if text.text == "SUBSCRIPTION":
            print("Pass Ayyindi Bro...")
        else:
            assert False, "Poyindi Kaka"

    def select_item(self):
        self.base.select_x_path_locator(locator='//a[@href="/product_details/2"]').click()
        self.base.driver.implicitly_wait(5)

    def product_title(self):
        text = self.base.select_x_path_locator(locator='// h2[text() = "Men Tshirt"]')
        print(text.text)
        print(self.base.driver.current_url)
        if text.text == "Men Tshirt" and self.base.driver.current_url == 'https://www.automationexercise.com/product_details/2':
            print("Pass Ayyindi Bro...")
        else:
            assert False, "Poyindi Kaka"

    def current_url(self):
        if self.base.driver.current_url == 'https://www.automationexercise.com/product_details/2':
            print("Pass Ayyindi Bro...")
        else:
            assert False, "Poyindi Kaka"

    def click_sigup_up(self):
        self.base.select_x_path_locator(locator='//a[@href="/login"]').click()


    def enter_new_user_name_and_email(self):
        user_name, user_mail =  self.base.enter_username_and_emai_id()
        self.base.select_x_path_locator(locator='//input[@placeholder="Name"]').send_keys(user_name)
        self.base.driver.implicitly_wait(5)
        self.base.select_x_path_locator(locator='(//input[@placeholder="Email Address"])[2]').send_keys(user_mail)
        self.base.driver.implicitly_wait(5)
        self.base.select_x_path_locator(locator='// button[ @ type = "submit" and text() = "Signup"]').click()
        self.base.driver.implicitly_wait(5)



    def validate_enter_deatils_text(self):
        #Enter Account Information
        text = self.base.select_x_path_locator(locator='(//h2[@class="title text-center"])[1]')
        print(text.text)
        if text.text == "ENTER ACCOUNT INFORMATION":
            print("Pass Ayyindi Bro...")
        else:
            assert False, "Poyindi Kaka"
        self.base.driver.implicitly_wait(5)

    def enter_star_feilds(self):
        self.base.scroll_page(0,188)
        self.base.select_x_path_locator(locator='//input[@type="password"]').send_keys(123654789)
        self.base.driver.implicitly_wait(5)
        self.base.scroll_page(0, 728)
        self.base.driver.implicitly_wait(5)
        self.base.select_x_path_locator(locator='//input[@id="first_name"]').send_keys('pkkkk')
        self.base.driver.implicitly_wait(5)
        self.base.select_x_path_locator(locator='//input[@id="last_name"]').send_keys('lastbname')
        self.base.driver.implicitly_wait(5)
        self.base.select_x_path_locator(locator='//input[@id="address1"]').send_keys('plot 4')
        self.base.driver.implicitly_wait(5)
        self.base.select_x_path_locator(locator='//input[@id="state"]').send_keys('telanagana')
        self.base.driver.implicitly_wait(5)
        self.base.select_x_path_locator(locator='//input[@id="city"]').send_keys('hyf')
        self.base.scroll_page(0, 1216)
        self.base.driver.implicitly_wait(5)
        self.base.select_x_path_locator(locator='//input[@id="zipcode"]').send_keys(1254789)
        self.base.driver.implicitly_wait(5)
        self.base.select_x_path_locator(locator='//input[@id="mobile_number"]').send_keys(1236547890)
        self.base.driver.implicitly_wait(5)

    def click_create_acc(self):
        self.base.select_x_path_locator(locator='//button[@type="submit" and text()="Create Account"]').click()
        self.base.driver.implicitly_wait(5)

    def verify_acc_create_cmp_msg(self):
        if self.base.select_x_path_locator(locator='//b[text()="Account Created!"]'):
            assert True
        else:
            assert False

    def enter_existed_user_details(self, username, password):
        self.base.select_x_path_locator(locator='(//input[@placeholder="Email Address" and @name="email"])[1]').send_keys(username=username)
        self.base.select_x_path_locator(locator='//input[@type="password"]').send_keys(password=password)
        self.base.driver.implicitly_wait(5)

    def click_login(self):
        self.base.scroll_page(0,100)
        self.base.select_x_path_locator(locator='//button[@type="submit" and text()="Login"]').click()
        self.base.driver.implicitly_wait(5)

    def logout_button(self):
        button = self.base.select_x_path_locator(locator='//a[@href="/logout"]')
        print(button.text)
        if button:
            assert True
        else:
            assert False


    def click_on_product(self):
        self.base.select_x_path_locator(locator='//a[@href="/products"]').click()
        self.base.driver.implicitly_wait(2)

    def search_for_product(self,product):
        self.base.select_x_path_locator(locator='//input[@id="search_product"]').send_keys(product)
        self.base.driver.implicitly_wait(5)

    def click_on_search_icon(self):
        self.base.select_x_path_locator(locator='//button[@type="button"]').click()

    def validate_results(self):
        Product_details = {'Product_title':[],
                           'Price':[]}

        elements = self.base.driver.find_elements(By.XPATH, '//div[@class="single-products"]')
        for elemenet in elements:
            lines = elemenet.text.split("\n")
            price = int(lines[0].replace("Rs.", "").strip())
            prdocut_title = lines[1].strip()
            Product_details["Price"].append(price)
            Product_details['Product_title'].append(prdocut_title)


    def close_brwoser(self):
        self.base.close_opened_browser()










