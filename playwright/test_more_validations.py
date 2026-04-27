from playwright.sync_api import Page, expect


def test_ui_checks(page: Page):

    # check the price of tomate is equal to 37
    # identify the price column
    # identify the tomato row
    # extract the price of the tomato

    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")
    column_count = page.locator("th").count()

    for indx in range(column_count):
        if page.locator("th").nth(indx).filter(has_text="Price").count() > 0:
            price_column_number = indx
            print(f"Price column index is {price_column_number}")
            break

    tomato_row_number = page.locator("tr").filter(has_text="Tomato")
    tomato_price_cell = tomato_row_number.locator("td").nth(price_column_number)
    print("Tomato price is", tomato_price_cell.inner_text())


def get_cell_value(
    page: Page, 
    table_selector: str, 
    target_row_text: str, 
    target_column_name: str
) -> str:
    """
    Finds a cell value based on a row identifier and a column header.
    """
    # 1. Locate the table
    table = page.locator(table_selector)
    
    # 2. Find the column index based on the header text
    # We look for the 'th' or 'td' in the header row
    headers = table.locator("thead th, tr:first-child th, tr:first-child td")
    column_count = headers.count()
    col_index = -1
    
    for i in range(column_count):
        if target_column_name in (headers.nth(i).inner_text()):
            col_index = i
            break
            
    if col_index == -1:
        raise ValueError(f"Column '{target_column_name}' not found.")

    # 3. Find the specific row that contains our unique parameter
    # We filter rows to find the one containing target_row_text
    target_row = table.locator("tbody tr, tr").filter(has_text=target_row_text)
    
    # 4. Extract the value from the cell at the identified column index
    # Note: nth() is 0-based
    target_cell = target_row.locator("td").nth(col_index)
    
    return target_cell.inner_text().strip()

def test_price_check(page: Page):
    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")
    tomato_price = get_cell_value(page, "table", "Tomato", "Price")
    assert(tomato_price) == '37'

