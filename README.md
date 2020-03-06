# Broadworks-Django-Auth 
[![PyPI pyversions](https://img.shields.io/pypi/status/Broadworks-Django-Authentication.svg)](https://pypi.org/project/Broadworks-Django-Authentication/)
[![PyPI version shields.io](https://img.shields.io/pypi/v/Broadworks-Django-Authentication.svg)](https://pypi.python.org/pypi/Broadworks-Django-Authentication/)
[![PyPI license](https://img.shields.io/pypi/l/Broadworks-Django-Authentication.svg)](https://pypi.python.org/pypi/Broadworks-Django-Authentication/)
[![PyPI Downloads](https://img.shields.io/pypi/dm/Broadworks-Django-Authentication.svg)](https://pypi.python.org/pypi/Broadworks-Django-Authentication/)
#  Broadworks OCI-P (Open Client Interface Provisioning) Client

## Install

```
pip install Broadworks-Django-Authentication

```


## Install the app
settings.py
```python
INSTALLED_APPS = [
    ...
    'broadworks_django_auth'
]

```
## Adding to Authentication Backends

settings.py
```python
AUTHENTICATION_BACKENDS = [
    'broadworks_django_auth.backends.BraodworksAuthentication',
]
```


## Adding your OCIP Address

settings.py

```python
BROADWORKS_ADDRESS = "https://api.broadsoft.com/webservice/services/ProvisioningService"

```
