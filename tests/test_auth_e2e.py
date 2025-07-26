import pytest
from playwright.sync_api import Page, expect

@pytest.mark.order(1)
def test_successful_registration(page: Page):
    page.goto("http://localhost:8000/register")

    page.fill("#email", "testuser@example.com")
    page.fill("#password", "securepass123")
    page.fill("#confirm", "securepass123")
    
    # Fill username field if present (depends on your HTML form)
    # But if it's auto-derived in JS from email, no need to do this here
    
    page.click("button")

    expect(page.locator("#message")).to_have_text("Registration successful!")

@pytest.mark.order(2)
def test_successful_login(page: Page):
    page.goto("http://localhost:8000/login")

    page.fill("#email", "testuser@example.com")
    page.fill("#password", "securepass123")
    page.click("button")

    expect(page.locator("#message")).to_have_text("Login successful!")

@pytest.mark.order(3)
def test_short_password_register(page: Page):
    page.goto("http://localhost:8000/register")

    page.fill("#email", "baduser@example.com")
    page.fill("#password", "123")
    page.fill("#confirm", "123")
    page.click("button")

    expect(page.locator("#message")).to_have_text("Password must be at least 8 characters.")

@pytest.mark.order(4)
def test_invalid_login(page: Page):
    page.goto("http://localhost:8000/login")

    page.fill("#email", "testuser@example.com")
    page.fill("#password", "wrongpassword")
    page.click("button")

    expect(page.locator("#message")).to_have_text("Invalid email or password")
