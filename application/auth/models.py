from application import db

class User(db.Model):
    __tablename__ = "account"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)
    ADMIN = db.Column(db.Boolean, nullable=False)

    threads = db.relationship("thread", backref='account', lazy = True)
    replies = db.relationship("reply", backref='account', lazy = True)


    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
        self.ADMIN = False

    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    def roles(self):
        if self.ADMIN:
            return ["ADMIN"]
        else:
            return ["USER"]