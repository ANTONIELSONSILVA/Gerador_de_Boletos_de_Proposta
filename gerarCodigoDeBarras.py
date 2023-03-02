#gerarCódigoDeBarras

def gerarCodigoDeBarra():

	# Para inserção dos dados na função de geração do código de barras, obedecer a ordem das variáveis. 
	
	Cod_Banco = 0    # BB 001
	Cod_Moeda = 0    # 9 (Real)
	DigitoVerificado = CalcularDigitoVerificador() # Para calcular o DV considerar 43 posições do Código de Barras sendo da posição 1 a 4 e da posição 6 a 44; 
												   # Instruções presentes na página 16 da normativa de geração

	# Nosso-número = Número do Convênio e Complemento
	NossoNumero = getNossoNumero() # Deve ser verificado o número de posições fornecidas pelo banco 4, 6, 7, 11. 

