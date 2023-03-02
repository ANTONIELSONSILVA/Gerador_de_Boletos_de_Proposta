#Desenha arquivo PDF
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
import os
from reportlab.lib.units import cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont



pastaApp=os.path.dirname(__file__)

def desenhaQuadrado():
	pdf=canvas.Canvas(pastaApp+"\\modelo.pdf", pagesize=A4)
	
	# Quadrado maior
	pdf.rect(1.5*cm,5.9*cm,18.2*cm,10.5*cm)


	# Quadrado nome, logo da instituição Particdipante Destinatária
	pdf.rect(1.5*cm,15.1*cm,2.9*cm,1.3*cm)

	# canvas.drawImage(self, image, x,y, width=None,height=None,mask=None)
	pdf.drawImage('logo_bb.jpg', 1.6*cm, 15.2*cm, width=2.7*cm, height=1.1*cm)

	#pdf.String(150,100, 'Hello World', fontSize=18)


	# Quadrado Prefixo
	pdfmetrics.registerFont(TTFont('Vera', 'Vera.ttf'))
	pdf.rect(4.4*cm,15.1*cm,1.9*cm,1.3*cm)
	pdf.setFont('Vera', 17)
	pdf.drawString(4.5*cm,15.5*cm, "341-7")



	# Quadrado linha digitável
	pdf.rect(6.3*cm,15.1*cm,13.4*cm,1.3*cm)
	pdf.setFont('Vera', 10)
	pdf.drawString(7*cm,15.5*cm, "34191.09008 00704.270016 88294.080002 1 74190000009000")


	# Quadrado Aviso de boleto de proposta
	#pdf.rect(1.5*cm,10.7*cm,18.3*cm,0.6*cm)
	pdf.setFont('Vera', 8.3)
	pdf.drawString(8*cm,14.7*cm, "BOLETO DE PROPOSTA")
	pdf.drawString(1.6*cm,14.3*cm, "ESTE BOLETO SE REFERE A UMA PROPOSTA JPA FEITA A VOÇÊ E O SEU PAGAMENTO NÃO É OBRIGATÓRIO.")
	pdf.drawString(1.6*cm,14.0*cm, "Deixar de paga-lo não dará causa a proposta, a cobrança judicial ou extrajudicial, nem inserção de seu nome em cadastro")
	pdf.drawString(1.6*cm,13.7*cm, "de restrição de crédito.")
	pdf.drawString(1.6*cm,13.4*cm, "Pagar até o vencimento significa aceitar a proposta.")
	pdf.drawString(1.6*cm,13.1*cm, "Informações adicionaissobre a proposta e sobre o respectivo contrato poderão ser solicitadas a qualquer momento ao")
	pdf.drawString(1.6*cm,12.8*cm, "beneficiário, por meio de seus canais de atendimento.")


	# Quadrado Local de Pagamento
	pdf.rect(1.5*cm,10.7*cm,18.2*cm,0.6*cm)
	pdf.setFont('Vera', 6)
	pdf.drawString(1.6*cm,11.1*cm, "Local de Pagamento:")



	# Quadrado Nome do beneficiário
	pdf.rect(1.5*cm,10.1*cm,13.5*cm,0.6*cm)
	pdf.drawString(1.6*cm,10.5*cm, "Beneficiário:")


	# Quadrado Data de Vencimento
	pdf.rect(15*cm,10.1*cm,4.7*cm,0.6*cm)
	pdf.drawString(15.1*cm,10.5*cm, "Data de Vencimento")


	# Quadrado Data de Processamento
	pdf.rect(1.5*cm,9.3*cm,2.9*cm,0.8*cm)
	pdf.drawString(1.6*cm,9.9*cm, "Data de Processamento")

	# Quadrado N° do documento
	pdf.rect(4.4*cm,9.3*cm,2.2*cm,0.8*cm)
	pdf.drawString(4.5*cm,9.9*cm, "N° do documento")

	# Quadrado Nosso-número
	pdf.rect(6.6*cm,9.3*cm,2.5*cm,0.8*cm)
	pdf.drawString(6.7*cm,9.9*cm, "Nosso-número")


	# Quadrado Agência/Cod. Beneficiário
	pdf.rect(9.1*cm,9.3*cm,2.9*cm,0.8*cm)
	pdf.drawString(9.2*cm,9.9*cm, "Agência/Cod. Beneficiário")

	# Quadrado Carteira
	pdf.rect(12*cm,9.3*cm,3*cm,0.8*cm)
	pdf.drawString(12.1*cm,9.9*cm, "Carteira")

	# Quadrado Valor do Documento
	pdf.rect(15*cm,9.3*cm,4.7*cm,0.8*cm)
	pdf.drawString(15.1*cm,9.9*cm, "Valor do Documento")



	# Quadrado informações de responsabilidade do beneficiário
	pdf.rect(1.5*cm,7.9*cm,13.5*cm,1.4*cm)
	pdf.drawString(1.6*cm,9*cm, "Informações de responsabilidade do beneficiário:")


	# Quadrado Desconto/Abatimento
	pdf.rect(15*cm,8.6*cm,4.7*cm,0.7*cm)
	pdf.drawString(15.1*cm,9.1*cm, "Desconto/Abatimento")

	# Quadrado Valor Pago
	pdf.rect(15*cm,7.9*cm,4.7*cm,0.7*cm)
	pdf.drawString(15.1*cm,8.4*cm, "(=)Valor Pago")


	# Quadrado Nome do Pagador
	pdf.rect(1.5*cm,5.9*cm,18.2*cm,2*cm)
	pdf.drawString(1.6*cm,7.6*cm, "Pagador")

	pdf.drawString(1.6*cm,6*cm, "Sacador/Avalista")
	pdf.drawString(14*cm,5.6*cm, "Autentição Mecânica - Ficha de Compesação")

	pdf.save()


desenhaQuadrado()


