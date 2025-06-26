import allure


@allure.epic('Return product.')
@allure.feature('Return ordered product by registered user.')
@allure.title('Check "Product Returns" information.')
def test_return_product(return_order):
    return_order.login_account()
    return_order.add_product_to_wish_list()
    return_order.filling_product_card()
    return_order.filling_checkout_order()
    massage = return_order.return_ordered_product()
    assert massage == 'Thank you for submitting your return request. Your request has been sent to the relevant department for processing.'
