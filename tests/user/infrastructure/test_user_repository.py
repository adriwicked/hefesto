import unittest

from src.user.domain.user import User
from src.user.infrastructure.user_repository import UserRepository

class TestUserRepository(unittest.TestCase):
    def setUp(self):
        self.repo = UserRepository()

    def test_save_user_returns_saved_user(self):
        user = User(name='Adrián', email='adrian@example.com')
        saved_user = self.repo.save(user)
        self.assertEqual(saved_user, user)

    def test_get_user_by_id(self):
        user = User(name='Adrián', email='adrian@example.com')
        self.repo.save(user)
        obtained_user = self.repo.find(user.get_id())
        self.assertEqual(user, obtained_user)