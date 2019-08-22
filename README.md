# Go-Team-203-Website
For our project website

# Windows
### Install
- https://www.python.org/downloads/
- https://gitforwindows.org/

### Restart computer

### Install server run 
- Start_Install_Django_Server.bat

### Run server
- Start_Django_Server.bat



# Mac
### Install
- https://www.python.org/downloads/mac-osx/
- https://sourceforge.net/projects/git-osx-installer/files/

### Restart computer

### Open a terminal and run 
- $ xcode-select --install
- /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
- $ brew install python3
- sudo easy_install pip

### You need to CD into to server folder
- cd <server path>

### Install
- sudo pip install -r requirements.txt

### Make sure the DB is up to date
- sudo python3 manage.py makemigrations
- sudo python3 manage.py migrate

### Create a user if you need it
- sudo python3 manage.py createsuperuser

### Run server
- cd <server path>
- sudo python3 manage.py runserver
- http://127.0.0.1:8000/

# Mac Git commands
### clone
- $ git clone https://github.com/Callum-Bartle-92019337/Go-Team-203-Website.git 

### Pull
```$ git fetch --all```
```$ git pull origin master```

### Push
- $ git add .
- $ git commit -m "<Commit message here>"
- $ git push