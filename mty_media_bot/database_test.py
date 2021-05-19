import unittest

from mty_media_bot import create_app
from mty_media_bot.service.parser_music import update_music, remove_music
from mty_media_bot.service.search_music import get_all_music, search_music


class MusicTest(unittest.TestCase):

    def setUp(self) -> None:
        create_app()
        self.filename = 'resource/music/Modern Talking.mp3'
        update_music(self.filename)
        self.music_list = get_all_music()
        self.assertEqual(1, len(self.music_list))

    def tearDown(self) -> None:
        for music in self.music_list:
            remove_music(music.id)

    def test_search_music(self):
        print('test')
        music_list = search_music("modern")
        self.assertEqual(self.filename, music_list[0].filename)
        self.assertEqual('Modern Talking', music_list[0].artist)


################################################################################

if __name__ == "__main__":
    unittest.main()
