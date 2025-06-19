from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.utils import ImageReader
from reportlab.lib.colors import black
from django.core.files.base import ContentFile
from io import BytesIO
import os
from django.conf import settings

def generate_certificate_pdf(certificate):
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)
    width, height = A4

    bg_path = os.path.join(settings.BASE_DIR, 'static', 'certificate_bg.jpg')
    if os.path.exists(bg_path):
        c.drawImage(ImageReader(bg_path), 0, 0, width=width, height=height)

    student_name = certificate.student.full_name
    course_title = certificate.course.title
    center_name = certificate.center.name
    issue_date = certificate.issue_date.strftime('%d.%m.%Y')

    c.setFillColor(black)
    c.setFont("Helvetica-Bold", 28)
    c.drawCentredString(width / 2, height / 2 + 40, student_name)
    c.setFont("Helvetica", 20)
    c.drawCentredString(width / 2, height / 2, f"Kurs: {course_title}")
    c.drawCentredString(width / 2, height / 2 - 30, f"Markaz: {center_name}")
    c.drawCentredString(width / 2, height / 2 - 60, f"Berilgan sana: {issue_date}")

    c.showPage()
    c.save()

    buffer.seek(0)
    content = ContentFile(buffer.read())
    filename = f"certificate_{certificate.id}.pdf"
    certificate.certificate_file.save(filename, content)
    certificate.save()