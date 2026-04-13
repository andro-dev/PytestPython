from playwright.sync_api import Page, expect
import time


# def test_playwright_basics(playwright):
#     browser = playwright.chromium.launch(headless=False)
#     context = browser.new_context()
#     page = context.new_page()
#     page.goto("https://tekforcellc.com")


# # chromium headless mode - 1 single context
# def test_playwright_shortcut(page: Page):
#     page.goto("https://tekforcellc.com")


def test_coreLocators(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("Learning@830$3mK2!")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role(
        "link",
        name="terms and\
											conditions"
        "",
    ).click()
    page.get_by_role("button", name="Sign In").click()
    expect(page.get_by_text("Incorrect username/password.")).to_be_visible()

    ##Incorrect username/password.

    # time.sleep(5)
