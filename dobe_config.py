
import configparser

class Dobe_Config():
    def __init__(self):
        self.configs = configparser.ConfigParser()
        self.configs.read("dobe.ini")
    
    @property
    def video_source(self):
        video_source = self.configs.get("Video", "Source")
        
        if video_source.isnumeric():
            video_source = int(video_source)

        return video_source

    @property
    def api_port(self):
        return self.configs.getint("API", "Port")

    @property
    def background_color(self):
        return self.configs.get("Colors", "Background")
        
    @property
    def primary_color(self):
        return self.configs.get("Colors", "Primary")

    @property
    def accent_color(self):
        return self.configs.get("Colors", "Accent")