[![Maintainability](https://api.codeclimate.com/v1/badges/6e8511dbcf29b1cee00a/maintainability)](https://codeclimate.com/github/frankopkusianwar/iReporter/maintainability) [![Build Status](https://travis-ci.org/frankopkusianwar/iReporter.svg?branch=develop)](https://travis-ci.org/frankopkusianwar/iReporter) [![Coverage Status](https://coveralls.io/repos/github/frankopkusianwar/iReporter/badge.svg?branch=develop)](https://coveralls.io/github/frankopkusianwar/iReporter?branch=develop)

# iReporter 
iReporter enables any/every citizen to bring any form of corruption to the notice of appropriate authorities and the general public. Users can also report on things that needs government intervention

# User Interface
The user  interface contains pages that allow the user to interact with the system
## Getting started
clone the project to your computer and improve on it
- https://github.com/frankopkusianwar/iReporter.git
## Project link
- https://github.com/frankopkusianwar/iReporter/tree/develop
## gh-pages link
- https://frankopkusianwar.github.io/iReporter/UI
## How to login
- As a USER username: user and password: user
- As an ADMIN username: admin and password: admin
## Required features
- Users can create an account and log in.
- Users can create a red-flag record (An incident linked to corruption).
- Users can create intervention record (a call for a government agency to intervene e.g repair bad road sections, collapsed bridges, flooding e.t.c).
- Users can edit their red-flag or intervention records.
- Users can delete their red-flag or intervention records.
- Users can add geolocation (Lat Long Coordinates) to their red-flag or intervention records.
- Users can change the geolocation (Lat Long Coordinates) attached to their red-flag or intervention records.
- Admin can change the status of a record to either under investigation, rejected (in the event of a false claim) or resolved (in the event that the claim has been investigated and resolved).
## Built with
- html5
- css3
## prerequisites
- An editor of your choice
- Web browser with suport for html5
- Internet connection

# API
## Requirements
- python 3.7 -programming language that can be used on any mordern operating system
- Virtual environment -allows you to have an issolated evnvironment for your project where you can install all your dependencies
- Flask -a python framework for that can be used to add functionality to your API endpoints
## Heroku Link
- https://ireporterapp.herokuapp.com/api/v1/red-flags
## Installation
Clone the repository
```
$ https://github.com/frankopkusianwar/iReporter.git
$ cd iReporter
```
Install virtualenv and create a virtual envirinment
```
$ pip install virtualenv
$ pip install virtualenvwrapper
$ virtualenv venv
$ source/venv/bin/activate
```
Install all the necessary dependencies
```
pip install -r requirements.txt
```

## Run the application
At the terminal or console type
```
python run.py
```
To run tests run this command at the console/terminal and add the test file name
```
pytest filename
```
## Versioning
```
This API is versioned using url versioning starting, with the letter 'v'
This is version one"v1" of the API
```

## Authors
- Okiror Frank
## licencing
This app is open source and therefore is free to all users
