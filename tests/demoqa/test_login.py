"""Test Demo Form"""
import os
import pytest
from common.webdriver_factory import create_driver_instance, ROOT_DIR
from pages.demoqa.login_form import LoginForm

USER_DATA = [
    ('Frank', '12345'),
    ('Didi', 'pet_1234'),
    ('Test', 'password')

]

@pytest.mark.parametrize("username, password", USER_DATA)


def test_login(username,password):
    driver = create_driver_instance('chrome')
    page = LoginForm(driver)
    page.open()
    page.wait_until_loaded()
    page.set_username(username)
    page.set_password(password)
    print(f'Username: {page.get_username()}')
    print(f'Password: {page.get_password()}')
    page.login()
    driver.close()