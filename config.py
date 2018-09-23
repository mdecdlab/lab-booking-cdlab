import authomatic
from authomatic.providers import oauth2

CONFIG = {
        'google': {
            'class_': oauth2.Google,
            'consumer_key': '864853543778-vfdhe8hvr6ltb1bjisvmjmfr9372arai.apps.googleusercontent.com',
            'consumer_secret': 'VSgv_v6kmtJHDPLUAJ5POhEi',
            'scope': oauth2.Google.user_info_scope
        }
    }
CALLBACK_URL = "https://localhost:8443"