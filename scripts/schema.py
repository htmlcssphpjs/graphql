import strawberry, hashlib
from typing import Optional, List
from scripts.send import emailt

from models import db_session
from models.users import User
from models.ideas import Idea

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
class IdeasType:
    id: str
    title: str
    pitch: str
    descriptions: str
    media: Optional[str]
    jobs: Optional[str]
    team: Optional[str]
    roadmap: Optional[str]

@strawberry.type
class Result:
    error: str
    id: str

@strawberry.type
class Mutation:
    Create = []

    @strawberry.mutation
    def create_user(self, id: str, name: str, pitch: str, picture: str, skills: str, roadmap: str, email: str, hashed_password: str) -> List[Result]:
        try:
            session = db_session.create_session()
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
            session.add(user)
            session.commit()
            result = Result(
                error='None',
                id=id
            )
            Create.append(result)
            try:
                data = {
                    "name": name,
                    "mail": email,
                    "username": id,
                    "url": 'url'
                }
                emailt(data, 'create', email)
            except Exception as e:
                print(e)

            return Create
        except Exception as e:
            print(e)
            Create = []
            result = Result(
                error='ID is busy',
                id='None'
            )
            Create.append(result)
            return Create

    @strawberry.mutation
    def create_idea(self, id: str, title: str, pitch: str, descriptions: str, media: Optional[str], jobs: Optional[str], team: Optional[str], roadmap: Optional[str]) -> List[Result]:
        try:
            session = db_session.create_session()
            Create = []

            idea = Idea(
                id=id,
                title=title,
                pitch=pitch,
                descriptions=descriptions,
                media=media,
                jobs=jobs,
                team=team,
                roadmap=roadmap
            )
            session.add(idea)
            session.commit()
            result = Result(
                error='None',
                id=id
            )
            Create.append(result)

            return Create
        except Exception as e:
            print(e)
            Create = []
            result = Result(
                error='ID is busy',
                id='None'
            )
            Create.append(result)
            return Create

    @strawberry.mutation
    def delete_user(self, id: str) -> List[Result]:
        try:
            session = db_session.create_session()
            user_all = session.query(User).all()
            Delete = []
            email = ''
            name = ''
            for user in user_all:
                if user.id == id:
                    email = user.email
                    name = user.name

            find = session.query(User).filter(User.id == id)
            find.delete()
            session.commit()
            result = Result(
                error='None',
                id=id
            )
            Delete.append(result)
            try:
                data = {
                    "name": name,
                    "mail": email,
                    "username": id,
                    "url": 'url'
                }
                emailt(data, 'delete', email)
            except Exception as e:
                print(e)

            return Delete
        except Exception as e:
            print(e)
            Delete = []
            result = Result(
                error='error',
                id='None'
            )
            Delete.append(result)
            return Delete

    @strawberry.mutation
    def delete_idea(self, id: str) -> List[Result]:
        try:
            session = db_session.create_session()
            Delete = []

            find = session.query(Idea).filter(Idea.id == id)
            find.delete()
            session.commit()
            result = Result(
                error='None',
                id=id
            )
            Delete.append(result)

            return Delete
        except Exception as e:
            print(e)
            Delete = []
            result = Result(
                error='error',
                id='None'
            )
            Delete.append(result)
            return Delete

    @strawberry.mutation
    def update_user(self, id: str, name: str, pitch: str, picture: str, skills: str, roadmap: str, email: str, hashed_password: str) -> List[Result]:
        try:
            session = db_session.create_session()
            Create = []

            user_all = session.query(User).all()

            for user in user_all:
                if user.id == id:
                    if id: user.id = id
                    if name: user.name = name
                    if pitch: user.pitch = pitch
                    if picture: user.picture = picture
                    if skills: user.skills = skills
                    if roadmap: user.roadmap = roadmap
                    if email: user.email = email
                    if hashed_password:
                        user.hashed_password = hash_password(hashed_password)

            session.commit()
            result = Result(
                error='None',
                id=id
            )
            Create.append(result)

            return Create
        except Exception as e:
            print(e)
            Create = []
            result = Result(
                error='ID is busy',
                id='None'
            )
            Create.append(result)
            return Create

    @strawberry.mutation
    def update_idea(self, id: str, title: str, pitch: str, descriptions: str, media: Optional[str], jobs: Optional[str], team: Optional[str], roadmap: Optional[str]) -> List[Result]:
        try:
            session = db_session.create_session()
            Create = []

            idea_all = session.query(Idea).all()

            for idea in idea_all:
                if idea.id == id:
                    idea.id = id
                    idea.title = title
                    idea.pitch = pitch
                    idea.descriptions = descriptions
                    idea.media = media
                    idea.jobs = jobs
                    idea.team = team
                    idea.roadmap = roadmap

            session.commit()
            result = Result(
                error='None',
                id=id
            )
            Create.append(result)

            return Create
        except Exception as e:
            print(e)
            Create = []
            result = Result(
                error='ID is busy',
                id='None'
            )
            Create.append(result)
            return Create

@strawberry.type
class Query:
    @strawberry.field
    def find_user(self, id: Optional[str] = None) -> List[UsersType]:
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
                break

        print(users_list)
        return users_list


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

    @strawberry.field
    def find_idea(self, id: Optional[str] = None) -> List[IdeasType]:
        session = db_session.create_session()
        idea_all = session.query(Idea).all()
        ideas_list = []

        for idea in idea_all:
            if (id):
                if str(idea.id) == str(id):
                    idea_as_dict = Idea(
                        id=idea.id,
                        title=idea.title,
                        pitch=idea.pitch,
                        descriptions=idea.descriptions,
                        media=idea.media,
                        jobs=idea.jobs,
                        team=idea.team,
                        roadmap=idea.roadmap
                    )
                    ideas_list.append(idea_as_dict)
                    break
            else:
                break

        print(ideas_list)
        return ideas_list

    @strawberry.field
    def get_ideas(self, id: Optional[str] = None) -> List[IdeasType]:
        session = db_session.create_session()
        idea_all = session.query(Idea).all()
        ideas_list = []

        for idea in idea_all:
            if (id):
                if str(idea.id) == str(id):
                    idea_as_dict = Idea(
                        id=idea.id,
                        title=idea.title,
                        pitch=idea.pitch,
                        descriptions=idea.descriptions,
                        media=idea.media,
                        jobs=idea.jobs,
                        team=idea.team,
                        roadmap=idea.roadmap
                    )
                    ideas_list.append(idea_as_dict)
                    break
            else:
                idea_as_dict = Idea(
                    id=idea.id,
                    title=idea.title,
                    pitch=idea.pitch,
                    descriptions=idea.descriptions,
                    media=idea.media,
                    jobs=idea.jobs,
                    team=idea.team,
                    roadmap=idea.roadmap
                )
                ideas_list.append(idea_as_dict)

        print(ideas_list)
        return ideas_list

schema = strawberry.Schema(query=Query, mutation=Mutation)
