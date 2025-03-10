import time

from pages.Base import Base
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException

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
        return Product_details


    def add_item_to_cart(self):
        elements = self.base.driver.find_elements(By.XPATH, '//div[@class="productinfo text-center"]')
        for i in range(1, len(elements) + 1):
            self.base.scroll_page(0, 500)
            self.base.driver.implicitly_wait(10)
            self.base.select_x_path_locator(
                 locator=f'(//a[@href="/product_details/2" or text()="View Product"])[{i}]').click()
            self.base.driver.implicitly_wait(10)
            item = self.base.driver.find_element(By.XPATH, '//button[@class="btn btn-default cart"]')
            item.click()
            self.base.driver.implicitly_wait(10)
            if self.base.select_x_path_locator(
                    locator='//i[@class="material-icons"]') and self.base.select_x_path_locator(
                    locator='(//p[@class="text-center"])[1]'):
                print('Product is added to cart')
                self.base.driver.implicitly_wait(10)
                self.base.select_x_path_locator(
                    locator='//button[@class="btn btn-success close-modal btn-block"]').click()
                self.base.driver.implicitly_wait(10)
                self.base.driver.back()
                self.base.driver.implicitly_wait(10)


    def launch_contact_us(self):
        self.base.open_url('https://www.automationexercise.com/contact_us')

    def verify_get_in_touch_form(self):
        if self.base.select_id_locator(locator="contact-us-form"):
            assert True
        else:
            assert False

    def fill_contact_us_form(self):
        self.base.select_x_path_locator(locator='//input[@placeholder="Name"]').send_keys('Praveen')
        self.base.select_x_path_locator(locator='//input[@placeholder="Email"]').send_keys('sfsfsbshfs@gmail.com')
        self.base.select_x_path_locator(locator='//input[@placeholder="Subject"]').send_keys('Your Product is Nyc - T shirt')
        self.base.select_x_path_locator(locator='//textarea[@placeholder="Your Message Here"]').send_keys('Hi this is me i hope u r u r fine, rendo sari fine, uh fine ...'
                                                                                                       'Bye bro inga')
    def click_on_submit(self):
        self.base.select_x_path_locator(locator='//input[@type="submit"]').click()
        self.base.alerts.accept()


    def verify_succes_msg(self):
        Text = self.base.select_x_path_locator(locator='//div[@class="status alert alert-success"]')
        print(Text.text)

    def close_brwoser(self):
        self.base.close_opened_browser()

