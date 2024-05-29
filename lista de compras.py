#Cria uma lista vazia
lista = []

#Cria o laço de repetição
while True:
    #Coleta a opção do usuário
    option = input('O que deseja saber? \n[A]dicionar, [L]istar ou [S]air? ').upper()
    #Condições e comandos para adicionar produtos
    if option == 'A':
        while True:
            try:
                #Pergunta ao usuário que produto ele quer adicionar
                prod = input('Digite o item que gostaria de adicionar (Digite cancelar para parar de adicionar itens): ').upper()
                if prod == 'CANCELAR':
                    break
                else:
                    lista.append(prod)
                    print(f'Produto {prod} adicionado a lista!')
            except:
                print('Inserção inválida, digite novamente')
    #Conições para listar os produtos
    elif option == 'L':
        #Printa os itens da lista com seus índices
        if lista == []:
            print('Lista Vazia')
        else:
            for item in lista:
                print(lista.index(item), item)
    #Condição para sair do programa
    elif option == 'S':
        print('Fechando o programa')
        break
    #Informa se uma opção inválida foi digitada
    else:
        print('Opção inválida!')
