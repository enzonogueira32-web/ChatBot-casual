import re

responses = {
    "oi": "Olá, seja bem vindo! Como posso ajudar você hoje?",
    "ola": "Olá! Como posso ajudar você hoje?",
    "tudo bem": "Tudo bem, e com você?",
    "como voce esta": "Estou bem, obrigado por perguntar!",
    "adeus": "Até mais! Foi um prazer conversar com você.",
    "obrigado": "De nada! Estou aqui para ajudar.",
    "valeu": "Por nada! Se precisar de mais alguma coisa, é só falar.",
    "ajuda": "Diga o que você precisa e eu tentarei ajudar.",
}

fallback_response = (
    "Desculpe, não entendi. Você pode reformular? "
    "Tente algo como 'oi', 'tudo bem', 'ajuda', ou 'adeus'."
)

quit_commands = {"sair", "tchau", "adeus", "quit", "exit"}


def normalize(text: str) -> str:
    text = text.strip().lower()
    text = re.sub(r"[^a-z0-9çãõáéíóúâêîôûàèìòù ]", "", text)
    return text


def get_response(user_input: str) -> str:
    text = normalize(user_input)
    if text in quit_commands:
        return "Até logo!"

    for key, response in responses.items():
        if key in text:
            return response

    return fallback_response


def main() -> None:
    print("Chatbot simples iniciado. Digite 'sair' para encerrar.")
    while True:
        user_input = input("Você: ").strip()
        if not user_input:
            continue

        response = get_response(user_input)
        print(f"Bot: {response}")

        if normalize(user_input) in quit_commands:
            break


if __name__ == "__main__":
    main()
