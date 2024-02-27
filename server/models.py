from sqlalchemy.orm import validates
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.ext.hybrid import hybrid_property

from config import db, metadata, bcrypt

# Models go here!

class User(db.Model, SerializerMixin):
    __tablename__= "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    computer = db.Column(db.Boolean)
    _password_hash = db.Column(db.String)

    # Foreign Keys

    # Relationsips
    monsters = db.relationship("Monster", back_populates = "user")
    battles = db.relationship("Battle_User", back_populates = "user")
    
    # Serialization
    serialize_rules = ("-monsters.user", "-battle_users.user")

    # Validations
    @validates("username")
    def validates_username(self, key, value):
        if not value:
            raise ValueError(f"{value} is not a valid {key}.")
        return value
    
    # @validates("computer")
    # def validates_computer(self, key, value):
    #     if not type(value) == Bool:
    #         raise ValueError("computer must be of type boolean.")
    #     return value

    @hybrid_property
    def password_hash(self):    
        raise Exception('Password hashes may not be viewed.')

    @password_hash.setter
    def password_hash(self, password):
        password_hash = bcrypt.generate_password_hash(
            password.encode('utf-8'))
        self._password_hash = password_hash.decode('utf-8')

    def authenticate(self, password):
        return bcrypt.check_password_hash(
            self._password_hash, password.encode('utf-8'))
    
    def __repr__(self):
        return f'<User {self.id}, {self.username}, {self.computer}>'


class Battle(db.Model, SerializerMixin):
    __tablename__ = "battles"

    id = db.Column(db.Integer, primary_key=True)
    user_turn = db.Column(db.Boolean)
    complete = db.Column(db.Boolean)

    # Foreign Keys

    # Relationships
    users = db.relationship("Battle_User", back_populates = "battle")
    
    # Serialization
    serialize_rules = ("-battle_users.battle",)

    # Validations
    # @validates("user_turn", "complete")
    # def validates_battle(self, key, value):
    #     if not type(value) == Bool:
    #         raise ValueError(f"{key} must be of type boolean.")
    #     return value
    
    def __repr__(self):
        return f'<Battle {self.id}, {self.user_turn}, {self.complete}>'


class Monster(db.Model, SerializerMixin):
    __tablename__ = "monsters"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    nickname = db.Column(db.String, default=None)
    type = db.Column(db.String)
    health = db.Column(db.Integer)
    image = db.Column(db.String)

    # Foreign Keys
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    # Relationships
    user = db.relationship("User", back_populates="monsters")
    moves = db.relationship("Monster_Move", back_populates= "monster")

    # Serialization
    serialize_rules = ("-moves.monster", "-user.monsters")
    
    # Validations
    @validates("name")
    def validates_name(self, key, value):
        if not value:
            raise ValueError(f"{value} is not a valid {key}.")
        return value
    
    @validates("type")
    def validates_type(self, key, value):
        if not value in ["Water", "Fire", "Leaf"]:
            raise ValueError(f"{value} is not a valid {key}.")
        return value
    
    @validates("health")
    def validates_health(self, key, value):
        if not value > 0:
            raise ValueError("health must be greater than 0.")
        return value
    
    def __repr__(self):
        return f'<Monster {self.id}, {self.name}, {self.nickname}, {self.type}, {self.health}>'

class Move(db.Model, SerializerMixin):
    __tablename__ = "moves"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    type = db.Column(db.String)
    damage = db.Column(db.Integer)

    # Foreign Keys

    # Relationships
    monsters = db.relationship("Monster_Move", back_populates= "move")
    
    # Serialization
    serialize_rules = ("-monsters.move",)
    
    # Validations
    @validates("name")
    def validates_name(self, key, value):
        if not value:
            raise ValueError(f"{value} is not a valid {key}.")
        return value

    @validates("type")
    def validates_type(self, key, value):
        if not value in ["Water", "Fire", "Leaf"]:
            raise ValueError(f"{value} is not a valid {key}.")
        return value

    @validates("damage")
    def validates_damage(self, key, value):
        if not value > 0:
            raise ValueError("damage must be greater than 0.")
        return value
    
    def __repr__(self):
        return f'<Move {self.id}, {self.name}, {self.type}, {self.damage}, {self.monster.name}>'

class Battle_User(db.Model, SerializerMixin):
    __tablename__ = "battle_users"

    id = db.Column(db.Integer, primary_key=True)
    
    # Foreign Keys
    battle_id = db.Column(db.Integer, db.ForeignKey("battles.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    # Relationships
    battle = db.relationship("Battle", back_populates= "users")
    user = db.relationship("User", back_populates= "battles")

    # Serialization
    serialize_rules = ("-battle.users", "-user.battles")

    def __repr__(self):
        return f'<Battle_User {self.id}, {self.battle_id}, {self.user_id}>'

class Monster_Move(db.Model, SerializerMixin):
    __tablename__ = "monster_moves"

    id = db.Column(db.Integer, primary_key=True)
    
    # Foreign Keys
    monster_id = db.Column(db.Integer, db.ForeignKey("monsters.id"))
    move_id = db.Column(db.Integer, db.ForeignKey("moves.id"))

    # Relationships
    monster = db.relationship("Monster", back_populates= "moves")
    move = db.relationship("Move", back_populates= "monsters")

    # Serialization
    serialize_rules = ("-monster.moves", "-move.monsters")

    def __repr__(self):
        return f'<Monster_Move {self.id}, {self.monster_id}, {self.move_id}>'