class Player():
    def __init__(self):
        self.id = int()
        self.name = str()
        self.rank = int()
        self.groupID = list()

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setID(self, ID):
        self.id = int(ID)

    def getID(self):
        return self.id

    def setRank(self, rank):
        if rank is not None:
            self.rank = int(rank)
        else:
            self.rank = None

    def getRank(self):
        return self.rank

    def setGroupID(self, groupID):
        self.groupID.extend(groupID)

    def getGroupID(self):
        return self.groupID

    def __str__(self):
        return f'ID: {self.id}, Name: {self.name}, Rank: {self.rank}, Group ID: {self.groupID}'
