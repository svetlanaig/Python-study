import pytest
from playwright.sync_api import sync_playwright

def test_form_data():
    # Start a Playwright session
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto('https://demoqa.com/text-box')

        input_data = {
            '#userName': 'Donald Duck',
            '#userEmail': 'donald.duck@example.com',
            '#currentAddress.form-control': '56 Main St',
            '#permanentAddress.form-control': '379 Apple Rd'
        }

        for selector, value in input_data.items():
            page.fill(selector, value)

        # Submit the form
        page.click('#submit')

        # Wait for the output data to be displayed after submission
        page.wait_for_selector("#output")

        # Retrieve data from the output section
        output = {
            'name': page.text_content('#name'),
            'email': page.text_content('#email'),
            'current_address': page.text_content('#currentAddress.mb-1'),
            'permanent_address': page.text_content('#permanentAddress.mb-1')
        }
        # Printing actual values for debugging
        print(f"Name: {output['name']}")
        print(f"Email: {output['email']}")
        print(f"Current Address: {output['current_address']}")
        print(f"Permanent Address: {output['permanent_address']}")

        # Validate the output data
        assert output['name'] == "Name:Donald Duck", "Name mismatch"
        assert output['email'] == "Email:donald.duck@example.com", "Email mismatch"
        assert output['current_address'] == "Current Address :56 Main St ", "Current address mismatch"
        assert output['permanent_address'] == "Permananet Address :379 Apple Rd", "Permanent address mismatch"

        # Close the browser
        browser.close()

# Execute the test function
test_form_data()
