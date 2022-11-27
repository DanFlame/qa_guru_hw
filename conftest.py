import pytest
from selene.support.shared import browser

@pytest.fixture(scope="session")
def open_browser():
    browser.config.window_height = 1920
    browser.config.window_width = 1080
    browser.open('https://google.com')
    yield  "Браузер открыт"
    browser.close()
    print("\nBrowser is closed")

