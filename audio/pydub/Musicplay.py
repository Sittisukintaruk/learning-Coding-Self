from pydub import AudioSegment
from pydub.playback import play
from pydub.silence import split_on_silence
sound = AudioSegment.from_mp3("anime-paradise_gintama-opening-12.mp3")


play(sound)



