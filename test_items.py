from selenium import webdriver
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_running_autotest_for_different_interface_languages(browser):
    browser.get(link)
    time.sleep(30)

    button = browser.find_element_by_css_selector("button.btn.btn-lg")
    button.click()
    assert button, "Should be a button"


    time.sleep(8)
    browser.quit()