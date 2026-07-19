# Import the library
from pydub import AudioSegment
from pydub.silence import detect_silence, split_on_silence
from pydub.effects import speedup
import os 



class MixtapeGenerator:
    def load_audio(self, audio_format:str, file_path:str="mp3"):
        """This function loads an audio file and returns an AudioSegment object.
        :param audio_format: The format of the audio file (e.g., 'mp3', 'wav').
        :param file_path: The path to the audio file.
        :return: An AudioSegment object representing the loaded audio.
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"The file {file_path} does not exist.")
        return AudioSegment.from_file(file_path, format=audio_format)


    def trim_audio(self, audio:AudioSegment, start_time:int, end_time:int):
        """This function trims an audio segment to the specified start and end times.
        :param audio: The AudioSegment object to be trimmed.
        :param start_time: The start time in seconds.
        :param end_time: The end time in seconds.
        :return: A trimmed AudioSegment object.
        """
        return audio[start_time*1000:end_time*1000]


    def normalize_audio(self, audio:AudioSegment):
        """This function normalizes the audio segment.
        :param audio: The AudioSegment object to be normalized.
        :return: A normalized AudioSegment object.
        """
        return audio.normalize()

    def apply_fade(self, audio:AudioSegment, fade_in_duration:int, fade_out_duration:int):
        """This function applies fade in and fade out effects to the audio segment.
        :param audio: The AudioSegment object to which to apply the fade effects.
        :param fade_in_duration: The duration of the fade in effect in seconds.
        :param fade_out_duration: The duration of the fade out effect in seconds.
        :return: An AudioSegment object with the fade effects applied.
        """
        return audio.fade_in(fade_in_duration*1000).fade_out(fade_out_duration*1000)


    def merge_tracks(self, tracks:list, crossfade_ms:int=1000):
        """This function merges multiple audio tracks into a single track.
        :param tracks: A list of AudioSegment objects to merge.
        :param crossfade_ms: The duration of the crossfade in milliseconds.
        :return: A merged AudioSegment object.
        """
        if not tracks:
            raise ValueError("The tracks list is empty. Nothing to merge.")
        
        mixtape = tracks[0]
        for track in tracks[1:]:
            # Ensure the crossfade isn't longer than the tracks themselves to avoid errors
            safe_crossfade = min(crossfade_ms, len(mixtape), len(track))
            mixtape = mixtape.append(track, crossfade=safe_crossfade)
        
        return mixtape


    def export(self, audio:AudioSegment, file_path:str, audio_format:str):
        """This function exports the audio segment to a file.
        :param audio: The AudioSegment object to export.
        :param file_path: The path where the audio file will be saved.
        :param audio_format: The format in which to save the audio file (e.g., 'mp3', 'wav').
        """
        os.makedirs(os.path.dirname(file_path), exist_ok=True)  # Ensure the directory exists
        print(f"Exporting mixtape to {file_path} in {audio_format} format.")
        audio.export(file_path, format=audio_format)
        print("Export completed successfully.")