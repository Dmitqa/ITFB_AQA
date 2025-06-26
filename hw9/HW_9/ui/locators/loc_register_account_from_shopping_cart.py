from selenium.webdriver.common.by import By


class LocRegisterAccountFromShoppingCart:
    CAMERAS_NAVBAR_BUTTON = (By.XPATH, '//ul[@class="nav navbar-nav"]/li/a[contains(text(), "Cameras")]')
    ADD_TO_CART_EOS_5D = (By.XPATH, '//button[@onclick="cart.add(\'30\', \'1\');"]')
    SELECT_AVAILABLE_OPTIONS = (By.XPATH, '//select[@id="input-option226"]')
    SELECT_RED_AVAILABLE_OPTIONS = (By.XPATH, '//option[contains(text(), "Blue")]')
    QTY_AVAILABLE_OPTIONS = (By.XPATH, '//input[@id="input-quantity"]')
    QTY_VALUE = 2
    ADD_TO_CART_BUTTON = (By.XPATH, '//button[@id="button-cart"]')
    ADD_TO_CART_ALERT = (By.XPATH, '//div[@id="alert"]')
    SHOPPING_CART_TOP_NAVBAR = (By.XPATH, '//span[contains(text(), "Cart")]')

    CART_HEADER = (By.XPATH, '//div[@id="content"]/h1')
    CHECKOUT_BUTTON = (By.XPATH, '//a[contains(text(), "Checkout")]')

    CHECKOUT_HEADER = (By.XPATH, '//div[@id="content"]/h1')
    REGISTER_ACCOUNT_CHECKBOX = (By.XPATH, '//input[@value="register"]')
    REGISTER_ACCOUNT_CONTINUE_BUTTON = (By.XPATH, '//input[@id="button-account"]')

    FIRST_NAME_FIELD = (By.XPATH, '//input[@name="firstname"]')
    FIRST_NAME_VALUE = 'Testname'
    LAST_NAME_FIELD = (By.XPATH, '//input[@name="lastname"]')
    LAST_NAME_VALUE = 'Testlastname'
    EMAIL_FIELD = (By.XPATH, '//input[@id="input-payment-email"]')
    EMAIL_VALUE = 'test@test.ru'
    TELEPHONE_FIELD = (By.XPATH, '//input[@name="telephone"]')
    TELEPHONE_VALUE = '89990005511'
    ADDRESS_1_FIELD = (By.XPATH, '//input[@name="address_1"]')
    ADDRESS_1_VALUE = 'Pushkina - Kolotushkina 4'
    CITY_FIELD = (By.XPATH, '//input[@name="city"]')
    CITY_VALUE = 'Testcity'
    POST_CODE_FIELD = (By.XPATH, '//input[@name="postcode"]')
    POST_CODE_VALUE = '123456'
    COUNTRY_DROPDOWN = (By.XPATH, '//select[@name="country_id"]')
    COUNTRY_VALUE = (By.XPATH, '//option[contains(text(), "Antigua")]')
    REGION_DROPDOWN = (By.XPATH, '//select[@name="zone_id"]')
    REGION_VALUE = (By.XPATH, '//select[@name="zone_id"]/option[contains(text(), "Barbuda")]')
    PASSWORD_FIELD = (By.XPATH, '//input[@id="input-payment-password"]')
    PASSWORD_VALUE = 'QWEr'
    PASSWORD_CONFIRM_FIELD = (By.XPATH, '//input[@name="confirm"]')
    PASSWORD_CONFIRM_VALUE = 'QWEr'
    PRIVACY_POLICY_CHECK_BOX = (By.XPATH, '//input[@name="agree"]')
    CONTINUE_BUTTON_STEP_2 = (By.XPATH, '//input[@value="Continue" and @id="button-register"]')

    MY_ACCOUNT_TOP_NAVBAR = (By.XPATH, '//a[@title="My Account"]')
    MY_ACCOUNT_FROM_DROPDOWN = (
    By.XPATH, '//ul[@class="dropdown-menu dropdown-menu-right"]/li/a[contains(text(), "My Account")]')
    EDIT_ACCOUNT_INFO_LINK = (By.XPATH, '//ul[@class="list-unstyled"]/li/a[contains(text(), "Edit your account")]')

    FIRST_NAME_FIELD_MY_ACCOUNT_INFO = (By.XPATH, '//input[@name="firstname"]')
    LAST_NAME_FIELD_MY_ACCOUNT_INFO = (By.XPATH, '//input[@name="lastname"]')
    EMAIL_FIELD_MY_ACCOUNT_INFO = (By.XPATH, '//input[@name="email"]')
    TELEPHONE_FIELD_MY_ACCOUNT_INFO = (By.XPATH, '//input[@name="telephone"]')
