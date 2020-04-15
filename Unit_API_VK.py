import requests

class Global_friends:
    def __init__(self):
        self.token = 'f521c678206906cf2f8a5d179f463407449a616469bddb48c7ebd1eab8b99a45b47c242adf63cef2b6c77'


    def friend(self, source_uid, target_uid):
        response = requests.get('https://api.vk.com/method/friends.getMutual',
                                params={
                                    'access_token': self.token,
                                    'source_uid': source_uid,
                                    'target_uid': target_uid,
                                    'order': 'random',
                                    'count': 50,
                                    'v': 5.103
                                })
        self.data = response.json()


    def conclusion(self):
        print('Список общих контактов:\n')
        a = 'https://vk.com/id'
        for user in self.data['response']:
            print('{}{}\n'.format(a, user))

total = Global_friends()
total.friend(115848491, 99982799)
total.conclusion()