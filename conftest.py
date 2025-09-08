import pytest
from selene import browser

@pytest.fixture()
def setup_browser():
    browser.config.window_height = 2560  # задает высоту окна браузера
    browser.config.window_width = 1664  # задает ширину окна браузера
    yield
    browser.quit()