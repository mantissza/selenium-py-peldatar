##Windows

Docker infos (without WSL 2 !)

1.) docker run -d nginx

2.) docker-compose up   (docker-compose.yml file mappájában futtatni)

3.) Open in browser || http://localhost:9999/

Note: (Ha vacak a géped) Dockert érdemes legelőször elindítani, ugyanis a chrome és pycharm könnyen megeszi előle a memóriát. Amikor sikeresen felállt a Docker a gépen, akkor kell ráereszteni a gépre minden egyéb memóriafalót.

*) pip install webdriver_manager OR pip3 install webdrivermanager
*) pip install -U pytest
*) pip freeze > requirements.txt

---

1. Navigate to: File->Settings->Project: [project name] -> Project Interpreter

2. On this page click the configuration wheel at the top which should provide a drop down menu. Click "Add" and a window should appear called "Add Python Interpreter"

3. You will be defaulted onto "Virtualenv Environment" tab.

4. There should be a checkbox called "Inherit global site-packages". Check this.

5. Click OK.

6. All your installed packages should be added.


---

##Linux:

sudo apt update

sudo apt-get update

sudo apt install docker.io

sudo docker version

sudo docker run nginx

sudo docker search nginx

docker-compose

sudo apt install docker-compose

docker-compose --help


sudo docker run nginx

docker-compose up



sudo docker container ls


??? -- sudo apt-get install docker-ce docker-ce-cli containerd.io
??? -- sudo apt-get install apt-transport-https ca-certificates curl gnupg-agent software-properties-common

---
Error message:

E: Could not get lock /var/lib/dpkg/lock - open (11: Resource temporarily unavailable)

E: Unable to lock the administration directory (/var/lib/dpkg/), is another process using it?

Solution:

sudo rm /var/cache/apt/archives/lock

sudo rm /var/lib/dpkg/lock