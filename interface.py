import gradio as gr
import importlib as IL

from PIL.ImageOps import scale

import utitity.page_utils as PU
import utitity.text_utils as TU
import solutions

_prob_names = solutions.__all__


def on_change(index):
    index = TU.de_format(index)
    mod = IL.import_module(solutions.__name__ + '.' + index)
    execution = PU.execution_time(getattr(mod, 'answer'))
    name = mod.name
    info = mod.info
    prob = mod.problem
    exec_time = execution[0]
    answer = execution[1]

    return name, info, prob, answer, exec_time

with gr.Blocks() as demo:
    with gr.Row():
        gr.Markdown(value='Euler Project')
    with gr.Row():
        with gr.Column(scale=1):
            radio = gr.Radio(TU.name_format(_prob_names), label="Problems", value='Problem 1')
        with gr.Column(scale=4):
            with gr.Row():
                values = on_change('problem1')
                output_info = gr.Label(label='Problem', value=values[1])
                output_name = gr.Label(label='Problem Title', value=values[0])
            with gr.Row():
                output_problem = gr.Label(label='Description', value=values[2])
            with gr.Row():
                output_answer = gr.Label(label='Result', value=values[3])
                output_exec = gr.Label(label='Execution Time', value=values[4])


        radio.select(on_change, inputs=radio, outputs=[
            output_name, output_info, output_problem, output_exec, output_answer
        ])






demo.launch()