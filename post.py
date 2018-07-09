import json
import facebook
import ast
from textblob import TextBlob

if __name__=='__main__':
    # token=os.environ.get('FACEBOOK_TEMP_TOKEN')
    # token='EAAGfzQMI8twBANZC7ymoYfGNscWWSpNygPVv7f3HTcjtSCisNhhCC9tdhqperhq7G8tY4MMLaB4Lzqkhwn2NhdI3dUnoMTZCfFNNmPxbNnINQcpCYOGBqFGb92sza9eLZB8IQaYbZCspdJuiRjxEHwHPLNrJnm9WZCZA5RBSozBwZDZD'
    token='EAACEdEose0cBAKHZACNUgBEPSUlPoXwC4dtPfztPpqPvyWOZCxugVjn9aXcB1gJFuELKSyvrV9vjBDnAGYZCEdpzhSrDeqxeobw9aAb6ZCqUYhcPNwQ6YwfD535WBjhhDM4yn9ZCDg3eZBatdT5AsINWdE3e45XAGe1nFbamAP9sUBQZCw1iMHEyrIWPJZBJICsc7LBhCRMFZAgZDZD'
    graph=facebook.GraphAPI(token)
    profile=graph.get_object('131919650173343',fields='name,posts')
    a=json.dumps(profile['posts']['data'],indent=4)

    y=ast.literal_eval(a).__len__()
    # print a

    x=json.loads('[ {"id":566,"message":"hha"}]')
    print(json.dumps(x,indent=4))

    for i in range(0,y):

        print json.dumps(profile['posts']['data'][i]['id']),json.dumps(profile['posts']['data'][i]['message'])
