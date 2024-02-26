#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from flask import Flask, request, make_response, session
from flask_restful import Resource

# Local imports
from config import app, db, api
# Add your model imports
from models import db, User, Battle, Monster, Move, Battle_User, Monster_Move

# Views go here!

@app.route('/')
def index():
    return '<h1>Project Server</h1>'

# @app.before_request
# def check_if_logged_in():
#     if not session["user_id"] and request.endpoint == "owner":
#         response = make_response({"error": "Unauthorized"}, 401)

#         return response

# class Login(Resource):
#     def post(self):
#         name = request.get_json()["name"]
#         user = User.query.filter(User.name == name).first()

#         session["user_id"] = user.id

#         response = make_response(
#             user.to_dict(),
#             200
#         )

#         return response

# api.add_resource(Login, "/login")

# class CheckSession(Resource):
#     def get(self):
#         user = User.query.filter(User.id == session.get("user_id")).first()

#         if user:
#             return user.to_dict()
        
#         else:
#             response = make_response({"message": "401: Not Authorized"}, 401)

#             return response

# api.add_resource(CheckSession, "/check_session")

# class Logout(Resource):
#     def delete(self):
#         session["user_id"] = None

#         response = make_response(
#             {},
#             200
#         )

#         return response

# api.add_resource(Logout, "/logout")

class Users(Resource):
    def get(self):
        users = [user.to_dict() for user in User.query.all()]

        response = make_response(
            users,
            200
        )

        return response

    def post(self):

        form_data = request.get_json()

        try:
            new_user = User(
                name=form_data["name"],
                computer=form_data["computer"]
            )
            
            db.session.add(new_user)
            db.session.commit()

            response =  make_response(new_user.to_dict(), 201)
        
        except ValueError:
            response = make_response({"errors": ["validation errors"]}, 400)
        
        return response

api.add_resource(Users, "/users")

class UsersById(Resource):
    def get(self, id):
        user = User.query.filter(User.id == id).first()

        if not user:
            response = make_response(
                {"error": "User not found"},
                404
            )
        
        else:
            response = make_response(
                user.to_dict(),
                200
            )
        
        return response

    def patch(self, id):
        user = User.query.filter(User.id == id).first()

        if not user:
            response = make_response({'error': 'User not found'}, 404)

        form_data = request.get_json()

        try:
            for attr in form_data:
                setattr(user, attr, form_data[attr])

            db.session.commit()

            user_dict = user.to_dict()

            response = make_response(user_dict, 202)

        except ValueError:
            response = make_response({"errors": ["validation errors"]}, 400)
        
        return response
    
    def delete(self, id):
        user = User.query.filter(User.id==id).first()

        if user:
            db.session.delete(user)
            db.session.commit()
            response = make_response({}, 200)
        
        else:
            response = make_response({"error": "User not found"}, 404)
        
        return response

api.add_resource(UsersById, "/users/<int:id>")

class Battles(Resource):
    def get(self):
        battles = [battle.to_dict() for battle in Battle.query.all()]

        response = make_response(
            battles,
            200
        )

        return response

    def post(self):

        form_data = request.get_json()

        try:
            new_battle = Battle(
                user_turn=form_data["user_turn"],
                computer=form_data["computer"]
            )
            
            db.session.add(new_battle)
            db.session.commit()

            response =  make_response(new_battle.to_dict(), 201)
        
        except ValueError:
            response = make_response({"errors": ["validation errors"]}, 400)
        
        return response

api.add_resource(Battles, "/battles")

class BattlesById(Resource):
    def get(self, id):
        battle = Battle.query.filter(Battle.id == id).first()

        if not battle:
            response = make_response(
                {"error": "Battle not found"},
                404
            )
        
        else:
            response = make_response(
                battle.to_dict(),
                200
            )
        
        return response

    def patch(self, id):
        battle = Battle.query.filter(Battle.id == id).first()

        if not battle:
            response = make_response({'error': 'Battle not found'}, 404)

        form_data = request.get_json()

        try:
            for attr in form_data:
                setattr(battle, attr, form_data[attr])

            db.session.commit()

            battle_dict = battle.to_dict()

            response = make_response(battle_dict, 202)

        except ValueError:
            response = make_response({"errors": ["validation errors"]}, 400)
        
        return response
    
    def delete(self, id):
        battle = Battle.query.filter(Battle.id==id).first()

        if battle:
            db.session.delete(battle)
            db.session.commit()
            response = make_response({}, 200)
        
        else:
            response = make_response({"error": "Battle not found"}, 404)
        
        return response

api.add_resource(BattlesById, "/battles/<int:id>")

class Monsters(Resource):
    def get(self):
        monsters = [monster.to_dict() for monster in Monster.query.all()]

        response = make_response(
            monsters,
            200
        )

        return response

    def post(self):

        form_data = request.get_json()

        try:
            new_monster = Monster(
                name=form_data["name"],
                nickname=form_data["nickname"],
                type=form_data["type"],
                health=form_data["health"],
                user_id=form_data["user_id"]
            )
            
            db.session.add(new_monster)
            db.session.commit()

            response =  make_response(new_monster.to_dict(), 201)
        
        except ValueError:
            response = make_response({"errors": ["validation errors"]}, 400)
        
        return response

api.add_resource(Monsters, "/monsters")

class MonstersById(Resource):
    def get(self, id):
        monster = Monster.query.filter(Monster.id == id).first()

        if not monster:
            response = make_response(
                {"error": "Monster not found"},
                404
            )
        
        else:
            response = make_response(
                monster.to_dict(),
                200
            )
        
        return response

    def patch(self, id):
        monster = Monster.query.filter(Monster.id == id).first()

        if not monster:
            response = make_response({'error': 'Monster not found'}, 404)

        form_data = request.get_json()

        try:
            for attr in form_data:
                setattr(monster, attr, form_data[attr])

            db.session.commit()

            monster_dict = monster.to_dict()

            response = make_response(monster_dict, 202)

        except ValueError:
            response = make_response({"errors": ["validation errors"]}, 400)
        
        return response
    
    def delete(self, id):
        monster = Monster.query.filter(Monster.id==id).first()

        if monster:
            db.session.delete(monster)
            db.session.commit()
            response = make_response({}, 200)
        
        else:
            response = make_response({"error": "Monster not found"}, 404)
        
        return response

api.add_resource(MonstersById, "/monsters/<int:id>")

class Moves(Resource):
    def get(self):
        moves = [move.to_dict() for move in Move.query.all()]

        response = make_response(
            moves,
            200
        )

        return response

    def post(self):

        form_data = request.get_json()

        try:
            new_move = Move(
                name=form_data["name"],
                type=form_data["type"],
                damage=form_data["damage"]
            )
            
            db.session.add(new_move)
            db.session.commit()

            response =  make_response(new_move.to_dict(), 201)
        
        except ValueError:
            response = make_response({"errors": ["validation errors"]}, 400)
        
        return response

api.add_resource(Moves, "/moves")

class MovesById(Resource):
    def get(self, id):
        move = Move.query.filter(Move.id == id).first()

        if not move:
            response = make_response(
                {"error": "Move not found"},
                404
            )
        
        else:
            response = make_response(
                move.to_dict(),
                200
            )
        
        return response

    def patch(self, id):
        move = Move.query.filter(Move.id == id).first()

        if not move:
            response = make_response({'error': 'Move not found'}, 404)

        form_data = request.get_json()

        try:
            for attr in form_data:
                setattr(move, attr, form_data[attr])

            db.session.commit()

            move_dict = move.to_dict()

            response = make_response(move_dict, 202)

        except ValueError:
            response = make_response({"errors": ["validation errors"]}, 400)
        
        return response
    
    def delete(self, id):
        move = Move.query.filter(Move.id==id).first()

        if move:
            db.session.delete(move)
            db.session.commit()
            response = make_response({}, 200)
        
        else:
            response = make_response({"error": "Move not found"}, 404)
        
        return response

api.add_resource(MovesById, "/moves/<int:id>")

class Battle_Users(Resource):
    def get(self):
        battle_users = [battle_user.to_dict() for battle_user in Battle_User.query.all()]

        response = make_response(
            battle_users,
            200
        )

        return response

    def post(self):

        form_data = request.get_json()

        try:
            new_battle_user = Battle_User(
                battle_id=form_data["battle_id"],
                user_id=form_data["user_id"]
            )
            
            db.session.add(new_battle_user)
            db.session.commit()

            response =  make_response(new_battle_user.to_dict(), 201)
        
        except ValueError:
            response = make_response({"errors": ["validation errors"]}, 400)
        
        return response

api.add_resource(Battle_Users, "/battle_users")

class Battle_UsersById(Resource):
    def get(self, id):
        battle_user = Battle_User.query.filter(Battle_User.id == id).first()

        if not battle_user:
            response = make_response(
                {"error": "Battle_User not found"},
                404
            )
        
        else:
            response = make_response(
                battle_user.to_dict(),
                200
            )
        
        return response

    def patch(self, id):
        battle_user = Battle_User.query.filter(Battle_User.id == id).first()

        if not battle_user:
            response = make_response({'error': 'Battle_User not found'}, 404)

        form_data = request.get_json()

        try:
            for attr in form_data:
                setattr(battle_user, attr, form_data[attr])

            db.session.commit()

            battle_user_dict = battle_user.to_dict()

            response = make_response(battle_user_dict, 202)

        except ValueError:
            response = make_response({"errors": ["validation errors"]}, 400)
        
        return response
    
    def delete(self, id):
        battle_user = Battle_User.query.filter(Battle_User.id==id).first()

        if move:
            db.session.delete(battle_user)
            db.session.commit()
            response = make_response({}, 200)
        
        else:
            response = make_response({"error": "Battle_User not found"}, 404)
        
        return response

api.add_resource(Battle_UsersById, "/battle_users/<int:id>")

class Monster_Moves(Resource):
    def get(self):
        monster_moves = [monster_move.to_dict() for monster_move in Monster_Move.query.all()]

        response = make_response(
            battle_users,
            200
        )

        return response

    def post(self):

        form_data = request.get_json()

        try:
            new_monster_move = Monster_Move(
                monster_id=form_data["monster_id"],
                move_id=form_data["move_id"]
            )
            
            db.session.add(new_monster_move)
            db.session.commit()

            response =  make_response(new_monster_move.to_dict(), 201)
        
        except ValueError:
            response = make_response({"errors": ["validation errors"]}, 400)
        
        return response

api.add_resource(Monster_Moves, "/monster_moves")

class Monster_MovesById(Resource):
    def get(self, id):
        monster_move = Monster_Move.query.filter(Monster_Move.id == id).first()

        if not monster_move:
            response = make_response(
                {"error": "Monster_Move not found"},
                404
            )
        
        else:
            response = make_response(
                monster_move.to_dict(),
                200
            )
        
        return response

    def patch(self, id):
        monster_move = Monster_Move.query.filter(Monster_Move.id == id).first()

        if not monster_move:
            response = make_response({'error': 'Monster_Move not found'}, 404)

        form_data = request.get_json()

        try:
            for attr in form_data:
                setattr(monster_move, attr, form_data[attr])

            db.session.commit()

            monster_move_dict = monster_move.to_dict()

            response = make_response(monster_move_dict, 202)

        except ValueError:
            response = make_response({"errors": ["validation errors"]}, 400)
        
        return response
    
    def delete(self, id):
        monster_move = Monster_Move.query.filter(Monster_Move.id==id).first()

        if move:
            db.session.delete(monster_move)
            db.session.commit()
            response = make_response({}, 200)
        
        else:
            response = make_response({"error": "Monster_Move not found"}, 404)
        
        return response

api.add_resource(Monster_MovesById, "/monster_moves/<int:id>")

if __name__ == '__main__':
    app.run(port=5555, debug=True)

