# route for user (create, edit, delete, view)
# @app.get('/v1/users/{id}')
# def read_users():
#     return [{"username": "Ricky"}, {"username": "Morty"}]

# @app.get("/")
# def getItems():
#     return ['Item 1', 'Item 2', 'Item 3']


# Adding user within a dict of dict
# @app.post("/users/create")
# def addUser(newUser:schemas.User):
#     newId = len(userData.keys()) + 1
#     userData[newId] = {"task":newUser.task}
#     return userData