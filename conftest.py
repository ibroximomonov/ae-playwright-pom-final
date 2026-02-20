import os
import allure
import pytest
from dotenv import load_dotenv

load_dotenv()

@pytest.fixture(scope="session")
def base_url() -> str:
    return os.getenv("BASE_URL", "https://automationexercise.com")

@pytest.fixture(scope="session")
def user_password() -> str:
    return os.getenv("USER_PASSWORD", "Test@12345")

@pytest.fixture(scope="session")
def payment_data() -> dict:
    return {
        "name_on_card": os.getenv("CARD_NAME", "Test User"),
        "card_number": os.getenv("CARD_NUMBER", "4111111111111111"),
        "cvc": os.getenv("CARD_CVC", "123"),
        "exp_month": os.getenv("CARD_EXP_MONTH", "12"),
        "exp_year": os.getenv("CARD_EXP_YEAR", "2030"),
    }

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        page = item.funcargs.get("page", None)
        if page is not None:
            try:
                png = page.screenshot(full_page=True)
                allure.attach(png, name="failure_screenshot", attachment_type=allure.attachment_type.PNG)
            except Exception:
                pass

@pytest.fixture(autouse=True)
def slowmo_if_needed(page):
    slowmo = os.getenv("PW_SLOWMO")
    if slowmo:
        page.wait_for_timeout(int(slowmo))
    yield
