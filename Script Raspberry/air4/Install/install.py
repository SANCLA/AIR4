sudo pip3 install --upgrade setuptools
sudo apt-get install -y python3 git python3-pip
sudo apt-get install -y python-smbus
sudo apt-get install -y i2c-tools

# Manual steps:
# sudo raspi-config -> Interfacing Options -> SPI -> Enable
# sudo raspi-config -> Interfacing Options -> 2CI -> Enable
# sudo raspi-config -> Interfacing Options -> Serial -> Enable (without login shell!)

sudo pip3 install RPI.GPIO
sudo pip3 install adafruit-blinka

sudo pip3 install adafruit-circuitpython-lis3dh
sudo pip3 install adafruit-circuitpython-ccs811

# GPS
sudo apt-get install -y gpsd gpsd-clients

# SQL Lite datalogger database
sudo apt-get install -y sqlite3