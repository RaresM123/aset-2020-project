from unittest import TestCase
import src.Monitors as monitors

class Test(TestCase):
    def test_monitor_input_sentence(self):
        """
            Monitor Rules:
                1. Sentence null -> return the test sentence
                2. If there are words from another language -> delete those words
                3. If there are spelling mistakes -> rewrite the sentence
        """
        "Rule 1"
        response = monitors.Monitor_InputSentence("")
        self.assertEqual(response,"I like eating bugs")

        "Rule 2"
        response = monitors.Monitor_InputSentence("I like eating castraveti ice")
        self.assertNotIn(response,"castraveti")
        self.assertEqual(response,"I like eating ice")

        "Rule 3"
        response = monitors.Monitor_InputSentence("A sentene for an new modil")
        self.assertEqual(response,"A sentence for a new model")

        "Rule 2 & 3"
        response = monitors.Monitor_InputSentence("A sentene for lamai an new modil")
        self.assertNotIn(response, "lamai")
        self.assertEqual(response, "A sentence for a new model")




