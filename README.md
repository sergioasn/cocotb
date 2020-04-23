# Dependencies

## cocotb
adder_sample



hoy to run : SIM=icarus pytest -s cocotest_adder_test.py

# install gtkwave:
sudo apt-get update -y
sudo apt-get install -y gtkwave


# Install cocotb:
pip install cocotb
pip install edalize
pip install cocotb-test
pip install cocotb-coverage
sudo apt install python-pytest

# instalar python3
apt-get install -y python3.6
apt install -y python3-pip

# Instalar herramientas necesarias adicionales
sudo apt update
sudo apt install -y git make gnat zlib1g-dev
#instalacion GHDL
git clone https://github.com/ghdl/ghdl
cd ghdl
./configure --prefix=/usr/local
make
sudo make install
echo "$0: All done!"

# install icarus
sudo apt install iverilog

# instalar LCOV y gcc
sudo apt-get update -y
sudo apt-get install -y lcov
install gcc

# instalar numpy
pip3 install numpy
sudo apt-get install python3-matplotlib
python -m pip install -U matplotlib


# Para GITLAB RUNNER:(activarlo)

wget https://gitlab-runner-downloads.s3.amazonaws.com/master/deb/gitlab-runner_amd64.deb

sudo dpkg -i gitlab-runner_amd64.deb
sudo gitlab-runner run


## Registrar un nuevo runner:
sudo gitlab-runner register
https://docs.gitlab.com/runner/register/

## activar gitlab runner
run

## Para el TOML:
si la imagen no esta en docker hub, hay que añadir en toml el pull policy = "if-not-present"

ubicaciion: /etc/gitlab-runner/config

## Crear imagen desde dockerfile:
ir a la carpeta donde esta dockerfile y escribir: docker build -t cocotb:1.0.1 .

## Para crear el contenedor a traves de la imagen anterior escribir:
docker run -i -v /home/sergioasn/repo/:/home/ -t multi:1.0.0 /bin/bash
te copia la carpeta que pones al home del docker y poner nombre de la imagen y version, luego te abre el bash

## Para borrar imagen escribir:
docker rmi y el Id de la imagen

## CUIDADO!! para poder poner por defecto el python 3:
update-alternatives --install /usr/bin/python python /usr/bin/python3.6 10
