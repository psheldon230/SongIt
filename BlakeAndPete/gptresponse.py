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

    more_instructions = input("What specific direction do you want this song to have?: \n ")

    print("\n")
    print("Great song combo! Generating your new song now.....\n\n")

    new_content = content + more_instructions
    print(new_content)
    completion = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = [
            {"role": "user", "content": new_content}
        ]
    )

    gpt_response = completion.choices[0].message.content
    print(gpt_response)
    keepGoing = input("Would you like to change anything about the song? Y or N")
    if keepGoing.lower() == "y":
        changing = True
        while changing:
            continueResponse = input("What would you like to change about this song? ")
            new_prompt = "Here is your previous output: " + gpt_response + "Return the same output, but with the following changes: " + continueResponse
            print("Working....")
            completion = openai.ChatCompletion.create(
                model = "gpt-3.5-turbo",
                messages = [
                    {"role": "user", "content": new_prompt}
                ]
            )
            gpt_response = completion.choices[0].message.content

            print(gpt_response)
            inp = input("Would you like to keep changing the Song? Y or N")
            if inp.lower() == "n":
                changing = False
