from playwright.sync_api import sync_playwright

def test_example():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto('http://127.0.0.1:5000')
        assert page.title() is 'AFTER LIFE', "title is diferent?"

        element = page.locator('#messageInput')
        assert element is not None, "Element with ID 'your_element_id' not found on the page."
        element.fill("Hello")

        browser.close()

if __name__ == "__main__":
    test_example()
