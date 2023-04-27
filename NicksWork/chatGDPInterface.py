import os
import openai


openai.api_key = "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"
completion = openai.Completion.create(
    engine="text-davinci-002",
    prompt="Tell the world about the ChatGPT API in the style of a pirate.",
    max_tokens=50,
)
print(completion.choices[0].text)

