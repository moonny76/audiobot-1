from mty_media_bot import create_app
from mty_media_bot.assistant import Word, Assistant, Friend
from mty_media_bot.service.command import ExitCommand, SearchCommand


def setup_command(assistant, friend):
    assistant.add_command(ExitCommand(assistant, friend))
    assistant.add_command(SearchCommand(assistant, friend))


word_list = [Word("유튜브에서 김광석 노래 찾아 줘", ""),
             Word("김광석 노래 찾아 줘", "")]


def test_words(assistant):
    failed_words = []
    for word in word_list:
        if not assistant.process(word):
            failed_words.append(word)
    print("Failed words")
    for index, word in enumerate(failed_words):
        print(f"{index}. {word.korean_word} / {word.english_word}")


def run_test_bot():
    assistant = Assistant("뷔", speaker_on=False)
    friend = Friend("친구", speaker_on=False)
    setup_command(assistant, friend)
    test_words(assistant)


if __name__ == "__main__":
    create_app()
    run_test_bot()
