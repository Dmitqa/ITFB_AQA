import allure


@allure.epic('Place an order by registered user.')
@allure.feature('Place an order by registered user from compare.')
@allure.title('Check "My Account Information" order customer.')
def test_order_from_compare(compare):
    compare.login_account()
    compare.add_product_to_compare()
    compare.add_searched_product_to_compare()
    compare.compare_product()
    compare.customize_product_in_cart()
    compare.estimate_shipping_and_taxes_in_cart()
    compare.filling_checkout_order()
    values = compare.check_order_history()
    assert values == 'Testname Testlastname'
