from slackclient import SlackClient
import time

gen_dict = {'reply': '', 'dictionary': {}}

slack_token = ""
sc = SlackClient(slack_token)

sc.api_call("chat.postMessage", channel="#general", text=gen_dict['reply'])

sc = SlackClient(slack_token)

if sc.rtm_connect():
    while True:
        gen_dict['dictionary'] = sc.rtm_read()
        try:
            print gen_dict['dictionary'][0]
            gen_dict['reply'] = gen_dict['dictionary'][0]['text']
            #sc.api_call("chat.postMessage", channel="#general", text=gen_dict['reply'])
        except (IndexError, KeyError):
            pass
        time.sleep(1)
else:
    print "Connection Failed, invalid token?"
