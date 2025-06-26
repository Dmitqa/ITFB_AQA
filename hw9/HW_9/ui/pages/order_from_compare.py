import allure
from selenium.webdriver import ActionChains
from ui.pages.base_page import BasePage
from ui.locators.loc_order_from_compare import LocOrderFromCompare as loc


class OrderFromCompare(BasePage):

    @allure.title('Login account.')
    def login_account(self):
        with allure.step('Go to "My Account/Login" from top navbar.'):
            self.clicking(self.element(loc.MY_ACCOUNT_TOP_NAVBAR))
            self.clicking(self.element(loc.LOGIN_FROM_DROPDOWN))
        with allure.step('Filling email and password fields.'):
            fields = [self.element(loc.EMAIL_RETURNING_CUSTOMER_FIELD),
                      self.element(loc.PASSWORD_RETURNING_CUSTOMER_FIELD)]
            values = [loc.EMAIL_VALUE,
                      loc.PASSWORD_VALUE]
            self.filling(fields, values)
        with allure.step('Click "Login" button.'):
            self.clicking(self.element(loc.LOGIN_RETURNING_CUSTOMER_BUTTON))

    @allure.title('Choose and add product to compare.')
    def add_product_to_compare(self):
        with allure.step('Choose category "Phones & PDAs".'):
            self.clicking(self.element(loc.PHONES_PDA_NAVBAR_BUTTON))
        with allure.step('Add product to compare.'):
            self.driver.execute_script("window.scrollBy(0, 400)")
            self.clicking(self.element(loc.COMPARE_HTC_BUTTON))
            self.clicking(self.element(loc.COMPARE_IPHONE_BUTTON))
            self.clicking(self.element(loc.COMPARE_PALM_TREO_PRO_BUTTON))

    @allure.title('Search and add product to compare.')
    def add_searched_product_to_compare(self):
        action = ActionChains(self.driver)
        with allure.step('Filling product name in search field.'):
            self.filling([self.element(loc.SEARCH_FIELD)],
                         [loc.SEARCH_VALUE])
            self.clicking(self.element(loc.SEARCH_BUTTON))
        with allure.step('Click "Search" button.'):
            action.move_to_element(self.element(loc.COMPARE_SAMSUNG_GALAXY_TAB_10_1_BUTTON)).perform()
            self.clicking(self.element(loc.COMPARE_SAMSUNG_GALAXY_TAB_10_1_BUTTON))

    @allure.title('Comparison product.')
    def compare_product(self):
        action = ActionChains(self.driver)
        with allure.step('Go to "Comparison".'):
            self.clicking(self.element(loc.PRODUCT_COMPARE_BUTTON))
        with allure.step('Remove product from comparison.'):
            action.move_to_element(self.element(loc.REMOVE_HTC_FROM_COMPARE_BUTTON)).perform()
            self.clicking(self.element(loc.REMOVE_HTC_FROM_COMPARE_BUTTON))
        with allure.step('Add product from comparison to cart.'):
            action.move_to_element(self.element(loc.ADD_IPHONE_FROM_COMPARE_BUTTON)).perform()
            self.clicking(self.element(loc.ADD_IPHONE_FROM_COMPARE_BUTTON))
            self.clicking(self.element(loc.ADD_PALM_TREO_PRO_FROM_COMPARE_BUTTON))

    @allure.title('Custom product in cart.')
    def customize_product_in_cart(self):
        action = ActionChains(self.driver)
        with allure.step('Go to "Shopping cart".'):
            action.move_to_element(self.element(loc.SHOPPING_CART_TOP_NAVBAR)).perform()
            self.clicking(self.element(loc.SHOPPING_CART_TOP_NAVBAR))
        with allure.step('Remove product from cart".'):
            self.clicking(self.element(loc.REMOVE_PALM_TREO_PRO_FROM_CART_BUTTON))
        with allure.step('Update product quantity in cart".'):
            action.move_to_element(self.element(loc.UPDATE_QTY_IPHONE_FROM_CART_BUTTON)).perform()
            self.filling([self.element(loc.QUANTITY_IPHONE_CART_FIELD)], [loc.QUANTITY_IPHONE_CART_VALUE])
            self.clicking(self.element(loc.UPDATE_QTY_IPHONE_FROM_CART_BUTTON))

    @allure.title('Estimate shipping and taxes in cart.')
    def estimate_shipping_and_taxes_in_cart(self):
        with allure.step('Go to "Estimate Shipping & Taxes".'):
            self.driver.execute_script("window.scrollBy(0, 500)")
            self.clicking(self.element(loc.SHIPPING_TAXES_CART_DROPDOWN))
        with allure.step('Filling "Country", "Region/State", "Post code" fields.'):
            self.clicking(self.element(loc.SHIPPING_COUNTRY_FIELD))
            self.clicking(self.element(loc.SHIPPING_COUNTRY_VALUE))
            self.clicking(self.element(loc.SHIPPING_REGION_STATE_VALUE))
            self.filling([self.element(loc.SHIPPING_POST_CODE_FIELD)],
                         [loc.SHIPPING_POST_CODE_VALUE])
        with allure.step('Go to "Get quotes" and cancel action.'):
            self.clicking(self.element(loc.SHIPPING_GET_QUOTES_BUTTON))
            self.clicking(self.element(loc.SHIPPING_METHOD_OPTIONS_CANCEL_BUTTON))
        with allure.step('Go to "Checkout".'):
            self.clicking(self.element(loc.SHIPPING_CHECKOUT_BUTTON))

    @allure.title('Filling checkout order.')
    def filling_checkout_order(self):
        with allure.step('Filling "Step 2: Billing Details".'):
            self.clicking(self.element(loc.SHIPPING_EXISTING_ADDRESS_CHECKBOX_STEP_2))
            self.clicking(self.element(loc.CHECKOUT_ADDRESS_VALUE_STEP_2))
            self.clicking(self.element(loc.CHECKOUT_CONTINUE_BUTTON_STEP_2))
        with allure.step('Filling "Step 3: Delivery Details".'):
            self.clicking(self.element(loc.SHIPPING_EXISTING_ADDRESS_CHECKBOX_STEP_3))
            self.clicking(self.element(loc.CHECKOUT_CONTINUE_BUTTON_STEP_3))
        with allure.step('Filling "Step 4: Delivery Method".'):
            self.driver.execute_script("window.scrollBy(0, 300)")
            self.filling([self.element(loc.CHECKOUT_COMMENTS_AREA)],
                         [loc.CHECKOUT_COMMENTS_VALUE])
            self.clicking(self.element(loc.CHECKOUT_CONTINUE_BUTTON_STEP_4))
        with allure.step('Filling "Step 5: Payment Method".'):
            self.clicking(self.element(loc.TERMS_CONDITIONS_CHECKBOX))
            self.clicking(self.element(loc.CHECKOUT_CONTINUE_BUTTON_STEP_5))
        with allure.step('Filling "Step 6: Confirm Order".'):
            self.clicking(self.element(loc.CONFIRM_ORDER_BUTTON))

    @allure.title('Check order history.')
    def check_order_history(self):
        action = ActionChains(self.driver)
        with allure.step('Go to "My Account" from top navbar.'):
            action.move_to_element(self.element(loc.MY_ACCOUNT_TOP_NAVBAR)).perform()
            self.clicking(self.element(loc.MY_ACCOUNT_TOP_NAVBAR))
        with allure.step('Go to "Order History".'):
            self.clicking(self.element(loc.ORDER_HISTORY_TOP_NAVBAR))
        with allure.step('Get customer Firstname and Lastname from order.'):
            customer_data = self.element(loc.ORDERS_CUSTOMER_DATA)
            return customer_data.text
