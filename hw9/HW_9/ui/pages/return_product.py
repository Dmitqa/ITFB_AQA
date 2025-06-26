import allure
from selenium.webdriver import ActionChains
from ui.pages.base_page import BasePage
from ui.locators.loc_return_product import LocReturnProduct as loc


class ReturnProduct(BasePage):

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

    @allure.title('Choose and add product to wish list.')
    def add_product_to_wish_list(self):
        action = ActionChains(self.driver)
        with allure.step('Choose category "Cameras/Monitors".'):
            self.clicking(self.element(loc.COMPONENTS_NAVBAR_BUTTON))
            self.clicking(self.element(loc.MONITORS_COMPONENTS_DROPDOWN))
        with allure.step('Add product to wish list.'):
            self.clicking(self.element(loc.APPLE_CINEMA_30_ADD_TO_WISHLIST))
            self.clicking(self.element(loc.SAMSUNG_SYNCMASTER_941BW_ADD_TO_WISHLIST))
        with allure.step('Go to "My Wish List".'):
            action.move_to_element(self.element(loc.WISHLIST_TOP_NAVBAR)).perform()
            self.clicking(self.element(loc.WISHLIST_TOP_NAVBAR))
        with allure.step('Add product to cart from @My Wish List".'):
            action.move_to_element(self.element(loc.ADD_TO_CARD_APPLE_CINEMA_30_FROM_WISHLIST_BUTTON)).perform()
            self.clicking(self.element(loc.ADD_TO_CARD_APPLE_CINEMA_30_FROM_WISHLIST_BUTTON))

    @allure.title('Filling available options product in card.')
    def filling_product_card(self):
        action = ActionChains(self.driver)
        with allure.step('Filling available options.'):
            self.driver.execute_script("window.scrollBy(0, 650)")
        with allure.step('Choose radio.'):
            self.clicking(self.element(loc.MEDIUM_RADIO_OPTIONS_PRODUCT_CARD))
        with allure.step('Choose checkbox.'):
            self.clicking(self.element(loc.CHECKBOX_3_OPTIONS_PRODUCT_CARD))
            self.clicking(self.element(loc.CHECKBOX_4_OPTIONS_PRODUCT_CARD))
        with allure.step('Choose color.'):
            self.clicking(self.element(loc.SELECT_OPTIONS_PRODUCT_CARD))
            self.clicking(self.element(loc.YELLOW_SELECT_OPTIONS_PRODUCT_CARD))
        with allure.step('Filling "text" and "textarea" fields.'):
            self.element(loc.TEXT_FIELD_OPTIONS_PRODUCT_CARD).clear()
            fields = [self.element(loc.TEXT_FIELD_OPTIONS_PRODUCT_CARD),
                      self.element(loc.TEXTAREA_OPTIONS_PRODUCT_CARD),
                      ]
            values = [
                loc.TEXT_FIELD_VALUE_OPTIONS_PRODUCT_CARD,
                loc.TEXTAREA_VALUE_OPTIONS_PRODUCT_CARD,
            ]
            self.filling(fields, values)
        with allure.step('Upload file.'):
            self.driver.execute_script("window.scrollBy(0, 600)")
            self.uploading(self.element(loc.UPLOAD_BUTTON), loc.UPLOAD_VALUE)
            self.accept_alert()
        with allure.step('Filling "Date", "Time", "Date & Time", "Qty" fields.'):
            fields = [
                      self.element(loc.DATE_OPTIONS_PRODUCT_CARD),
                      self.element(loc.TIME_OPTIONS_PRODUCT_CARD),
                      self.element(loc.DATE_TIME_OPTIONS_PRODUCT_CARD),
                      self.element(loc.QTY_OPTIONS_PRODUCT_CARD),
                      ]
            values = [
                loc.DATE_VALUE_OPTIONS_PRODUCT_CARD,
                loc.TIME_VALUE_OPTIONS_PRODUCT_CARD,
                loc.DATE_TIME_VALUE_OPTIONS_PRODUCT_CARD,
                loc.QTY_VALUE_OPTIONS_PRODUCT_CARD,
            ]
            self.filling_datetime(fields, values)
        with allure.step('Click "Add to Cart" button.'):
            self.clicking(self.element(loc.ADD_TO_CARD_BUTTON_PRODUCT_CARD))
        with allure.step('View cart.'):
            action.move_to_element(self.element(loc.CART_BUTTON))
            self.wait_clickable(self.element(loc.CART_BUTTON))
            self.clicking(self.element(loc.CART_BUTTON))
        with allure.step('Go to checkout.'):
            action.move_to_element(self.element(loc.CHECKOUT_CART_BUTTON))
            self.clicking(self.element(loc.CHECKOUT_CART_BUTTON))

    @allure.title('Filling checkout order.')
    def filling_checkout_order(self):
        with allure.step('Go to "Estimate Shipping & Taxes".'):
            self.clicking(self.element(loc.SHIPPING_EXISTING_ADDRESS_CHECKBOX_STEP_2))
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

    @allure.title('Filling checkout order.')
    def return_ordered_product(self):
        action = ActionChains(self.driver)
        with allure.step('Go to "My Account" from top navbar.'):
            action.move_to_element(self.element(loc.MY_ACCOUNT_TOP_NAVBAR)).perform()
            self.clicking(self.element(loc.MY_ACCOUNT_TOP_NAVBAR))
        with allure.step('Go to "Order History".'):
            self.clicking(self.element(loc.ORDER_HISTORY_TOP_NAVBAR))
        with allure.step('View required order.'):
            self.clicking(self.element(loc.ORDERS_VIEW))
        with allure.step('Click "Return" button.'):
            self.clicking(self.element(loc.ORDER_RETURN))
        with allure.step('Filling "Telephone" field.'):
            self.filling([self.element(loc.TELEPHONE_RETURNS_FIELD)],
                         [loc.TELEPHONE_RETURNS_VALUE])
        with allure.step('Choose Reason for Return.'):
            self.clicking(self.element(loc.ORDER_ERROR_REASON_RETURNS_INFO))
        with allure.step('Click "Submit" button.'):
            self.clicking(self.element(loc.SUBMIT_RETURNS_INFO))
        with allure.step('Return result text about return request.'):
            return self.element(loc.PRODUCT_RETURN_MESSAGE).text
