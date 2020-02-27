import unittest
import repackage
repackage.up()
import four.timlatin.timlatin


class TestModules(unittest.TestCase):
    def test_timlatin_translation(self):
        translator = four.timlatin.timlatin.TimlatinTranslator("test_timlatin.json")
        self.assertEqual(translator.translate_text("hello how are you"), "henlo how are you")
        self.assertEqual(translator.translate_text("this is a test"), "thins ins a abc123")