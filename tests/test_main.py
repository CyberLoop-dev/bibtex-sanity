import unittest
from main import validate
class BibTests(unittest.TestCase):
    def test_valid_article(self):
        src="@article{x, author={A}, title={T}, journal={J}, year={2024}}"
        self.assertEqual(validate(src)["issue_count"],0)
    def test_missing_field(self):
        src="@article{x, author={A}, title={T}, year={2024}}"
        self.assertTrue(any("journal" in x["message"] for x in validate(src)["issues"]))
    def test_duplicate_key(self):
        src="@misc{x, title={A}}\n@misc{X, title={B}}"
        self.assertTrue(any("Duplicate" in x["message"] for x in validate(src)["issues"]))
if __name__=="__main__": unittest.main()
