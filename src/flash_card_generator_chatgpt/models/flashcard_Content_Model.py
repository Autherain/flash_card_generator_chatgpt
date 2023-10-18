"""Define GPT response"""


class Flashcard_Content_Model:
    def __init__(self) -> None:
        self.flashcard_content = []

    def append(self, gpt_response):
        if not isinstance(gpt_response, str):
            raise ValueError("La réponse de GPT n'est pas un STRING")
        self.flashcard_content.append(gpt_response)

    def __str__(self) -> str:
        backslash = "\n"

        return rf"""
Generated flashcards => 
{backslash.join(map(str, self.flashcard_content))}"""
