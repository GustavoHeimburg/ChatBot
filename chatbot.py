import openai

chave_api = "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"
openai.api_key = chave_api

def enviar_chat(chat):
    resposta = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": chat}
        ],
    )

    return resposta.choices[0].message.content

pergunta = "Como tratar ferimentos?"
resposta = enviar_chat(pergunta)
print(resposta)


