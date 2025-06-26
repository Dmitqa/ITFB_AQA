from selenium.webdriver.common.by import By


class LocReturnProduct:
    MY_ACCOUNT_TOP_NAVBAR = (By.XPATH, '//a[@title="My Account"]')
    LOGIN_FROM_DROPDOWN = (By.XPATH, '//nav[@id="top"]//a[contains(text(), "Login")]')

    EMAIL_RETURNING_CUSTOMER_FIELD = (By.XPATH, '//input[@id="input-email"]')
    EMAIL_VALUE = 'test@test.ru'
    PASSWORD_RETURNING_CUSTOMER_FIELD = (By.XPATH, '//input[@id="input-password"]')
    PASSWORD_VALUE = 'QWEr'
    LOGIN_RETURNING_CUSTOMER_BUTTON = (By.XPATH, '//input[@type="submit"]')

    COMPONENTS_NAVBAR_BUTTON = (By.XPATH, '//ul[@class="nav navbar-nav"]/li/a[contains(text(), "Components")]')
    MONITORS_COMPONENTS_DROPDOWN = (By.XPATH, '//a[contains(text(), "Monitors")]')
    APPLE_CINEMA_30_ADD_TO_WISHLIST = (By.XPATH, '//button[@onclick="wishlist.add(\'42\');"]')
    SAMSUNG_SYNCMASTER_941BW_ADD_TO_WISHLIST = (By.XPATH, '//button[@onclick="wishlist.add(\'33\');"]')

    WISHLIST_TOP_NAVBAR = (By.XPATH, '//a[@id="wishlist-total"]/span')

    ADD_TO_CARD_APPLE_CINEMA_30_FROM_WISHLIST_BUTTON = (
        By.XPATH, '//td[contains(text(), "Product 15")]/..//../td/button[@data-original-title="Add to Cart"]')
    MEDIUM_RADIO_OPTIONS_PRODUCT_CARD = (By.XPATH, '//input[@value="6"]')
    CHECKBOX_3_OPTIONS_PRODUCT_CARD = (By.XPATH, '//input[@value="10"]')
    CHECKBOX_4_OPTIONS_PRODUCT_CARD = (By.XPATH, '//input[@value="11"]')
    TEXT_FIELD_OPTIONS_PRODUCT_CARD = (By.XPATH, '//input[@value="test"]')
    TEXT_FIELD_VALUE_OPTIONS_PRODUCT_CARD = 'Текст'
    SELECT_OPTIONS_PRODUCT_CARD = (By.XPATH, '//select[@id="input-option217"]')
    YELLOW_SELECT_OPTIONS_PRODUCT_CARD = (By.XPATH, '//option[contains(text(), "Yellow")]')
    TEXTAREA_OPTIONS_PRODUCT_CARD = (By.XPATH, '//textarea[@id="input-option209"]')
    TEXTAREA_VALUE_OPTIONS_PRODUCT_CARD = 'Текст'
    UPLOAD_BUTTON = (By.XPATH, '//button[@id="button-upload222"]')
    UPLOAD_VALUE = 'new.txt'
    DATE_OPTIONS_PRODUCT_CARD = (By.XPATH, '//input[@id="input-option219"]')
    DATE_VALUE_OPTIONS_PRODUCT_CARD = '2024-04-16'
    TIME_OPTIONS_PRODUCT_CARD = (By.XPATH, '//input[@id="input-option221"]')
    TIME_VALUE_OPTIONS_PRODUCT_CARD = '11:33'
    DATE_TIME_OPTIONS_PRODUCT_CARD = (By.XPATH, '//input[@id="input-option220"]')
    DATE_TIME_VALUE_OPTIONS_PRODUCT_CARD = '2024-04-16 11:33'
    QTY_OPTIONS_PRODUCT_CARD = (By.XPATH, '//input[@id="input-quantity"]')
    QTY_VALUE_OPTIONS_PRODUCT_CARD = '2'
    ADD_TO_CARD_BUTTON_PRODUCT_CARD = (By.XPATH, '//button[@id="button-cart"]')

    CART_BUTTON = (By.XPATH, '//div[@id="cart"]/button')
    CHECKOUT_CART_BUTTON = (By.XPATH, '//strong[contains(text(), "Checkout")]')

    SHIPPING_EXISTING_ADDRESS_CHECKBOX_STEP_2 = (
        By.XPATH, '//a[contains(text(), "Step 2")]/../../../div//input[@value="existing"]')
    CHECKOUT_CONTINUE_BUTTON_STEP_2 = (By.XPATH, '//input[@value="Continue"]')
    SHIPPING_EXISTING_ADDRESS_CHECKBOX_STEP_3 = (
        By.XPATH, '//a[contains(text(), "Step 3")]/../../../div//input[@value="existing"]')
    CHECKOUT_CONTINUE_BUTTON_STEP_3 = (By.XPATH, '//input[@id="button-shipping-address"]')
    CHECKOUT_COMMENTS_AREA = (By.XPATH, '//textarea[@name="comment"]')
    CHECKOUT_COMMENTS_VALUE = 'Thank you!'
    CHECKOUT_CONTINUE_BUTTON_STEP_4 = (By.XPATH, '//input[@id="button-shipping-method"]')
    TERMS_CONDITIONS_CHECKBOX = (By.XPATH, '//input[@type="checkbox" and @value="1"]')
    CHECKOUT_CONTINUE_BUTTON_STEP_5 = (By.XPATH, '//input[@id="button-payment-method"]')
    CONFIRM_ORDER_BUTTON = (By.XPATH, '//input[@value="Confirm Order"]')

    ORDER_HISTORY_TOP_NAVBAR = (By.XPATH, '//nav[@id="top"]//a[contains(text(), "Order History")]')
    ORDERS_VIEW = (By.XPATH, '//div[@id="content"]//td/a[@data-original-title="View"]')
    ORDER_RETURN = (By.XPATH, '//div[@id="content"]//td/a[@data-original-title="Return"]')
    TELEPHONE_RETURNS_FIELD = (By.XPATH, '//input[@id="input-telephone"]')
    TELEPHONE_RETURNS_VALUE = '89991117744'
    ORDER_ERROR_REASON_RETURNS_INFO = (By.XPATH, '//input[@value="3"]')
    SUBMIT_RETURNS_INFO = (By.XPATH, '//input[@value="Submit"]')
    PRODUCT_RETURN_MESSAGE = (By.XPATH, '//div[@id="content"]/p[1]')
