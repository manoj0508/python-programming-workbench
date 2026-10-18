from openai import OpenAI


def main() -> None:
    with open("openapiKey.txt") as key_file:
        openai_api_key = key_file.read().strip()
    client = OpenAI(api_key=openai_api_key)

    history = []
    system_message = """You are known to be polite and helpful AI BOT.
                                                                  Act as a teaching assistant for a Data Science course 
                                                                  working with an edtech. Your job here is to help students
                                                                  resolve their doubts regarding specific data science topics.
                                                                  If the doubt is not relevant to data science, you can politely 
                                                                  ask user another doubt and don't give answer for that particular question."""

    while True:
        user_input = input("User : ")
        if user_input.lower() in ["bye", "close", "exit", "quit"]:
            break
        response = chat_bot(client, user_input, history, system_message)
        print("*AI 🙂: ", response)


def chat_bot(client, prompt, history, system_message):
    history.append({"role": "user", "content": prompt})
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "system", "content": system_message}] + history,
    )
    answer = response.choices[0].message.content
    history.append({"role": "assistant", "content": answer})
    return answer



if __name__ == "__main__":
    main()