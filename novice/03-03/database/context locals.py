from email.mime import application
from flask import request

with application.test_request_context('/hello', method='POST'):
    assert request.path == '/hello'
    assert request.method == 'POST'