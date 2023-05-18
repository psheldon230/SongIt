import os
import openai


openai.api_key = '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'
completion = openai.Completion.create(
    engine="text-davinci-002",
    prompt="Tell the world about the ChatGPT API in the style of a pirate.",
    max_tokens=50,
)
print(completion.choices[0].text)

