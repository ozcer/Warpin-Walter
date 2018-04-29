from src.const import *


class SoundManager:
    
    def __init__(self):
        self.library = {}
        self.load_sounds("../sfx")
        
        path = "../bgm"
        cwd = os.path.dirname(__file__)
        relative_path = os.path.join(cwd, path)
        for file in os.listdir(relative_path):
            _path = os.path.join(relative_path, file)
            pygame.mixer.music.load(_path)
            #pygame.mixer.music.play(loops=-1)
        
    def load_sounds(self, path):
        cwd = os.path.dirname(__file__)
        relative_path = os.path.join(cwd, path)
        for file in os.listdir(relative_path):
            _path = os.path.join(relative_path, file)
            if os.path.isdir(_path):
                self.load_sounds(_path)
            else:
                self.library[file.split(".")[0]] = pygame.mixer.Sound(_path)

    def play(self, sound_name, loops=0, maxtime=0, fade_ms=0):
        self.library[sound_name].play(loops, maxtime, fade_ms)