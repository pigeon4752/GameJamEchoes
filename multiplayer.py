import requests
import json
class Multiplayer:
    url = 'http://gobbo.luhc.org.uk/'
    session = requests.Session()
    headers = {'Content-Type': 'application/json'} 
    valid = True
    def __init__(self,player):
        notinit = True
        while notinit:
            try:

                data_to_send = {'width':24,'size':24,'xPos':player.position.x,'yPos':player.position.y,'hp':player.health,'xVel':0,'yVel':0}
        
                response = self.session.post(self.url + 'receive_initial_data/', data=json.dumps(data_to_send), headers=self.headers,timeout = 1)
                print(response.content)
                self.key = json.loads(response.content)['key']
                if self.key == 0:
                    self.valid = False
                notinit = False
            except:
                print("fail")

    def getOtherPlayer(self):

        data_to_send = {'key':self.key}
        try:
            response = self.session.get(self.url + 'retrieve_opponent/', data=json.dumps(data_to_send), headers=self.headers,timeout = 1)
            print(response.content)
            data = json.loads(response.content)
            if data['status'] == 200:
            
                return(True,data['opponent'])
            return(False,())#If it ever tries to read that empty bracket it will break, Don't let it do that.
        except:
           
            return(False,())

    def updateOpponent(self,player,opponent):
        data_to_send = {'key': '2','xPos':player.xPosition,'yPos':player.yPosition,'hp':player.health,'xVel':player.xVelocity,'yVel':player.yVelocity}
        try:
            response = self.session.get(self.url + 'update_data/', data=json.dumps(data_to_send), headers=self.headers,timeout = 1)
            oppo = json.loads(response.content)["opponent"]
            opponent.xPosition = oppo["xPos"]
            opponent.yPosition = oppo["yPos"]
            opponent.health = oppo["hp"]
            opponent.xVelocity = oppo["xVel"]
            opponent.yVelocity = oppo["yVel"]
        except:
            print("b")

        
        #print(data["opponent"]["xPos"])
    def wipe(self):
        self.session.post(url + 'wipe_data/')


