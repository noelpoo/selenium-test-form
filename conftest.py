import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions

def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Choose a browser to run tests on"
    )

@pytest.fixture
def browser(request):
    browser_type = request.config.getoption("--browser")
    if browser_type == "chrome":
        options = ChromeOptions()
        options.add_argument("--headless")
        driver = webdriver.Chrome(options=options)

    elif browser_type == "firefox":
        options = FirefoxOptions()
        options.add_argument("--headless")
        driver = webdriver.Firefox(options=options)

    elif browser_type == "edge":
        options = EdgeOptions()
        options.use_chromium = True
        options.add_argument("--headless")
        driver = webdriver.Edge(options=options)

    else:
        raise ValueError(f"Unsupported browser: {browser_type}")
    
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

# @pytest.fixture
# def browser():
#     options = Options()
#     options.add_argument("--headless")
#     driver = webdriver.Chrome(options=options)
#     driver.implicitly_wait(10)
#     yield driver
#     driver.quit()
