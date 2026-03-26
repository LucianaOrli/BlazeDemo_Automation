import pytest
from pytest_bdd import scenarios, given, when, then
from playwright.sync_api import Page, expect

scenarios('../features/compra_passagem.feature')

@given('que eu acesso o portal BlazeDemo')
def abrir_site(page: Page):
    page.goto("https://www.blazedemo.com/")

@when('eu seleciono a origem "Paris" e o destino "London"')
def selecionar_rota(page: Page):
    page.locator('select[name="fromPort"]').select_option("Paris")
    page.locator('select[name="toPort"]').select_option("London")

@when('clico no botão de procurar voos')
def procurar(page: Page):
    page.locator('input[type="submit"]').click()

@when('escolho o primeiro voo disponível')
def escolher_voo(page: Page):
    page.locator('input[type="submit"]').first.click()

@when('preencho os dados para "Luciana - Grupo 4 Israel"')
def preencher_dados(page: Page):
    # Obedecendo o site, mas personalizando o conteúdo
    page.fill("#inputName", "Luciana - Missao 4 Amigos Israel")
    page.fill("#address", "Jerusalem Street, 777")
    page.fill("#city", "Tel Aviv")
    page.fill("#zipCode", "12345")
    page.locator('input[type="submit"]').click()

@then('o sistema deve exibir "Thank you for your purchase today!"')
def validar(page: Page):
    expect(page.locator("h1")).to_have_text("Thank you for your purchase today!")
