# OPENDATA - Backend

## Requirements

- Python 3.9
- Django 3.2
- GDAL 2.2.3
- Postgres 12
- Virtual Enviroment

## RUN

First, clone the repository:

```shell
git clone https://github.com/saraivaufc/opendata-backend
```

After, you need to create your virtual enviroment. You can create using Virtualenv (apt install virtualenv):

```shell
virtualenv env -p python3.9
source env/bin/activate
```

### Install PostgreSQL and PostGIS

```shell
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
echo "deb http://apt.postgresql.org/pub/repos/apt/ `lsb_release -cs`-pgdg main" |sudo tee  /etc/apt/sources.list.d/pgdg.list
sudo apt update
sudo apt -y install postgresql-12 postgresql-client-12
```

### Install unrar

```shell
sudo apt install unrar
```

Inside the project directory, run the command to install the env requirements:

```shell
pip3 install -r requirements.txt
```

### Install GDAL development libraries:

Go to the root directory of this project locate gdal.sh and execute it with sudoer permission.

```shell
sudo apt-get update -y
sudo apt-get install -y libgdal-dev python3-dev gdal-bin python3-gdal
pip3 install GDAL==$(gdal-config --version) --global-option=build_ext --global-option="-I/usr/include/gdal"
```

Inside the coamo folder create a new file called _local_settings.py_:

```shell
touch opendata/local_settings.py
```

Inside the file _local_settings.py_ configure your database, bellow is a template:

```python
DEBUG = True

SECRET_KEY = 'adasdn(xs2dc+5(v-z0(j_-5'

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'opendata',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'localhost',
    }
}
```

Create databases:

```
psql -U postgres -W -h localhost

CREATE DATABASE "coamo-rastreabilidade";
```

Run the migrations :

```shell
#python3 manage.py makemigrations data
python3 manage.py migrate
```

Create your Django User:

```shell
python3 manage.py createsuperuser
username: <YOUR_USERNAME>
password: <YOUR_PASSWORD>
```

Run the server:

```shell
python3 manage.py runserver
```

#### Install and initialize rabbitmq

```
sudo apt-get install rabbitmq-server
sudo /etc/init.d/rabbitmq-server start
sudo rabbitmq-plugins enable rabbitmq_management
sudo rabbitmqctl add_user admin @dmin123
sudo rabbitmqctl set_user_tags admin administrator
firefox http://localhost:15672/
```

Configure Celery Logs:

```shell
sudo mkdir /var/log/opendata && sudo chmod 777 /var/log/opendata
```

Execute the Celery:

```shell
bash worker.sh
```

If you get the error :

```shell
Cannot connect to amqp://guest:**@127.0.0.1:5672//: Server unexpectedly closed connection.
```

It can be related to IPv6, so, you can uncomment line "#NODE_IP_ADDRESS=127.0.0.1" in the conf file:

```shell
sudo vi /etc/rabbitmq/rabbitmq-env.conf
```

Use the Celery Flower to manage tasks and workers

```shell
flower -A opendata.celery --port=5555
```