# WoG Project
## DevOps Project

WoG(World of Games) project is a project for self learn and parctice purposes only.
The project includes work with the following Technologies:

- Python - Flask, Tkinter, Requests(API Calls)
- Docker
- MySql Database
- AWS - RDS, EC2 , ALB
- Jenkins (Not finished) - Creating pipeline for image build, running and testing
- K8s (Not Finished) - Creation of K8s Objects
## Games - MainGame.py


The Application running on Client (Windows OS) side.

* Every game has different difficulty levels between 1-5.
* The score is calcualted based on the difficulty levels
### Games:
- Memory Game -  Random numbers will appear for 0.8 seconds the user should memorize these numbers(Tkinter based)
- Guess Game - The user need to guess a number the app choosed
- Currency Roullette - The App generates a amount in $(US Dollar) the user need to type the amount in ILS based on current currency  


## Flask Server - MainScores.py

The Server side based on Flask App that receives HTTP GET\POST and performing
Read\Write actions on the MySQL Database.

The Flask Server is running on Docker container in AWS EC2 instance and connects to MySQL Database(RDS)
the Application requires the following Enviroment variables:
- DB_USER (default-root)
- DB_PASSWORD (default-root)
- DB_HOST (default-localhost)
- DB_DATABASE (default-flaskdb)

## Installation
- Make sure MySQL DB is up and running
- Run the Server Side before
### Server 

Clone the Repository

```sh
$ git clone https://github.com/orderzi/Py_Project.git
```
Run the Application
- use Docker\K8s ConfigMaps and Secrets in Enviroment variables

```sh
$ docker run -d -p 80:5001 -e DB_HOST='db_address' \
-e DB_PASSWORD='db_password' \
--name WoG_App derzi\flaskapp
```

### Client (Windows only)
Clone the repository
```sh
git clone https://github.com/orderzi/Py_Project.git
```
Install the dependencies
```sh
pip install requirements.txt
```
Start the game
```sh
python Main_Game.py
```
