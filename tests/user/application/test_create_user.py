import unittest

from src.user.application.create_user import get_create_user
from src.user.infrastructure.user_repository import UserRepository


class TestCreateUser(unittest.TestCase):
    def setUp(self):
        self.repo = UserRepository()
        return super().setUp()

    def test_create_user(self):
        name = 'adrian'
        email = 'adrian@email.com'
        create_user = get_create_user(self.repo)
        created_user = create_user(name, email)

        self.assertEqual(created_user._name, name)

    def test_create_user_without_name_email_raise_error(self):
        create_user = get_create_user(self.repo)

        with self.assertRaises(AssertionError):
            create_user(name='', email='')

    def test_create_user_providing_id(self):
        google_uid = "Qo5mSFM3ezWJmieFglaB56i4Btx2"
        name = 'adrian'
        email = 'adrian@email.com'
        create_user = get_create_user(self.repo)
        created_user = create_user(name, email, google_uid)

        self.assertEqual(created_user.get_id().value, google_uid)
