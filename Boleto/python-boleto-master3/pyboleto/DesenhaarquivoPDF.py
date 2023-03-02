#Desenha arquivo PDF
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

def desenhaQuadrado():
	pdf=canvas.Canvas("modelo.pdf", pagesize=A4)
	cnv.save()


