Setup virtualEnv with python3
```shell script
virtualenv -p python3 .venv
```
Activate VirtualEnv
```shell script
source .venv/bin/activate
```
Install Dependancies
```shell script
pip3 install -r requirement.txt
```
Run App with Gunicorn
```shell script
gunicorn --reload uploader.app
```