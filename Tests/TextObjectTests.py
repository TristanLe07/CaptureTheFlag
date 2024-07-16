from GameFrame import TextObject
import unittest


class TextObjectTests(unittest.TestCase):
    def test_split_half_on_space(self):
        # Arrange
        params = (
            {"case": "Two Words 11 Chars", "input": "Teams Names", "expected output": ("Teams", "Names")},
            {"case": "Space at start", "input": "T eamsNames", "expected output": ("T eamsNames", "")},
            {"case": "Space at end", "input": "TeamsName s", "expected output": ("TeamsName s", "")},
            {"case": "Space first", "input": " TeamsNames", "expected output": ("TeamsNames", "")},
            {"case": "Space last", "input": "TeamsNames ", "expected output": ("TeamsNames", "")},
            {"case": "No Space", "input": "TeamsNames", "expected output": ("TeamsNames", "")},
            {"case": "Mid Space", "input": "Teams Names", "expected output": ("Teams", "Names")},
            {"case": "Short with spaces", "input": "Team Nam", "expected output": ("Team Nam", "")},
        )
        for param in params:
            with self.subTest(param["case"]):
                input = param["input"]
                expected_output = param["expected output"]

                # Act
                actual_output = TextObject.split_half_on_space(input)

                # Assert
                self.assertEqual(expected_output[0], actual_output[0])
                self.assertEqual(expected_output[1], actual_output[1])


if __name__ == "__main__":
    unittest.main()
