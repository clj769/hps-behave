from behave import given, when, then
from src.coffee_machine import CoffeeMachine  # Assuming this is the Python module handling the coffee machine operations

@given('the coffee machine is started')
def step_given_coffee_machine_is_started(context):
    context.machine = CoffeeMachine()
    context.machine.start()

@when('I take a coffee')
def step_when_take_coffee(context):
    # context.machine.take_coffee()
    context.actionwords.i_take_a_coffee()

@then('coffee should be served')
def step_then_coffee_served(context):
    context.actionwords.coffee_should_be_served()
    # assert context.machine.coffee_served() is True
