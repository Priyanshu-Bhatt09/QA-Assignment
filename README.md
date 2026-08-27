# Swag Labs QA Assignment

This repository contains:

- A test plan
- A bug report
- Selenium automation tests for the main user flows

## Files

- `test-plan.md` - test scope, cases, risks, and environment
- `bug-report.md` - 5 documented bugs
- `tests/test_saucedemo.py` - automated Selenium tests
- `requirements.txt` - Python dependencies

## Setup

1. Install Python 3.13 or later
2. Install the dependencies:

```bash
python -m pip install -r requirements.txt
```

## Run tests

```bash
python -m pytest -q
```

If you are using Git Bash on Windows, this is the safest way to run the tests.

## How to confirm the tests are correct

Each test checks one required flow:

- `test_valid_login` checks that `standard_user` reaches the Products page
- `test_add_item_to_cart_and_checkout` checks add-to-cart and checkout success
- `test_locked_out_user_error_message` checks the locked-out login error

Run them with:

```bash
python -m pytest -vv
```

You should see 3 passing tests. If one fails, the browser flow or selector is not matching the site.

## What the automation covers

- Valid login with `standard_user`
- Add item to cart and complete checkout
- Locked out user login error

## Test data

- Username: `standard_user`
- Username: `locked_out_user`
- Password: `secret_sauce`
