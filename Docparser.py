from docx import Document
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from docx_form import DocxForm

full_path = r"C:\Users\sathw\Desktop\Notice Template.docx"
doc = Document(full_path)
doc_elm = doc.element
contentControls = doc_elm.xpath('.//w:ffData')
print(contentControls)