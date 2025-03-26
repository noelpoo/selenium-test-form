import pytest
import os
from pages.form.form_page import FormPage
from utils.config import BASE_URL

@pytest.mark.parametrize("first_name, should_pass", [
        ("Noel", True),                  
        ("Shaw-Kiat", True),                                                   
        ("123", True),  
        ("@@@", True),
        # (" ", False),                
])
def test_first_name(browser, first_name, should_pass):
    form = FormPage(browser)
    form.load(BASE_URL)

    form.first_name.enter_text(first_name)
    form.click_submit

    if should_pass:
        assert form.first_name.get_value() == first_name
        assert form.first_name_feedback.is_visible() == False
    else:
        assert form.first_name_feedback.is_visible() == True


@pytest.mark.parametrize("last_name, should_pass", [
    ("Noel", True),
    ("Shaw-Kiat", True),
    ("123", True),
    ("@@@", True),
    (" ", False),
])
def test_last_name(browser, last_name, should_pass):
    form = FormPage(browser)
    form.load(BASE_URL)

    form.last_name.enter_text(last_name)
    form.click_submit()

    if should_pass:
        assert form.last_name.get_value() == last_name
        assert form.last_name_feedback.is_visible() == False
    else:
        assert form.last_name_feedback.is_visible() == True


@pytest.mark.parametrize("email, should_pass", [
    ("noel@noel.com", True),
    ("noel-noel@noel.com", True),
    ("noel|noel@noel.com" ,True),
    ("noel,noel@noel.com", False),
    ("noel@noel", False),
    ("noel.com", False),
    ("@@@", False),
    (" ", False),
])
def test_email(browser, email, should_pass):
    form = FormPage(browser)
    form.load(BASE_URL)

    form.email.enter_text(email)
    form.click_submit()

    if should_pass:
        assert form.email_feedback.is_visible() == False
    else:
        assert form.email_feedback.is_visible() == True


@pytest.mark.parametrize("mobile_number, should_pass", [
    ("91111111", True),
    ("80001111", True),
    ("9111 1111", True),
    ("8000 1111", True),
    ("62423007", False),
    ("abc", False),
    ("11111111", False),
    ("8231123", False),
])
def test_mobile_number(browser, mobile_number, should_pass):
    form = FormPage(browser)
    form.load(BASE_URL)

    form.mobile_number.enter_text(mobile_number)
    form.click_submit()

    if should_pass:
        assert form.mobile_number_feedback.is_visible() == False
    else:
        assert form.mobile_number_feedback.is_visible() == True


@pytest.mark.parametrize("gender, should_pass", [
    ("Male", True),
    ("Female", True),
    ("", False)
])
def test_gender(browser, gender, should_pass):
    form = FormPage(browser)
    form.load(BASE_URL)

    if gender == "Male":
        form.gender_female_radio.select()
    elif gender == "Female":
        form.gender_female_radio.select()
    else:
        pass
    form.click_submit()

    if should_pass:
        assert form.gender_feedback.is_visible() == False
    else:
        assert form.gender_feedback.is_visible() == True


@pytest.mark.parametrize("date_of_birth, should_pass", [
    ("11/11/2000", True),
    ("17/12/1000", True),
    ("01/01/3000", False),
    ("00/01/1990", False),
    ("12/00/1990", False),
    ("32/01/1990", False),
    ("01/13/1990", False),
])
def test_date_of_birth(browser, date_of_birth, should_pass):
    form = FormPage(browser)
    form.load(BASE_URL)

    form.date_of_birth.enter_date(date_of_birth)
    form.click_submit()

    if should_pass:
        assert form.date_of_birth_feedback.is_visible() == False
    else:
        assert form.date_of_birth_feedback.is_visible() == True

@pytest.mark.parametrize("hobbies, should_pass", [
    (["Sports"], True),
    (["Music"], True),
    (["Reading"], True),
    (["Sports", "Music"], True),
    (["Sports", "Reading"], True),
    (["Music", "Reading"], True),
    (["Sports", "Music", "Reading"], True),
    ([], False)
])
def test_hobbies(browser, hobbies, should_pass):
    form = FormPage(browser)
    form.load(BASE_URL)

    form.hobbies_sports_checkbox.uncheck()
    form.hobbies_music_checkbox.uncheck()
    form.hobbies_reading_checkbox.uncheck()

    if "Sports" in hobbies:
        form.hobbies_sports_checkbox.check()
    if "Music" in hobbies:
        form.hobbies_music_checkbox.check()
    if "Reading" in hobbies:
        form.hobbies_reading_checkbox.check()

    form.click_submit()

    if should_pass:
        assert form.hobbies_feedback.is_visible() == False
    else:
        assert form.hobbies_feedback.is_visible() == True


@pytest.mark.parametrize("file_name, should_pass", [
    ("testfile_50MB.pdf", False),
    ("testfile_5kb.png", True)
])
def test_attachment(browser, file_name, should_pass):
    form = FormPage(browser)
    form.load(BASE_URL)

    file_path = os.path.abspath(os.path.join("data", file_name))
    form.attachments.upload(file_path)

    if should_pass:
        assert form.attachments_feedback.is_visible() == False
    else:
        assert form.attachments_feedback.is_visible() == True

@pytest.mark.skip(reason="Skipping this test temporarily")
@pytest.mark.parametrize("location, should_pass", [
    ("North", True),
    ("South", True),
    ("East", True),
    ("West", True),
])
def test_location(browser, location, should_pass):
    form = FormPage(browser)
    form.load(BASE_URL)

    form.location_dropdown.select_by_text(location)
    form.click_submit()

    if should_pass:
        assert form.location_dropdown.get_selected_value() == location
