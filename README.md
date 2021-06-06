# CrewStreet back

## Start

### Intall PC

```bash
pip install -r requirements.txt
python app.py
```

### Install heroku

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

## Usage

### get users

```
{
  getUsers {
    id
    name
    pitch
    picture
    skills
    roadmap
    email
    hashedPassword
  }
}
```

### find user

```
{
  getUser(id: "admin") {
    id
    name
    pitch
    picture
    skills
    roadmap
    email
    hashedPassword
  }
}
```

## delete user

```
mutation {
  deleteUser(
    id: "admin"
  ) {
    error
    id
  }
}
```

### create user

```
mutation {
  createUser(
    id: "vsecoder"
    name: "Всеволод"
    pitch: "Coding all in my live!"
    picture: "https://avatars.githubusercontent.com/u/84876354?s=200&v=4"
    skills: "JS"
    roadmap: "What this?"
    email: "kreepmeister@yandex.ru"
    hashedPassword: "password"
  ) {
    error
    id
  }
}
```

## update user

```
mutation {
  updateUser(
    id: "vsecoder"
    name: "Всеволод"
    pitch: "Coding all in my live!"
    picture: "https://avatars.githubusercontent.com/u/84876354?s=200&v=4"
    skills: "JS, Python, html/css"
    roadmap: "What this?"
    email: "kreepmeister@yandex.ru"
    hashedPassword: "password"
  ) {
    error
    id
  }
}
```

## get ideas

```
{
  getIdeas {
    id
    title
    pitch
    descriptions
    media
    jobs
    team
    roadmap
  }
}
```

## find idea

```
{
  getIdea(id: "crewstreet") {
    id
    title
    pitch
    descriptions
    media
    jobs
    team
    roadmap
  }
}
```

## create idea

```
mutation {
  createIdea(
    id: "test"
    title: "test"
    pitch: "test"
    descriptions: "test"
    media: "test"
    jobs: "test"
    team: "test"
    roadmap: "test"
  ) {
    error
    id
  }
}
```
## delete idea

```
mutation {
  deleteIdea(
    id: "test"
  ) {
    error
    id
  }
}
```

## update idea

```
mutation {
  updateIdea(
    id: "test"
    title: "test1"
    pitch: "test"
    descriptions: "test"
    media: "test"
    jobs: "test"
    team: "test"
    roadmap: "test"
  ) {
    error
    id
  }
}
```