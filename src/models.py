from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class grand_parents(db.Model):
    __tablename__ = 'grand_parents'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    last_name = db.Column(db.String(120), unique=True, nullable=False)
    age = db.Column(db.String(3), unique=False, nullable=False)
    children_id = db.Column(db.Integer, db.ForeignKey('parents.id'), nullable=False)
   

    def __repr__(self):
        return '<grand_parents %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "last_name": self.last_name,
            "age": self.age

        }

class parents(db.Model):
    __tablename__ = 'parents'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    last_name = db.Column(db.String(120), unique=True, nullable=False)
    age = db.Column(db.String(3), unique=False, nullable=False)
    children_id = db.Column(db.Integer, db.ForeignKey('children.id'), nullable=False)
    grand_parents = db.relationship('grand_parents', lazy=True)

    def __repr__(self):
        return '<parents %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "last_name": self.last_name,
            "age": self.age


        }

class children(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    last_name = db.Column(db.String(80), unique=False, nullable=False)
    age = db.Column(db.String(3), unique=False, nullable=False)
    grand_parents = db.relationship('parents', lazy=True)


    def __repr__(self):
        return '<children %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "last_name": self.last_name,
            "age": self.age
 
        }


