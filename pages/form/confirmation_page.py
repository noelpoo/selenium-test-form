from selenium.webdriver.common.by import By

class ConfirmationPage:
    def __init__(self, driver):
        self.driver = driver
        self.message_locator = (By.XPATH, "//*[contains(text(), 'Thank you for filling out the form.')]")

    def get_confirmation_message(self):
        return self.driver.find_element(*self.message_locator).text

    def is_displayed(self):
        elements = self.driver.find_elements(*self.message_locator)
        return len(elements) > 0 and elements[0].is_displayed()