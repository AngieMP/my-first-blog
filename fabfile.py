from fabric.api import run 
from fabric.context_managers import cd
from fabric.api import env
from fabric.contrib.files import exists


PROJECT_NAME = "myfirstblog"
PROJECT_PATH = f'/home/angela/{PROJECT_NAME}'
REPO_URL = 'https://github.com/AngieMP/my-first-blog.git'
VENV_PYTHON = f'{PROJECT_PATH}/.venv/bin/python'
VENV_PIP = f'{PROJECT_PATH}/.venv/bin/pip'

env.hosts = ['3.15.38.15', '18.217.241.86']

def clone():
    
    print(f"clone: {REPO_URL}...")

    if exists(PROJECT_PATH):
        print("project already exists")
    else:
        run(f"git clone {REPO_URL} {PROJECT_PATH}")


def create_venv():

    print("creating venv...")

    with cd(PROJECT_PATH):
        run("python3 -m venv .venv")


def install_requirements():

    print("installing requirements.txt...")

    with cd(PROJECT_PATH):
        run(f"{VENV_PIP} install -r requirements.txt ")
        
        
def django_makemigrations():

    print("making migrations...")
    
    with cd(PROJECT_PATH):
        run(f"{VENV_PYTHON} manage.py makemigrations")

        
def django_migrate():

    print("executing django migrations...")

    with cd(PROJECT_PATH):
        run(f"{VENV_PYTHON} manage.py migrate ")

        
def django_loaddata():

    print("loading initial data...")

    with cd(PROJECT_PATH):
        run(f"{VENV_PYTHON} manage.py loaddata db.json ")

        
def django_runserver():

    print("runing server...")

    with cd(PROJECT_PATH):
        run(f"{VENV_PYTHON} manage.py runserver")

        
def deploy():
    clone()
    create_venv()
    install_requirements()
    django_makemigrations()
    django_migrate()
    django_loaddata()
    django_runserver()
    
