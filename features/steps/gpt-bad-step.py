# from behave import given, when, then, use_step_matcher
# from src.coffee_machine import CoffeeMachine  # Assuming this is the Python module handling the coffee machine operations
# use_step_matcher('re')
#
# @given('the coffee machine is started')
# def step_given_coffee_machine_is_started(context):
#     context.machine = CoffeeMachine()
#     context.machine.start()
#
# @given('I handle everything except the grounds')
# def step_given_handle_all_except_grounds(context):
#     context.actionwords.i_handle_water_tank()
#     context.actionwords.i_handle_beans()
#
# @when(r'I take "(.*)" coffees')
# def impl(context, coffee_number = 50):
#     context.actionwords.i_take_coffee_number_coffees(coffee_number)
#
# @then('message "Empty grounds" should be displayed')
# def impl(context, message = ""):
#     context.actionwords.message_message_should_be_displayed(message)
#
# @then('coffee should be served')
# def step_then_coffee_served(context):
#     context.actionwords.coffee_should_be_served()
