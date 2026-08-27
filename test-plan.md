# Swag Labs Test Plan

**Project:** SauceDemo / Unque Software Automation Assignment  
**Date:** August 26, 2026

## 1. Scope

I will test these main areas of the site:

- Login
- Product browsing
- Product sorting
- Product details
- Cart
- Checkout flow

Out of scope:

- Backend code
- Payment gateway
- Email delivery

## 2. Types of Testing

- Functional testing
- UI testing
- Negative testing
- Edge case testing
- Cross-browser testing

## 3. Test Environment

- Windows 11 desktop
- Google Chrome
- Mozilla Firefox
- Selenium WebDriver for automation

## 4. Test Data

Provided users:

- `standard_user`
- `locked_out_user`
- `problem_user`
- `performance_glitch_user`

Password for all users:

- `secret_sauce`

## 5. Test Cases

### TC01 - Valid login
- **Precondition:** User is on the login page
- **Steps:**
  1. Enter `standard_user`
  2. Enter `secret_sauce`
  3. Click `Login`
- **Expected result:** User should land on the product page

### TC02 - Locked out user login
- **Precondition:** User is on the login page
- **Steps:**
  1. Enter `locked_out_user`
  2. Enter `secret_sauce`
  3. Click `Login`
- **Expected result:** Error message should show that the user is locked out

### TC03 - Add product to cart
- **Precondition:** User is logged in
- **Steps:**
  1. Click `Add to cart` on one product
  2. Open cart
- **Expected result:** Selected product should appear in the cart

### TC04 - Complete checkout
- **Precondition:** User has one item in cart
- **Steps:**
  1. Open cart
  2. Click `Checkout`
  3. Enter first name, last name, and zip code
  4. Click `Continue`
  5. Click `Finish`
- **Expected result:** Order should complete successfully

### TC05 - Sort products
- **Precondition:** User is logged in
- **Steps:**
  1. Open sort dropdown
  2. Select `Name (A to Z)`
  3. Select `Price (low to high)`
- **Expected result:** Product list should reorder correctly each time

## 6. Risk Assessment

Most likely failure areas:

- Login for special users
- Checkout form fields
- Product sorting and item display
- Pages that load slowly
- UI behavior on `problem_user` and `visual_user`

## 7. Exit Criteria

Testing is complete when:

- Main flows are checked
- At least 5 bugs are documented
- Automation runs for the 3 required flows

