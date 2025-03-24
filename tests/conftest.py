import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

@pytest.fixture
def driver():
    # Instancier le driver  pour le navigateur Chrome

    browser = webdriver.Chrome()
    
    # Aller sur la page 
    browser.get("https://demoqa.com/")

    # Maximiser la fenêtre
    browser.maximize_window()

    yield browser  

   
    browser.quit()  # Fermeture du navigateur


@pytest.fixture
def wait(driver):
    # Instancier le wait explicit pour le driver
    return WebDriverWait(driver, 10)


