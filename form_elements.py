from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

from driver import *


class Form:
    def __init__(self):
        self.page = driver.find_element(By.ID, "body")
        self.name_input = driver.find_element(By.ID, "name-input")
        self.password_input = driver.find_element(By.XPATH, "//input[@type='password']")
        self.checkbox_drink_1 = driver.find_element(By.ID, "drink1")
        self.checkbox_drink_2 = driver.find_element(By.ID, "drink2")
        self.checkbox_drink_3 = driver.find_element(By.ID, "drink3")
        self.checkbox_drink_4 = driver.find_element(By.ID, "drink4")
        self.checkbox_drink_5 = driver.find_element(By.ID, "drink5")
        self.radiobutton_color_1 = driver.find_element(By.ID, "color1")
        self.radiobutton_color_2 = driver.find_element(By.ID, "color2")
        self.radiobutton_color_3 = driver.find_element(By.ID, "color3")
        self.radiobutton_color_4 = driver.find_element(By.ID, "color4")
        self.radiobutton_color_5 = driver.find_element(By.ID, "color5")
        self.select_automation = driver.find_element(By.ID, "automation")
        self.tools = driver.find_elements(By.XPATH, "//form[@id='feedbackForm']/ul/li")
        self.email_input = driver.find_element(By.ID, "email")
        self.message_input = driver.find_element(By.ID, "message")
        self.submit_button = driver.find_element(By.ID, "submit-btn")

    def check_form_is_open(self):
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "body")))
        assert self.page

    def scroll_to(self, element):
        ActionChains(driver).scroll_to_element(element).perform()

    def enter_name(self, name):
        self.name_input.clear()
        self.name_input.send_keys(name)

    def enter_password(self, password):
        self.password_input.clear()
        self.password_input.send_keys(password)

    def choose_drink(self, drink):
        drinks = {"Water": self.checkbox_drink_1,
                  "Milk": self.checkbox_drink_2,
                  "Coffee": self.checkbox_drink_3,
                  "Wine": self.checkbox_drink_4,
                  "Ctrl-Alt-Delight": self.checkbox_drink_5}
        drinks[drink].click()

    def choose_color(self, color):
        colors = {"Red": self.radiobutton_color_1,
                  "Blue": self.radiobutton_color_2,
                  "Yellow": self.radiobutton_color_3,
                  "Green": self.radiobutton_color_4,
                  "#FFC0CB": self.radiobutton_color_5}
        chosen_color = colors[color]
        self.scroll_to(chosen_color)
        chosen_color.click()

    def select_love_automation(self, text):
        select_element = self.select_automation
        self.scroll_to(select_element)
        select = Select(select_element)
        select.select_by_visible_text(text)

    def enter_email(self, email):
        email_input = self.email_input
        self.scroll_to(email_input)
        email_input.clear()
        email_input.send_keys(email)

    def count_automation_tools(self):
        count = len(self.tools)
        return count

    def get_longest_tool(self):
        longest_tool = self.tools[0].text
        for i in range(1, len(self.tools)):
            tool = self.tools[i].text
            if len(tool) > len(longest_tool):
                longest_tool = tool
        return longest_tool

    def enter_message(self, message):
        message_input = self.message_input
        self.scroll_to(message_input)
        message_input.send_keys(message)

    def submit(self):
        button = self.submit_button
        self.scroll_to(button)
        button.click()

    def check_receive_message_alert(self):
        WebDriverWait(driver, 10).until(EC.alert_is_present())
        alert_text = driver.switch_to.alert.text
        assert alert_text == "Message received!", "Unknown alert"

    def close_alert(self):
        WebDriverWait(driver, 10).until(EC.alert_is_present())
        driver.switch_to.alert.accept()
