import json
import facebook
import ast
from textblob import TextBlob
import key
if __name__=='__main__':
    # token=os.environ.get('FACEBOOK_TEMP_TOKEN')
    # token='EAAGfzQMI8twBANZC7ymoYfGNscWWSpNygPVv7f3HTcjtSCisNhhCC9tdhqperhq7G8tY4MMLaB4Lzqkhwn2NhdI3dUnoMTZCfFNNmPxbNnINQcpCYOGBqFGb92sza9eLZB8IQaYbZCspdJuiRjxEHwHPLNrJnm9WZCZA5RBSozBwZDZD'
    token=key.token
    graph=facebook.GraphAPI(token)
    profile=graph.get_object('100000637257950',fields='posts.limit(20), email')
    print(profile)
    a=json.dumps(profile['posts']['data'])
    y=ast.literal_eval(a).__len__()
    for i in range(0,y):
        # print i+1,')',json.dumps(profile['posts']['data'][i][],indent=4),'\n'
        if json.dumps(profile['posts']['data'][i]).__contains__('message'):
            print i+1,')',json.dumps(profile['posts']['data'][i]['message'], indent=4),'\n',json.dumps(profile['posts']['data'][i]['id']),'\n'

        elif json.dumps(profile['posts']['data'][i]).__contains__('story'):
             print i + 1, ')', json.dumps(profile['posts']['data'][i]['story'], indent=4),'\n', json.dumps(profile['posts']['data'][i]['id']),'\n'






    profile2=graph.get_object('100000637257950',fields='posts.limit(20){comments.limit(20)}')
    for i in range(0, y):
        count_pos=0
        count_neg=0
        count_ntrl=0
        count=0
        if json.dumps(profile2['posts']['data'][i]).__contains__('comments'):
            a2 = json.dumps(profile2['posts']['data'][i]['comments']['data'])
            y2 = ast.literal_eval(a2).__len__()
            print i + 1, ') ',json.dumps(profile2['posts']['data'][i]['id'])
            for j in range(0,y2):
                pol = TextBlob(json.dumps(profile2['posts']['data'][i]['comments']['data'][j]['message'])).sentiment.polarity * 100
                count+=1
                if pol > 0:
                    count_pos += 1
                elif pol < 0:
                    count_neg += 1
                else:
                    count_ntrl += 1
                print '      ',json.dumps(profile2['posts']['data'][i]['comments']['data'][j]['message'],indent=4),pol,'%'
            print '      ',(count_pos*100)/count ,'% people spoke positive'
            print '      ',(count_neg * 100) / count, '% people spoke negative'
            print '      ',(count_ntrl * 100) / count, '% people spoke neutral'
        else:
            print i+1,') No comments ',json.dumps(profile2['posts']['data'][i]['id'])











    # profile2 = graph.get_object('131919650173343', fields='posts.limit(20){comments.limit(20)}')
    # for i in range(0, y):
    #     print(json.dumps(profile2['posts']['data'][i]['id'], indent=4))









#     # print json.dumps()
    # # for i in range(0,y):
    # #     if profile2['posts']['data'][i].has_key('comments'):
    # #         print json.dumps(profile2['posts']['data'][i]['comments']['data'],indent=4)
    #
    # print json.dumps(profile2['posts']['data'][0]['id'])
    # s=json.dumps(profile2['posts']['data'][0]['id']).__str__()
    # print(s)

