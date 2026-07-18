# Import the library
from pydub import AudioSegment
from pydub.silence import detect_silence, split_on_silence
from pydub.effects import speedup
import os 



class MixtapeGenerator:
    def load_audio(self, audio_format:str, file_path:str="mp3"):
        """This function loads an audio file and returns an AudioSegment object."""
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"The file {file_path} does not exist.")
        return AudioSegment.from_file(file_path, format=audio_format)


    def trim_audio(self, audio:AudioSegment, start_time_ms:int, end_time_ms:int):
        """This function trims an audio segment to the specified start and end times."""
        return audio[start_time_ms:end_time_ms]


    def normalize_audio(self): 
        pass


    def apply_fade(self):
        pass


    def merge_tracks(self):
        pass


    def export(self):
        pass