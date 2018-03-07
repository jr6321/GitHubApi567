import unittest 
import urllib.parse
import urllib.error
import requests
import json
from HW04-aperry567 import github_id
from HW04-aperry567 import repo_commits


def github_id(username):
    """ Method from main program"""
    return repo_commits(username, user_repo) == username, user_repo


#Unittest case:
class github_idTest(unittest.TestCase):
    def test_github_id(self):
        self.assertEqual(len(user_repo),4)




