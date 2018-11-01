# Api automation Behave + Requests!
## Pre-requisites
We need to install the following tools as part or the pre-requisites to be able to run this demo.
### Tech
* [Python3] -- Python is a programming language that lets you work more quickly and integrate your systems more effectively.
    * Check the python version in this way, i.e
        ```ssh 
        $ python3.x -V
        Python 3.7.0
        ```  
* [Pip] -- pip is a package management system used to install and manage software packages written in Python.
    * Check the pip version in this way, i.e 
        ```ssh 
        $ pip --version
        pip 18.1 from /Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/pip (python 3.7)
        ```     
### Install [VirtualEnv]
For more deep information about VirtualEnv, click on the link above. But basically the idea with a virtual environment is to have an isolated environment where you can run your proyect with some specific tools versions. It allow us to have more than one environment in a single local machine.

```ssh
pip install virtualenv
```

### Creating a workspace
Lets create a new folder to start working and creating our local working environment.
```sh
$ mkdir ~/demo_workspace            ## create a new folder in your favourite path
$ cd ~/demo_workspace               ## move to the new workspace
$ virtualenv -p python3.7 api_demo  ## Create a new virtualenv
$ cd api_demo                       ## go into the virtualenv folder
$ source bin/activate               ## active the virtualenv
```

### Clone this project
In this step we are going to clone the code from this repository.
```ssh
$ git clone https://github.com/ovalerio280788/api_django_behave_requests.git
```

At this point we will have something like this in the virtualenv directory:
```ssh
api_django_behave_requests	bin				include				lib				pip-selfcheck.json
```

### Install libraries for [Behave] and [Requests]
Here we will use pip to install all the required libraries into the active virtual environment.
In this case we have a requirements.txt file, that contain all the libraries needed to run this demo project.
```ssh
$ cd api_django_behave_requests
$ pip install -r requirements.txt
```



[Python3]: <https://www.python.org/downloads/>
[PIP]: <https://pip.pypa.io/en/stable/installing/>
[VIRTUALENV]: <https://virtualenv.pypa.io/en/latest/>
[BEHAVE]: <https://behave.readthedocs.io/en/latest/>
[REQUESTS]: <>
