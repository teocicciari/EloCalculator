
class Player(object):

    def __init__(self, name, rating, results):
        self.name = name
        self.rating = rating
        self.results = results
        self.rankeado = False
        self.id = 0

    def refresh_data_r(self, id, n_games, k):
        self.id = id
        self.n_games = n_games
        self.k = k
        self.rankeado = True

    def refresh_data_nr(self, n_games, score, av_op):
        self.n_games = n_games
        self.score = score
        self.av_op = av_op

    def refresh_rating(self, new_rating, n_games):
        self.n_games = self.n_games + n_games
        self.old_rating = self.rating
        self.rating = new_rating
        self.variation = new_rating - self.old_rating
    
    def set_rating(self, rating):
        self.rating = rating

class Rated_player(object):

    def __init__(self, id, name, rating, n_games):
        self.id = int(id)
        self.name = name
        self.rating = rating
        self.n_games = n_games

        if(n_games < 30):
            self.k = 40
        else: 
            self.k = 20

class Entry_player(object):

    def __init__(self, name, n_games, score, av_op):
        self.name = name
        self.n_games = n_games
        self.score = score
        self.av_op = av_op
        self.entring = False
    
    def refresh(self, score, n_games, av_op):
        self.score = score
        self.n_games = n_games
        self.av_op = av_op

    def new_rated(self, rating):
        self.rating = int(rating)
        self.entring = True
