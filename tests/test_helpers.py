import unittest
import repackage
repackage.up()
import four.bot.helpers


class TestBotHelpers(unittest.TestCase):

    def test_get_json(self):
        expected = {
                    "SECRET_TEST1": "abc",
                    "SECRET_TEST2": "123",
                    }
        self.assertEqual(four.helpers.get_json("test_json.json"), expected)

