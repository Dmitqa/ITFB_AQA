logger_set = {
    'version': 1,
    'formatters': {
        'classic': {
            'format': '[%(asctime)s] - %(name)s - %(module)-22s : %(lineno)-3d - %(levelname)-8s - %(message)s'
        },
        'minimalism': {
            'format': '[%(asctime)s] - %(message)s'
        }
    },
    'handlers': {
        'file': {
            'class': 'logging.FileHandler',
            'level': 'INFO',
            'formatter': 'classic',
            'filename': 'D:/PycharmProjects/hw6/hw7/logexample.log'
        },
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'INFO',
            'formatter': 'classic',
        }
    },
    'loggers': {
        'my_logger': {
            'level': 'INFO',
            'handlers': ['file'],
            'propagate': False,
        },
        'console_logger': {
            'level': 'INFO',
            'handlers': ['console'],
            'propagate': False,
        },
    },
}

# results = 'pytest --alluredir=allure_results/ tests/test_main.py'
# report = 'allure generate allure_results'
