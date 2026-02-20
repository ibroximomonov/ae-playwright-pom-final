# AE Playwright POM (Pytest + Playwright + Allure)

This project implements **POM** using **Python + Pytest + Playwright**, and includes an E2E scenario:

- Registration
- Add 2 products to Cart
- Check added products in Cart
- Buy all products in the Cart (Checkout + Payment)
- Allure report (steps + screenshot on failure)

Target: https://automationexercise.com

## Run locally

### 1) Install
```bash
python -m venv .venv
# Windows:
# .venv\Scripts\activate
# mac/linux:
# source .venv/bin/activate

pip install -r requirements.txt
playwright install
```

### 2) Run tests + generate Allure results
```bash
pytest --alluredir=allure-results
```

### 3) Open Allure report
Install Allure Commandline, then:
```bash
allure serve allure-results
```

## Optional: .env
Create `.env` (optional):
```env
BASE_URL=https://automationexercise.com
USER_PASSWORD=Test@12345
PW_SLOWMO=
CARD_NAME=Test User
CARD_NUMBER=4111111111111111
CARD_CVC=123
CARD_EXP_MONTH=12
CARD_EXP_YEAR=2030
```

## Push to GitHub (you do this part)
```bash
git init
git add .
git commit -m "POM: Playwright + Pytest + Allure E2E flow"
git branch -M main
git remote add origin https://github.com/<USERNAME>/<REPO>.git
git push -u origin main
```
