# DJANGO TODOLIST

This is a simple todo list project with django!

### Get started!

<small>Step by Step guide to run Django Todo list</small>

#### Step 01:

Clone the repo [here](https://github.com/AleejandroReyna/django-todolist).

#### Step 02:

Clone the submodules. [Guide here](https://git-scm.com/book/en/v2/Git-Tools-Submodules)

#### Step 03:

Give me a star on [Github ](https://github.com/AleejandroReyna/django-todolist).

### With Docker Compose (Recommended method)

#### Step 04:

Install [Docker](https://docs.docker.com/engine/install/)

#### Step 05: 

Copy `.env.example` and rename to `.env`

#### Step 06:

Set values for .env file (Instructions in file)

#### Final Step: 

Run `docker-compose up` and that's all!

### Manual Installation

#### Step 04:

Install [Python](https://www.python.org/downloads/) and [VirtualEnv](https://virtualenv.pypa.io/en/latest/) for run this project.

#### Step 05:

Generate virtualenv for project using `python3 -venv ./venv`

#### Step 06:

Activate virtualenv for project. (`source venv/bin/activate` on linux or macOS, `.\venv\Scripts\activate` on Windows.)

#### Step 07:

Install the dependencies in `requirements.txt`

#### Step 08:

Define environment variables described in .env.example in your environment. (You can use `export MY_VARIABLE=my_value` on linux and macOS, `set MY_VARIABLE=my_value` with CMD and `$env:MY_VARIABLE=my_value` with Powershell).

#### Step 09:

Run the command: `python manage.py migrate`

#### Final Step:

That's all! Run the command `python manage.py runserver`