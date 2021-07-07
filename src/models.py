from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

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

class Member(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    last_name = db.Column(db.String(80))
    age = db.Column(db.Integer)
    parent_id = db.Column(db.Integer, db.ForeignKey('member.id'))
    parent = db.relationship('Member')


    def __repr__(self):
        return '<Member %s' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "last name": self.last_name,
            "age": self.age,
            "parent_id": self.parent_id,
            # do not serialize the password, its a security breach
        }
class GrandParents(db.Model):
    __tablename__ = 'grandparents'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    last_name = db.Column(db.String(80), unique=False, nullable=False)
    age = db.Column(db.Integer, nullable=False)
  
    

    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "last_name": self.last_name,
            "age": self.age,
            # do not serialize the password, its a security breach
        }

class Parents(db.Model):
    __tablename__ = 'parents'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    last_name = db.Column(db.String(80), unique=False, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    grandparent_id = db.Column(db.Integer, db.ForeignKey('grandparents.id'))
    grandparent = db.relationship('GrandParents')
    

    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "last_name": self.last_name,
            "age": self.age,
            "grandparent_id": self.grandparent_id
            # do not serialize the password, its a security breach
        }



class Current_Generation(db.Model):
    __tablename__ = 'current_generation'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    last_name = db.Column(db.String(80), unique=False, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    parent_id = db.Column(db.Integer, db.ForeignKey('parents.id'))
    parent = db.relationship('Parents')

    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "last_name": self.last_name,
            "age": self.age,
            "parent_id": self.parent_id
            # do not serialize the password, its a security breach
        }






