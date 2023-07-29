import gradio as gr
import pipeline
title = "Add Text/Caption to your YouTube Shorts - MultiLingual"

block = gr.Blocks()

with block:

    with gr.Group():
        with gr.Box():
            with gr.Row().style():

                inp_video = gr.Video(
                    label="Input Video",
                    #type="filepath",
                    mirror_webcam = False
                )
                op_video = gr.Video()
        btn = gr.Button("Generate Subtitle Video")
        btn.click(pipeline.create_output_video, inputs=[inp_video], outputs=[op_video])

        gr.HTML('''
        <div class="footer">
                    <p>Model by <a href="https://github.com/openai/whisper">OpenAI</a> - Gradio App by Ai Diomio
                    </p>
        </div>
        ''')

block.launch(debug = True)