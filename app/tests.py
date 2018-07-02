from app.user import User
from app.moderator import Moderator
import unittest


class TestApp(unittest.TestCase):
    """Handles tests for the application"""


def setUp(self):
    self.user = User(1, "username", "name", "password")
    self.moderator = Moderator(1, "moderator_name")


def test_isinstance(self):
    self.assertIsInstance(self.user, User)
    self.assertIsInstance(self.moderator, Moderator)


def test_login_user_successfully(self):
    res = self.user.login("username", "password")
    self.assetEqual(res, True)


def test_create_comment_successfully(self):
    res = self.user.create_comment("comment")
    self.assetEqual(res, True)


def test_edit_my_comment(self):
    res = self.user.edit_my_comment(1, self.user)
    self.assetEqual(res, True)


def test_delete_comment(self):
    res = self.user.delete_comment(self.user.id, self.comment)
    self.assetEqual(res, True)
