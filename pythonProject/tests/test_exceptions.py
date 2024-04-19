import pytest
from page_objects.exceptions_page import Exceptions


class TestExceptions:
    @pytest.mark.exceptions
    def test_no_such_element_exception(self, driver):
        exceptions_page = Exceptions(driver)
        exceptions_page.open()
        exceptions_page.add_second_row()
        assert exceptions_page.is_row2_displayed(), "Row 2 input should be displayed, but it's not"

    @pytest.mark.exceptions
    def test_element_not_interactable_exception(self, driver):
        exceptions_page = Exceptions(driver)
        exceptions_page.open()
        exceptions_page.add_second_row()
        exceptions_page.row2_type_and_save("My text")
        assert exceptions_page.get_confirmation() == "Row 2 was saved", "Confirmation message is unexpected"

    @pytest.mark.exceptions
    def test_invalid_element_state_exception(self, driver):
        exceptions_page = Exceptions(driver)
        exceptions_page.open()
        exceptions_page.modify_row1_input("sushi")
        assert exceptions_page.get_confirmation() == "Row 1 was saved", "Confirmation message is unexpected"

    @pytest.mark.exceptions
    def test_stale_element_reference_exception(self, driver):
        exceptions_page = Exceptions(driver)
        exceptions_page.open()
        exceptions_page.add_second_row()
        assert not exceptions_page.are_instructions_displayed(), "Instructions are displayed"