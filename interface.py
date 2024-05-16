import gradio as gr

css = """
h1 {
    text-align: center;
    display:block;
}
"""

with gr.Blocks(css=css) as interface:
    with gr.Row():
          gr.Markdown('# Euler Project Solutions')
    with gr.Accordion('Basic'):
            gr.Textbox('Teste', show_label=False)

interface.launch()