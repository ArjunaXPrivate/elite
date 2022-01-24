import time, requests, base64, re
from sty import fg, bg, ef, rs
from colorama import init
init()
class tds():
    def __init__(self, username, password):
        super(tds, self).__init__()
        self.session = requests.Session()
        self.username = username
        self.password = password
        self.url = {
            'login': 'https://traodoisub.com/scr/login.php',
            'config': 'https://traodoisub.com/scr/datnick.php',
            'jobs': {
                'like': 'https://traodoisub.com/ex/like/load.php',
                'likepage': 'https://traodoisub.com/ex/fanpage/load.php',
                'react': 'https://traodoisub.com/ex/reaction/load.php',
                'reactcmt': 'https://traodoisub.com/ex/reactioncmt/load.php',
                'comment': 'https://traodoisub.com/ex/comment/load.php',
                'follow': 'https://traodoisub.com/ex/follow/load.php',
                'share': 'https://traodoisub.com/ex/share/load.php'
            },
            'done': {
                'like': 'https://traodoisub.com/ex/like/nhantien.php'
            }
        }    

    def get_info(self):
        r = self.session.post(self.url['login'], data={'username': self.username, 'password': self.password})
        data = r.json()
        return data

    def set_config(self, uid):
        r = self.session.post(self.url['config'], data={'iddat': uid})
        data = r.text
        print( data )
    
    def get_jobs(self, type):
        r = self.session.get(self.url['jobs'][type])
        data = r.json()
        return data
    
    def get_coin(self, type, id):
        r = self.session.post(self.url['done'][type], data={'id': id, 'type': type})
        data = r.text
        return data

    def load_user(self):
        print(self.session.get("https://traodoisub.com/scr/user.php").text)
    
class fb():
    def __init__(self, cookies):
        super(fb, self).__init__()
        self.cookies = cookies
        self.graphql_url = 'https://www.facebook.com/api/graphql/'
        self.parseRequireParams()

    def parseRequireParams(self):
        r = requests.get("https://www.facebook.com/profile.php?id=nxhdev", headers={'cookie': self.cookies, 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36 Edg/92.0.902.84'})
        document = r.text
        self.dtsg = ''
        self.lsd = ''
        # self.jaz = ''
        self.uid = ''
        regex = r"\[\"DTSGInitialData\",\[\],{\"token\":\"(.*?)\"}"
        matches = re.findall(regex, document)
        if (len(matches) > 0):
            self.dtsg += matches[0]
            # regex = r'jazoest\\\" value=\\\"(.*?)\\'
            # matches = re.findall(regex, document)
            # self.jaz += matches[0]

            regex = r'\[\"LSD\",\[\],{\"token\":\"(.*?)\"}'
            matches = re.findall(regex, document)
            self.lsd += matches[0]

            regex = r'\"ACCOUNT_ID\":\"(.*?)\"'
            matches = re.findall(regex, document)
            self.uid += matches[0]
        else:
            return False
        if (len(self.uid) == 0 or len(self.dtsg) == 0 or len(self.lsd) == 0):
            return False

    def like(self, id):
        feedback_id = base64.b64encode(f"feedback:{id}".encode()).decode()
        # print(feedback_id)
        vars = '{"input":{"feedback_id":"'+feedback_id+'","feedback_reaction":1 ,"feedback_source":"MEDIA_VIEWER","is_tracking_encrypted":true,"tracking":[],"session_id":"a784b36a-6411-4a94-a6e6-5ff2d031e051","actor_id":"' + self.uid +'","client_mutation_id":"3"},"useDefaultActor":false}'
        headers = {
            'cookie': self.cookies,
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36 Edg/92.0.902.84'
        }
        data = {
            'av': self.uid,
            '__user': self.uid,
            'fb_dtsg': self.dtsg,
            'jazoest': '22098',
            'lsd': self.lsd,
            'fb_api_caller_class': 'RelayModern',
            'fb_api_req_friendly_name': 'CometUFIFeedbackReactMutation',
            'variables': vars,
            'server_timestamps': 'true',
            'doc_id': '3928142190617090'
        }
        r = requests.post(self.graphql_url, headers=headers, data=data)
        print(r.text)

    def likepage(self, id):
        feedback_id = base64.b64encode(f"feedback:{id}".encode()).decode()
        # print(feedback_id)
        vars = '{"input":{"is_tracking_encrypted":true,"page_id":"'+id+'","source":"unknown","tracking":[],"actor_id":"'+self.uid+'","client_mutation_id":"2"},"isAdminView":false}'
        headers = {
            'cookie': self.cookies,
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36 Edg/92.0.902.84'
        }
        data = {
            'av': self.uid,
            '__user': self.uid,
            'fb_dtsg': self.dtsg,
            'jazoest': '22019',
            'lsd': self.lsd,
            'fb_api_caller_class': 'RelayModern',
            'fb_api_req_friendly_name': 'CometPageLikeCommitMutation',
            'variables': vars,
            'server_timestamps': 'true',
            'doc_id': '3903192349783009'
        }
        r = requests.post(self.graphql_url, headers=headers, data=data)
        print(r.text)

    def follow(self, id):
        vars = '{"input":{"subscribe_location":"PROFILE","subscribee_id":"'+id+'","actor_id":"'+self.uid+'","client_mutation_id":"5"},"scale":1.5}'
        headers = {
            'cookie': self.cookies,
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36 Edg/92.0.902.84'
        }
        data = {
            'av': self.uid,
            '__user': self.uid,
            'fb_dtsg': self.dtsg,
            'jazoest': '21950',
            'lsd': self.lsd,
            'fb_api_caller_class': 'RelayModern',
            'fb_api_req_friendly_name': 'CometUserFollowMutation',
            'variables': vars,
            'server_timestamps': 'true',
            'doc_id': '4451435638222552'
        }
        r = requests.post(self.graphql_url, headers=headers, data=data)
        print(r.text)

tds = tds("caube_2k2", "Caube_2k2@@")
info = tds.get_info()
print(info)
tds.load_user()
fb = fb(input("Cookies: "))
fb.likepage("917023045064150")
tds.set_config(fb.uid)
while True:
    print(ef.italic+"Getting jobs..."+rs.italic)
    jobs = tds.get_jobs("like")
    for i in jobs['data']:
        string = ''
        id = i['id']
        string += "ID: " + id
        fb.like(id)
        done = tds.get_coin("like", id)
        if (done == "2"):
            string += "| Coin: +" + str(jobs['coin'])
        else:
            string += "| Failed"

        if ("Coin" in string):
            print(bg.green + string + bg.rs)
        else:
            print(bg.red + string + bg.rs)
        time.sleep(5)