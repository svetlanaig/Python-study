import pytest
from playwright.sync_api import sync_playwright

"""Common settings set up"""
@pytest.fixture(scope="module")  # define base url
def base_url():
    return "https://demoqa.com"


""" 
Test1
This test case adding data into input form and output check after adding
"""

def test_form_data(base_url):
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(f"{base_url}/text-box")

        input_data = {
            '#userName': 'Donald Duck',
            '#userEmail': 'donald.duck@example.com',
            '#currentAddress.form-control': '56 Main St',
            '#permanentAddress.form-control': '379 Apple Rd'
        }
        #fill data in
        for selector, value in input_data.items():
            page.fill(selector, value)

        # Submit the form
        page.click('#submit')

        # Wait for the output data to be displayed after submission
        # page.wait_for_selector("#output")

        # Retrieve data from the output section
        output = {
            'name': page.text_content('#name'),
            'email': page.text_content('#email'),
            'current_address': page.text_content('#currentAddress.mb-1'),
            'permanent_address': page.text_content('#permanentAddress.mb-1')
        }

        # Validate the output data
        assert output['name'] == "Name:Donald Duck", "Name mismatch"
        assert output['email'] == "Email:donald.duck@example.com", "Email mismatch"
        assert output['current_address'] == "Current Address :56 Main St ", "Current address mismatch"
        assert output['permanent_address'] == "Permananet Address :379 Apple Rd", "Permanent address mismatch"

        # Close the browser
        browser.close()

""" 
Test2
This test case open another page and check on it if contains visible elements (radiobuttons)
"""
@pytest.mark.parametrize("radio_button_id",  #define locators
[
    "#impressiveRadio",
    "#yesRadio",
    "#noRadio"
])
def test_radio_button_visible(base_url, radio_button_id):
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(f"{base_url}/radio-button")
        radio_button_locator = page.locator(radio_button_id)

        assert radio_button_locator.is_visible(), f"Radio button {radio_button_id} is not visible"
        assert not radio_button_locator.is_checked(), f"Radio button {radio_button_id} is already checked"

""" 
Test3
This test case click radiobuttons and check it if checked after it. 
NOTE:
It is expected to last result to be failed!!!
"""

@pytest.mark.parametrize("radio_button_id",  #define locators
[
    "label.custom-control-label[for='impressiveRadio']",
    "label.custom-control-label[for='yesRadio']",
    "label.custom-control-label[for='noRadio']"
])

def test_radio_button_clicking (base_url, radio_button_id):
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(f"{base_url}/radio-button")

        radio_button_locator = page.locator(radio_button_id)
        radio_button_locator.click()
        assert radio_button_locator.is_checked(), f"Radio button {radio_button_id} is not checked after clicking"

""" 
Test4
This test case click link on the page using text as locator
"""

def test_link_click1 (base_url):
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(f"{base_url}/links")

        link_locator1 = page.locator("text='Home'")
        link_locator1.click()

        page.wait_for_timeout(1000)   #to see the case execution more obviosly
        element_find = page.locator('a[href="https://demoqa.com"] img')
        assert element_find.is_visible(), f"Header element is not visible"
        
""" 
Test5
This test case click links on the page using id as locator
"""

def test_link_click2 (base_url):
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(f"{base_url}/links")

        link_locator2 = page.locator("#dynamicLink")
        link_locator2.click()

        page.wait_for_timeout(1000) #to see the case execution more obviosly and wait the uploading of the page content
        element_find = page.locator('a[href="https://demoqa.com"] img')
        assert element_find.is_visible(), f"Header element is not visible"
