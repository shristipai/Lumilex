import openai
import gradio as gr

openai.api_key = "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"

messages = [
    {"role": "system", "content": "You are an AI specialized in law. Do not answer anything other than law-related queries."},
]


def legal_chatbot(input):
    response = openai.Completion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a legal chatbot."},
            {"role": "user", "content": input}
        ]
    )
    reply = response.choices[0].message.content
    return reply

inputs = gr.inputs.Textbox(label="User Input")
outputs = gr.outputs.Textbox(label="Chatbot Response")

gr.Interface(fn=legal_chatbot, inputs=inputs, outputs=outputs, title="Lumilex",
             description="Ask legal questions and get answers.",
             theme="compact").launch(share=True)
