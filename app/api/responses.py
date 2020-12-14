from flask import jsonify


def response(status_code, message=None):
    payload = {'status': status_code}
    if message:
        payload['message'] = message
    response = jsonify(payload)
    response.status_code = status_code
    return response


def malformed_request(message):
    return response(400, message)


def invalid_plate(message):
    return response(422, message)


def valid_plate(message):
    return response(200, message)