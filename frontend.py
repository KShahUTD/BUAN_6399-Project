# Frontend# 
#---Chat Interface---
import ipywidgets as widgets
from IPython.display import display, HTML

# Title for the chat interface
title = widgets.HTML(value="<h2>FliptRx Configuration Lead AI Mentor</h2>")

# Input field for claim description or question with adjusted size
input_box = widgets.Textarea(
    value="",
    placeholder="What can I assist you with today?",
    description="Input:",
    layout=widgets.Layout(width='30%', height='300px')
)

# Button to trigger analysis
button = widgets.Button(description="Ask")

# Output widget for displaying the chat messages
output = widgets.Output()

# When the button is clicked, analyze input
def on_click(_):
    with output:
        output.clear_output()
        text = input_box.value.strip()
        if not text:
            print("Please type your question here.")
            return
        try:
            resp = analyze_input(text)
            print(resp)
        except Exception as e:
            print("Error:", e)

button.on_click(on_click)

# Create the layout with title, input box, button, and output container
ui_layout = widgets.VBox([title, input_box, button, output])
