import pytest
from common.webdriver_factory import create_driver_instance
from pages.demoqa.book_store import BookStore

BOOKS_DATA = ['GIT', 'learning', ' ', '', 'no registrado']


@pytest.mark.parametrize("books", BOOKS_DATA)
def test_books(books):
    driver = create_driver_instance('chrome')
    page = BookStore(driver, 5)
    page.open()
    page.wait_until_loaded()
    page.search(books)
    results = page.get_table_info()
    print(results)
    page.close()
