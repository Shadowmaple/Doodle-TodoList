# Doodle-TodoList

### Environment

#### env variables

```shell
export TODO_LIST_DB_URL=mysql+pymysql://root:root@localhost:3306/todolist
export TODO_LIST_SECRET_KEY='my todo list secret key'
```

#### virtual env

```shell script
python3 -m venv venv
source ./venv/bin/activate
```

#### plugins

```shell script
pip3 install -r requirements
```

### Database

```shell script
mysql -h 127.0.0.1 -P 3306 -uroot -proot -D todolist < db.sql
```

### Run

```shell script
python3 run.py

# or
chmod +x run.py
./run.py
```

Open url on http://127.0.0.1:3300/
