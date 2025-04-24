# Lista para armazenar os gastos 
gastos = []

# Carga os gastos salvos
try:
    with open("gastos.txt" "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            descricao,valor = linha.strip().split(",")
            gastos.append((descricao,float(valor)))
except FileExistsError:
    pass

# Menu principal
while True:
    print("\n--- Controle de Gastos Pessoais ---")
    print("1 - Adicionar Gasto")
    print("2 - Ver todos os gastos")
    print("3 - Zerar a lista de gastos")
    print("4 - Sair")

    opcao = input("Escolha uma opção (1-4):")

    if opcao == "1":
        descricao = input("Descrição do gasto:")
        valor = float(input("Valor do gasto: R$"))
        gastos.append({"descricao":descricao,"valor":valor})

        # Salvar o arquivo
        with open("gastos.txt" , "a", encoding="utf-8") as arquivo: arquivo.write(f"{descricao},{valor}\n")

        print("Gasto registrado com sucesso!")  
    
    elif opcao == "2":
        if not gastos:
            print("Nenhum gasto registrado ainda.")
        else:
            print("\n--- Lista de Gastos---")
            total = 0
            for i, gasto in enumerate(gastos,start=1):
                print(f"{i}. {gasto['descricao']} - R${gasto['valor']:.2f}")
                total += gasto["valor"]
            print(f"\nTotal gasto: R${total:.2f}")
    
    elif opcao == "3":
        gastos.clear()
        # Limpar o arquivo
        with open("gastos.txt" , "w", encoding="utf-8"):
            pass
        print("Todos os gastos foram apagados com sucesso.")
    
    elif opcao == "4":
        print("Saindo...Até Logo!")
        break
    else:
        print("Opção Inválida. Tente Novamente.")
        