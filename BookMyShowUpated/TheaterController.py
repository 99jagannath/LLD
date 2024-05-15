
class TheaterController:

    def __init__(self) -> None:
        self.theaterList = []
        self.theaterCityMap = {}

    def addTheater(self, theater, city):
        theaters = self.getTheatersByCity(city)
        theater.append(theater)
        self.theaterCityMap[city] = theaters
        self.theaterList.append(theater)

    def getTheatersByCity(self, city):
        theaters = []
        if city in self.theaterCityMap:
            theaters = self.theaterCityMap[city]
        return theaters
    
    def getShowsByNameAndCity(self, movie, city):
        shows = []
        for theater in self.getTheatersByCity(city):
            showsList = theater.showList
            for show in showsList:
                if show.movie.name == movie.name:
                    shows.append(show)
        return shows