from selenium.webdriver.common.by import By


class LocOrderFromCompare:
    MY_ACCOUNT_TOP_NAVBAR = (By.XPATH, '//a[@title="My Account"]')
    LOGIN_FROM_DROPDOWN = (By.XPATH, '//nav[@id="top"]//a[contains(text(), "Login")]')

    EMAIL_RETURNING_CUSTOMER_FIELD = (By.XPATH, '//input[@id="input-email"]')
    EMAIL_VALUE = 'test@test.ru'
    PASSWORD_RETURNING_CUSTOMER_FIELD = (By.XPATH, '//input[@id="input-password"]')
    PASSWORD_VALUE = 'QWEr'
    LOGIN_RETURNING_CUSTOMER_BUTTON = (By.XPATH, '//input[@type="submit"]')

    PHONES_PDA_NAVBAR_BUTTON = (By.XPATH, '//ul[@class="nav navbar-nav"]/li/a[contains(text(), "Phones & PDA")]')
    COMPARE_HTC_BUTTON = (By.XPATH, '//button[@onclick="compare.add(\'28\');"]')
    COMPARE_IPHONE_BUTTON = (By.XPATH, '//button[@onclick="compare.add(\'40\');"]')
    COMPARE_PALM_TREO_PRO_BUTTON = (By.XPATH, '//button[@onclick="compare.add(\'29\');"]')

    SEARCH_FIELD = (By.XPATH, '//div[@id="search"]/input')
    SEARCH_VALUE = 'Samsung'
    SEARCH_BUTTON = (By.XPATH, '//span[@class="input-group-btn"]/button')

    COMPARE_SAMSUNG_GALAXY_TAB_10_1_BUTTON = (By.XPATH, '//button[@onclick="compare.add(\'49\');"]')
    PRODUCT_COMPARE_BUTTON = (By.XPATH, '//a[@id="compare-total"]')

    REMOVE_HTC_FROM_COMPARE_BUTTON = (By.XPATH, '//input[@onclick="cart.add(\'28\', \'1\');"]/../a')
    ADD_IPHONE_FROM_COMPARE_BUTTON = (By.XPATH, '//input[@onclick="cart.add(\'40\', \'1\');"]')
    ADD_PALM_TREO_PRO_FROM_COMPARE_BUTTON = (By.XPATH, '//input[@onclick="cart.add(\'29\', \'1\');"]')

    SHOPPING_CART_TOP_NAVBAR = (By.XPATH, '//span[contains(text(), "Cart")]')

    REMOVE_PALM_TREO_PRO_FROM_CART_BUTTON = (
        By.XPATH, '//td[contains(text(), "Product 2")]/..//../td//button[@data-original-title="Remove"]')
    QUANTITY_IPHONE_CART_FIELD = (
        By.XPATH, '//td[contains(text(), "product 11")]/..//../td//input[@type="text"]')
    QUANTITY_IPHONE_CART_VALUE = '2'
    UPDATE_QTY_IPHONE_FROM_CART_BUTTON = (
        By.XPATH, '//td[contains(text(), "product 11")]/..//../td//button[@data-original-title="Update"]')

    SHIPPING_TAXES_CART_DROPDOWN = (By.XPATH, '//a[contains(text(), "Estimate Shipping & Taxes")]')
    SHIPPING_COUNTRY_FIELD = (By.XPATH, '//select[@id="input-country"]')
    SHIPPING_COUNTRY_VALUE = (By.XPATH, '//option[contains(text(), "Antigua")]')
    SHIPPING_REGION_STATE_FIELD = (By.XPATH, '//select[@id="input-zone"]')
    SHIPPING_REGION_STATE_VALUE = (By.XPATH, '//select[@id="input-zone"]/option[contains(text(), "Barbuda")]')
    SHIPPING_POST_CODE_FIELD = (By.XPATH, '//input[@id="input-postcode"]')
    SHIPPING_POST_CODE_VALUE = '123456'
    SHIPPING_GET_QUOTES_BUTTON = (By.XPATH, '//button[@id="button-quote"]')
    SHIPPING_METHOD_OPTIONS_CANCEL_BUTTON = (By.XPATH, '//button[contains(text(), "Cancel")]')
    SHIPPING_CHECKOUT_BUTTON = (By.XPATH, '//a[contains(text(), "Checkout")]')

    SHIPPING_EXISTING_ADDRESS_CHECKBOX_STEP_2 = (
    By.XPATH, '//a[contains(text(), "Step 2")]/../../../div//input[@value="existing"]')
    CHECKOUT_ADDRESS_VALUE_STEP_2 = (By.XPATH, '//option[contains(text(), "Testname Testlastname")]')
    CHECKOUT_CONTINUE_BUTTON_STEP_2 = (By.XPATH, '//input[@value="Continue"]')

    SHIPPING_EXISTING_ADDRESS_CHECKBOX_STEP_3 = (
    By.XPATH, '//a[contains(text(), "Step 3")]/../../../div//input[@value="existing"]')
    CHECKOUT_ADDRESS_VALUE_STEP_3 = (By.XPATH, '//div[@id="shipping-existing"]/select')
    CHECKOUT_CONTINUE_BUTTON_STEP_3 = (By.XPATH, '//input[@id="button-shipping-address"]')

    CHECKOUT_COMMENTS_AREA = (By.XPATH, '//textarea[@name="comment"]')
    CHECKOUT_COMMENTS_VALUE = 'Thank you!'
    CHECKOUT_CONTINUE_BUTTON_STEP_4 = (By.XPATH, '//input[@id="button-shipping-method"]')

    TERMS_CONDITIONS_CHECKBOX = (By.XPATH, '//input[@type="checkbox" and @value="1"]')
    CHECKOUT_CONTINUE_BUTTON_STEP_5 = (By.XPATH, '// input[ @ id = "button-payment-method"]')

    CONFIRM_ORDER_BUTTON = (By.XPATH, '//input[@value="Confirm Order"]')

    CHECKOUT_SUCCESS_HEADER = (By.XPATH, '//div[@id="content"]/h1')
    CHECKOUT_SUCCESS_CONTINUE_BUTTON = (By.XPATH, '//div[@class="pull-right"]/a')

    ORDER_HISTORY_TOP_NAVBAR = (By.XPATH, '//nav[@id="top"]//a[contains(text(), "Order History")]')
    ORDERS_CUSTOMER_DATA = (By.XPATH, '//td[contains(text(), "Testname Testlastname")]')
