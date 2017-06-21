# -*- coding: utf-8 -*-
import facebook


token = facebook.GraphAPI().get_app_access_token(
    app_id = '439307303100997',app_secret= '649e5f5046501fa3812494ade78c35ac', offline=False)

print(token)
token = '439307303100997|QvGUYDSlfw54K4bUq8mofza_Kmo'

graph = facebook.GraphAPI(token)
deb = graph.debug_access_token(token,
        '439307303100997','649e5f5046501fa3812494ade78c35ac')
print(deb)
me = graph.get_object("me")
print(users)














#facebook.FACEBOOK_OAUTH_DIALOG_URL

#graph.get_access_token_from_code
#users = graph.search(type='user',q='Mark Zuckerberg')

#graph = facebook.GraphAPI(access_token='EAACEdEose0cBAIQYTf1QSV5CWzFTY4wRqmhnfmHVpr2MeZC7ZC4oPolmCzmKbNBz7J77R3zplqU34iZC00z4umYZBVP8XRAAVwsnz9t97F7mQqZAhggxEvhQcirzvDlSZAsjkZBw9QwBo0M2TXERhoevr4AH0ZAnpMNVgZBuOZAbQTruEVp9klMw354Cki2E7cO6EZD')
#me = graph.get_object("me")
