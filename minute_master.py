from transformers import pipeline
import processor
import video_tools

class MinuteMaster(processor.Processor):
    def __init__(self):
        self.filters = list()
        self.meeting_summary= {'input_video': object(),
           'audio_file': object(),
           'transcript': object(),
           'output_video':object(),
           'content': str(),
           'summary':str(),
           'action_items':[]
           }
        self.meet_summarizer= pipeline("summarization")
 
    def assign_input_video( self,input_video):
        self.meeting_summary['input_video']= input_video

    def get_audio(self,meeting_summary):
        meeting_summary['audio_file'] = video_tools.video2mp3(self.meeting_summary['input_video'], output_ext="mp3" )

    def get_transcript(self, meeting_summary):
        meeting_summary['transcript'] = video_tools.translated_transcript( self.meeting_summary['audio_file'] )

    def generate_subtitled_video(self,meeting_summary):
        meeting_summary['audio_file'] = video_tools.create_output_video(self.meeting_summary['audio_file'], self.meeting_summary['input_video'],meeting_summary['transcript'])

    def get_meeting_content(self, meeting_summary):
        meeting_summary['content'] = self.meeting_summary['transcript']['text']

    def summarize(self, meeting_summary):
        meeting_summary['summary'] = self.meet_summarizer(self.meeting_summary['content'] )

    def process(self):
        self.add([self.get_audio,self.get_transcript,self.generate_subtitled_video,self.get_meeting_content,self.summarize])
        self.execute(self.meeting_summary)
        print(self.meeting_summary['summary'])
        return self.meeting_summary

    def get_meeting_summary(self):
        return self.meeting_summary
    
 



 

