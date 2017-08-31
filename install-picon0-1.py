sudo apt-get install python-smbus python3-smbus python-dev python3-dev
print('Add The following lines to the file thats about to open:')
print('dtparam=i2c1=on')
print('dtparam=i2c_arm=o')
raw_input()
sudo nano /boot/config.txt
print('Now reboot...')