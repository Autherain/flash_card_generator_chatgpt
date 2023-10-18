import openai
import os

from models.Pdf_Model import Pdf_Model
from models.flashcard_Content_Model import Flashcard_Content_Model
from pathlib import PurePath
import json

from decorators.timeit import timeit


class GPT_Communication_Model:
    def __init__(self, pdf_model: Pdf_Model) -> None:
        self.pdf_model = pdf_model

        self.Flashcard_content_model = Flashcard_Content_Model()

    def get_message(self, text_content: str):
        return [
            {"role": "system", "content": "You are a helpful assistant."},
            {
                "role": "user",
                "content": f"Create anki flashcards with the following text using a format like question;answer next line question;answer etc...{text_content}.",
            },
        ]

    def get_api_key(self):
        config_file_path = PurePath(__file__).parents[3].joinpath("config.json")

        json_content = json.load(open(config_file_path))
        self.api_key = json_content["api_gpt_key"]

    def set_api_key(self):
        openai.api_key = self.api_key

    @timeit
    def get_response_from_gpt(self):
        for pdf_content in self.pdf_model.pdf_content:
            try:
                gpt_answer_content = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=self.get_message(pdf_content),
                )

                self.Flashcard_content_model.append(
                    gpt_answer_content["choices"][0]["message"]["content"]
                )

            except Exception as e:
                # The code 1 will terminate the code without executing anything else
                raise e

    def write_response(self):
        # Get filename and extension separately
        filename, ext = os.path.splitext(os.path.basename(self.pdf_model.pdf_pathfile))

        # Get filename without extension
        name_only = filename.split(".")[0]

        with open(
            rf"../../generated_card/{os.path.basename(name_only).split('/')[-1]}_flashcard.txt",
            "w",
        ) as fp:
            fp.write("\n".join(self.Flashcard_content_model.flashcard_content))
