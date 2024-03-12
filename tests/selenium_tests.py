from playwright.sync_api import sync_playwright

def test_example():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto('https://127.0.0.1:5000')
        assert page.title() == 'AFTER LIFE'
        browser.close()

if __name__ == "__main__":
    test_example()
