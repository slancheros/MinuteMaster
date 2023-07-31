import gradio as gr
import video_tools
import processor
title = "Minute Master -- Your usual meetings, but better!"

block = gr.Blocks()

with block:

    with gr.Group():
        with gr.Box():
            with gr.Row():

                inp_video = gr.Video(
                    label="Input Video",
                    #type="filepath",
                    mirror_webcam = False
                )
                op_video = gr.Video(label="Captioned Video")
                summary = gr.TextArea(label="Summary")
                content = gr.TextArea(label="Content in English")
        btn = gr.Button("Generate Meeting Summary")
        btn.click(video_tools.create_output_video, inputs=[inp_video], outputs=[op_video,summary,content])
       
        gr.HTML('''
        <div class="footer">
                    <p>Model by <a href="https://github.com/openai/whisper">OpenAI</a> - Gradio App by Ai Diomio
                    </p>
        </div>
        ''')

block.launch(server_name="0.0.0.0",server_port=7860,debug = True, share=True)