class Player(object):

    def __init__(self, id, name, rating, n_games):
        self.id = id
        self.name = name
        self.rating = rating
        if (n_games > 30):
            self.k = 20  
        else:
            self.k = 40
            
        