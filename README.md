# MeetHub + Django Cloud Deployer

This is a [Meethub Project](https://github.com/iyanuashiri/meethub) fork that serves as part of the validation process of the [django-cloud-deployer](https://pypi.org/project/django-cloud-deployer/) plugin package that was developed as a Proof of Concept for a part of my Master's Degree thesis work.

Feel free to [try out the deployment](http://mhub.thesis.ruialves.me/).

## Implemented Changes

- Fixed a multitude of things that were broken in the project
    - Added missing project-required python packages
    - Added missing migrations (initial migration missing in `accounts` model)
    - Added missing database connection configurations to `settings.py`
    - Fixed broken deprecated `whitenoise` configurations
    - Fixed wrong static files path in a set of html templates
    - Fixed wrong account `user` model configurations
    - Added missing `nickname` field to `accounts` model
- Updated project requirements to feature the `django-cloud-deployer` package dependency
- Updated the app's `settings.py` configurations to read information (such as database configurations) from environment variables
- Updated apps url routes with `runInPaaS` and `runInFaaS` annotations

## Cloud Deployment Annotations - System Partitioning

The system's url endpoints were seperated (between PaaS and FaaS) as following:

- Running in PaaS:
    - `comment/*` details routes (content, sub comments, etc)
    - `event/*` participants list routes
    - `password/*` reset and updating routings
- Running in FaaS: Remaining routes

## Replicate this deployment

First, please refer to the [django-cloud-deployer](https://pypi.org/project/django-cloud-deployer/) package documentation.

- Install the requirements with `pip install -r requirements.txt`
- Configure the project:
    - Create a `.env` file with the required environment variables
    - Apply any required migrations with `python manage.py migrate`
- (*Optional*) Check which urls will run in which cloud service with the package's `check_deploy` command, with `python -m django_cloud_deployer check_deploy`
- Deploy the project with `python -m django_cloud_deployer deploy heroku azure`

## Notes and other regards

- A test account under the login email `jay@email.com` and password `jaymeet123`
- The DNS configuration was made manually (it was out of the scope of the validation purposes) and is not part of the package deployment script as of now; However, it may be tackled as future work