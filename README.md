# Sistemas Inteligentes - Backend Repo

Project made using Python 3 and MySQL.

### Some necessary tools you will need to run this project

  - Python 3
  - pip
  - Flask

## Configuring the project in order to be able to run it on your computer

After cloning this repository, follow the instructions below.

### Linux

This process has been tested on Linux Mint 19.3.

Install pip in case you have not installed it yet. In Debian/Ubuntu derived distros, you will also need a package named python3-venv in order to be able to create virtual environments.

```sh
$ sudo apt update
$ sudo apt install python-pip
$ sudo apt install python3-pip
$ sudo apt install python3-venv #Run it if you are in Debian/Ubuntu
```
Once the installation is complete, verify the installation by checking the pip version:
```sh
$ pip --version
$ pip3 --version
```

Now we are going to create a virtual environment inside the project folder
***Note***: *I recommend naming yout virtual environment as "si-project-back" because the command for creating a virtual environment creates a new folder with the same name as the virtual environment. That folder **should not** be included on the git repository, so I already added that folder name to the .gitignore file. If you want to give a different name to your virtual environment and want to commit changes to this repo, make sure to add it to the .gitignore file.*

```sh
$ cd si-project-back
$ python3 -m venv environment_name
```

Next, you need to activate the environment you just created. You can activate the virtual environment using the following command

```sh
$ source environment_name/bin/activate
```

Now that you have activated the virtual environment, you will need to install all the dependencies of the project. To achieve this, there is a file in this repo called "requirements.txt", which haves the name of all the dependencies that this project uses (similar to Node js package.json file). In order to install all the project dependencies in your virtual environment, you will run the following command, which works similar as when you run "npm install" on a cloned repo.

```sh
$ pip install -r requirements.txt 
```

### New Libraries

Installing new libraries on your virtual environment is done with the pip command. After installing something, please run the following command

```sh
$ pip freeze > requirements.txt
```

This is done in order to save the new required libraries on the requirements.txt file.

And we are done. If you want to close the virtual environment, use the following command

```sh
$ deactivate
```

## Running the project

Now that you finished configuring the virtual environment and installed all dependencies (listed on requirements.txt), you are able to run this project.
In order to run this project, run the following commands.

```sh
$ cd si-project-back #go to the project directory folder
$ source environment_name/bin/activate #open the virtual environment
$ python3 app.py #run the project
```

And that's all! The server will start listening on port 5000.
The file "app.py" is the one that has all the endpoints of the REST Api.

Fun fact: if you open the project directory with Visual Studio Code, the VS Code terminal will automatically start running the virtual environment, in that way you won't have to activate and deactivate the virtual environment manually.