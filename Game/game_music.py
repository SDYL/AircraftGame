import os       # 需要遍历Game/sound下的文件
import pygame


class MusicPlayer(object):
    """音乐播放器类"""
    res_path = "../Game/sound/"

    def __init__(self, music_file):
        """初始化 方法
        :param music_file: 背景音乐文件名
        """
        # 1.加载背景音乐
        pygame.mixer_music.load(self.res_path + music_file)
        pygame.mixer.music.set_volume(0.2)

        # 2.加载音效字典
        # 1>定义音效字典属性
        self.sound_dict = {}
        # 2>获取目录下的文件列表
        files = os.listdir(self.res_path)
        # 3>遍历文件列表
        for file_name in files:
            # 排除背景音乐
            if file_name == music_file:
                continue
            # 创建声音对象
            sound = pygame.mixer.Sound(self.res_path + file_name)
            # 添加到音效字典，使用文件名作为字典的key
            self.sound_dict[file_name] = sound

    @staticmethod
    def play_music():
        pygame.mixer.music.play(-1)

    @staticmethod
    def pause_music(is_pause):
        if is_pause:
            pygame.mixer_music.pause()
        else:
            pygame.mixer_music.unpause()

    def play_sound(self, wav_name):
        """
        播放音效
        :param wav_name: 音效文件名
        :return:
        """
        self.sound_dict[wav_name].play()
