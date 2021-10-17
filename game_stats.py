import json
class GameStats():
    """Track statistics for Alien Invasion."""
    
    def __init__(self, ai_settings):
        """Initialize statistics."""
        self.ai_settings = ai_settings
        self.read_stats()
        
        # Start game in an inactive state.
        self.game_active = False
        
        # High score should never be reset.
        with open("config.json") as f:
            conf = json.load(f)
        self.high_score = conf['game']['score']['highest']
        
    def read_stats(self):
        """Initialize statistics that can change during the game."""
        with open("config.json") as f:
            conf = json.load(f)
        self.ships_left = self.ai_settings.ship_limit
        self.score = conf['game']['score']['highest']
        self.level = 1
