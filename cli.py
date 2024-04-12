import os
os.environ['OPENAI_API_KEY'] = 'YOUR_API_KEY_HERE'
import sys
import json
from openai import OpenAI


def main():
    try:
        client = OpenAI()
        user_input = "User:   "
        while True:
            completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": "You are an intelligent assistant called ChatGPT. Introduce yourself, chat with clients, & help anyway you can."},
            {"role":"user", "content":user_input},])
            print("\n\nChatGPT: \n\n       {0}".format(completion.choices[0].message.content))
            user_input = input("\n\n                                                    User:   ")
    except KeyboardInterrupt:
        sys.exit(1)

    
if __name__ == "__main__":
    main()
    sys.exit(1)

