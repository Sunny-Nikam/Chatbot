import openai

openai.api_key = "key"

messages = []
system_msg = input("hello\n")
messages.append({"role": "system", "content": system_msg})

print("How can i help you?")
while input != "quit()":
    message = input()
    messages.append({"role": "user", "content": message})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages)
    reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": reply})
    print("\n" + reply + "\n")