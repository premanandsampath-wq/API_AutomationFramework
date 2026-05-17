from playwright.sync_api import Playwright, sync_playwright, expect

def test_playwright(page):
    page.goto("https://www.qaplayground.com/practice") 
    try:
     page.get_by_placeholder("Search practice elements...").fill("Input Fields") 
     page.wait_for_timeout(2000) 
     page.get_by_test_id("card-link-input-fields").click()
     page.wait_for_timeout(3000) 
     assert "input-fields" in page.url
     print("Element found and clicked successfully!")
    except:
        print("Assertion failed")
        raise AssertionError("Test failed due to assertion error")
    page.close()

