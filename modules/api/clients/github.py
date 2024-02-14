import requests

# this class creates API clien that will be used in tests
class Github:
    def get_user(self, username):
        r = requests.get(f"https://api.github.com/users/{username}") # returns an HTTP response object
        body = r.json() # converts the JSON response (body) into a Python list

        return body
    
    def search_repo(self, name):
        r = requests.get("https://api.github.com/search/repositories",
                        params={"q": name})
        body = r.json() # converts the JSON response (body) into a Python list

        return body


    def get_emoji(self):
        r = requests.get("https://api.github.com/emojis") # returns an HTTP response object
        body = r.json() # converts the JSON response (body) into a Python list

        return body
    

    def get_body_of_commits_list(self, name, repo):
        r = requests.get(f"https://api.github.com/repos/{name}/{repo}/commits") # returns an HTTP response object
        #body = r.json() # converts the JSON response (body) into a Python list

        return r #body