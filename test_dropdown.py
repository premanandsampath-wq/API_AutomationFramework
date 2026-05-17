from playwright.sync_api import Playwright, sync_playwright, expect 
def test_dropdown(page): 
    page.goto("https://www.qaplayground.com/practice") 
    try:
        page.get_by_placeholder("Search practice elements...").fill("Dropdowns") 
        page.wait_for_timeout(2000) 
        page.get_by_test_id("card-link-dropdowns").click() 
        page.wait_for_timeout(3000) 
        
        print("Element found and clicked successfully!")
    except:
        print("Assertion failed")
        raise AssertionError("Test failed due to assertion error")
    
    dropdown =  page.get_by_test_id("dropdown-fruit").click()
    page.get_by_role("option", name="Banana").click() 
    page.wait_for_timeout(2000)
  #  selected_option = page.locator('//Span[@class ="font-semibold capitalize"]')
    selected_option = page.get_by_test_id("result-fruit").locator("span") 
    
    text = selected_option.inner_text().strip()
    #page.get_by_role("option", name="Apple").click() 
    #dropdown.get_by_role("option", name="Apple").click()
#selected_option = dropdown.input_value() 
    print(f"Selected option: {text}") 
    #assert selected_option == "Apple", f"Expected 'option2', but got '{selected_option}'"
    page.get_by_test_id("dropdown-country").click()
    page.get_by_role("option", name="India").click() 
    selected_option = page.get_by_test_id("dropdown-country").locator("span") 
    text = selected_option.inner_text().strip()
    print(f"Selected option: {text}")