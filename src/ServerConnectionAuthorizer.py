"""Decorator implemented for Authorizing the Requests made to Server"""

AUTHORIZATION_TOKEN_EXPECTED = 'xy124zjw3'
def authorize(_function):
    """These will be used for making a simple form of authentication when requests are made to server"""
    def wrapper(*args, **kwargs):
        authentication_token = request.headers.get('AuthorizationToken')
        if authentication_token == AUTHORIZATION_TOKEN_EXPECTED:
            return _function(*args, **kwargs)
        else:
            return '', requests.status_codes.codes['unauthorized']
    return wrapper

"""this is where the authorization is made"""
@app.route('/check_statement', methods=['POST','GET'])
@authorize
def SendStatement():
    ...