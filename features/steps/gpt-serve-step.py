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
# @when('I take a coffee')
# def step_when_i_take_a_coffee(context):
#     actionwords.i_take_a_coffee()
#
# @then('coffee should be served')
# def step_then_coffee_should_be_served(context):
#     actionwords.coffee_should_be_served()
