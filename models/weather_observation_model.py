from datetime import datetime
from database.db import db


class WeatherObservation(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    city = db.Column(db.String, nullable=False)
    text = db.Column(db.String, nullable=False)
    datetime = db.Column(db.DateTime,
                         nullable=False, default=datetime.now)

    def __repr__(self):
        return f'<WeatherObservation {self.id} {self.city} {self.text}>'
