# Swag Labs Bug Report

**Project:** SauceDemo / Swag Labs QA Assignment  
**Date:** August 26, 2026

## Bug 1: Product sort/filter does not work

- **User:** `problem_user`
- **Severity:** High
- **Priority:** High
- **Steps to reproduce:**
  1. Log in as `problem_user`
  2. Open the sort dropdown
  3. Select `Name (A to Z)`, `Name (Z to A)`, `Price (low to high)`, and `Price (high to low)`
- **Expected result:** Products should sort correctly based on the selected option
- **Actual result:** Sorting does not work correctly
- **Notes:** This affects browsing and shopping flow

## Bug 2: Wrong product opens after clicking a product

- **User:** `problem_user`
- **Severity:** High
- **Priority:** High
- **Steps to reproduce:**
  1. Log in as `problem_user`
  2. Click on a product such as `Sauce Labs Backpack`
  3. Observe the product detail page
- **Expected result:** The selected product detail page should open
- **Actual result:** A different product appears, or the page shows incorrect item data
- **Notes:** Some items also appear unavailable after clicking

## Bug 3: First and last name fields are mixed up in checkout

- **User:** `problem_user`
- **Severity:** High
- **Priority:** High
- **Steps to reproduce:**
  1. Log in as `problem_user`
  2. Add an item to cart
  3. Go to checkout
  4. Type a character in the Last Name field
- **Expected result:** The typed character should appear in Last Name
- **Actual result:** The character appears in First Name instead, and Last Name does not fill correctly
- **Notes:** This blocks checkout form completion

## Bug 4: Performance is slow for `performance_glitch_user`

- **User:** `performance_glitch_user`
- **Severity:** Medium
- **Priority:** Medium
- **Steps to reproduce:**
  1. Log in as `performance_glitch_user`
  2. Open the product page
  3. Go back and reopen the page
- **Expected result:** Pages should load in normal time
- **Actual result:** Login and page navigation take much longer than usual
- **Notes:** This reduces usability and can affect test timing

## Bug 5: Checkout continue leads to blank page / error

- **User:** `error_user`
- **Severity:** Critical
- **Priority:** High
- **Steps to reproduce:**
  1. Log in as `error_user`
  2. Add an item to cart
  3. Go to checkout
  4. Fill the form
  5. Click `Continue`
  6. Click 'Finish'
- **Expected result:** Order should get completed
- **Actual result:** Nothing happens, shows timeout error on the console
- **Notes:** This blocks checkout completely

## Summary

The five main issues found are:

- Sorting failure
- Wrong product details
- Checkout name field mismatch
- Slow performance
- Checkout continue failure

