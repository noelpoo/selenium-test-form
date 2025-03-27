import pytest
import os
from pages.form.form_page import FormPage
from pages.form.confirmation_page import ConfirmationPage
from utils.config import BASE_URL
from utils.data_loader import load_json_data

form_test_data = load_json_data("form_test_data.json")

@pytest.mark.parametrize("data", form_test_data)
def test_full_form_submission(browser, data):
    form = FormPage(browser)
    form.load(BASE_URL)

    form.first_name.enter_text(data["first_name"])
    form.last_name.enter_text(data["last_name"])
    form.email.enter_text(data["email"])
    
    gender = data["gender"]
    if gender == "Male":
        form.gender_male_radio.select()
    elif gender == "Female":
        form.gender_female_radio.select()
    else:
        pass

    form.mobile_number.enter_text(data["mobile_number"])
    form.date_of_birth.enter_date(data["date_of_birth"])

    checkbox_map = {
    "Sports": form.hobbies_sports_checkbox,
    "Music": form.hobbies_music_checkbox,
    "Reading": form.hobbies_reading_checkbox,
    }

    for cb in checkbox_map.values():
        cb.uncheck()

    for hobby in data["hobbies"]:
        checkbox_map[hobby].check()

    if data["attachment"]:
        file_path = os.path.abspath(os.path.join("data", data["attachment"]))
        form.attachments.upload(file_path)

    form.location_dropdown.select(data["location"])
    form.address.enter_text(data["address"])

    form.click_submit()

    confirmation_page = ConfirmationPage(browser)
    if data["should_pass"]:
        assert confirmation_page.is_displayed()
    else:
        assert not confirmation_page.is_displayed()
