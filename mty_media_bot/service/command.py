from abc import abstractmethod

from mty_media_bot.service.search_music import search_music
from mty_media_bot.service.youtube import search_video


class Command:
    @abstractmethod
    def execute(self, word):
        pass

    @abstractmethod
    def get_word(self):
        pass


class ExitCommand(Command):

    def __init__(self, assistant, partner):
        self.assistant = assistant
        self.partner = partner

    def execute(self, word):
        self.assistant.speak("안녕, " + self.partner.name + '.')
        exit(-1)

    def get_word(self):
        return ["exit", "bye", "sleep", "끝", "안녕", "종료"]


class SearchCommand(Command):
    youtube = ['youtube', '유튜브', '유투브']

    def __init__(self, assistant, partner):
        self.assistant = assistant
        self.partner = partner

    def execute(self, word):
        for youtube_word in SearchCommand.youtube:
            if youtube_word in word.korean_word or youtube_word in word.english_word:
                self.assistant.speak("youtube 에서 음악을 찾고 있어요.")
                search_video(word.korean_word)
                return
        search_music(word.korean_word)

    def get_word(self):
        return ["search", "find", "검색", "찾기", "찾아 줘"]