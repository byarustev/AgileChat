from AgileChat import users


class User:
    def __init__(self, _id, username, name, password):
        self.user_id = _id
        self.username = username
        self.name = name
        self.password = password

    @staticmethod
    def login(username, password):
        for user in users:
            if user.username == username and user.password == password:
                return True

        return False

    @staticmethod
    def create_account(username, name, password):
        for user in users:
            if user.username == username or user.name == name:
                print("User already exists")
                return False

        user = User(len(users), username, name, password)
        users.append(user)
        return True

    def create_comment(self, comment):
        pass

    def edit_my_comment(self, comment_id, user_id, user_type):
        pass

    def comments_list(self):
        pass

    def my_comments_list(self):
        pass
