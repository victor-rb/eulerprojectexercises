import gradio as gr
import solutions
import importlib

from utitity import page_utils as pu
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
      result = pu.execution_time(getattr(mod, 'answer'))

      exec_time = result[0]
      name, info, problem, answer = result[1]

      with gr.Accordion(f"{info} - {name}", open=False):
            gr.Markdown(exec_time)
            gr.HTML(problem, show_label=False)
            gr.Markdown('Resposta : ' + answer)
    
interface.launch()