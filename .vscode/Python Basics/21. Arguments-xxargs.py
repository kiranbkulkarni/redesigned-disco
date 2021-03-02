def save_user(**user):
    print(user)


print(save_user(id=1, name="admin"))


def save_user_by_id(**user):
    print(user['id'])
    print(user['name'])


print(save_user_by_id(id=2, name="BC"))
