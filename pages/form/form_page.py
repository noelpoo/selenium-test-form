from pages.form.fields import TextInput, FieldFeedback, RadioButton, CheckBox, FileUploadInput, Dropdown
from selenium.webdriver.common.by import By

class FormPage:
    def __init__(self, driver):
        self.driver = driver

        self.submit_button = (By.XPATH, "//button[normalize-space(text())='Submit now']")

        self.first_name = TextInput(driver, (By.ID, "64532b5f00efba00121f117e"))
        self.first_name_feedback = FieldFeedback(driver, (By.ID, "64532b5f00efba00121f117e-feedback"))

        self.last_name = TextInput(driver, (By.ID, "64532b696a6af30013dc8321"))
        self.last_name_feedback = FieldFeedback(driver, (By.ID, "64532b696a6af30013dc8321-feedback"))

        self.email = TextInput(driver, (By.ID, "6453521e35eb0c00128fa97d"))
        self.email_feedback = FieldFeedback(driver, (By.ID, "6453521e35eb0c00128fa97d-feedback"))

        self.gender_male_radio = RadioButton(driver, (By.XPATH, "//label[.//input[@value='Male']]"))
        self.gender_female_radio = RadioButton(driver, (By.XPATH, "//label[.//input[@value='Female']]"))
        self.gender_feedback = FieldFeedback(driver, (By.ID, "6453524b93ceeb0012cbe76e-feedback"))

        self.mobile_number = TextInput(driver, (By.ID, "6453527335eb0c00128fbabf"))
        self.mobile_number_feedback = FieldFeedback(driver, (By.ID, "6453527335eb0c00128fbabf-feedback"))

        self.date_of_birth = TextInput(driver, (By.ID, "645352c16dc31e001202f56f"))
        self.date_of_birth_feedback = FieldFeedback(driver, (By.ID, "645352c16dc31e001202f56f-feedback"))

        self.hobbies_sports_checkbox = CheckBox(driver, (By.XPATH, "//label[.//span[text()='Sports']]"))
        self.hobbies_music_checkbox = CheckBox(driver, (By.XPATH, "//label[.//span[text()='Music']]"))
        self.hobbies_reading_checkbox = CheckBox(driver, (By.XPATH, "//label[.//span[text()='Reading']]"))
        self.hobbies_feedback = FieldFeedback(driver, (By.ID, "645354a681cb0e001299b47c-feedback"))

        self.attachments = FileUploadInput(driver, (By.ID, "645354f093ceeb0012cc628a"))
        self.attachments_feedback = FieldFeedback(driver, (By.ID, "645354f093ceeb0012cc628a-feedback"))

        # need to fix this locator, its not working
        self.location_dropdown = Dropdown(
            driver, 
            toggle_locator=(By.ID, "downshift-0-toggle-button"),
            options_locator=(By.CSS_SELECTOR, "li[role='option']"),
            input_locator=(By.ID, "6453551e00efba001225204b")
        )

        self.address = TextInput(driver, (By.ID, "6453553781cb0e001299cc83"))

    def load(self, base_url):
        self.driver.get(f"{base_url}")

    def click_submit(self):
        self.driver.find_element(*self.submit_button).click()
