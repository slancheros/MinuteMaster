import processor
import video_tools
from transformers import pipeline

meeting_processor = processor.Processor()

#as message
meeting_summary = {'input_video': object(),
           'audio_file': object(),
           'transcript': object(),
           'output_video':object(),
           'content': str(),
           'summary':str(),
           'action_items':[]
           }

def assign_input_video( meeting_summary):
   meeting_summary['input_video']= "reunion_efectiva.mp4"

def get_audio(meeting_summary):
    meeting_summary['audio_file'] = video_tools.video2mp3(meeting_summary['input_video'], output_ext="mp3" )

def get_transcript(meeting_summary):
    meeting_summary['transcript'] = video_tools.translated_transcript( meeting_summary['audio_file'] )

def generate_subtitled_video(meeting_summary):
     meeting_summary['audio_file'] = video_tools.create_output_video(meeting_summary['audio_file'], meeting_summary['input_video'],meeting_summary['transcript'])

def get_meeting_content(meeting_summary):
    meeting_summary['content'] = meeting_summary['transcript']['text']

def get_meeting_summary(meeting_summary):
    summarizer = pipeline("summarization")
    meeting_summary['summary'] = summarizer(meeting_summary['content'] )

meeting_processor.add([assign_input_video,get_audio,get_transcript, generate_subtitled_video,get_meeting_content,get_meeting_summary])
meeting_processor.execute(meeting_summary)
print(meeting_summary['summary'])