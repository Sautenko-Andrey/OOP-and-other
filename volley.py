import random
class BeachVolley:
    def __init__(self,list):
        self.__rank=list

    def get_teams(self,name,rank):
            self.__rank[name]=rank
            return self.__rank

    def jrebiy(self):
            return self.__rank

    def net(self,list):
        net=random.choice(list)
        return net






