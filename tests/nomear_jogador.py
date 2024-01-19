


def nomear_jogador(simbolo: str, numero: int) -> str:
    
    """Checa se o nome do jogador é válido"""
    
    while True:
        
        print(f"\nJogador {numero} ({simbolo}), digite seu nome: ")
        
        nome_jogador = input().title()
        
        if nome_jogador != "":
            
            return nome_jogador
        
        print('Nome Inválido, digite novamente')