from behave import given, when, then
from selenium import webdriver
from pages.imdb_home_page import ImdbHomePage
from pages.imdb_results_page import ImdbResultsPage
from pages.imdb_movie_page import ImdbMoviePage
from selenium.webdriver.common.by import By

@given('El usuario se encuentra en la pagina principal de IMDb')
def step_given_user_on_imdb(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.imdb.com/")
    context.imdb_home_page = ImdbHomePage(context.driver)


@when('El usuario busca la pelicula "{movie}"')
def step_when_user_searches_movie(context, movie):
    context.imdb_home_page.search(movie)
    context.imdb_results_page = ImdbResultsPage(context.driver)

@when('El usuario abre el primer resultado')
def step_when_user_opens_first_result(context):
    context.imdb_results_page.open_first_result()
    context.imdb_movie_page = ImdbMoviePage(context.driver)


@then('Se muestra la pagina de la pelicula "{movie}"')
def step_then_movie_page(context, movie):
    assert context.imdb_movie_page.get_title() == movie

@then('Se muestra la calificacion de la pelicula')
def step_then_movie_rating(context):
    print("Calificacion:", context.imdb_movie_page.get_rating())
    assert context.imdb_movie_page.is_rating_valid() is True
