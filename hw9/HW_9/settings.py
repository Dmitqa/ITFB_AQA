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
            'filename': 'D:/PycharmProjects/hw9/logfile_hw9.log'
        },
        'api': {
            'class': 'logging.FileHandler',
            'level': 'INFO',
            'formatter': 'classic',
            'filename': 'D:/PycharmProjects/hw9/logfile_api_hw9.log'
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
        'api_logger': {
            'level': 'INFO',
            'handlers': ['api'],
            'propagate': False,
        },
        'console_logger': {
            'level': 'INFO',
            'handlers': ['console'],
            'propagate': False,
        },
    },
}

# pytest --alluredir=results
# allure generate results
