import gradio as gr
import solutions
import importlib

css = """
h1 {
    text-align: center;
    display:block;
}
"""

with gr.Blocks(css=css) as interface:
    with gr.Row():
          gr.Markdown('# Euler Project Solutions')

    for module in solutions.__all__:
      mod = importlib.import_module(solutions.__name__ + '.' + module)
      name, problem, answer = getattr(mod, 'answer')()

      with gr.Accordion(name, open=False):
            gr.Textbox(problem, show_label=False)
            gr.Markdown('Resposta : ' + answer)
    
interface.launch()