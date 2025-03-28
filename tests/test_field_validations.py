import pytest
import os
from pages.form.form_page import FormPage
from utils.config import BASE_URL
from utils.assertions import assert_feedback

@pytest.mark.parametrize("first_name, should_pass", [
        ("Noel", True),                  
        ("Shaw-Kiat", True),                                                   
        ("123", True),  
        ("@@@", True),
        (" ", False),                
])
def test_first_name_required_and_valid_validation(browser, first_name, should_pass):
    form = FormPage(browser)
    form.load(BASE_URL)

    form.first_name.enter_text(first_name)
    form.click_submit()

    assert_feedback(form.first_name_feedback, should_pass)


@pytest.mark.parametrize("last_name, should_pass", [
    ("Noel", True),
    ("Shaw-Kiat", True),
    ("123", True),
    ("@@@", True),
    (" ", False),
])
def test_last_name_required_and_valid_validation(browser, last_name, should_pass):
    form = FormPage(browser)
    form.load(BASE_URL)

    form.last_name.enter_text(last_name)
    form.click_submit()

    assert_feedback(form.last_name_feedback, should_pass)


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
def test_email_required_and_valid_validation(browser, email, should_pass):
    form = FormPage(browser)
    form.load(BASE_URL)

    form.email.enter_text(email)
    form.click_submit()

    assert_feedback(form.email_feedback, should_pass)


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
def test_mobile_number_required_and_valid_validation(browser, mobile_number, should_pass):
    form = FormPage(browser)
    form.load(BASE_URL)

    form.mobile_number.enter_text(mobile_number)
    form.click_submit()

    assert_feedback(form.mobile_number_feedback, should_pass)


@pytest.mark.parametrize("gender, should_pass", [
    ("Male", True),
    ("Female", True),
    ("", False)
])
def test_gender_required_validation(browser, gender, should_pass):
    form = FormPage(browser)
    form.load(BASE_URL)

    if gender == "Male":
        form.gender_female_radio.select()
    elif gender == "Female":
        form.gender_female_radio.select()
    else:
        pass
    form.click_submit()

    assert_feedback(form.gender_feedback, should_pass)


@pytest.mark.parametrize("date_of_birth, should_pass", [
    ("11/11/2000", True),
    ("17/12/1000", True),
    ("01/01/3000", False),
    ("00/01/1990", False),
    ("12/00/1990", False),
    ("32/01/1990", False),
    ("01/13/1990", False),
])
def test_date_of_birth_required_and_valid_validation(browser, date_of_birth, should_pass):
    form = FormPage(browser)
    form.load(BASE_URL)

    form.date_of_birth.enter_date(date_of_birth)
    form.click_submit()

    assert_feedback(form.date_of_birth_feedback, should_pass)


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
def test_hobbies_required_validation(browser, hobbies, should_pass):
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

    assert_feedback(form.hobbies_feedback, should_pass)


@pytest.mark.parametrize("file_name, should_pass", [
    ("testfile_50MB.pdf", False),
    ("testfile_5kb.png", True)
])
def test_attachment_size_validation(browser, file_name, should_pass):
    form = FormPage(browser)
    form.load(BASE_URL)

    file_path = os.path.abspath(os.path.join("data", file_name))
    form.attachments.upload(file_path)

    assert_feedback(form.attachments_feedback, should_pass)
    