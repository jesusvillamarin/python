# Platzi course

How create an virtual enviroment to project.

#### Install Virtualenv

Is necessary install virtualenv
> pip install virtualenv

OR

> python -m pip install virtualenv

#### Create a virtual envrioment for project

> python -m venv .venv

OR

> venv .venv

#### Activate virtual enviroment on Windows
> source .venv/Scripts/activate

#### How to view the installed packages
> python -m pip freeze

OR

> pip freeze


#### Create the requeriments.txt file to manage and install the dependencies

The requeriments.txt file must have content like the following
```txt
numpy==1.18.0
Click==7.0
Flask==1.1.1
itsdangerous==1.1.0
Jinja2==2.10.3
MarkupSafe==1.1.1
numpy==1.18.0
Werkzeug==0.16.0
...
```

#### Install the dependencies from requeriments.txt file 

> python -m pip install -r requeriments.txt

OR

> pip install -r requeriments.txt
