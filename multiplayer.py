import requests
import json
class Multiplayer:
    url = 'http://gobbo.luhc.org.uk/'
    session = requests.Session()
    def __init__(self,player):

        data_to_send = {'width':24,'size':24,'xPos':player.xPosition,'yPos':player.yPosition,'hp':player.health,'xVel':0,'yVel':0}

        response = self.session.post(self.url + 'receive_initial_data/', data=json.dumps(data_to_send), headers=headers)
        self.key = json.loads(response.content)['key']

    def getOtherPlayer(self):

        data_to_send = {'key',self.key}
        response = self.session.post(self.url + 'retrieve_opponent/', data=json.dumps(data_to_send), headers=headers)
        
        data = json.loads(response.content)['']
        if data['status'] == 1:
            return(True,data['opponent'])
        return(False,())#If it ever tries to read that empty bracket it will break, Don't let it do that.
    
    def updateOpponent(self,player,opponent):
        data_to_send = {'key': '2','xPos':player.xPosition,'yPos':player.yPosition,'hp':player.health,'xVel':player.xVelocity,'yVel':player.yVelocity}
        oppo = json.loads(response.content)["opponent"]
        opponent.xPosition = oppo["xPos"]
        opponent.yPosition = oppo["yPos"]
        opponent.health = oppo["hp"]
        opponent.xVelocity = oppo["xVel"]
        opponent.yVelocity = oppo["yVel"]

        
        #print(data["opponent"]["xPos"])


