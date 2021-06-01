import strawberry
from strawberry.flask.views import GraphQLView
from typing import Optional, List
import hashlib, os
from flask import Flask, render_template, request, redirect, jsonify

from models import db_session
from models.users import User

app = Flask(__name__)

db_session.global_init('database.db')

def hash_password(password):
    h = hashlib.md5(password.encode())
    return h.hexdigest()

@strawberry.type
class UsersType:
    id: str
    name: str
    pitch: str
    picture: str
    skills: Optional[str]
    roadmap: Optional[str]
    email: str
    hashed_password: str

@strawberry.type
class Mutation:
    Create = []
    @strawberry.field
    def create_user(self, id: str, name: str, pitch: str, picture: str, skills: str, roadmap: str, email: str, hashed_password: str) -> Create:
        session = db_session.create_session()
        print(1)
        Create = []

        user = User(
            id=id,
            name=name,
            pitch=pitch,
            picture=picture,
            skills=skills,
            roadmap=roadmap,
            email=email,
            hashed_password=hash_password(hashed_password)
        )
        print(2)
        session.add(user)
        session.commit()
        Create.append({"error": "None", "id": id})
        
        return Create


@strawberry.type
class Query:
    @strawberry.field
    def get_users(self, id: Optional[str] = None) -> List[UsersType]:
        session = db_session.create_session()
        user_all = session.query(User).all()
        users_list = []

        for user in user_all:
            if (id):
                if str(user.id) == str(id):
                    user_as_dict = User(
                        id=user.id,
                        name=user.name,
                        pitch=user.pitch,
                        picture=user.picture,
                        skills=user.skills,
                        roadmap=user.roadmap,
                        email=user.email,
                        hashed_password=user.hashed_password
                    )
                    users_list.append(user_as_dict)
                    break
            else:
                user_as_dict = User(
                    id=user.id,
                    name=user.name,
                    pitch=user.pitch,
                    picture=user.picture,
                    skills=user.skills,
                    roadmap=user.roadmap,
                    email=user.email,
                    hashed_password=user.hashed_password
                )
                users_list.append(user_as_dict)

        print(users_list)
        return users_list


schema = strawberry.Schema(query=Query)
app.add_url_rule(
    "/graphql",
    view_func=GraphQLView.as_view(
        "graphql_view", schema=schema, mutation=Mutation
    ),
)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
