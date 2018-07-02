from user import User


class Comment:

    def __init__(self, _id, global_id, user_id, message, timestamp):
        self.comment_id = _id
        self.user_id = user_id
        self.global_id = global_id
        self.message = message
        self.timestamp = timestamp
