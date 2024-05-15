## ISsue

'''
error: externally-managed-environment

× This environment is externally managed
╰─> To install Python packages system-wide, try apt install
    python3-xyz, where xyz is the package you are trying to
    install.

    If you wish to install a non-Debian-packaged Python package,
    create a virtual environment using python3 -m venv path/to/venv.
    Then use path/to/venv/bin/python and path/to/venv/bin/pip. Make
    sure you have python3-full installed.

    If you wish to install a non-Debian packaged Python application,
    it may be easiest to use pipx install xyz, which will manage a
    virtual environment for you. Make sure you have pipx installed.

    See /usr/share/doc/python3.12/README.venv for more information.


'''

## solution 

- https://stackoverflow.com/questions/75608323/how-do-i-solve-error-externally-managed-environment-every-time-i-use-pip-3

- put your environment in your file folder

### Install 

- sudo apt-get install libmysqlclient-dev
- sudo apt-get install pkg-config
- sudo chown -R $USER:$USER /var/www/html/ICPEPWebsite2024/venv
- pip install tzdata typing_extensions sqlparse pillow mysqlclient asgiref Django django-jazzmin
