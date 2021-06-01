import strawberry
from typing import Optional, List
import uvicorn, json, hashlib, os
from fastapi import FastAPI
from starlette.graphql import GraphQLApp
from fastapi.encoders import jsonable_encoder
from fastapi.responses import HTMLResponse, JSONResponse

from models import db_session
from models.users import User

db_session.global_init('database.db')

app = FastAPI()

#app.add_middleware(
#    #CORSMiddleware,
#    #allow_origins=settings.ALLOWED_HOSTS,
#    allow_credentials=True,
#    allow_methods=["*"],
#    allow_headers=["*"],
#)

html = """
<!DOCTYPE html>
<html>
    <head>
        <title>API</title>
    </head>
    <body>
        <h1><a href="/api">API</a></h1>
    </body>
</html>
"""

def hash_password(password):
    h = hashlib.md5(password.encode())
    return h.hexdigest()


@strawberry.type
class UsersType:
  id: str
  name: str
  fullname:str
  username:str
  mail:str
  hashed_password:str
  resume: Optional[str]

#class CreateUser:
#
#    class Arguments:
#        id = ID(required=True)
#        name = String(required=True)
#        fullname = String(required=True)
#        username = String(required=True)
#        mail = String(required=True)
#        hashed_password = String(required=True)
#        resume = String()
#
#    def mutate(self, info, id, name, fullname, username, mail, hashed_password, resume):
#        session = db_session.create_session()
#        Create = []
#
#        user = User(
#            id=id,
#            name=name,
#            fullname=fullname,
#            username=username,
#            mail=mail,
#            hashed_password=hash_password(hashed_password),
#            resume=resume
#		)
#        session.add(user)
#        session.commit()
#        Create.append({"error": "None", "username": username})
#        
#        return Create[-1]

#class Mutation:
#    create_user = CreateUser.Field()

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
                        fullname=user.fullname,
                        username=user.username,
                        mail=user.mail,
                        hashed_password=user.hashed_password,
                        resume=user.resume
                    )
                    users_list.append(user_as_dict)
                    break
            else:
                user_as_dict = User(
                    id=user.id,
                    name=user.name,
                    fullname=user.fullname,
                    username=user.username,
                    mail=user.mail,
                    hashed_password=user.hashed_password,
                    resume=user.resume
                )
                users_list.append(user_as_dict)

        print(users_list)
        return users_list

@app.get("/")
async def main():
    return HTMLResponse(html)

#app.add_route("/api", GraphQLApp(
#    schema=Schema(query=Query))
#)

app.add_route(
    "/api", GraphQLApp(
        schema=strawberry.Schema(
            query=Query, 
            #mutation=Mutation
        )
    )
)

#if __name__ == '__main__':
    #port = int(os.environ.get("PORT", 5000))
    #uvicorn.run(app, host="0.0.0.0", port=port)
