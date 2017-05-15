import os
from github import Github
from assembla import API

from conf import *


# Assembla instance
assembla = API(key=ASSEMBLA_KEY, secret=ASSEMBLA_SECRET)

# Github instance:
github = Github(GITHUB_USER, GITHUB_PASSWORD)

def clone_git(url):
    print('Cloning url: {url}'.format(url=url))
    os.system('git clone --bare {url}'.format(url=url))

def get_repo_name(url):
    # Example: git@git.assembla.com:spacename.gitname.git
    return url.split(':')[1][0:-4]

def create_repo(name):
    github.get_user().create_repo(name, private=True)

def push_repo(name):
    os.chdir('{name}.git'.format(name=name))
    os.system('git push --mirror git@github.com:{user}/{name}.git'.format(user=GITHUB_USER, name=name))
    os.chdir('..')

for space in assembla.spaces():
    print("Working for {space}".format(space=space['name']))
    for git_repo in space.tools(type='GitTool'):
        repo_name = get_repo_name(git_repo['url'])
        clone_git(git_repo['url'])
        create_repo(repo_name)
        push_repo(repo_name)
