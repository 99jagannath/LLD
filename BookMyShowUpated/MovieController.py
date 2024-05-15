
class MovieController:

    def __init__(self) -> None:
        self.cityVsMovie = {}
        self.movieList = []

    def addMovie(self, movie, city):
        movieList = self.getMovieByCity(city)
        movieList.append(movie)
        self.movieList[city] = movieList

    def getMovieByCity(self, city):
        movieList = []
        if city in self.cityVsMovie:
            movieList = self.cityVsMovie[city]
        return movieList
