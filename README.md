# WeaveGrid File Explorer API

## Description
This repository provides an API to explore the contents of a directory. It is written in python using the FastAPI framework and is served in a docker container.

The `bin` directory provides scripts for setting up the dev environment, starting the application locally (for development), launching and stopping the application in docker.

API documentation is served with Swagger, and is available at `localhost:80/docs` when the application is launched.

## How to Install and Run

*Pre-requirements*
- docker
- python3.7.10 (set by .python-version)
- Clone this repo and cd into the project folder


### How to run
1. `bin/start.sh <root_dir>` will start the application in a docker container, connected to host: 0.0.0.0 port 80. You must pass an absolute directory to `<root_dir>` for the application to set as its target directory
2. Navigate to `localhost:80/docs` to see the API docs and test out the endpoints
3. When done, run `bin/stop.sh` to stop the container


### How to develop
1. `bin/dev-setup.sh` will create, activate and install necessary requirements into a `venv` for local development, if desired
2. `bin/start_local.sh` will start the application in development mode
3. start building


### Running Tests
1. `bin/run_tests.sh` will run the tests in `/tests`. Currently only unit tests are configured, in the future we should build out integration tests
