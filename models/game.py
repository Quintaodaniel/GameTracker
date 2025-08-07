class Game:
    def __init__(self, name, genre, game_type, platform, hours_played, start_date,
                 last_session, stats, stopped_at, rating, notes):
        self.name = name
        self.genre = genre
        self.game_type = game_type
        self.platform = platform
        self.hours_played = hours_played
        self.start_date = start_date
        self.last_session = last_session
        self.stats = stats
        self.stopped_at = stopped_at
        self.rating = rating
        self.notes = notes

    def to_dict(self):
        return self.__dict__
