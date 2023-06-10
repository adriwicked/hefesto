import unittest

from src.user.domain.user_id import UserID


class TestUserID(unittest.TestCase):
    def test_user_id_default_value(self):
        user_id = UserID()
        self.assertIsNotNone(user_id.value)
        self.assertIsInstance(user_id.value, str)
        uuid4_regex = r'^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$'
        self.assertRegex(user_id.value, uuid4_regex)

    def test_user_id_providing_value(self):
        google_uid = "Qo5mSFM3ezWJmieFglaB56i4Btx2"
        user_id = UserID(value=google_uid)
        self.assertEqual(user_id.value, google_uid)

    def test_compare_same_user_ids(self):
        user_id1 = UserID(value='abc')
        user_id2 = UserID(value='abc')
        self.assertEqual(user_id1, user_id2)

    def test_compare_different_user_ids(self):
        user_id1 = UserID()
        user_id2 = UserID()
        self.assertNotEqual(user_id1, user_id2)
