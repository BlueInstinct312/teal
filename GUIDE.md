# Refresher Guide
-------------------Git
git init
git add *
git commit -m "message"
git branch -M main
git remote add origin https://github.com/BlueInstinct312/dev2-tourCompany.git
git push -u origin main

-------------------Virtual Env
### 1. Create a virtual environment named ".venv"
python -m venv .venv

### 2. Activate the virtual environment
source .venv/Scripts/activate

### 3. Upgrade pip and install your packages (example: requests)
pip install --upgrade pip
pip install requests

### 4. Deactivate the environment when you are done
deactivate

-------------------FAST API
## To start a server
uvicorn main:app --port 80 --reload

## Example post/get command
curl -X POST -H "Content-Type: application/json" 'http://127.0.0.1:80/items?item=apple'
curl -X GET 'http://127.0.0.1:80/items/0'
curl -X POST -H "Content-Type: application/json" -d '{"text":"apple"}' 'http://127.0.0.1:80/items'

## Docs URL
127.0.0.1:80/docs

-------------------Docker 

docker pull mysql
docker images 
docker run --name mysql-db -e MYSQL_ROOT_PASSWORD=password1234! -p 3333:3306 -d mysql:tag
docker ps
## Get the name of the Container id running (391ec1829e7f in my case)
docker exec -it 391ec1829e7f sh
docker stop 391ec1829e7f

## Extra Exploratory on machine
mysql -p
SHOW DATABASES;
CREATE DATABASE TealDB;
USE TealDB;
SHOW TABLES;

-------------------Jupyter Notebook 

python -m ipykernel install --user --name=.venv --display-name "Python (.venv)"

-------------------Visual Studio Code
Multi-cursor editing (CTRL + ALT + UP/DOWN Arrow)

-------------------LLama
ollama run llama3.2

