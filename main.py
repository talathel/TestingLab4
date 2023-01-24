import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
browser = webdriver.Firefox()
browser.execute_script("window.focus();")

def test_404_search():
    browser.implicitly_wait(10)
    browser.get("https://ya.ru/")
    assert "Яндекс" in browser.title

    elem = browser.find_element(By.ID, "text")  # Find the search box
    elem.send_keys("fgjdhsjghsjdfghld" + Keys.RETURN)
    try:
        browser.find_element(By.CLASS_NAME, "EmptySearchResults")
    except NoSuchElementException:
        assert False
    assert True


def test_search():
    browser.implicitly_wait(10)
    browser.get("https://ya.ru/")
    assert "Яндекс" in browser.title

    elem = browser.find_element(By.ID, "text")  # Find the search box
    elem.send_keys("Погода" + Keys.RETURN)
    try:
        browser.find_element(By.ID, "search-result")
    except NoSuchElementException:
        assert False
    assert True


def test_incorrect_login():
    browser.implicitly_wait(10)
    browser.find_element(By.TAG_NAME, "body").send_keys(Keys.CONTROL + "t")
    browser.get("https://orioks.miet.ru/user/login")
    browser.implicitly_wait(10)
    assert "Авторизация" in browser.title
    browser.find_element(By.ID, "loginform-login").send_keys("8200133")
    browser.find_element(By.ID, "loginform-password").send_keys(
        "123" + Keys.RETURN
    )
    try:
        alert = (
            browser.find_element(By.CLASS_NAME, "alert-danger")
            .find_element(By.TAG_NAME, "b")
            .text
        )
        assert alert == "Неверный логин или пароль"
    except NoSuchElementException:
        assert False


def test_poll():
    browser.get(
        "https://onlinetestpad.com/ru/survey/135761-opros-po-kachestvu-pitaniya-dlya-roditelej"
    )
    browser.find_element(By.ID, "btnNext").click()
    browser.implicitly_wait(5)
    browser.find_element(By.ID, "s_ans_2427420").find_element(By.XPATH,'..').find_element(By.TAG_NAME,'i').click()
    browser.find_element(By.ID, "s_ans_2427423").send_keys("пропустить")
    browser.find_element(By.ID, "s_ans_2427424").find_element(By.XPATH,'..').find_element(By.TAG_NAME,'i').click()
    browser.find_element(By.ID, "s_ans_2427427").find_element(By.XPATH,'..').find_element(By.TAG_NAME,'i').click()
    browser.find_element(By.ID, "s_ans_2427432").find_element(By.XPATH,'..').find_element(By.TAG_NAME,'i').click()
    browser.find_element(By.ID, "s_ans_2427439").find_element(By.XPATH,'..').find_element(By.TAG_NAME,'i').click()
    browser.find_element(By.ID, "s_ans_2427442").find_element(By.XPATH,'..').find_element(By.TAG_NAME,'i').click()
    browser.find_element(By.ID, "s_ans_2427445").send_keys("всё")
    browser.find_element(By.ID, "btnFinish").click()
    browser.implicitly_wait(10)
    try:
        browser.find_element(By.CLASS_NAME, "otp-item-view-stat-tbl")
        assert True
    except NoSuchElementException:
        assert False

def test_spravochnik():
    browser.get('https://telspravki.info/rossiya/moskovskaya-oblast/stolitsa-rossii/moskva')
    browser.find_element(By.ID,'phone').send_keys('6147748'+Keys.RETURN)
    try:
        assert browser.find_element(By.XPATH,'/html/body/div[1]/div/div[7]/div/div[3]/table/tbody/tr/td[2]').text=='Кисенко Ю.В.'
    except NoSuchElementException:
        assert False