import allure
import requests
from loggers import logger_api as logger


@allure.title('Get user api-token based on "username", "key", "url".')
def get_api_token(username, key, url):
    logger.info(f"Get api-token value based on {username}, {key}, {url}.")
    user_data = {'username': username, 'key': key}
    response = requests.post(f'{url}login', data=user_data, verify=False)
    return response.json()['api_token']
