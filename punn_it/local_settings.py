TWITTER_CONSUMER_KEY              = 'qwGfmeTz4u6rwTvSMVlIg'
TWITTER_CONSUMER_SECRET           = 'UfMLwl9bWCAPJz4JnKV1n7xRWUZaPzosBkA8Cofzwa0'
FACEBOOK_APP_ID                   = ''
FACEBOOK_API_SECRET               = ''
GOOGLE_OAUTH2_CLIENT_ID           = ''
GOOGLE_OAUTH2_CLIENT_SECRET       = ''
SOCIAL_AUTH_CREATE_USERS          = True
SOCIAL_AUTH_FORCE_RANDOM_USERNAME = False
SOCIAL_AUTH_DEFAULT_USERNAME      = 'socialauth_user'
SOCIAL_AUTH_COMPLETE_URL_NAME     = 'socialauth_complete'
SOCIAL_AUTH_ASSOCIATE_BY_MAIL     = False
LOGIN_ERROR_URL                   = '/login/error/'
GITHUB_APP_ID                     = ''
GITHUB_API_SECRET                 = ''

SOCIAL_AUTH_COMPLETE_URL_NAME  = 'socialauth_complete'
SOCIAL_AUTH_ASSOCIATE_URL_NAME = 'socialauth_associate_complete'

SOCIAL_AUTH_EXPIRATION = 'expires'

SOCIAL_AUTH_PIPELINE = (
   'social_auth.backends.pipeline.social.social_auth_user',
   'social_auth.backends.pipeline.associate.associate_by_email',
   'social_auth.backends.pipeline.misc.save_status_to_session',
   'punns.pipeline.redirect_to_form',
   'punns.pipeline.username',
   'social_auth.backends.pipeline.user.create_user',
   'social_auth.backends.pipeline.social.associate_user',
   'social_auth.backends.pipeline.social.load_extra_data',
   'social_auth.backends.pipeline.user.update_user_details',
)
