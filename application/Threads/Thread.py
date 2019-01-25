from application import db

class Thread(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(50), nullable=False)

    ##date_created = db.Column(db.DateTime, default=db.func.current.timestamp())


    def __init__(self, name):
        self.name = name
