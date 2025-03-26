import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


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
    def __init__(self, driver, toggle_locator, options_locator, input_locator):
        self.driver = driver
        self.toggle_locator = toggle_locator
        self.options_locator = options_locator
        self.input_locator = input_locator

    def open(self):
        self.driver.find_element(*self.toggle_locator).click()

    def select_by_text(self, text):
        self.open()
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_any_elements_located(self.options_locator)
        )

        spans = self.driver.find_elements(By.CSS_SELECTOR, "li[role='option'] span.css-0")
        for span in spans:
            print('logging', span)
            if span.text.strip().lower() == text.lower():
                ActionChains(self.driver).move_to_element(span).click().perform()
                return

        raise ValueError(f"Option with text '{text}' not found in dropdown.")
    
    def get_selected_value(self):
        input_el = self.driver.find_element(*self.input_locator)
        return input_el.get_attribute("value")
