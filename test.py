from form_elements import *


def test_fill_form_fields():
    driver.get("https://practice-automation.com/form-fields/")
    form = Form()
    form.check_form_is_open()

    form.enter_name("Edward")
    form.enter_password("qwerty123")
    form.choose_drink("Milk")
    form.choose_drink("Coffee")
    form.choose_color("Yellow")
    form.select_love_automation("Yes")
    form.enter_email("name@example.com")
    message_count_tools = form.count_automation_tools()
    form.enter_message(message_count_tools)
    form.enter_message(" ")
    message_longest_tool = form.get_longest_tool()
    form.enter_message(message_longest_tool)

    form.submit()
    form.check_receive_message_alert()

    form.close_alert()
    driver.close()
