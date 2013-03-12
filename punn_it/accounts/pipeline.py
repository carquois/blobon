from django.core.files.base import ContentFile
from datetime import datetime, timedelta
import facebook


def load_facebook_extra_data(backend, details, response, uid, user, social_user=None, *args, **kwargs):
    """
    Load extra data from Facebook and save it in the user's profile
    """
    if backend.name is not "facebook":
        return

    oauth_access_token = response['access_token']
    graph = facebook.GraphAPI(oauth_access_token)
    fb_profile = graph.get_object("me")
    fb_friends = graph.get_connections("me", "friends")
    fb_likes = graph.get_connections("me", "likes")
    
    profile = user.get_profile()
    profile.fb_friends = fb_friends
    profile.fb_likes = fb_likes
    profile.gender = fb_profile['gender'][:1]
    profile.birthdate = datetime.strptime(fb_profile['birthday'], "%m/%d/%Y").date()
    profile.facebook_link = fb_profile['link']
    
    fb_profile_pic= graph.get_object("me/picture", width=800)
    fb_profile_pic_file = ContentFile(fb_profile_pic['data'])
    file_extension = fb_profile_pic['mime-type'].split("/")[1]
    profile.fb_avatar.save("%s_fb_profile.%s" % (user.username, file_extension), fb_profile_pic_file) 
    
    #use it for default avatar if there wasn't an avatar already
    if not profile.avatar:
        profile.avatar = profile.fb_avatar
    
    profile.save()

