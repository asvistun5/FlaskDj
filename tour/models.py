from main.settings import db

class Article(db.Model):
    id = db.Column(db.Integer(), primary_key = True)
    title = db.Column(db.Text, nullable=False)
    date = db.Column(db.Text, nullable=False)
    country = db.Column(db.Text, nullable=False)
    price = db.Column(db.Integer(), nullable=False)
    description = db.Column(db.Text, nullable=False)

    def __repr__(self) -> str:
        return f"id: {self.id}"