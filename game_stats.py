class GameStats():

    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = False

        with open('high_score.txt') as high_score_file:
            self.high_score = int(high_score_file.read())

    def reset_stats(self):

        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1