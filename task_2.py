from selene.support.shared import browser
from selene import be, have
import pytest


@pytest.fixture
def browser_configs():
    browser.config.window_width = 690
    browser.config.window_height = 1080

    yield browser
    browser.quit()


def test_search(browser_configs):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_google_search_not_found(browser_configs):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('poiuytrtyuiop[sfdsvmkkjkfdfsd').press_enter()
    browser.element('#appbar').should(have.text('Результатов: примерно 0'))
