import unittest

from src.user.infrastructure.user_repository import UserRepository

class TestCreateUser(unittest.TestCase):
    def test_create_user(self):
        user_repository = UserRepository()
        create_user = CreateUser(user_repository)
        created_user = create_user.execute()