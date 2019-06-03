import Credentials
import State
import pprint
from json import loads, dumps
from watson_developer_cloud import PersonalityInsightsV3 as PIV3
from watson_developer_cloud.personality_insights_v3 import Content

service = PIV3(version='2017-10-13', iam_apikey=Credentials.watsonKey(),
               url='https://gateway.watsonplatform.net/personality-insights/api')


def analisarTexto():
    texto = 'Just arrived in the United Kingdom. The only problem is that @CNN is the primary source of news available from the U.S. After watching it for a short while, I turned it off. All negative & so much Fake News, very bad for U.S. Big ratings drop. Why doesn’t owner @ATT do something? London part of trip is going really well. The Queen and the entire Royal family have been fantastic. The relationship with the United Kingdom is very strong. Tremendous crowds of well wishers and people that love our Country. Haven’t seen any protests yet, but I’m sure the Fake News will be working hard to find them. Great love all around.Also, big Trade Deal is possible once U.K. gets rid of the shackles. Already starting to talk!'
    #texto = State.load()

    #json content_type='application/json'


    profile = service.profile(texto, content_type='text/plain;charset=utf-8', raw_scores=True,
                              consumption_preferences=False, accept_language='pt-br').get_result()
    pprint.pprint(profile)
    State.save(profile)
