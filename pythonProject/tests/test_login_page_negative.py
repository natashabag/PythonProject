import time
import pytest
from selenium.webdriver.common.by import By


class TestNegativeScenarios:
    @pytest.mark.login
    @pytest.mark.negative
    @pytest.mark.parametrize("username, password, expected_error_message",
                             [("Incorrect", "Password123", "Your username is invalid!"),
                              ("student", "Wrong1", "Your password is invalid!")])
    def test_negative_login(self, driver, username, password, expected_error_message):
        # Open page
        driver.get("https://practicetestautomation.com/practice-test-login/")
        # Type username incorrectUser into Username field
        username_locator = driver.find_element(By.ID, "username")
        username_locator.send_keys(username)
        # Type password Password123 into Password field
        password_locator = driver.find_element(By.NAME, "password")
        password_locator.send_keys(password)
        # Push Submit button
        submit_locator = driver.find_element(By.XPATH, "//button[@class='btn']")
        submit_locator.click()
        time.sleep(5)
        # Verify error message is displayed
        error_locator = driver.find_element(By.ID, "error")
        assert error_locator.is_displayed(), "Error message is not displayed, but it should"
        # Verify error message text is Your username is invalid!
        error_message = error_locator.text
        assert error_message == expected_error_message, "Error message is unexpected"

    def test_negative_username(self, driver):
        # Open page
        driver.get("https://practicetestautomation.com/practice-test-login/")
        # Type username incorrectUser into Username field
        username_locator = driver.find_element(By.ID, "username")
        username_locator.send_keys("Incorrect")
        # Type password Password123 into Password field
        password_locator = driver.find_element(By.NAME, "password")
        password_locator.send_keys("Password123")
        # Push Submit button
        submit_locator = driver.find_element(By.XPATH, "//button[@class='btn']")
        submit_locator.click()
        time.sleep(5)
        # Verify error message is displayed
        error_locator = driver.find_element(By.ID, "error")
        assert error_locator.is_displayed(), "Error message is not displayed, but it should"
        # Verify error message text is Your username is invalid!
        error_message = error_locator.text
        assert error_message == "Your username is invalid!", "Error message is unexpected"

    def test_negative_password(self, driver):
        # Open page
        driver.get("https://practicetestautomation.com/practice-test-login/")
        # Type username incorrectUser into Username field
        username_locator = driver.find_element(By.ID, "username")
        username_locator.send_keys("student")
        # Type password Password123 into Password field
        password_locator = driver.find_element(By.NAME, "password")
        password_locator.send_keys("Wrong1")
        # Push Submit button
        submit_locator = driver.find_element(By.XPATH, "//button[@class='btn']")
        submit_locator.click()
        time.sleep(5)
        # Verify error message is displayed
        error_locator = driver.find_element(By.ID, "error")
        assert error_locator.is_displayed(), "Error message is not displayed, but it should"
        # Verify error message text is Your username is invalid!
        error_message = error_locator.text
        assert error_message == "Your password is invalid!", "Error message is unexpected"
