# Api automation Behave + Requests!
## Pre-requisites
We need to install the following tools as part of the pre-requisites to be able to run this demo.
### Tech.
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
### Install [VirtualEnv].
For more deep information about VirtualEnv, click on the link above. But basically the idea with a virtual environment is to have an isolated environment where you can run your proyect with some specific tools versions. It allow us to have more than one environment in a single local machine.

```ssh
pip install virtualenv
```

### Creating a workspace.
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

### Install libraries to be able to run this demo project.
Here we will use pip to install all the required libraries into the active virtual environment.
In this case we have a [requirements.txt] file, that contain all the libraries needed to run this demo project.
```ssh
$ cd api_django_behave_requests     ## Move into the repository folder.
$ pip install -r requirements.txt   ## To install libs into this file.
$ pip freeze                        ## to see the installed libs.
```

### Running the API application.
Into the repository directory, execute the following command to generate the migrations for this demo proyect.
```ssh
$ ./manage.py migrate       ## build the database
$ ./manage.py runserver        ## Run the local server
$ ./manage.py createsuperuser  ## Create a new user ovalerio/admin123 is used on tests
```
Now you van go to your favorite browser and open this url http://127.0.0.1:8000/ 


### Running all the existing test cases from terminal.
Here we are going to use behave to execute all the test cases we have in the repository at this point.

```ssh
$ behave zapi_testing/
```

### References
* https://www.python.org/downloads/
* https://behave.readthedocs.io/en/latest/ 
* http://docs.python-requests.org/en/master/user/quickstart/ 
* http://allure.qatools.ru/


[Python3]: <https://www.python.org/downloads/>
[PIP]: <https://pip.pypa.io/en/stable/installing/>
[VIRTUALENV]: <https://virtualenv.pypa.io/en/latest/>
[BEHAVE]: <https://behave.readthedocs.io/en/latest/>
[REQUESTS]: <http://docs.python-requests.org/en/master/user/quickstart/>
[requirements.txt]: <https://github.com/ovalerio280788/api_django_behave_requests/blob/master/requirements.txt>
