import allure
from selenium.webdriver import ActionChains
from ui.pages.base_page import BasePage
from ui.locators.loc_register_account_from_shopping_cart import LocRegisterAccountFromShoppingCart as loc


class RegisterAccountFromShoppingCart(BasePage):

    @allure.title('Add product to cart.')
    def add_product_to_cart(self):
        action = ActionChains(self.driver)
        with allure.step('Choose category "Cameras".'):
            self.clicking(self.element(loc.CAMERAS_NAVBAR_BUTTON))
        with allure.step('Add to cart "Canon EOS 5D".'):
            action.move_to_element(self.element(loc.ADD_TO_CART_EOS_5D)).perform()
            self.clicking(self.element(loc.ADD_TO_CART_EOS_5D))
        with allure.step('Select product colour.'):
            action.move_to_element(self.element(loc.SELECT_AVAILABLE_OPTIONS)).perform()
            self.clicking(self.element(loc.SELECT_AVAILABLE_OPTIONS))
            self.clicking(self.element(loc.SELECT_RED_AVAILABLE_OPTIONS))
        with allure.step('Select product quantity.'):
            action.move_to_element(self.element(loc.QTY_AVAILABLE_OPTIONS)).perform()
            self.filling([self.element(loc.QTY_AVAILABLE_OPTIONS)], [loc.QTY_VALUE])
        with allure.step('Click "Add to Cart" button.'):
            action.move_to_element(self.element(loc.ADD_TO_CART_BUTTON)).perform()
            self.clicking(self.element(loc.ADD_TO_CART_BUTTON))
        with allure.step('Screenshot system message.'):
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name=f'screenshot',
                attachment_type=allure.attachment_type.PNG)
            self.driver.refresh()

    def go_to_shopping_cart(self):
        action = ActionChains(self.driver)
        with allure.step('Go to "Shopping Cart".'):
            action.move_to_element(self.element(loc.SHOPPING_CART_TOP_NAVBAR)).perform()
            self.clicking(self.element(loc.SHOPPING_CART_TOP_NAVBAR))
        with allure.step('Click "Checkout" button.'):
            action.move_to_element(self.element(loc.CHECKOUT_BUTTON)).perform()
            self.clicking(self.element(loc.CHECKOUT_BUTTON))

    @allure.title('Register account after add product in cart.')
    def register_account_from_checkout(self):
        with allure.step('Filling "Step 1: Checkout Options".'):
            self.clicking(self.element(loc.REGISTER_ACCOUNT_CHECKBOX))
            self.clicking(self.element(loc.REGISTER_ACCOUNT_CONTINUE_BUTTON))
            self.driver.execute_script("window.scrollBy(0, 450)")
        with allure.step('Filling "Step 2: Account & Billing Details" fields.'):
            fields = [self.element(loc.FIRST_NAME_FIELD),
                      self.element(loc.LAST_NAME_FIELD),
                      self.element(loc.EMAIL_FIELD),
                      self.element(loc.TELEPHONE_FIELD),
                      self.element(loc.ADDRESS_1_FIELD),
                      self.element(loc.CITY_FIELD),
                      self.element(loc.POST_CODE_FIELD),
                      self.element(loc.PASSWORD_FIELD),
                      self.element(loc.PASSWORD_CONFIRM_FIELD),
                      ]
            values = [loc.FIRST_NAME_VALUE,
                      loc.LAST_NAME_VALUE,
                      loc.EMAIL_VALUE,
                      loc.TELEPHONE_VALUE,
                      loc.ADDRESS_1_VALUE,
                      loc.CITY_VALUE,
                      loc.POST_CODE_VALUE,
                      loc.PASSWORD_VALUE,
                      loc.PASSWORD_CONFIRM_VALUE
                      ]
            self.filling(fields, values)
        with allure.step('Choose country and region.'):
            self.clicking(self.element(loc.COUNTRY_DROPDOWN))
            self.clicking(self.element(loc.COUNTRY_VALUE))
            self.clicking(self.element(loc.REGION_DROPDOWN))
            self.clicking(self.element(loc.REGION_VALUE))
        with allure.step('Enable "Privacy policy" checkbox.'):
            self.clicking(self.element(loc.PRIVACY_POLICY_CHECK_BOX))
        with allure.step('Click "Continue" button.'):
            self.clicking(self.element(loc.CONTINUE_BUTTON_STEP_2))

    @allure.title('Go to "My account".')
    def go_to_my_account(self):
        action = ActionChains(self.driver)
        with allure.step('Go to navbar "My Account/My account".'):
            action.move_to_element(self.element(loc.MY_ACCOUNT_TOP_NAVBAR)).perform()
            self.wait_visible(loc.MY_ACCOUNT_TOP_NAVBAR)
            self.driver.refresh()

    @allure.title('Edit account after registration.')
    def edit_account(self):
        with allure.step('Go to navbar "My Account/My account".'):
            self.clicking(self.element(loc.MY_ACCOUNT_TOP_NAVBAR))
            self.clicking(self.element(loc.MY_ACCOUNT_FROM_DROPDOWN))
            self.clicking(self.element(loc.EDIT_ACCOUNT_INFO_LINK))
        with allure.step('Screenshot page "My Account Information".'):
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name=f'screenshot',
                attachment_type=allure.attachment_type.PNG)
        with allure.step('Get account field values.'):
            first_name = self.element(loc.FIRST_NAME_FIELD_MY_ACCOUNT_INFO)
            last_name = self.element(loc.LAST_NAME_FIELD_MY_ACCOUNT_INFO)
            email = self.element(loc.EMAIL_FIELD_MY_ACCOUNT_INFO)
            telephone = self.element(loc.TELEPHONE_FIELD_MY_ACCOUNT_INFO)
            return (first_name.get_attribute('value'),
                    last_name.get_attribute('value'),
                    email.get_attribute('value'),
                    telephone.get_attribute('value'))
