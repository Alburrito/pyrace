from pydub import AudioSegment
from pydub.playback import _play_with_simpleaudio
import threading
from utils import SOUND_PATH


class MusicPlayer:

    _current_music_thread = None
    _current_music_player = None

    @classmethod
    def __play_music(cls, mp3_file_name: str) -> None:
        def play_music():
            music = AudioSegment.from_mp3(f"{SOUND_PATH}/{mp3_file_name}")
            cls._current_music_player = _play_with_simpleaudio(music)
            cls._current_music_player.wait_done()

        cls.__stop_music()

        cls._current_music_thread = threading.Thread(target=play_music)
        cls._current_music_thread.start()

    @classmethod
    def __stop_music(cls) -> None:
        if cls._current_music_player:
            cls._current_music_player.stop()
            cls._current_music_player = None

        if cls._current_music_thread and cls._current_music_thread.is_alive():
            cls._current_music_thread.join()
            cls._current_music_thread = None

    @classmethod
    def stop_music(cls) -> None:
        cls.__stop_music()

    @classmethod
    def play_start_music(cls) -> None:
        cls.__play_music("race-start-beeps.mp3")

    @classmethod
    def play_race_sound(cls) -> None:
        cls.__play_music("race-music.mp3")

    @classmethod
    def play_finish_music(cls) -> None:
        cls.__play_music("race-finish.mp3")

    @classmethod
    def play_crowd_cheer(cls) -> None:
        cls.__play_music("crowd-cheer.mp3")
