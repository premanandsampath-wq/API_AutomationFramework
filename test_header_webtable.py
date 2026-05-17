from playwright.sync_api import Playwright, sync_playwright, expect
def test_headerwebtable(page): 
    page.goto("https://www.qaplayground.com/practice") 
    try:
        page.get_by_placeholder("Search practice elements...").fill("Data Table") 
        page.wait_for_timeout(2000) 
        page.get_by_test_id("card-link-data-table").click() 
        page.wait_for_timeout(3000) 
        page.queryselectorall("table tbody tr").length > 0
        page.locator("table tbody tr td").first.wait_for(state="visible")
        page.wait_for_timeout(12000)
           
        print("Element found and clicked successfully!")
    except:
         print("Failed to find or click the element.")

    table = page.wait_for_selector('//table[@id="books-table"]') 
    rows = table.query_selector_all("thead tr")
    th = table.query_selector_all("thead tr th")
    td = table.query_selector_all("tbody tr td") 
    print(len(rows))
    print(len(th))
    print(len(td))
    for i in range(len(rows)):
        print(rows[i].inner_text())

    