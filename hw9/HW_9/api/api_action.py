import allure
import requests
from api.get_api_token import get_api_token
from loggers import logger_api as logger

username = 'Default'
key = 'RsFsq8LQwiqJbnafQxTsF6q8PRuiVmjGJw8FbVkocpNEeuIldjlIOPGXpyACDRJISC9YGcyaMDSIXmDvyjloE8neAYKgwzmR6fNuVv9vhyRzXReqjscwUXKVk9WGpvz0kxeu2Zj3dsDBYQgVtI3TcTv95GpCywSkvbYw3kfFTri3oEuunX5JhBGMtSa97CmlFgeOfnfhgTwpvY7pt8trxPpV5TlYTi7XvELtNRuKratyErt6HzUaMINBBcRZOgDg'
url = 'https://192.168.0.103/index.php?route=api/'
# api_token = 'd8ab10cdda13f3708e2ed694df'
api_token = f'&api_token={get_api_token(username, key, url)}'


@allure.title('Add product in cart.')
def add_products(user_data):
    logger.info(f"Add product {user_data} in cart.")
    with allure.step(f"Add product {user_data} in cart."):
        response = requests.post(f'{url}cart/add{api_token}', data=user_data, verify=False)
        return response


@allure.title('Edit product in cart.')
def edit_products(user_data):
    logger.info(f"Edit product {user_data} in cart.")
    with allure.step(f"Edit product {user_data} in cart."):
        response = requests.post(f'{url}cart/edit{api_token}', data=user_data, verify=False)
        return response


@allure.title('Remove product from cart.')
def remove_products(user_data):
    logger.info(f"Remove product {user_data} from cart.")
    with allure.step(f"Remove product {user_data} from cart."):
        response = requests.post(f'{url}cart/remove{api_token}', data=user_data, verify=False)
        return response


@allure.title('Show all products in cart.')
def show_products():
    logger.info(f"Show all products in cart.")
    with allure.step(f"Show all products in cart."):
        response = requests.post(f'{url}cart/products{api_token}', verify=False)
        return response


@allure.title('Set product currency.')
def set_currency(user_data):
    logger.info(f"Set product currency: {user_data}.")
    with allure.step(f"Set product currency: {user_data}."):
        response = requests.post(f'{url}currency{api_token}', data=user_data, verify=False)
        return response


@allure.title('Show product current currency.')
def get_products_currency():
    logger.info(f"Show product current currency.")
    with allure.step(f"Show product current currency."):
        response = requests.get(f'{url}cart/products{api_token}', verify=False)
        return response


@allure.title('Add voucher to product in cart.')
def add_voucher(user_data):
    logger.info(f"Add voucher {user_data} to product in cart.")
    with allure.step(f"Add voucher {user_data} to product in cart."):
        response = requests.post(f'{url}voucher/add{api_token}', data=user_data, verify=False, )
        return response


@allure.title('Get info about product voucher.')
def get_voucher_info():
    logger.info(f"Get info about product voucher.")
    with allure.step(f"Get info about product voucher."):
        response = requests.get(f'{url}cart/products{api_token}', verify=False)
        return response
