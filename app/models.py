from app import db
from datetime import datetime
import re


class Plate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    plate = db.Column(db.String(64), index=True, unique=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __init__(self, plate):
        self.plate = plate

    def __repr__(self):
        return '<Plate {}>'.format(self.plate)

    def to_dict(self):
        data = {
            'id': self.id,
            'plate': self.plate,
            'timestamp': self.timestamp
        }

        return data

    def is_valid(self):
        if self.plate.strip():
           return True
        else:
            return False

    def check_chars(self, chars, max_length):
        if chars.isalpha() and len(chars) <= max_length:
            return True
        else:
            return False

    def check_digits(self, digits, max_length):
        if digits.isnumeric() and len(digits) <= max_length:
            return True
        else:
            return False


class GermanPlate(Plate, db.Model):

    def is_valid(self):

        splits = re.split('(\d+|-)', self.plate)

        if not splits and len(splits) > 4:
            return False

        else:
            valid = self.check_chars(splits[0], 3)
            valid = valid and splits[1] == "-"
            valid = valid and self.check_chars(splits[2], 2)
            valid = valid and self.check_digits(splits[3], 4)

            return valid