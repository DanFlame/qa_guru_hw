from selene.support.shared import browser
from selene import be, have


def test_positive_search(open_browser):
    browser.element('[name="q"]').should(be.blank).type('selene').press_enter()
    return browser.element('[id="search"]').should(have.text('yashaka/selene: User-oriented Web UI browser tests')), "Поиск произведён успешно"

def test_negative_search(open_browser):
    browser.element('[name="q"]').clear()
    browser.element('[name="q"]').should(be.blank).type('kdjadasldjlakdjslkajdlsajdlkasjdlkjdk').press_enter()
    return browser.element('[id="result-stats"]').should(have.text('Результатов: примерно 0')), "Поиск не дал результатов"