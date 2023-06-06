import unittest

from src.user.application.create_user import get_create_user
from src.user.infrastructure.user_repository import UserRepository


class TestCreateUser(unittest.TestCase):
    def test_create_user(self):
        user_repository = UserRepository()
        name = 'adrian'
        email = 'adrian@email.com'
        create_user = get_create_user(user_repository)
        created_user = create_user(name, email)

        self.assertEqual(created_user._name, name)
