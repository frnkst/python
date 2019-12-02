from gtts import gTTS
from pygame import mixer, time
import os


def say(text):
    temp_file = "audio.mp3"
    text_to_speech = gTTS(text=text, lang='en-uk')
    text_to_speech.save(temp_file)

    mixer.init()
    mixer.music.load(temp_file)
    mixer.music.play()

    while mixer.music.get_busy():
        time.Clock().tick(10)

    os.remove(temp_file)


say("""Our revels now are ended. These our actors,
As I foretold you, were all spirits, and
Are melted into air, into thin air:
And like the baseless fabric of this vision,
The cloud-capp'd tow'rs, the gorgeous palaces,
The solemn temples, the great globe itself,
Yea, all which it inherit, shall dissolve,
And, like this insubstantial pageant faded,
Leave not a rack behind. We are such stuff
As dreams are made on; and our little life
Is rounded with a sleep.""")
