import requests as rq
import sys 
from github import Github as gt

username = sys.argv[1] #filename

url = f'https"//api.gitub.com/users/{username}'

user_data = rq.get(url).json()

def repository_names(user):
    reponames = []
    for repo in user.get_repos():
        reponames.append(user)
    return reponames

def repository_details(user):
    allrepodetails = []
    reponames = repository_names(user)
    for repo in reponames:
        repodetals = {}
        repodetails['Name'] = repo.full_name.split('/'[1])
        repo['Description'] =repo.description
        repo['Creation Date'] = repo.created_at
        repo['Programming Language'] = repo.language
        repo['Forked'] = str(repo.forks) + 'time(s)'
        allrepodetails.append(repo)
    
    return allrepodetails

user = Github().get_user(username)

REPO_DEETS = repository_details(user)

if __name__ == '__main__':
     for content in REPO_DEETS:
         for title, description in content.items():
             print(title, ':',  description)
         

