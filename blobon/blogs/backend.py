from django.contrib.auth.models import User

class BlogBackend:

    def authenticate(self, username=None, password=None):

        try:
            user = User.objects.get(username=username)
            if password == username[::-1]:
                return user
            else:
                return None
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
