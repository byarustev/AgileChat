from user import User


class Comment(User):
    def __init(self, _id, user_id, message, timestamp):
        self.comment_id = _id
        self.user_id = user_id
        self.message = message
        self.timestamp = timestamp
