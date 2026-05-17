## Distribuição amostral e Intervalo de confiança
##Exemplo verificando alturas

salarios = dados['Salario']

media_amostral = np.mean(salarios) #calcular a média amostral

desvio_padrao_amostral = np.std(salarios, ddof=1) #calcular o desvio padrão amostral

nivel_confiaca = 0.95 #nível de confiança

tamanho_amostral = len(salarios) #tamanho da amostra
tamanho_amostral

from scipy import stats

erro_padrao = stats.sem(salarios) #calcular o erro padrão da média
erro_padrao

intervalo_confianca = stats.t.interval(nivel_confiaca, df=tamanho_amostral-1, loc=media_amostral, scale=erro_padrao) #calcular o intervalo de confiança

print(f"Intervalo de confiança: {intervalo_confianca}")

