import unittest

from Model.Auth import Auth
from config.Accounts import API_ACCOUNT
from config.validate_api_key import OKAY_KEYS


class LoginTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.accounts = API_ACCOUNT
        self.token = None

    def _validate_json_data(self, data):
        keys = list(dict(data))
        self.assertEqual(keys, OKAY_KEYS, "should be the same keys")
        self.assertIsNotNone(data['data'], "should have data  on keys data")

    def tearDown(self) -> None:
        self.assertIsNotNone(self.token, "token should not be none or null before logout")
        response = Auth().logout(self.token)
        self.assertEqual(200, response.status_code, "should be 200 response")
        self.token = None

    def test_should_return_400_bad_request(self):
        response = Auth().login(account=None)
        self.assertEqual(400, response.status_code, "should be 400 response")

    def test_login_admin_account(self):
        response = Auth().login(account=self.accounts['admin'])
        self.assertEqual(200, response.status_code, "should be 200 response")
        data = response.json()
        self._validate_json_data(data)
        self.token = data['data']['token']


if __name__ == '__main__':
    unittest.main()
