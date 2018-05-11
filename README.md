# PrismWebsite
```
apt install libpq-dev
pip3 install django
pip3 install psycopg2
```
- Create a database named `prism_certification`
- Copy db_conf.py.example to db_conf.py and same for app_conf.py.example
- Fill the configurations as desired, but be careful not to commit your own configs
```
python3 manage.py makemigrations
python3 manage.py migrate
```
Run the server with
```
python3 manage.py runserver
```