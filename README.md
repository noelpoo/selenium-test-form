# Selenium Automation Suite - Test Form Submission

This project automates the testing of a web form using **Selenium WebDriver** with **Python**, applying the **Page Object Model (POM)** design pattern, **data-driven testing**, and supporting both positive and negative validation flows.

---

## Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Setup](#setup)
- [Test Strategy Overview](#test-strategy-overview)
  - [Approach](#approach)
  - [Page Object Model (POM)](#page-object-model-pom-architecture)
  - [Component Classes](#field-specific-component-classes)
  - [Validation Strategy](#validation-strategy)
  - [Data-Driven Testing](#data-driven-testing)
  - [Cross-Browser Testing](#cross-browser-testing)
  - [CI Integration with GitHub Actions](#ci-integration-with-github-actions)

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

## Test Strategy Overview

### **Approach**

1. **Page Object Model (POM) Architecture**
    - The test suite is built around the **Page Object Model**, which cleanly separates test logic from UI element handling.
    - Each field type is abstracted into **reusable, modular components**: `TextInput`, `RadioButton`, `CheckBox`, `FieldFeedback`.
2. **Field-specific Component Classes**
    - `TextInput`: handles both text and date input types.
    - `RadioButton`: abstracts the behavior for selecting gender options.
    - `CheckBox`: smartly handles state-based toggling and selection.
    - `FieldFeedback`: handles validation feedback visibility.
    - `FileUploadInput` : handles file uploads
3. **Separation of Concerns**
    - The `FormPage` object is clean and focused on mapping elements and not logic. The test logic stays in the test files.
4. **Validation Strategy**
    - **Positive tests** assert that valid inputs bypass validation.
    - **Negative tests** assert that invalid/missing inputs trigger visible feedback errors.
    - **Feedback checks** rely on the visibility of Chakra UI's feedback elements.
5. **Data-Driven Testing**
    - Field Validation test cases are driven by `@pytest.mark.parametrize` decorators, enabling broad input coverage for each form field.
    - For full form validation, the test suite uses a **JSON data file (`form_test_data.json`)** as the source of truth for test input. Each object in the JSON array represents a complete form submission, including all fields (both required and optional) and an expected outcome (`should_pass`). The data is loaded dynamically using a utility loader function and passed into the test via `@pytest.mark.parametrize`. This approach makes the test logic clean, allows non-technical contributors to add new test cases, and separates test data from test code for better maintainability.
    - This allows concise, readable tests while testing many combinations.
6. **Cross-Browser Testing**
    - The test suite supports **Chrome, Firefox, Safari, and Edge** via a configurable `--browser` command-line flag.
    - A custom `pytest_addoption` hook enables dynamic browser selection at runtime.
    - In CI/CD, GitHub Actions is configured with a **matrix strategy** to run tests in **parallel** across Chrome, Firefox, and Edge, validating that the form behaves consistently regardless of browser.
    - Safari is supported locally on macOS but **excluded** from CI due to its lack of headless mode and limited Linux support.
7. **CI Integration with GitHub Actions**
    - The test suite is fully integrated with **GitHub Actions** for automated execution on every pull request merge to the `develop` branch.
    - A CI workflow defined in `.github/workflows/on_merge.yml` runs all test suites in headless mode using a **matrix strategy**, allowing parallel execution across multiple browsers (Chrome, Firefox, Edge).
    - Environment variables and secrets are stored in repository secrets
    - The workflow automatically:
        - Installs dependencies from `requirements.txt`
        - Launches Selenium-compatible browsers via the GitHub-hosted runners
        - Executes tests and reports results
        - Uploads test reports as artifacts