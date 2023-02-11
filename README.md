# Political Candidate Website

This website has a political candidate theme and includes a blog and a VIP area with login access.

## Description

The website can be used by a political candidate. This website includes:
* home page for candidate overview and email list sign up,
* about page for more detail regarding candidate, candidate mission and what other people say,
* programs page for showing what programs the candidate promotes, 
* blog page for candidate influence,
* vip login area where candidate can provide special value for registered members and
* contact page to communicate with candidate staff.

## Table of Content
1.  Implementing the website in a Django virtual environment.
    - 1.1   Dependencies
    - 1.2   Installing Python3
    - 1.3   Installing Pip
    - 1.4   Installing Django
    - 1.5   Copying Files
    - 1.6   Activate and Run Website
             
2.  Implementing the website in a Docker environment.
    - 2.1   Creating a Docker account
    - 2.2   Preparing Docker Playground
    - 2.3   Copying Files
    - 2.4   Activate and Run Website
  
3.  Authors

### 1.  Implementing the website in a Django virtual environment.

##### 1.1   Dependencies

The Django virtual environment requires the installation of python, pip and django.

##### 1.2   Installing Python3

Download the lates Python version for your system at [Python.org](https://www.python.org/downloads/) and follow the instructions for installation.  Make sure that you
answer yes when you are asked if you want to include Python in the PATH.

##### 1.3   Installing Pip and your virtual environment

Open your command prompt and enter the following commands:

Use the built-in pip module to install PIP.
This is so that you can use pip normally when installing packages.
The command for this is:
```
>python -m pip install pip
```
The next thing is to install the package to enable virtual environments using:
```
>pip install virtualenv
```
There is a wrapper available to enable some handy commands such as mkvirtualenv and workon.
More about these below. 

Use the below command to implement the wrapper for Linux and MacOS.
```
>pip install virtualenvwrapper
```
If you have a windows machine, use the below command to implement the wrapper.
```
>pip install virtualenvwrapper-win
```
Now that we have virtual environments and handy commands set up with the wrapper, 
we can set up the virtual environment. Let’s set up a virtual environment called my_django
using the below command.
```
>mkvirtualenv my_django
```
If this command worked, then you will notice the (my_django) in the beginning of the command line.

When we use the mkvirtualenv command, this creates and activates the virtual environment.
Next time if you have closed the command prompt window, the virtual environment will still 
exist but it will not be activated.

We use the following command to activate only if the virtual environment already exist:
```
>workon my_django
```
Once again remember if this command worked, then you will notice the (my_django) in the beginning of the command line.

Let's now install django in the virtual environment with the following command:
```
>pip install django
```
If we have installed Python correctly, the above should all work.

##### 1.4   Installing Django

Let's now install django in the virtual environment with the following command:
```
>pip install django
```
If Python was installed correctly, the above should all work.

##### 1.5   Copying Files

Go to the directory or folder where you want to install the project and enter the following command in the command line:
```
>git clone https://github.com/riaandeventer/politician-site
```
If you are asked for a login then it should be because you might have made a typing error with the link.

##### 1.6   Activate and Run Website

If your files copied successfully, there should be a folder politician-site when you enter the >dir command.
Go to this directory with below command.
```
>cd politician-site
```
Now we can activate the server with below command:
```
>python manage.py runserver
```
To see the site we need to go to our web browser and enter the following address: [http://localhost:8000](http://localhost:8000/)

### 2.  Implementing the website in a Docker environment.

##### 2.1   Creating a Docker account

##### 2.2   Preparing Docker Playground

##### 2.3   Copying Files

##### 2.4   Activate and Run Website

### 3.  Authors

Riaan Deventer  - [@riaandeventer](https://twitter.com/riaandeventer)
