# SW installation
## Virtual folder with python3
python3 -m venv .venv
- Activarlo:
source .venv/bin/activate
- desactivarlo
deactivate

# Python3
- apt-get install -y python3.6
- apt install -y python3-pip

## Cocotb
- pip install cocotb
- pip install edalize
- pip install cocotb-test
- pip install cocotb-coverage
- sudo apt install python-pytest

## Gtkwave
- sudo apt-get update -y
- sudo apt-get install -y gtkwave

## Aditional tools
- sudo apt update
- sudo apt install -y git make gnat zlib1g-dev

## GHDL
- git clone https://github.com/ghdl/ghdl
- cd ghdl
- ./configure --prefix=/usr/local
- make
- sudo make install
- echo "$0: All done!"

## Icarus
- sudo apt install iverilog

## LCOV y gcc
- sudo apt-get update -y
- sudo apt-get install -y lcov
- install gcc

## Numpy
- pip3 install numpy
- sudo apt-get install python3-matplotlib
- python -m pip install -U matplotlib


# GITLAB RUNNER:(activarlo)
- wget https://gitlab-runner-downloads.s3.amazonaws.com/master/deb/gitlab-runner_amd64.deb
- sudo dpkg -i gitlab-runner_amd64.deb
- sudo gitlab-runner run

## Register a new runner:
- sudo gitlab-runner register
https://docs.gitlab.com/runner/register/

## Activate gitlab runner
- sudo gitlab-runner run

## Configuration TOML:
If the doccker image is not in docker hub, we have to addd into toml: pull policy = "if-not-present"
Route: /etc/gitlab-runner/config

# Docker
## Create a docker image:
Open a terminal in the dockerfile route and enter: docker build -t cocotb:1.0.1 .

## Create a docker container from a docker image:
docker run -i -v /home/sergioasn/repo/:/home/ -t name:1.0.0 /bin/bash

It copies the route folder into the route docker, then a docker name with version,
it will open command line with bash

## Delete a docker image:
- docker rmi y el Id de la imagen --force
- docker rm ID_name removes docker image

### CAUTION!! if we want to set python3 by default:
- update-alternatives --install /usr/bin/python python /usr/bin/python3.6 10

# Nexus server
- cd opt
- mkdir /install_dir
- Download from sanatype web
- Extract: tar xvzf nexus-<version>.<tar file extension>
- navigate till nexus-<version>/bin/
- run the server: ./nexus run

## Registry a new server
Elegir el npm host para publicar codigo privado
Si añadimos primero el user nos crea automáticamente el .npmrc
añadir el registro del .npmrc:
registry=http://your-host:8081/repository/npm-group/
_auth=YWRtaW46YWRtaW4xMjM= es validad para admin/admin123
si queremos otra para nuestra cuenta escribir en la terminal:
echo -n 'myuser:mypassword' | openssl base64
esa sera nuestro token que cambiaremos por el anteror de admin

añadir usser:
npm adduser --registry=http://10.20.100.245:8081/repository/verilog_probe/ --always-auth

Esto genera un archivo en el home del user con las claves para publicar

importante en nexus3 ir a Security y Realms y añadir el siguiente realm
npm Bearer Token Realm

### Additional comments
How to run makefile with pytest
hoy to run : SIM=icarus pytest -s cocotest_adder_test.py
