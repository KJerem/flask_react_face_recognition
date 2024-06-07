# E-COURSE - Project

---

## Descriptions:
This is a course project where we are building a full stack web application using MySQL as database, React.js as Frontend, and Flask as Backend. In this project, a person can login via face recognition and after logging in, you can see a personal timetable, the classes scheduled in the coming one hour, and course details.

# Setup Details:

## Backend Setup:

For Backend, first enter the backend director and create a data directory if it doesn't already exist:

```terminal/cmd
cd backend
mkdir data
```

### *Now Let's setup the face recognition system:*

### Setting Environment

Create virtual environment in windows.
```
python3 -m venv venv

./venv/Scripts/activate

pip install -r requirements.txt
```

or Create virtual environment in linux.

```
python3 -m venv venv

source ./venv/bin/activate

pip install -r requirements.txt
```

### MySQL Install

[Mac] https://dev.mysql.com/doc/mysql-osx-excerpt/5.7/en/osx-installation-pkg.html

[Ubuntu] https://dev.mysql.com/doc/mysql-linuxunix-excerpt/5.7/en/linux-installation.html

[Windows] https://dev.mysql.com/downloads/installer/

*******

#### To Collect Face Data

```
"""
user_name = "Jack"   # the name
NUM_IMGS = 400       # the number of saved images
"""
python face_capture.py
```
The camera will be activated and the captured images will be stored in `data/Jack` folder.      
**Note:** Only one person’s images can be captured at a time.

#### Now Train a Face Recognition Model
```
python train.py
```
`train.yml` and `labels.pickle` will be created at the current folder.


#### Now Let's Check If The Is Trained Correctly:
Go to either faces_gui.py or faces_.py and run the following the command:

```terminal/cmd
python faces.py
```
The camera will be activated and recognize your face using the pretrained model. 
If output is like `('Hello ', {name}, 'You did attendance today')` then the face is trained correctly.

#### Importing Database

Open mysql server and import the file `RealFinal.sql`.

```
# login the mysql command
mysql -u root -p

# create database.  'mysql>' indicates we are now in the mysql command line

# import from sql file. Replace the filename `RealFinal.sql` with the path to RealFinal.sql file on your local system
mysql> source RealFinal.sql
```

## Finally Running the Backend:
Go into jamm-backend  directory and run main.py
```terminal/cmd
python main.py
```

# Settting Up The Frontend:

Firstly, change the directory to `frontend` then run following command:
```terminal/cmd
npm install
```

Then run the following command:
```terminal/cmd
npm start
```

# Important Note:
 While running, if some of the libraries are missing, do install them via `pip install {library-name}` or `npm install {library-name}`.


Thank you for reading. Enjoy the app! Stay happy and stay safe :)
