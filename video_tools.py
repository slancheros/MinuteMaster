import whisper
import os
import sys
import subprocess
#from moviepy.editor import VideoFileClip


from whisper.utils import write_vtt


model = whisper.load_model("small")

def video2mp3(video_file, output_ext="mp3"):
    filename, ext = os.path.splitext(video_file)
    subprocess.call(["ffmpeg", "-y", "-i", video_file, f"{filename}.{output_ext}"],
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.STDOUT)
    return f"{filename}.{output_ext}"

def translated_transcript( audio_file ):
    options = dict(beam_size=5, best_of=5,fp16=False)
    translate_options = dict(task="translate", **options)
    result = model.transcribe(audio_file,**translate_options)
    return result

def create_output_video(input_video):
  output_dir = '/content/'
  audio_file = video2mp3(input_video, output_ext="mp3")
  transcript = translated_transcript(audio_file)
  audio_path = audio_file.split(".")[0]

  with open(os.path.join(output_dir, audio_path + ".vtt"), "w") as vtt:
    write_vtt(transcript["segments"], file=vtt)
    subtitle = audio_path + ".vtt"
    output_video = audio_path + "_subtitled.mp4"
    os.system(f"ffmpeg -i {input_video} -vf subtitles={subtitle} {output_video}")
  return output_video
