from Movie import Movie
from Language import Language
from Genre import Genre
from datetime import datetime

class productionHouse:

    def __init__(self, name, actors) -> None:
        self.name = name
        self.actors = actors

    def createMovie(self):
        newMovie = Movie(1, "ANIMAL", "220", Language.HINDI.value, Genre.ACTION.value, datetime.utcnow("dd-mm-yy"), self)
        return newMovie