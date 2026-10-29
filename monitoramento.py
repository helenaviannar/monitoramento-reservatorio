from colorama import Fore, Style, init

# Inicializa o colorama (necessário para compatibilidade com o terminal do Windows)
init()

# 1. Utilizando uma lista para armazenar as mensagens dos níveis do reservatório
mensagens_reservatorio = [
    "Nível 1: Muito baixo (crítico)",
    "Nível 2: Baixo",
    "Nível 3: Médio",
    "Nível 4: Alto",
    "Nível 5: Muito alto (alerta)"
]

# 2. Função responsável por definir a cor da mensagem conforme o nível
def definir_cor_alerta(nivel):
    """
    Retorna a cor correspondente baseada no nível da água (1 a 5).
    """
    if nivel == 1:
        return Fore.RED      # Vermelho
    elif nivel == 2:
        return Fore.YELLOW   # Amarelo
    elif nivel == 3:
        return Fore.GREEN    # Verde
    elif nivel == 4:
        return Fore.CYAN     # Ciano
    elif nivel == 5:
        return Fore.BLUE     # Azul
    else:
        return Fore.WHITE    # Cor padrão para níveis desconhecidos

# 3. Função principal para simular o monitoramento
def simular_monitoramento():
    print("Iniciando simulação de monitoramento do reservatório...\n")
    
    # Percorre a lista simulando o aumento do nível da água
    for indice in range(len(mensagens_reservatorio)):
        nivel_atual = indice + 1
        mensagem = mensagens_reservatorio[indice]
        
        # Puxa a cor através da função criada
        cor = definir_cor_alerta(nivel_atual)
        
        # Exibe a mensagem colorida e restaura o estilo padrão com Style.RESET_ALL
        print(f"{cor}{mensagem}{Style.RESET_ALL}")
        
    print("\nSimulação concluída. Estilo do terminal restaurado.")

# Executa o programa
if __name__ == "__main__":
    simular_monitoramento()