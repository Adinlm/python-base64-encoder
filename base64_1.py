import base64

with open("resume_AdinLopez.pdf", "rb") as pdf_file:
    encoded_string = base64.b64encode(pdf_file.read()).decode('utf-8')

print(encoded_string)