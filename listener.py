# 3 environment variables needed
# GH_TOKEN
# USER
# API_SECRET

from flask import Flask, request, Response
import json
import requests
import datetime
import configparser
import os
import hmac
import hashlib
import base64


def get_configs():
    configs = configparser.ConfigParser()    
    configs.read('configs/config.ini')
    configs.sections()
    return configs['DEFAULT']

app                     = Flask(__name__)
configs                 = get_configs()
api_url                 = configs['api_url']
token                   = os.environ.get('GH_TOKEN')
user                    = os.environ.get('USER')
secret                  = os.environ.get('WH_SECRET')
mention                 = "@" + user
headers                 = {
    'Authorization': 'token ' + token, 
    'Accept': 'application/vnd.github.luke-cage-preview+json'
    }

# verify signature using hmac, sha256
def verifye_signature(payload, rawSignature, secret):
    signature_array     = rawSignature.split('=')
    signature           = signature_array[1]
    secret              = secret.encode('utf-8')
    hash_byte            = 'sha256=' + hmac.new(secret, payload, hashlib.sha256).hexdigest()
    return hmac.compare_digest(rawSignature.encode('utf-8'), hash_byte.encode('utf-8'))

# protect main branch
def protect_branch(owner, repo, branch):
    url                 = "{}/repos/{}/{}/branches/{}/protection".format(api_url, owner, repo, branch)  
    file_path = 'configs/branch_config.json'
    if os.path.exists(file_path):
        with open(file_path) as json_file:
            try:
                data = json.load(json_file)    
                response            = requests.put(url, data=json.dumps(data), headers=headers)
            except:
                print("error while trying to open file {}".format(file_path))
                print(sys.exc_info()[0])
                raise
            return True if response.status_code == 200 else False

# create an issue and mention user
def create_issue(owner, repo):
    url = "{}/repos/{}/{}/issues".format(api_url, owner, repo)
    data = {
        "title":"{} repository has been created".format(repo), 
        "body": "Hi {}".format(mention)
    }
    try:
        response = requests.post(url, data=json.dumps(data), headers=headers)
    except:
        print(sys.exc_info()[0])
        raise
    return True if response.status_code == 201 else False

def repo_created(body):
    repo                = body['repository']['name']
    owner               = body['repository']['owner']['login']
    branch_protected    = protect_branch(owner, repo, 'main')
    issue_created       = create_issue(owner, repo)        
    return True if branch_protected and issue_created else False


@app.route('/', methods=['POST'])
def list_to_events():
    body                = request.json   
    headers             = request.headers
    # check if request comes from GitHub 
    # using hmac
    valid               = verifye_signature(request.data, headers['X-Hub-Signature-256'], secret)
    success             = False
    status_code         = 200

    if valid:
        # Take action if a new repository created
        # first protect main branch
        # then create an issue and mention user
        if request.headers['X-Github-Event'] == 'repository' and body['action'] == 'created':
            success     = repo_created(body)
            status_code = 200 if success else 500            
    else:
        status_code = 400
    return {'success':success}, status_code

if __name__ == "__main__":
    app.run()


