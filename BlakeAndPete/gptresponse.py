import os
import openai
import pickle

openai.api_key = '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'

while True:
    print("Welcome to SongIt\n")
    os.system("python3 NicksWork/runInterface.py")
    with open('BlakeAndPete/gptPrompt.pkl', 'rb') as f:
        # Load the data from the file using pickle.load()
        interface_output = pickle.load(f)
    content = interface_output

    print("\n")
    print("Great song combo! Generating your new song now.....\n\n")

    completion = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = [
            {"role": "user", "content": content}
        ]
    )

    print(completion.choices[0].message.content)
    continueResponse = input("Would you like to run SongIt again? Y or N\n")
    if continueResponse.strip().lower() == "y":
        print("Great! Starting again: \n")
    else:
        break
