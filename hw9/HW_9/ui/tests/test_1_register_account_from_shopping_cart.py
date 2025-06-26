import allure

from ui.locators.loc_register_account_from_shopping_cart import LocRegisterAccountFromShoppingCart as loc


@allure.epic('Register.')
@allure.feature('Register after add product in cart.')
@allure.title('Check "My Account Information" after register.')
def test_register_account_from_shopping_cart(register):
    register.add_product_to_cart()
    register.go_to_shopping_cart()
    register.register_account_from_checkout()
    register.go_to_my_account()
    account_values = register.edit_account()
    test_values = (loc.FIRST_NAME_VALUE,
                   loc.LAST_NAME_VALUE,
                   loc.EMAIL_VALUE,
                   loc.TELEPHONE_VALUE)
    assert account_values == test_values
