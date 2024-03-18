import random
import os
from docx import Document
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from PIL import Image, ImageDraw, ImageFont
from reportlab.lib import colors


def get_file_name():
    return f"file_{random.randint(1000000, 99999999)}"


def dict_to_pdf(data_dict, filename='default_name.pdf'):
    filename = get_file_name() + '.pdf'
    file_path = os.path.join('media', 'PDF', filename)

    doc = SimpleDocTemplate(file_path, pagesize=letter)
    table_data = []

    for key, value in data_dict.items():
        table_data.append([str(key), str(value)])

    table = Table(table_data)
    style = TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                        ('GRID', (0, 0), (-1, -1), 1, colors.black)])

    table.setStyle(style)
    doc.build([table])
    return file_path


def dict_to_word(data_dict, filename='default_name.docx'):
    filename = get_file_name() + '.docx'
    file_path = os.path.join('media', 'Word', filename)

    doc = Document()

    table = doc.add_table(rows=1, cols=2)
    table.style = 'Table Grid'
    hdr_cells = table.rows[0].cells
    hdr_cells[0].text = 'Key'
    hdr_cells[1].text = 'Value'

    for key, value in data_dict.items():
        row_cells = table.add_row().cells
        row_cells[0].text = str(key)
        row_cells[1].text = str(value)

    doc.save(file_path)
    return file_path


def dict_to_img(data_dict, filename='default_name.png'):
    image_width = 800
    image_height = 600
    font_size = 20
    font = ImageFont.truetype("arial.ttf", font_size)
    line_spacing = font.getsize("A")[1] + 10

    img = Image.new('RGB', (image_width, image_height), color='white')
    draw = ImageDraw.Draw(img)

    y_position = 10
    for key, value in data_dict.items():
        draw.text((10, y_position), str(key), fill='black', font=font)
        draw.text((400, y_position), str(value), fill='black', font=font)
        y_position += line_spacing

    filename = filename.split('.')[0] + '.png'
    file_path = os.path.join('media', 'images', filename)
    img.save(file_path)

    return file_path


def dict_to_txt(data_dict, filename='default_name.txt'):
    filename = filename.split('.')[0] + '.txt'
    file_path = os.path.join('media', 'text', filename)

    with open(file_path, 'w') as file:
        for key, value in data_dict.items():
            file.write(f"{key}: {value}\n")

    return file_path


def get_generate(file_type: str, data: dict):
    if file_type == 'pdf':
        path = dict_to_pdf(data_dict=data)
        return path
    elif file_type == 'word':
        path = dict_to_word(data_dict=data)
        return path
    else:
        return None
