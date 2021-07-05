from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class BasicModel():
    @classmethod
    def get_all(cls):
        return cls.query.all()
        
    @classmethod
    def get_member(cls,model_id):
        return cls.query.filter_by(id = model_id).first()

class GrandParents(db.Model, BasicModel):
    __tablename__ = "grandparents"
    id_grandparents = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    last_name = db.Column(db.String(80), unique=False, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    parents_id = db.Column(db.Integer, db.ForeignKey('parents.id_parents'))
    childs_id = db.Column(db.Integer, db.ForeignKey('childrens.id_children'))
    childs = db.relationship('Childrens', lazy='dynamyc', backref='childrens', primaryjoin="Childrens.id_children==GrandParents.id_grandparents")
    parents = db.relationship('Parents', lazy='dynamic', backref='parents', primaryjoin="Parents.id_parents==GrandParents.id_grandparents")

    def db_post(self):        
        db.session.add(self)
        db.session.commit()
    
    def set_granpa(self,json):
        self.name = json["name"]
        self.last_name = json["last_name"]
        self.age = json["age"]
        return self
    
    def serialize(self):
        return {
            "id_grandparents": self.id_grandparents,
            "name": self.name,
            "last_name": self.last_name,
            "age": self.age,
            # do not serialize the password, its a security breach
        }
class Parents(db.Model, BasicModel):
    __tablename__ = "parents"
    id_parents = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    last_name = db.Column(db.String(80), unique=False, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    grandparent_id = db.Column(db.Integer, db.ForeignKey('grandparents.id_grandparents'))
    child_id = db.Column(db.Integer, db.ForeignKey('childrens.id_children'))

    grandparents = db.relationship('GrandParents', lazy='dynamyc', backref='grandparents', primaryjoin="GrandParents.id_Grandparents==Parents.id_parents")
    childs = db.relationship('Childrens', lazy='dynamyc', backref='childrens', primaryjoin="Childrens.id_children==Parents.id_parents")
    # childrens = db.relationship('Children', secondary=tags, lazy='subquery', backref=db.backref('parents', lazy=True))
    # grandparents = db.relationship('GrandParents', secondary=tags, lazy='subquery', backref=db.backref('parents', lazy=True))
    

    def db_post(self):        
        db.session.add(self)
        db.session.commit()
    
    def set_parents(self,json):
        self.name = json["name"]
        self.last_name = json["last_name"]
        self.age = json["age"]
        return self

    def serialize(self):
        return {
            "id_parents": self.id_parents,
            "name": self.name,
            "last_name": self.last_name,
            "age": self.age,
            # do not serialize the password, its a security breach
        }

class Childrens(db.Model, BasicModel):
    __tablename__ = "children"
    id_children = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    last_name = db.Column(db.String(80), unique=False, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    parents_id = db.Column(db.Integer, db.ForeignKey('parents.id_parents'))
    grandpa_id = db.Column(db.Integer, db.ForeignKey('granparents.id_grandparents'))
    parents = db.relationship('Parents', lazy='dynamic', backref='parents', primaryjoin="Parents.id_parents==Childrens.id_children")
    grandparents = db.relationship('GrandParents', lazy='dynamyc', backref='grandparents', primaryjoin="GrandParents.id_Grandparents==Childrens.id_children")

    def db_post(self):        
        db.session.add(self)
        db.session.commit()
    
    def set_children(self,json):
        self.name = json["name"]
        self.last_name = json["last_name"]
        self.age = json["age"]
        return self
    
    def serialize(self):
        return {
            "id_children": self.id_children,
            "name": self.name,
            "last_name": self.last_name,
            "age": self.age,
            # do not serialize the password, its a security breach
        }
# family = db.Table('family'),
#     db.Column('parents_id', db.Integer, db.ForeignKey('parents.id_parents'), primary_key=True),
#     db.Column('grandparents_id', db.Integer, db.ForeignKey('grandparents.id_grandparents'), primary_key=True)
#     db.Column('children_id', db.Integer, db.ForeignKey('children.id_children'), primary_key=True)







