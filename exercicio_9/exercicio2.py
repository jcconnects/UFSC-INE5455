# 2. Utilizando o Selenium Web Driver, faça os seguintes testes de uma calculadora do duckduckgo.com :
#     A - Somar dois números diferentes e verificar o resultado.
#     B - Multiplicar dois números diferentes e em seguida dividir o resultado por 10 e verificar o resultado.
#     C - Fazer duas operações diferentes (uma sendo subtração) e verificar o resultado da última operação.
#     D - Fazer três operações diferentes, verificar o resultado de cada uma delas, e verificar que as três operações aparecem no histórico.

import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

URL = "https://duckduckgo.com/?q=10+%2B+10&ia=calculator"


@pytest.fixture
def driver():
    drv = webdriver.Chrome()
    drv.get(URL)
    WebDriverWait(drv, 10).until(EC.presence_of_element_located((By.ID, "display")))
    drv.find_element(By.CSS_SELECTOR, 'button[id="clear_button"]').click()
    yield drv
    drv.quit()


def click(driver, value):
    driver.find_element(
        By.CSS_SELECTOR, f'button.tile__ctrl__btn[value="{value}"]'
    ).click()


def display(driver):
    return driver.find_element(By.ID, "display").text


def history(driver):
    return driver.find_elements(By.CSS_SELECTOR, ".tile__history .tile__past-calc")


def test_a_soma(driver):
    click(driver, "2")
    click(driver, "+")
    click(driver, "3")
    click(driver, "=")
    time.sleep(0.5)
    assert display(driver) == "5"


def test_b_multiplica_divide(driver):
    click(driver, "5")
    click(driver, "×")
    click(driver, "4")
    click(driver, "=")
    time.sleep(0.5)
    click(driver, "÷")
    click(driver, "1")
    click(driver, "0")
    click(driver, "=")
    time.sleep(0.5)
    assert display(driver) == "2"


def test_c_subtracao_e_adicao(driver):
    click(driver, "9")
    click(driver, "-")
    click(driver, "4")
    click(driver, "=")
    time.sleep(0.5)
    click(driver, "+")
    click(driver, "1")
    click(driver, "=")
    time.sleep(0.5)
    assert display(driver) == "6"


def test_d_tres_operacoes_historico(driver):
    click(driver, "1")
    click(driver, "+")
    click(driver, "1")
    click(driver, "=")
    time.sleep(0.5)
    click(driver, "C")
    click(driver, "3")
    click(driver, "×")
    click(driver, "2")
    click(driver, "=")
    time.sleep(0.5)
    click(driver, "C")
    click(driver, "8")
    click(driver, "-")
    click(driver, "5")
    click(driver, "=")
    time.sleep(0.5)
    # history(driver) -> [<WebElement li.tile__past-calc>, <WebElement li.tile__past-calc>, ...]
    formulas = [h.text for h in history(driver)]
    # formulas -> ["8 - 5\n3", "3 × 2\n6", "1 + 1\n2", "10 + 10\n20"]
    joined = " | ".join(formulas)
    assert "1 + 1" in joined
    assert "3 × 2" in joined
    assert "8 - 5" in joined
    assert display(driver) == "3"
