from application import db

##DATABASE TABLE thread
##comment is only the opening comment for each thread.
class thread(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    comment = db.Column(db.String(500), nullable=False)
    votes = db.Column(db.Integer, nullable=False)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)

    def __init__(self, name, comment):
        self.name = name
        self.comment = comment
        self.votes = 0
