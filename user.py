class User:
    def __init__(self, _id, username, name, password):
        self.user_id = _id
        self.username = username
        self.name = name
        self.password = password

    @staticmethod
    def login(username, password):
        pass

    def create_comment(self, comment):
        pass

    def edit_my_comment(self, comment_id, user_id, user_type):
        pass

    def comments_list(self):
        pass

    def my_comments_list(self):
        pass
