from models.Pdf_Model import Pdf_Model
from controllers.base import Controller
from views.base import View

import sys

import argparse

parser = argparse.ArgumentParser(
    prog="PDF_to_flashcard",
    description="""
    Script will use openAI chatGPT API to transcribe a local .pdf into flashcards.
    Don't forget to add your chatGPT API key
    """,
    epilog="""Have a nice day :)""",
)
parser.add_argument("pdf_path", help="Path need to be absolute with /home/etc...")
args = parser.parse_args()


def main():
    if len(sys.argv) >= 3 or len(sys.argv) == 0:
        raise ValueError("Only 1 argument is authorized")
    else:
        pdf_path = sys.argv[1]

    view = View()

    pdf_model = Pdf_Model(pdf_path)

    Controller(pdf_model, view).run()


if __name__ == "__main__":
    main()
