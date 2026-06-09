# SISTEMA SOLARIA - GLOBAL SOLUTION 2026
# INTEGRANTES: Guilherme Rosa - 569000, Luiz Izumi - 572328, Rafael Souza - 571628, Valéria Barbosa - 573829

from datetime import datetime

datas_coleta = [
    "01/06/2024", "02/06/2023", "03/06/2025", "04/06/2020", "05/06/2018", "06/06/2017", "07/06/2017", "08/06/2021", "09/06/2026", "10/06/2026",
    "11/06/2023", "12/06/2022", "13/06/2021", "14/06/2019", "15/06/2018", "16/06/2022", "17/06/2022", "18/06/2024", "19/06/2025", "20/06/2026"
]
historico_radiacao = [
    120.5, 130.0, 115.2, 140.1, 145.0, 155.3, 160.0, 142.1, 138.5, 125.0,
    110.0, 105.5, 135.0, 148.2, 152.0, 128.4, 118.9, 144.4, 139.0, 149.9
]
historico_temperatura = [
    45.0, 46.5, 44.0, 48.0, 49.5, 52.0, 53.5, 48.5, 47.0, 45.5,
    43.0, 42.5, 47.5, 50.0, 51.5, 46.0, 44.5, 49.0, 48.0, 49.8
]
status_alertas = [
    "Normal", "Normal", "Normal", "Normal", "Normal", "ALERTA", "ALERTA", "Normal", "Normal", "Normal",
    "Normal", "Normal", "Normal", "Normal", "ALERTA", "Normal", "Normal", "Normal", "Normal", "Normal"
]



def exibir_descricao():
    """Opção 1: Exibe a definição clara do problema e da solução"""
    print("\n" + "=" * 45)
    print(" PROJETO SOLARIA - DEFINIÇÃO DO PROBLEMA ")
    print("=" * 45)
    print("Problema: Tempestades solares podem causar apagões e destruir satélites.")
    print("Isso gera prejuízos bilionários e caos social em redes terrestres.")
    print("Solução: A Solaria é uma plataforma de inteligência preditiva.")
    print("Conectada a um microssatélite, ela monitora radiação em tempo real.")
    print("Seu objetivo é antecipar tempestades e emitir alertas críticos.")


def obter_numero_valido(mensagem):
    """Função auxiliar com uso de try/except e repetição (while)"""
    while True:
        try:
            valor = float(input(mensagem))
            if valor < 0:
                print("[ERRO] O valor não pode ser negativo. Tente novamente.")
                continue
            return valor
        except ValueError:
            print("[ERRO] Entrada inválida! Por favor, digite apenas números.")
            
def obter_data(mensagem):
    while True:
        data_digitada = input(mensagem).strip()
        try:
            datetime.strptime(data_digitada, "%d/%m/%Y")
            return data_digitada
        except ValueError:
            print("[ERRO] Entrada inválida! Por favor, digite a data no formato DD/MM/AAAA (ex: 15/08/2026).")

def ingerir_dados():
    """Opção 2: Recebe novos dados e adiciona às 4 listas globais."""
    print("\n--- INGESTÃO DE DADOS DO SATÉLITE ---")
    data_atual = obter_data("Digite a data da leitura (ex: 21/06/2020): ").strip()
    radiacao = obter_numero_valido("Digite o fluxo de radiação solar (W/m²): ")
    temperatura = obter_numero_valido("Digite a temperatura do sensor (°C): ")


    limite_seguro = 150.0
    status = "ALERTA" if radiacao > limite_seguro else "Normal"

    datas_coleta.append(data_atual)
    historico_radiacao.append(radiacao)
    historico_temperatura.append(temperatura)
    status_alertas.append(status)

    print(f"\n[SUCESSO] Dados salvos! Total de leituras no sistema: {len(historico_radiacao)}")


def triagem_alertas():
    """Opção 3: Varre as listas usando 'for' para mostrar os dados."""
    print("\n--- TRIAGEM E HISTÓRICO DE ALERTAS ---")


    for i in range(len(datas_coleta)):
        linha = f"Data: {datas_coleta[i]} | Radiação: {historico_radiacao[i]} W/m² | Temp: {historico_temperatura[i]} °C | Status: {status_alertas[i]}"

        if status_alertas[i] == "ALERTA":
            print(f"[!] {linha} [PERIGO]")
        else:
            print(f"[-] {linha}")


def simular_cenario_historico():
    """Opção 4: Carrega dados do Evento de Carrington de 1859."""
    print("\n--- SIMULADOR DE CENÁRIOS HISTÓRICOS ---")
    print("Carregando dados do Evento de Carrington (1859)...")


    datas_coleta.append("01/09/1859")
    historico_radiacao.append(850.0)
    historico_temperatura.append(120.0)
    status_alertas.append("ALERTA MÁXIMO")

    print("Leitura de radiação extrema (850.0 W/m²) simulada com sucesso!")
    print("[AVISO] Verifique a Opção 3 para ver o comportamento do sistema!")


def emitir_relatorio():
    """Opção 5: Exibe recomendações com base no setor com match/case."""
    print("\n--- RELATÓRIO DE PREVISÃO E MITIGAÇÃO ---")
    print("1 - Setor de Energia (Distribuidoras)")
    print("2 - Setor de Telecomunicações / Satélites")

    setor = input("Selecione o setor para visualizar o plano de contingência: ").strip()


    match setor:
        case "1":
            print("\n[PLANO DE MITIGAÇÃO - ENERGIA]")
            print("Ação imediata: Isolar subestações de energia e acionar geradores de backup.")
            print("Tempo estimado até o impacto na Terra: 14 minutos.")
        case "2":
            print("\n[PLANO DE MITIGAÇÃO - TELECOM]")
            print("Ação imediata: Orientar satélites em órbita para o modo de segurança (Safe Mode).")
            print("Tempo estimado até o impacto na Terra: 14 minutos.")
        case _:
            print("[ERRO] Setor inválido.")


# ==========================================
# LOOP PRINCIPAL DO MENU
# ==========================================
while True:
    print("\n" + "=" * 45)
    print("         S O L A R I A  -  DASHBOARD         ")
    print("=" * 45)
    print("1. Descrição do Problema e Solução")
    print("2. Ingestão de Dados do Satélite")
    print("3. Triagem e Histórico Geral")
    print("4. Simulador de Cenários Históricos")
    print("5. Relatório de Previsão e Mitigação")
    print("6. Sair do Sistema")
    print("=" * 45)

    opcao = input("Escolha uma opção (1-6): ").strip()

    if opcao == "1":
        exibir_descricao()
    elif opcao == "2":
        ingerir_dados()
    elif opcao == "3":
        triagem_alertas()
    elif opcao == "4":
        simular_cenario_historico()
    elif opcao == "5":
        emitir_relatorio()
    elif opcao == "6":
        print("\nEncerrando o sistema Solaria. Monitoramento finalizado com segurança.")
        break
    else:
        print("\n[ERRO] Opção inválida! Digite um número de 1 a 6.")

