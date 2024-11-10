# ivis

A DRF API to visualize D3 charts for authenticated usersor through the web interface. The application registers and authenticates users. The chart data is accessible through the API endpoint, `{{ hostname}}/api/data` or on the web application just after login.

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

License: MIT

## Settings

Moved to [settings](https://cookiecutter-django.readthedocs.io/en/latest/1-getting-started/settings.html).

## Basic Commands

### Setting Up Your Users

- To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

- To create a **superuser account**, use this command:

      $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

### Type checks

Running type checks with mypy:

    $ mypy ivis

### Test coverage

To run the tests, check your test coverage, and generate an HTML coverage report:

    $ coverage run -m pytest
    $ coverage html
    $ open htmlcov/index.html

#### Running tests with pytest

    $ pytest

### Live reloading and Sass CSS compilation

Moved to [Live reloading and SASS compilation](https://cookiecutter-django.readthedocs.io/en/latest/2-local-development/developing-locally.html#using-webpack-or-gulp).

## Deployment

The following details how to deploy this application.

It is important to replace the following environment variables in the `DJANGO_ADMIN_URL`, `DJANGO_SECRET_KEY`, `DJANGO_SETTINGS_MODULE`, `DJANGO_ADMIN_URL`, `DJANGO_ALLOWED_HOSTS`, `DJANGO_SERVER_EMAIL`, `SENDGRID_API_KEY`, `SENDGRID_GENERATE_MESSAGE_ID`, `SENDGRID_MERGE_FIELD_FORMAT`, `SENDGRID_API_URL`, `DJANGO_ACCOUNT_ALLOW_REGISTRATION`, `WEB_CONCURRENCY`, and `REDIS_URL` with appropriate values for security and enabling user registration emails.

The application is designed to run in a containerised environment, in a single click, `podman-compose -f docker-compose.production.yml up` or `docker-compose -f docker-compose.production.yml up` (depending on your tools) with the correct environment variables, get's the application up and running. The environment variables should be located in  a file named `.envs/.production/.django` on the project's root directory. Additionally, variables to run a postgres container should be stored in this file`.envs/.production/.postgres` on the project root directory. The environment variables for postgres are: POSTGRES_HOST=postgres
`POSTGRES_PORT`, `POSTGRES_DB`, `POSTGRES_USER`, and `POSTGRES_PASSWORD`.

The traefik container needs access to a privileged port (<=1024), in order to expose the API on port 80 (http) and 443 (https) using self signed SSL certificates.

To tear down the application run, `podman-compose -f docker-compose.production.yml up` or `docker-compose -f docker-compose.production.yml up` again this depends on the tools at your disposal, ideally podman or docker.

### Docker

See detailed [cookiecutter-django Docker documentation](https://cookiecutter-django.readthedocs.io/en/latest/3-deployment/deployment-with-docker.html).

### SetUp
A fresh DJANGO_SECRET_KEY value can be generated using ```code python3 -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())' ```. A SENDGRID_API_KEY and SENDGRID_API_URL should be gotten from the sendgrid console.
