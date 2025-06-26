import allure
import pytest
from api.cart_model import CartModel, VoucherProperties
from api.api_action import (add_products, edit_products, remove_products, show_products, set_currency,
                            get_products_currency, add_voucher, get_voucher_info)


@allure.feature('Add product in cart.')
@allure.title('Add product in cart with Product ID and Quantity.')
def test_add_product_in_cart():
    user_data = {'product_id': 31, 'quantity': 4}
    response = add_products(user_data)
    assert response.status_code == 200
    assert response.json().get('success') == 'Success: You have modified your shopping cart!'


@allure.feature('Change product parameters in cart.')
@allure.title('Change product quantity based on "key".')
def test_change_qty_added_product():
    user_data = {'key': 24, 'quantity': 10}
    response = edit_products(user_data)
    assert response.status_code == 200
    assert response.json().get('success') == 'Success: You have modified your shopping cart!'


@allure.feature('Remove product from cart.')
@allure.title('Remove product from cart based on "key".')
def test_remove_added_product():
    user_data = {'key': 4}
    response = remove_products(user_data)
    assert response.status_code == 200
    assert response.json().get('success') == 'Success: You have modified your shopping cart!'


@allure.feature('Show product cart.')
@allure.title('Show product cart.')
def test_get_cart_info():
    response = show_products()
    assert response.status_code == 200
    CartModel.model_validate(response.json())


@allure.feature('Set product currency.')
@allure.title('Set "GBR" as current product currency.')
def test_change_currency():
    user_data = {'currency': 'GBP'}
    response = set_currency(user_data)
    assert response.status_code == 200
    assert response.json().get('success') == 'Success: Your currency has been changed!'


@allure.feature('Check products currency.')
@allure.title('Check current products currency in "totals".')
@pytest.mark.parametrize("index", range(4))
def test_check_change_currency(index):
    response2 = get_products_currency()
    assert response2.status_code == 200
    assert response2.json()['totals'][index]['text'][0] == '£'


@allure.feature('Add product voucher.')
@allure.title('Add product voucher data.')
def test_add_voucher():
    user_data = {
        "from_name": "John",
        "from_email": "John@mail.com",
        "to_name": "Timofei",
        "to_email": "Timofei@mail.com",
        "amount": "144.00",
        "code": "1001",
        "message": "This is voucher."
    }
    response = add_voucher(user_data)
    assert response.status_code == 200
    assert response.json().get('success') == 'Success: You have modified your shopping cart!'


@allure.feature('Check product voucher.')
@allure.title('Check product voucher info.')
def test_check_voucher():
    response = get_voucher_info()
    data = response.json().get("vouchers")[0]
    assert response.status_code == 200
    assert data and VoucherProperties.model_validate(data)
