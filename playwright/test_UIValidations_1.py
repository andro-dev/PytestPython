from playwright.sync_api import Page, expect
import time

# def test_UIValidationDinamicScript(page:Page):
#     # select iphone X and Nokia Edge -> verify 2 items are showing in cart.
#     page.goto("https://rahulshettyacademy.com/loginpagePractise/")
#     page.get_by_label("Username:").fill("rahulshettyacademy")
#     page.get_by_label("Password:").fill(
#         "Learning@830$3mK2")  # @@@ remove "!" - last char in password to pass
#     page.get_by_role("combobox").select_option("teach")
#     page.locator("#terms").check()
#     page.get_by_role("button", name="Sign In").click()
#     page.locator("app-card").filter(has_text="iphone X")
#     iphoneProduct = page.locator("app-card").filter(has_text="iphone X")
#     iphoneProduct.get_by_role("button").click()
#     nokiaProduct = page.locator("app-card").filter(has_text="Nokia Edge")
#     nokiaProduct.get_by_role("button").click()
#     page.get_by_text("Checkout").click()
#     time.sleep(5)
#     expect(page.locator(".media-body")).to_have_count(2)

def test_childWindowHandle(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")

    with page.expect_popup() as page1_info:
        page.get_by_role("link", name="Free Access to InterviewQues/").click()
    page1 = page1_info.value
    text = page1.get_by_text("Please email us at mentor@").text_content()
    print(text)
    email = text.split("at ")[1].split(" with")[0]
    assert email == "mentor@rahulshettyacademy.com"

# zsh: uv run pytest test_UIValidations_1.py --headed
