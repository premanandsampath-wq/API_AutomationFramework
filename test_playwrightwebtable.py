from playwright.sync_api import expect

def test_webtable(page):
    page.goto("https://www.qaplayground.com/practice/data-table")
    page.wait_for_selector("#books-table tbody tr", timeout=15000)

    rows = page.locator("#books-table tbody tr")
    row_count = rows.count()
    print(f"Number of rows: {row_count}")

    assert row_count > 0, "Expected at least one row in the dynamic table"

    for row_index in range(row_count):
        row = rows.nth(row_index)
        cells = row.locator("td")
        cell_count = cells.count()
        values = [cells.nth(cell_index).inner_text() for cell_index in range(cell_count)]
        print(f"Row {row_index + 1}: {values}")
