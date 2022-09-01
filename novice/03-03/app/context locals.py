from email.mine import application
from flask import request

with application.test_request_context('/hello', method='POST'):
    # now you can do something with the request untill the
    # end of the with block, such as basic assertions:
    assert request.path =='/hello'
    assert request.method == 'POST'