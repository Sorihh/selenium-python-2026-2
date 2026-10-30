from behave import given, when, then
from selenium import webdriver
from pages.lobby_login_page import LobbyLoginPage
from pages.lobby_dashboard_page import LobbyDashboardPage
from selenium.webdriver.common.by import By

@given('El usuario se encuentra en la pagina de login')
def step_given_user_on_login(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://lobby-global.vercel.app/")
    context.lobby_login_page = LobbyLoginPage(context.driver)
    

@when('El usuario ingresa con el nombre "{username}"')
def step_when_user_logs_in(context, username):
    context.lobby_login_page.login(username)
    context.lobby_dashboard_page = LobbyDashboardPage(context.driver)

@then('El nombre del usuario "{username}" aparece en el dashboard')
def step_then_user_login(context, username):
    assert context.lobby_dashboard_page.find_username(username) is True


@when('El usuario intenta ingresar con un nombre con espacios "{username}"')
def step_when_user_logs_in_with_spaces(context, username):
    context.lobby_login_page.login(username)

@then('Se muestra el mensaje de error "{message}"')
def step_then_error_message(context, message):
    error = context.lobby_login_page.get_error_message()
    assert message in error

@then('El usuario sigue en la pagina de login')
def step_then_still_on_login(context):
    assert context.lobby_login_page.is_login_form_displayed()