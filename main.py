from services.mixtape_generator import MixtapeGenerator
import os

def generate_my_mixtape():
    print("Hello from youtube-mixtape-creation!")
    generator = MixtapeGenerator()

    base_dir = os.path.dirname(os.path.abspath(__file__))
    audio_file_path = os.path.join(base_dir, 'assets', 'audio')
    output_file_path = os.path.join(base_dir, 'outputs')

    track1_path = os.path.join(audio_file_path, "Maahi.wav")
    track2_path = os.path.join(audio_file_path, "mein_agar.mp3")


    # Load the audio files
    track1 = generator.load_audio(audio_format="wav", file_path=track1_path)
    track2 = generator.load_audio(audio_format="mp3", file_path=track2_path)

    # trim the audio 1
    trimmed_track1 = generator.trim_audio(track1, start_time=1, end_time=5)
    normalize_track1 = generator.normalize_audio(trimmed_track1)

    # normalize the second track
    normalize_track2 = generator.normalize_audio(track2)

    # merging the tracks with a crossfade of 2 seconds (2000 milliseconds)
    merged_mixtape = generator.merge_tracks([normalize_track1, normalize_track2], crossfade_ms=2)

    # 6. Apply a master fade to the very beginning and very end of the final 
    final_mixtape = generator.apply_fade(merged_mixtape, fade_in_duration=2000, fade_out_duration=5000)
    
    # 7. Export to the outputs folder
    output_path = os.path.join(output_file_path, "my_final_mixtape.mp3")
    generator.export(audio=final_mixtape, file_path=output_path, audio_format="mp3")



if __name__ == "__main__":
    generate_my_mixtape()
