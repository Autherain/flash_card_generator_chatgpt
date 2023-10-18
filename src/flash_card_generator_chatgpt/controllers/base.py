from models.Pdf_Model import Pdf_Model
from models.GPT_Communication_Model import GPT_Communication_Model
from views.base import View


class Controller:
    def __init__(self, pdf_model: Pdf_Model, view: View) -> None:
        self.Pdf_Model = pdf_model

        self.conversation = GPT_Communication_Model(self.Pdf_Model)

        self.view = view

    def run(self):
        # self.view.show_pathfile()

        self.view.show_pdf_pathfile(self.Pdf_Model)

        self.Pdf_Model.read_pdf()
        self.Pdf_Model.extract_content_pdf()

        self.conversation.get_api_key()

        # self.view.established_connection()

        self.conversation.get_response_from_gpt()
        self.conversation.write_response()

        self.view.show_generated_flashcard(self.conversation.Flashcard_content_model)

        # self.view.show_located_file()
