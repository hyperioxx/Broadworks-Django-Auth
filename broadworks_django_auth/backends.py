from BroadworksOCIP import Client
from .models import Broadworks
from django.conf import settings
from django.contrib.auth.models import User


class BraodworksAuthentication:

    def authenticate(self, request, username=None, password=None):
        client = Client(username=username, password=password, address=settings.BROADWORKS_ADDRESS)
        try:
            client.login()
        except Exception:
            return None
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            user = User(username=username)
            user.is_staff = False
            user.is_superuser = False
            user.save()
            b = Broadworks()
            b.user = user
            b.jsession = client.get_jsession()
            b.bwsession = client.get_bw_session()
            if client.get_login_type() == "System":
                b.is_system = True
            elif client.get_login_type() == "Service Provider":
                b.is_serviceprovider = True
            elif client.get_login_type() == "Group":
                b.is_group = True
            else:
                b.is_user = True
            b.save() 
        user.broadworks.jsession = client.get_jsession()
        user.broadworks.bwsession = client.get_bw_session()
        user.broadworks.save()
        return user


    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

        
        
