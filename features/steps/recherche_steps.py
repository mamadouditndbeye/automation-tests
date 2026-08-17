from behave import given, when, then
from pages import PageAccueilDuckDuckGo
import time

@given('je suis sur la page d\'accueil de DuckDuckGo')
def step_ouvrir_page(context):
    context.page = PageAccueilDuckDuckGo(context.driver)
    time.sleep(2)

@when('je recherche "{texte}"')
def step_rechercher(context, texte):
    context.page.rechercher(texte)
    time.sleep(3)

@then('le titre de la page contient "{texte}"')
def step_verifier_titre(context, texte):
    assert texte in context.driver.title