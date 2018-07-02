from AgileChat import users
from AgileChat import comments
from comment import Comment
import time
import datetime


class User:
    def __init__(self, _id, username, name, password):
        self.user_id = _id
        self.username = username
        self.name = name
        self.password = password
        self.comments_list = []

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
        curr_time = time.time()
        timestamp = datetime.datetime.fromtimestamp(curr_time).strftime('%Y-%m-%d %H:%M:%S')
        new_comment = Comment(len(self.comments_list),
                              len(comments), self.user_id, comment, timestamp)
        self.comments_list.append(new_comment)
        comments.append(new_comment)

    def edit_my_comment(self, comment_id, user_id, user_type):
        pass

    def comments_list(self):
        return self.comments_list

    def my_comments_list(self):
        pass
