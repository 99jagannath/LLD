from Show import Show
class Theater:

    def __init__(self, name: str, city: str) -> None:
        self.name = name
        self.city = city
        self.showList = []
        self.screenList = []

    def addShow(self, movie, screen, startTime, endTime):
        show = Show(movie, screen, startTime, endTime)
        self.showList.append(show)

    def getShows(self):
        return self.showList
    
    def getShowByMovieName(self, movie):
        shows = []

        for show in self.showList:
            if show.getMovie() == movie:
                shows.append(show)
        return shows
    
    def addScreen(self, screen):
        self.screenList.append(screen)