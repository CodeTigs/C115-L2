import time


def chatbot():
    while True:
        exibir_menu()
        escolha = input("Digite o número correspondente à sua escolha ou descreva o problema: ").lower()

        if "1" in escolha or "internet" in escolha or "rede" in escolha:
            problemas_internet()
        
        elif "2" in escolha or "wifi" in escolha or "conexão" in escolha:
            problemas_wifi()
        
        elif "3" in escolha or "falar com atendente" in escolha:
            falar_com_atendente()

        elif "4" in escolha or "consultar planos" in escolha or "planos" in escolha:
            consultar_planos()

        elif "5" in escolha or "sair" in escolha or "encerrar" in escolha or "exit" in escolha:
            if encerrar_atendimento():
                break  

        else:
            print("Desculpe, não entendi sua solicitação. Por favor, tente novamente.")
        
        time.sleep(3)
        print("\n--- Conexão encerrada ---\n")

# Executar o chatbot
chatbot()