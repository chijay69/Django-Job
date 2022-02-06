Instructions for using this application

Uncompress the files if compressed.
Create a postgres database
Edit the settings.py file in the project root directory i.e $PREFIX/Job/Job to connect your database to your project
Install your requirements from requirements.txt
Run migrations then makemigration (app_name) eg. makemigrations hack
Now your app should be setup
start your postgres server use psql db_name to confirm database is runing
Run the runserver command to start django server

Note: if app scheduler is fucking up just goto apps.py file in the app directory eg Job/hack/apps.py and comment the function under the class

Then go to project/app/ directory eg Job/hack/. And run the Job2.py file i.e python Job2.py to get api data and write to data.json file
Run populate.py directory to populate database with retrieved data from data.json

MVT Model View Template is complete
