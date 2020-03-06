# Broadworks-Django-Auth 

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
