import os
from selenium.webdriver.common.by import By

class TextInput:
    def __init__(self, driver, locator):
        self.driver = driver
        self.locator = locator

    def enter_text(self, text):
        el = self.driver.find_element(*self.locator)
        el.clear()
        el.send_keys(text)

    def enter_date(self, date):
        el = self.driver.find_element(*self.locator)
        el.clear()
        el.click()
        el.send_keys(date)

    def get_value(self):
        return self.driver.find_element(*self.locator).get_attribute("value")
    
class FieldFeedback:
    def __init__(self, driver, locator):
        self.driver = driver
        self.locator = locator
    
    def is_visible(self):
        elements = self.driver.find_elements(*self.locator)
        return len(elements) > 0 and elements[0].is_displayed()
    
class RadioButton:
    def __init__(self, driver, locator):
        self.driver = driver
        self.locator = locator

    def select(self):
        self.driver.find_element(*self.locator).click()

    def is_selected(self):
        return self.driver.find_element(*self.locator).is_selected()
    
class CheckBox:
    def __init__(self, driver, label_locator):
        self.driver = driver
        self.label_locator = label_locator

    def toggle(self):
        self.driver.find_element(*self.label_locator).click()

    def is_checked(self):
        label_el = self.driver.find_element(*self.label_locator)
        input_el = label_el.find_element(By.TAG_NAME, "input")
        return input_el.is_selected()

    def check(self):
        if not self.is_checked():
            self.toggle()

    def uncheck(self):
        if self.is_checked():
            self.toggle()

class FileUploadInput:
    def __init__(self, driver, locator):
        self.driver = driver
        self.locator = locator

    def upload(self, file_path):
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")
        self.driver.find_element(*self.locator).send_keys(file_path)

class Dropdown:
    def __init__(self, driver, toggle_locator, option_locator, input_locator):
        self.driver = driver
        self.toggle_locator = toggle_locator
        self.option_locator = option_locator 
        self.input_locator = input_locator

    def open(self):
        toggle = self.driver.find_element(*self.toggle_locator)
        toggle.click()

    def input_text(self, text):
        input_el = self.driver.find_element(*self.input_locator)
        input_el.clear()
        input_el.send_keys(text)

    def select(self, text):
        if not text:
            return
            
        self.open()
        self.input_text(text)
        option = self.driver.find_element(*self.option_locator)
        option.click()

