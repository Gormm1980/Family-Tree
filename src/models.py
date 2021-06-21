from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class BasicMode():
    @classmethod
    def get_all(cls):
        return cls.query.all()
        
    @classmethod
    def get_member(cls,model_id):
        return cls.query.filter_by(id = model_id).first()
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class GrandParents(db.Model, BasicMode):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    last_name = db.Column(db.String(80), unique=False, nullable=False)
    age = db.Column(db.Integer, nullable=False)

    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "last_name": self.last_name,
            "age": self.age
            # do not serialize the password, its a security breach
        }
class Parents(db.Model, BasicMode):
    id_parents = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    last_name = db.Column(db.String(80), unique=False, nullable=False)
    age = db.Column(db.Integer, nullable=False)

    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "last_name": self.last_name,
            "age": self.age
            # do not serialize the password, its a security breach
        }

class Children(db.Model, BasicMode):
    id_children = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    last_name = db.Column(db.String(80), unique=False, nullable=False)
    age = db.Column(db.Integer, nullable=False)

    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "last_name": self.last_name,
            "age": self.age
            # do not serialize the password, its a security breach
        }