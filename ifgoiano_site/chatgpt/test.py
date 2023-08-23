import openai, decouple

KEY = decouple.config('API_KEY')


def ask(*questions) -> str:
    msgs = list()
    for q in questions:
        msgs.append(
            {
                'role': 'user',
                'content': q
            }
        )
    response = openai.ChatCompletion.create(
        api_key=KEY,
        model='gpt-3.5-turbo',
        messages=msgs
    )
    return response['choices'][0]['message']['content']


if __name__ == '__main__':
    print(ask("Gambira is an unofficial kind of trending or exchange in Brazil, such that does not demand any written document or paper", "Based on context, what is a gambira in Brazil?"))
    