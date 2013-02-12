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
    profile.birthdate = datetime.strptime(fb_profile['birthday'], "%d/%m/%Y").date()
    profile.facebook_link= fb_profile['link']
    profile.save()

