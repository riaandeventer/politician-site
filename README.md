# Political Candidate Website

This website is for a political candidate and includes a projects, blog and a VIP area with login access.

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
    - 2.1   Creating a Docker Hub account
    - 2.2   Prepare the Docker Environment
    - 2.3   Copying Files and Publishing the Site to Docker Hub
    - 2.4   Activate and Run Website
  
3.  Sphinx documentation
 
4.  Authors

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

##### 2.1   Creating a Docker Hub Account

Go to [https://hub.docker.com/](https://hub.docker.com/) and create a docker account.

##### 2.2   Prepare the Docker Environment

To publish to Docker Hub, we have 2 options. Firstly we can install Docker Desktop if your machine meet the system requirements or we can 
use Docker Playground that gives us an online virtual space where we can test Docker Containers.

**For installing Docker Desktop**, go to [https://www.docker.com/products/docker-desktop](https://www.docker.com/products/docker-desktop).

Open a command prompt and enter the following command to test if Docker Desktop was installed successfully:
```
>docker run hello-world
```
It will do some downloads and, finally, you’ll see output starting with “Hello from Docker!”.

**For using the Docker Playground**, go to [https://labs.play-with-docker.com/](https://labs.play-with-docker.com/) and log in with your 
https://hub.docker.com/ docker account that you created in step 2.1 .

After logging in with Docker Playground, click “Start”. The playground has a 4-hour time limit, 
after which everything you did there will be deleted.

After clicking “Start” you’ll be able to create an instance.

##### 2.3   Copying Files and Publishing the Site to Docker Hub

Regardless if you are now in the desktop command prompt or the docker playground instance, run the following commands:

Copy the required files.
```
>git clone https://github.com/riaandeventer/politician-site
```
If you are asked for a login then it should be because you might have made a typing error with the link.

First we have to go into the folder that was created from the clone.
```
>cd politician-site
```
Now we have to build the site with following commands:
```
>docker build -t politician-site ./
```
Now we need to connect the build name with the docker hub repository that we want to create.
We will do this with the below command.
```
>docker tag politician-site [docker hub username without square brackets]/politician-site
```
Now we need to copy our build to our docker hub. We need to use the push command from the command prompt
or the playground prompt (Which ever one we are using).
To be able to push to docker hub, we need access to docker hub from the command line. Let's use the following commands:
```
>docker login
```
You will be asked for your docker hub username and password. Enter these and lookout for the login succeeded message.
If the login was successful, let's push our build to docker hub with the following command:
```
>docker push [docker hub username without square brackets]/politician-site
```
We have now created our project on docker hub. Go to Docker Hub and confirm that there is now a politician-site repository
indicating that a push took place.

If you have been working with Docker Desktop, we are no done with Docker Desktop and will complete the rest with Docker Playground.

##### 2.4   Activate and Run Website

Just a reminder **if you have been working with Docker Desktop**, go to [https://labs.play-with-docker.com/](https://labs.play-with-docker.com/)
to test the site. Login with your Docker Hub account if you are not already logged in. Then click “Start”, and on the next screen
click “add new instance”.

**If you have used Docker Playground for Copying Files and Publishing the site to Docker Hub** then you can just continue with the following commands:

```
>docker run --publish 8000:8000 [docker hub username without square brackets]/politician-site
```
Docker on the VM will download your image from Docker Hub and do all the relevant preparations and installation to make your app work.

When the run command is done, you should see a button with the number “8000” next to “OPEN PORT” at the top of the webpage. 
Click on it to visit that VM’s exposed port 8000. You should see your website now running completely on its own
in the world wide web.

### 3.  Sphinx Documentation

For further documentation on the python modules, visit [Sphinx Documentation](./docs/_build/html/index.html).

### 4.  Authors

Riaan Deventer  - [LinkedIn: @riaandeventer](https://www.linkedin.com/in/riaandeventer/)
