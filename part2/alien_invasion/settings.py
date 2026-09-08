class Settings:
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)
        self.ship_speed = 25.0
        self.bullet_speed = 50.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (250,0,0)
        self.bullet_allowed = 3
        self.alien_speed = 10.0
        self.aline_drop_speed = 10
        self.fleet_direction = 1 #1为向右，-1为向左
        self.ship_limit = 3
        self.speed_scale = 1.1
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed = 25
        self.bullet_speed = 50
        self.aliens_speed = 10
        self.fleet_direction = 1

    def increse_speed(self):
        self.ship_speed *= self.speed_scale
        self.bullet_speed *= self.speed_scale
        self.aliens_speed *= self.speed_scale
