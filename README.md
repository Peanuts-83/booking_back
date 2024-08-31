[![FastApi](https://img.shields.io/badge/PythonBackEnd-FastApi-info?logo=fastapi&logoColor=white&color=009688)](https://fastapi.tiangolo.com/)
[![Pydantic](https://img.shields.io/badge/DataValidation-Pydantic-info?logo=pydantic&logoColor=white&color=E92063)](https://docs.pydantic.dev/latest/)
[![Uvicorn](https://img.shields.io/badge/ASGIWebServer-Uvicorn-info?logo=gunicorn&logoColor=white&color=499848)](https://www.uvicorn.org/)
[![Starlette](https://img.shields.io/badge/ASGIWebServer-Starlette-info?logo=&logoColor=white&color=4285F5)](https://www.starlette.io/)
[![SQLAlchemy](https://img.shields.io/badge/ORM-SQLAlchemy-info?logo=sqlalchemy&logoColor=white&color=D71F00)](https://docs.pydantic.dev/latest/)
[![MariaDB](https://img.shields.io/badge/Database-MariaDB-info?logo=mariadb&logoColor=white&color=003545)](https://mariadb.org/)


# Booking back-end - FastApi (python)

Back-end part of Booking app project, using FastApi (python). This is an experimental managment application for hotel, with booking, invoice and customer modules.

Communicates with Front-end (angular) and database (mariadb).

Final project should be packed in a Docker public image in order to be displayed in containers anywhere required.

## Setup procedure

*requirements: [pip](https://pypi.org/) & [python](https://www.python.org/downloads/)*

### Install new project from scratch

* Find the right python env for your project. Mine is set up in conda
    * Find the right env : ```conda env list```
    * Activate it : ```conda activate my_env```
* add files :
    * requirements.txt (I prefer **pipreqs** to pip freeze that gets ALL packages in env)
    * environment.yml
    * main.py

```bash
pip install "fastapi[all]" databases aiomysql sqlalchemy
pipreqs .
```

### Install requirements for this project

As development is going on, requirements file is increasing. Please note above install commands are only the less required for startup.

```bash
pip install -r requirements.txt
```

### Setup database

*requirements: [Docker](https://docs.docker.com/get-started/get-docker/)*

You can use bash script file **generator.sh** to create a container based on mariadb:latest Docker image. Just one line to make it come to life, that simple!

```bash
./generator.sh --mariadb
# OR
./generator.sh -m

# mariadb is served at 192.168.168.2:3306
# connect and use password 'myuserpassword' at prompt
mysql -h 192.168.168.2 -u myuser -p
```

Credentials and connection procedure are given at the end of the process. Feel free to update login and password for securizing your database.

I used [mockaroo.com](http://www.mockaroo.com) to fill the database **mydatabase** with tables and mocked data.

*Next coming soon : database already filled with tables and data in a Docker image - working on it!*

* db: mydatabase
* tables:
    * booking
    * comment
    * customer
    * invoice
    * room

## Run project

Navigate to the directory where your main.py file is located (remember python path is done by '.' and not '/') and run:

```bash
uvicorn src.main.main:app --reload
```

**--reload** option is a watch mode that reloads app at each change in the source code.

Once served:

* the app shall be available at: <http://localhost:8000/>
* **OpenApi documentation** (ex-OpenApi) is served at: <http://localhost:8000/docs>
* Redoc documentation is served at: <http://localhost:8000/redoc>

## Debug project

You shall find at root of global project **.vscode/launch.json** convenient configuration file to run vscode debugger - just click Play button in **Run & Debug** menu.
The same file is duplicated at root of this project (back-end part) with path modified, just in case you would work on this side of the project separatly.
