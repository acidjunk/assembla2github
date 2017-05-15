from conf import *

from github import Github
from assembla import API

# Assembla instance
assembla = API(key=ASSEMBLA_KEY, secret=ASSEMBLA_SECRET)

# Github instance:
github = Github(GITHUB_USER, GITHUB_PASSWORD)

def clone_git(url):
    print('Cloning url: {url}'.format(url=url))

def get_repo_name(url):
    # Example: git@git.assembla.com:spacename.gitname.git
    return url.split(':')[1][0:-4]

for space in assembla.spaces():
    print("Working for {space}".format(space=space['name']))
    for git_repo in space.tools(type='GitTool'):
        repo_name = get_repo_name(git_repo['url'])
        clone_git(git_repo['url'])


## Then play with your Github objects:
#for repo in github.get_user().get_repos():
#    print repo.name