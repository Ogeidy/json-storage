from json_storage import db


class Jsons(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'(Jsons: {self.id})'
