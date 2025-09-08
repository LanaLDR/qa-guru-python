from selene import browser, be, have

def test_valid_search(setup_browser):
    browser.open('https://ya.ru')
    browser.element('[name="text"]').should(be.blank).type('qa.guru').press_enter()
    browser.element('[data-fast="1"]').should(have.text('Курсы тестировщиков — обучение'))

def test_empty_search_result(setup_browser):
    browser.open('https://ya.ru')
    browser.element('[name="text"]').should(be.blank).type('asdfinadfijnaiadjfnaf').press_enter()
    browser.element('.EmptySearchResults-Title').should(have.text("Ничего не нашли"))