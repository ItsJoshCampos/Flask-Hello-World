import json
import os
from dotenv import dotenv_values
from flask import Flask
from flask_oidc import OpenIDConnect

app = Flask(__name__)

config_env = {
    **dotenv_values(".env"),  # load local development variables
    **os.environ,  # override loaded values with environment variables
}

app.config.update({
    'SECRET_KEY': config_env["SECRET_KEY"], # Flask Secret Key
    'TESTING': (config_env["TESTING"] == 'True'),
    'DEBUG': (config_env["DEBUG"] == 'True'),
    # OIDC Settings
    'OIDC_CLIENT_SECRETS': F'oidc_settings.{config_env["FLASK_ENV"]}.json',
    'OIDC_ID_TOKEN_COOKIE_SECURE': False,
    'OIDC_REQUIRE_VERIFIED_EMAIL': False,
    'OIDC_USER_INFO_ENABLED': True,
    'OIDC_SCOPES': ['openid', 'profile'],
    'OIDC_INTROSPECTION_AUTH_METHOD': 'client_secret_post'
})

oidc = OpenIDConnect(app)

print(app.config)

# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return "pong!"


@app.route('/')
def index():
    if oidc.user_loggedin:
        return 'Welcome %s' % oidc.user_getfield('sub')
    else: return 'Not logged in'

@app.route('/login')
@oidc.require_login
def login():
    info = oidc.user_getinfo(['emailAddress', 'displayName', 'sub'])
    return 'Welcome %s' % info


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, ssl_context='adhoc')