import requests


class User:
    def __init__(self, id):
        self.id = id
        print(f'https://vk.com/id{id}')


    def __str__(self):
        return f'пользователь {self.id}'

    def __and__(self, other):
        self.total_id = [str(self.id), str(other.id)]



class Global_friends(User):
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

user1 = User(115848491)
print(user1.id)
user2 = User(99982799)
print(user2.id)

user1.__and__(user2)
print(user1.total_id)





total = Global_friends()
total.friend(115848491, 99982799)
total.conclusion()
