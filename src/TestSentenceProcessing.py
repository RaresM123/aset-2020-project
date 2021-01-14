from unittest import TestCase
import unittest
from ServerConnectionAuthorizer import processSentence

class Test(TestCase):
    def test_resulted_sentence(self):
        sentence = processSentence("Anna likes walking on the sky.")
        print(sentence)
        self.assertTrue(sentence is not None)
        self.assertTrue(len(sentence) > 10)
        self.assertTrue(len(sentence.split(" ")) > 3)



if __name__ == '__main__':
    unittest.main()