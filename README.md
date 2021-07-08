# Web service - Protect main branch automatically upon repository creation

## Question


**PART 2**

For this section of the screener, we would like to gain insight into your ability to learn technical topics. Customers will frequently ask for assistance on projects. These requests will require you to learn new topics. This exercise will hopefully give us insight into your approach and aptitude in meeting these customers' needs.

##### ****GitHub** API Challenge**

**GitHub** has [a powerful API](https://developer.github.com/v3/) that enables developers to easily access **GitHub** data. Companies often ask us to craft solutions to their specific problems. A common request we receive is for branches to be automatically protected upon creation.

Please create a simple web service that listens for [organization events](https://developer.github.com/webhooks/#events) to know when a repository has been created. When the repository is created please automate the protection of the main branch. Notify yourself with an [@mention](https://help.github.com/articles/basic-writing-and-formatting-syntax/#mentioning-users-and-teams) in an issue within the repository that outlines the protections that were added.

Some things you will need:

* a **GitHub** account
* an organization (you can create one for free)
* a repository (in order to get a branch, you need a commit! Make sure to initialize with a README)
* a web service that listens for [webhook](https://developer.github.com/webhooks/) deliveries
* A README.md file in your web service's repository that documents how to run and use the service. Documentation is highly valued at **GitHub** and on the Professional Services team.
* Be prepared to demo this solution during your following interview

## Solution

### How does this work

This web service listens to GitHub organization's webhook for new repository creation and calls GitHub APIs to protect the main branch and create an issue and mention the user.

As soon as GH webhook sends event to web service telling that a new repository is created, the web services calls 2 GH APIs:

1. Repository protection branch API to protect main branch
2. Issue API by creating a new issue and mention the user in the issue comment

If these calls are successful it returns http code 200 otherwise responds with 4xx or 5xx code.

#### Web service security

To ensure API calls are initiated from GH webhook, the web service verifies request payload using HMAC,SHA-256 and webhook secrets to authenticate messages.

The security can be expanded by whitelisting requests coming from GitHub IPs, list of GH IPs can be obtained from https://api.github.com/meta (this is not included in this implementation)

### How to run the web service

#### 1. Requirements

To run the web service, you need to have

* A GitHub organization and a user with role=owner in the organization
* A public IP/url, this allows webhook to reach out to web service
    * If you do not have a server with public IP, you can install and run '[ngrok](https://ngrok.com/)' in local computer
* Installed Docker in your server

#### 2. Create GitHub personal Access token

To access to GihHub APIs you need personal access token (PAT), please refer to [Creating a personal access token](https://docs.github.com/en/github/authenticating-to-github/keeping-your-account-and-data-secure/creating-a-personal-access-token)

#### 3. Configure Webhook + secret

You can create a new webhook under GH organization and point it to web service access url. By default this web service listens to route '/' on port 5000, for instance if you run ngrok the API can be accessed via randomly generated url, here the url I got from ngrok 'https://7dff5d84c1.ngrok.io:5000/' you will get a different url.

#### 4. Configure system environment variables

For keeping sensitive information such as secrets and Github token we store them as environment variables. These variables can be sent when you start a docker container. Here is list of variables:

> 1. FLASK_APP=listener.py (allways value is listener.py)
> 2. USER="your-gh-username"
> 3. WH_SECRET="your webhook secret"
> 4. GH_TOKEN="Your GH personal access token"

#### 5. Docker image

You can pull this docker image **ghcr.io/zettayottaorg/task** from GitHub Container Registry (ghcr.io) which I created before or build it locally. To build a docker image in local computer ,you can clone this repository, navigate to root directory and run following command and replace docker image name with your preferred name. If you create new image please replace 'ghcr.io/zettayottaorg/task with new image name in section #6.

```apache
docker build -t <your-docker-image-name> .
```

#### 6. Run docker image

To start docker image with default configurations, run

```apache
docker run -d \
            -e GH_TOKEN=${GH_TOKEN} \
            -e USER=${USER}  \
            -e WH_SECRET=${WH_SECRET} \
            -p 5000:5000 \
            --name protect_main_branch \
            ghcr.io/zettayottaorg/task
```

If you'd like to customize configurations, you can follow these steps

* Create a new directory called configs and add 2 files
  * config.ini
  * branch_config.json
* You can map local configs directory to /apps/configs in docker container
* To start docker, run

```apache
docker run -d \
            -e GH_TOKEN=${GH_TOKEN} \
            -e USER=${USER}  \
            -e WH_SECRET=${WH_SECRET} \
            -p 5000:5000 \
            -v /tmp/configs:/apps/configs \
            --name protect_main_branch \
            ghcr.io/zettayottaorg/task
```

Sample of config.ini

```apache
[DEFAULT]
api_url = https://api.github.com
```

Sample of branch_config.json

```apache
{
    "required_status_checks": null,
    "enforce_admins": null,
    "required_pull_request_reviews" : {
        "dismissal_restrictions": {},  
        "require_code_owner_reviews": true,
        "dismiss_stale_reviews": false,
        "required_approving_review_count": 1
    },
    "restrictions": null
}
```

## CI/CD

Deployment is done via GitHub actions, the action is triggered by merging a pull request to main branch and it builds and push new docker image to GitHub organization packages.
