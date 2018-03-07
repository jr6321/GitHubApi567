""" Homework#4: """

import urllib.request
import urllib.parse
import urllib.error
import requests
import json


def github_id(username):
    """ retrieve a user's list of repositories, use this API """
    api_url = requests.get("https://api.github.com/users/"+ID+"/"+repo+"/")
    try:
        url = api_url + urllib.parse.urlencode({'name':name})
    except urllib.request.URLError:
        print("The URL is not correct")
        return

    """ Formatting the json output """
    print('Retrieving the username', url)
    uh = urllib.request.urlopen(url)
    user_id = json.loads(user.text)
    print('Retrieved', len(user_id))

    try:
        js = json.loads(user_id)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('====FAILURE TO RETRIEVE====')
        print(user_id)

    print(json.dumps(js, indent=4))

    """ Building out the dictionary """
    output = js['results'][0]['name']['repo_url']
    return output


def repo_commits(username, user_repo):
    """ retrieve the commits for a user's repository """
    user_repo = requests.get("https://api.github.com/users/"+ID+"/"+repo+"/commits")

    try:
        js = json.loads(user_repo.text)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('====FAILURE TO RETRIEVE====')
        print(user_repo)

    return len(user_repo)


def main():
    """ main function"""
    user_id = input('Enter Your GitHub username:')
    try:
        user_address = str(user_id)
    except TypeError:
        print('You must submit a valid id')
        return None

        github_api(username)

if __name__ == "__main__":
        main()