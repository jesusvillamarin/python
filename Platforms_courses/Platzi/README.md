<h1 style="color: #00ff93;"> 
    Platzi course
</h1>
Commands on how to create a virtual enviroment to specific project.

It is not always necessary to use the command like this "python -m bla bla.."

<h3 style="color: #00ff93;"> 
    Install Virtualenv
</h3>

Is necessary install virtualenv
> pip install virtualenv

OR

> python -m pip install virtualenv

<h3 style="color: #00ff93;"> 
    Create a virtual envrioment for project
</h3>

> virtualenv venv 

OR
> python -m venv venv

<h3 style="color: #00ff93;"> 
    Activate virtual enviroment on Windows
</h3>

> source .venv/Scripts/activate

<h3 style="color: #00ff93;"> 
    How to view the installed packages
</h3>

> python -m pip freeze

OR

> pip freeze

<h3 style="color: #00ff93;"> 
    Create the requeriments.txt file to manage and install the dependencies
</h3>


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

<h3 style="color: #00ff93;"> 
    Install the dependencies from requeriments.txt file 
</h3>

> python -m pip install -r requeriments.txt

OR

> pip install -r requeriments.txt
