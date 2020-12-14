from app.api import bp
from app.models import Plate, GermanPlate
from flask import jsonify
from app import db
from app.api.responses import malformed_request, invalid_plate, valid_plate
from flask import request


@bp.route('/plate', methods=['GET'])
def get_plates():
    return jsonify("GET REQ")


@bp.route('/plate', methods=['POST'])
def create_plate():
    data = request.get_json() or {}
    if 'plate' not in data:
        return malformed_request('Request body must include plate field.')
    else:
        plate = GermanPlate(data['plate'])
        print(plate.plate)

        if plate.is_valid():
            if not Plate.query.filter_by(plate=plate.plate).first():
                db.session.add(plate)
                db.session.commit()

            return valid_plate("Plate is a valid German plate.")
        else:
            return invalid_plate("Plate is not a valid German plate.")