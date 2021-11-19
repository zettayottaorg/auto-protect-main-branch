**PART 1**

This section of the screener will provide you with an opportunity to demonstrate clear written communication, an ability to think through solutions for complex problems, and aptitude in helping **GitHub**’s largest customers scale their software solutions.

You will need to:

* Communicate clearly with customers
* Give expert guidance in the future direction of software delivery for their organization
* Collaborate with teams within **GitHub** to solve customers' problems
* Be able to roll up your sleeves and help the customer deliver on technical initiatives

Please create a [**GitHub** gist](https://gist.github.com/) and paste the questions asked here into the gist in [Markdown format](https://guides.github.com/features/mastering-markdown/). Please add your responses inline under each question. Format the answers so they are easy to read. Your answers should be *your work and ideas* but you are free to use other resources if they are noted at the bottom of the file.

#### **Prompt one**

Company: Acme computers

Version control platform(s): Many **GitHub** Enterprise instances installed throughout the company by different teams. Acme Computers is trying to standardize on **GitHub** Enterprise and consolidate their **GitHub** usage onto a single instance. The company has many instances of other Git hosting solutions installed as well. Some are fully supported applications. Other instances are on machines under people's desks.

**Shrink large repository** :** Acme wants **GitHub** to help them shrink the large repository to a more manageable size that is performant for common Git operations. The large repo is a project that is high visibility with an aggressive roadmap. They request that we help them within the month. It's a large, monolithic repository.

Acme: Consolidate instances: Acme wants you to tell them the best way to move all the other teams, using **GitHub** Enterprise or other Git solutions, onto their consolidated **GitHub** Enterprise instance. They have asked you to give them five or six bullet points about how you would approach that initiative, both technically and culturally.

Customer requests:

* **Shrink large repository:** Acme wants **GitHub** to help them shrink the large repository to a more manageable size that is performant for common Git operations. The large repo is a project that is high visibility with an aggressive roadmap. They request that we help them within the month. It's a large, monolithic repository.

  > For reducing a repository size, we shall make a full repository backup (if we need to undo changes) and clone the main repository into a new one. We will reduce the new repository size and all changes should be properly tested and validated by the owners before pushing them to the main repository or keep new repository as main repository. The main repository needs to be read only during updating process to avoid missing new changes. Here is list of steps to reduce a repository size
  >
  > * **Identify large files**: This can be done by using tools such as git-size
  > * **Remove large files if possible** : These files such as build artifacts, media files and executable files can be removed from repository and copied into a storage. To store files there are multiple options such as GitHub Packages build packages, blob storages  for large files and CDN for media files.
  > * **GIT LFS** : If you'd like to keep some large files, git lfs replaces large files with text pointers while large files are stored in remote servers such as GitHub.com
  > * **Purge untracked files from history**.  This can be done by tools such as git gc.
  > * **Clean repository**: such as removing orphaned branches, removing large files from all commits.
  >
* Consolidate instances: Acme wants you to tell them the best way to move all the other teams, using **GitHub** Enterprise or other Git solutions, onto their consolidated **GitHub** Enterprise instance. They have asked you to give them five or six bullet points about how you would approach that initiative, both technically and culturally.

  > Consolidating all repositories into GH Enterprise instance helps to have better collaboration between teams, end to end security, workflow automation, monitoring. To achieve this, we beside focusing on architectural approach, we focus on collaboration with stakeholders to discuss challenges, roadmaps and solutions. I recommend following steps for consolidation:
  >
  > * **Communicate with all involving teams** to understand their timelines, priorities, repositories, organizations, dependencies and workflows.
  > * **Create a roadmap** and present it to teams.
  > * **Automate migration progress**: Create scripts and automate their executions, this help to repeat same process faster, orchestrate sequence of executions and reuse them for future consolidations.
  > * **Migrating Data**: It is about all data associated with a repository
  >   * Such as users, repositories, organizations, teams, projects, issues and more
  > * **Test migration**: Test each migration
  > * **Trial runs in staging instance** to test changes before migration to the production instance
  > * **Migration from another GH Enterprise**:
  >   * We need administrative access to generate token
  >   * Prepare repositories for export and generate archive file
  >   * Import archive file to target instance and import data
  > * **Migration from GitHub.com or other git repositories** is similar to GH Enterprise by creating git archive file and copy to target server
  >
* Migrate an SVN repo: The customer has one SVN repository that hasn't migrated over to a Git solution. They would like help moving this one large repository over. The team has a trunk based development pattern with this repository and is unfamiliar with Git.

  > Training SVN users during migration will help them to have easier transition to GitHub.
  >
  > * **Migrate SVN to GH Enterprise**:
  >   * Create an empty repository in GH Enterprise service
  >   * Create users and provide right access to new Git repo for SVN users
  >   * Import svn repo to GH Enterprise server using tools such as git-import-svn-raw
  >   * Review imported repo and re-write authors and branches
  >   * Push changes to new GH Enterprise repository
  > * **Team Training**:
  >   * Train team to learn Git workflow, git commands and related tools
  >   * Allow team to use SVN until they are ready to use Git as primart version control.
  >

#### **Prompt two**

Company: Dunder Mifflin Technologies

Version control platform(s): They currently use Gerrit, out-of-the-box Git, Subversion, and Team Foundation Server.

Customer requests:

* Help us modernize our practices: Dunder Mifflin is worried they are falling behind their industry. They have lots of legacy software and development patterns that were created 20 years ago. They have found it incredibly difficult to change any aspect of their SDLC because of their infrastructure, processes, and long-tenured team members who are resistant to change.

> Changing is difficult especially when a pattern or practice has been established and practiced in many years. To make this change easier we can consider migrating repositories to GitHub incrementally in which help teams have time to learn GitHub and adopt Agile methodology. These steps can help us to achieve our goal
>
> * **Defining a Roadmap**: We should identify order of repositories to migrate to GitHub, this will be matched with company's timeline, budget, infrastructure and business goals.
> * **Plan and move repositories based on plan**: Plan and implement moving each repository to GitHub.
> * **Demonstrate what modernization offers**: This help to be on bring more team members on the same page.
> * **Train team members to modernize their skills**: train team members to learn required skills to help them to get up to speed.
> * **Adopt agile methodology**: Work with teams members and managers to learn key concepts of agile and how to implement the agile methodologies in their plannings and implementations for new developments in GitHub repository
> * **Revisiting our approach after each iteration**: Conducting retrospective meetings help us to understand how we did in past iteration and keep up with good part and avoid previous mistakes.
> * **Move toward automation and CI/CD practices**: Automation, Continuous integration and continuous delivery is helping teams to focus on their development with less time spending on deployment and configurations.

* Help us release more often: Dunder Mifflin releases software four times a year. They are shipping largely web-based applications. They want to increase more frequently, but they are unsure of the best first steps. What areas would you explore with the customer to help them move this goal forward?

> Increasing number of releases through the year can be done by reducing number of features in each release, testing automation, continuous integration and continuous delivery which can be done in an agile fashion. We can break down these steps as follow
>
> * **Plan for small releases**: Leaderships can plan to introduce iterative releases with fewer features, this helps to have faster developments, testings and deployments and more releases in each year. They can achieve their milestone with these releases during specified timeline.
> * **Adopting git flow/github flow**: follow branch based workflow for development, pull request and merge to other branches and create releases from merged branch.
> * **Automation**: automating tests, create CI/CD pipeline to automatically execute test and deploy codes to proper environment after branch merges. Plan to deploy to production after deploying and testing code in stage environment.

* Commit/merge/deploy permissions: Dunder Mifflin has expressed concern about moving away from Gerrit. They have asked how they can control repository access, merging, and deployment permissions within **GitHub**, and what aspects of their desired security setup can be enforced programmatically.

> User accesses can be defined as an individual account or can be role based access
>
> * **Levels of access to a repository**: each organization can have owner, member or billing managers account, owners can control other members level of access to each repository such as read, write and admin permissions.
> * **Merging and deploying**: GitHub allows to protect a repository branch by creating protection rule. By applying this rule merging to the branch can include pull request review, requiring status checks to pass before merge to the protected branch
> * **Enforce security programmatically**: Only an authenticated user can access to GitHub API, there are 2 available authentication methods: 1. Personal access token (PAT) 2. Oauth token for apps: an admin user can revoke or limit access to a third party app.

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

## Answer

Please refer to: [auto-protect-main-branch](https://github.com/zettayottaorg/auto-protect-main-branch)
GitHub Organization: [https://github.com/zettayottaorg](https://github.com/zettayottaorg)

## References Part 1 and 2

* [GitHub Docs](https://docs.github.com/en)
* [GitHub Blog - Measuring the many sizes of a Git repository](https://github.blog/2018-03-05-measuring-the-many-sizes-of-a-git-repository/)
* [git-sizer](https://github.com/github/git-sizer/)
* [From Gerrit to Github](https://medium.com/compass-true-north/from-gerrit-to-github-cebc463ec01b)
* [Flask Projects](https://flask.palletsprojects.com/en/2.0.x/)
* [git-scm](https://git-scm.com/)
