# Selenium Automation Suite - Test Form Submission

This project automates the testing of a web form using **Selenium WebDriver** with **Python**, applying the **Page Object Model (POM)** design pattern, **data-driven testing**, and supporting both positive and negative validation flows.

---

## Features
-  Full-form end-to-end test coverage
-  Field-by-field validation (required fields, formats, etc.)
-  Data-driven tests from JSON
-  Page Object Model for modular, maintainable code
-  Cross-browser testing support (Chrome, Firefox, Edge)
-  Integrated into GitHub Actions CI pipeline

---

## Project Structure

```
selenium-test-form/
├── .github/
│   └── workflows/
│       └── on_merge.yml           # GitHub Actions CI workflow
├── data/
│   ├── form_test_data.json        # JSON test datasets
│   ├── testfile_50MB.pdf          # File upload test file
│   └── testfile_5kb.png           # File upload test file
│
├── pages/
│   └── form/
│       ├── form_page.py           # Main form Page Object
│       ├── fields.py              # Modular form components 
│       └── confirmation_page.py   # Page object for post-submission confirmation
│
├── tests/
│   ├── test_form_validations.py   # Data-driven test using the full form
│   └── test_field_validations.py  # Field-by-field validation tests
|
├── utils/
│   ├── config.py                  # Test environment config (e.g., BASE_URL)
│   └── data_loader.py             # Utility to load test data from JSON
│
├── .gitignore                     # Files and folders to exclude from Git
├── requirements.txt               # Project dependencies
└── README.md                      # Project documentation (you’re here!)

```
## Setup

Follow these steps to set up the project:

1. **Clone the repository**:
    ```sh
    git clone https://github.com/noelpoo/selenium-test-form.git
    cd selenium-test-form
    ```

2. **Create and activate a virtual environment**:
    ```sh
    python -m venv venv
    source venv/bin/activate
    ```

3. **Install dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Set up environment variables**:
    - Create a `.env` file in the root directory.
    - Add the necessary environment variables (e.g., `BASE_URL`).
    ```
    BASE_URL=https://example.com 
    ```

5. **Add Test Data:**
    - Place test data files in the `data/` directory.
    ```
    data
    ├── testfile_50MB.pdf
    └── testfile_5kb.png
    └── form_test_data.json
    ```

6. **Run the tests**:
    ```sh
    pytest --html=report.html
    ```
7. **Run the tests in various browsers:**
    - Chrome:
    ```
    pytest --html=report.html --browser=chrome
    ```
    - Firefox:
    ```
    pytest --html=report.html --browser=firefox
    ```
    - MS Edge:
    ```
    pytest --html=report.html --browser=edge
    ```
