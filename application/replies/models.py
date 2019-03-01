from application import db

##DATABASE TABLE reply
class reply(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    reply = db.Column(db.String(500), nullable=False)
    votes = db.Column(db.Integer, nullable=False)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    thread_id = db.Column(db.Integer, db.ForeignKey('thread.id'), nullable=False)


    def __init__(self, reply):
        self.reply = reply
        self.votes = 0
