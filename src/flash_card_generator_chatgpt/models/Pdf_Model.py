""" Define the pdf """
from PyPDF2 import PdfReader
import os

from decorators.timeit import timeit


class Pdf_Model:
    def __init__(self, pdf_pathfile) -> None:
        self.pdf_pathfile: str = pdf_pathfile
        self.pdf_content = []

    @timeit
    def read_pdf(self):
        if not os.path.exists(self.pdf_pathfile):
            raise ValueError("File does not exist")
        elif os.path.splitext(self.pdf_pathfile)[1] != ".pdf":
            raise ValueError("! File extension is not .PDF !")

        self.reader: object = PdfReader(self.pdf_pathfile)

    @timeit
    def extract_content_pdf(self):
        for page in self.reader.pages:
            text = page.extract_text()
            print(text)
            self.pdf_content.append(text)

    def __str__(self) -> str:
        return f""" Choose pdf.file : {self.pdf_pathfile}. 
        """
