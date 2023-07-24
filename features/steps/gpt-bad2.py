# # Add the following code to your step_definitions.py file:
#
# from behave import given, when, then
# from actionwords import Actionwords
#
# actionwords = Actionwords()
#
# @given('the coffee machine is started')
# def step_given_the_coffee_machine_is_started(context):
#     actionwords.the_coffee_machine_is_started()
#
# @given('I handle everything except the grounds')
# def step_given_i_handle_everything_except_the_grounds(context):
#     actionwords.i_handle_everything_except_the_grounds()
#
# @when('I take "{coffee_number}" coffees')
# def step_when_i_take_coffees(context, coffee_number):
#     actionwords.i_take_coffee_number_coffees(coffee_number)
#
# @then('message "{message}" should be displayed')
# def step_then_message_message_should_be_displayed(context, message):
#     actionwords.message_message_should_be_displayed(message)
#
# @then('coffee should be served')
# def step_then_coffee_should_be_served(context):
#     actionwords.coffee_should_be_served()
