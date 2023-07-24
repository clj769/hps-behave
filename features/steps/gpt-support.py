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
# @when('I shutdown the coffee machine')
# def step_when_i_shutdown_the_coffee_machine(context):
#     actionwords.i_shutdown_the_coffee_machine()
#
# @then('message "{message}" should be displayed')
# def step_then_message_should_be_displayed(context, message):
#     actionwords.message_message_should_be_displayed(message)
#
#
# @when('I start the coffee machine using language "{language}"')
# def step_when_i_start_the_coffee_machine_using_language_lang(context, language):
#     actionwords.i_start_the_coffee_machine_using_language_lang(language)
#
#
