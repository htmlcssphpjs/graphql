# graphql

## get users

```
{
  getUsers {
    id
    name
    username
    fullname
    mail
    resume
  }
}
```

## find user

```
{
  getUsers(id: "admin") {
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

## create user

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
