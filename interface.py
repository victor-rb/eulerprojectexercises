import gradio as gr
from gradio.themes.builder_app import text_size
from matplotlib.pyplot import title

import solutions
import importlib

from utitity import page_utils as pu
css = """
h1 {
    text-align: center;
    display:block;
    style="font-size:50px;
}
textarea{
    font-size: 40px;
}

"""

def on_calculate():
    result = pu.execution_time(getattr(mod, 'answer'))
    return f"{result[1]}    :    Exec. Time ({result[0]})"


with gr.Blocks(css=css) as interface:
    with gr.Row():
        gr.Markdown('# Euler Project Solutions')

    for module in solutions.__all__:
        mod = importlib.import_module(solutions.__name__ + '.' + module)

        with gr.Accordion(f"{mod.info} - {mod.name}", open=False):
            gr.HTML(mod.problem, show_label=False)
            output = gr.Textbox(label="Answer")

            trigger_button = gr.Button("Calculate", size="sm", scale=0)
            trigger_button.click(on_calculate, inputs=None, outputs=output)

interface.launch()