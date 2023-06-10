import unittest

from src.user.application.create_user import get_create_user
from src.user.infrastructure.user_repository import UserRepository
from src.user.application.find_user import get_find_user


class TestFindUser(unittest.TestCase):
    def setUp(self):
        self.repo = UserRepository()

        self.create_user = get_create_user(self.repo)
        self.find_user = get_find_user(self.repo)

        self.created_user = self.create_user(
            name='Adrián',
            email='adrian@email.com'
        )
        return super().setUp()

    def test_find_user(self):
        found_user = self.find_user(self.created_user.get_id())
        self.assertEqual(found_user, self.created_user)