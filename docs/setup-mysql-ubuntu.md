# Setup MYSQL Ubuntu

## Step 1 (Getting Started)
``sudo apt update -y``

``sudo apt upgrade -y``
## Step 2 (Install Apache Web Server)
``apt install apache2 libapache2-mod-wsgi-py3``

``systemctl start apache2``

``systemctl enable apache2``

Prompt: 
<p>Synchronizing state of mysql.service with SysV service script with /lib/systemd/systemd-sysv-install.
Executing: /lib/systemd/systemd-sysv-install enable mysql
</p>

### Got Any Problems? 
try this: <h6>Re-installing: https://stackoverflow.com/questions/41147609/unable-to-start-the-mysql-server-in-ubuntu</h6>
``sudo apt-get update``
``sudo apt-get install mysql-server``
``sudo apt install python3-mysqldb``


## Step 3 (Creating Database)
``sudo mysql -u root -p``

``CREATE DATABASE icpep_data CHARACTER SET utf8;``

``CREATE USER 'root'@'localhost' IDENTIFIED BY 'password@123';``

``GRANT ALL ON icpep_data.* TO 'user'@'localhost';``

``FLUSH PRIVILEGES``

``EXIT``
### Drop User
``DROP USER 'djangouser'@'localhost';``

## Exit Mysql Server
``ctrl + d``

https://cloudinfrastructureservices.co.uk/how-to-setup-django-with-mysql-database-on-ubuntu-22-04/