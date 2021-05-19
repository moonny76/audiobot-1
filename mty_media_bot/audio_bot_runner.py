from mty_media_bot import create_app
from mty_media_bot.assistant import Assistant, Friend
from mty_media_bot.service.command import ExitCommand, SearchCommand


def run_bot():
    assistant = Assistant("철수")
    friend = Friend("친구")
    assistant.add_command(ExitCommand(assistant, friend))
    assistant.add_command(SearchCommand(assistant, friend))
    assistant.speak(f"나는 {assistant.name}라고 해.")
    assistant.speak("너 이름은 뭐야?")
    word = assistant.listen()
    if word is None:
        assistant.speak("미안, 못 알아 들었어. 그냥 친구라 부를게")
    else:
        friend.name = word.korean_word
    assistant.speak(f'{friend.name}, 무엇을 도와줄까?')
    while 1:
        word = assistant.listen()
        if word is None:
            assistant.speak("미안, 못 알아 들었어")
            continue
        if assistant.process(word):
            assistant.speak(f'{friend.name}, 잘한거 같아?')
        else:
            assistant.speak(f'{friend.name}, 내가 못 하는 거네.')
        assistant.speak(f'{friend.name}, 다른 무엇을 도와줄까?')


if __name__ == "__main__":
    create_app()
    run_bot()
