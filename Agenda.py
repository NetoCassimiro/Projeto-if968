#arquivo = open("todo.txt","w+")
#arquivo.write("25062019 1850 (A) "+"Final de Estatística "+ "\n""21062019 2359 (A) "+"Entrega do projeto de @P1  + IF968" +"\n""01072019 1700 (A) "+"Prova de Programação " +"\n""(B) "+"Terminar artigo @IF762 + Pesquisa" +"\n""(D) "+"Terminar The Big Bang Theory @Casa"+"\n""(B) "+ "Concluir os cursos @Udemy + Pesquisa"+ "\n""(C) "+"Acordar Cedo" +"\n""(A) "+"Fazer exércícios @Emagrecer" +"\n""12072019 (F)"+" Viajar com Amanda,Aldo,Arthur @Taquaritinga"+ "\n""15072019 (E) "+"Comprar roupas @SantaCruzCapibaribe" +"\n""19072019 (E) "+"Voltar de Viajem @SantaCruzCapibaribe" +"\n""22072019 (F) "+"Passear com Sobrinhas Sophie,Fernanda,Julia,Vitoria @Shopping" +"\n""01082019 (A) "+"Ter três certificados @Udemy" +"\n""(Z) "+"Me atualizar nos animes @casa" +"\n""(B) "+"Arrumar Notebook @Assistencia" +"\n""05082019 (C) "+"Pegar Óculos Novos @Recife" +"\n""10082019 (A)"+" Sair pra jantar com Amanda @Sushi" +"\n""20082019 (A) "+"Ter perdido 10kg @Emagrecer" +"\n")
#arquivo.close()

import sys

TODO_FILE = 'todo.txt'
ARCHIVE_FILE = 'done.txt'

RED   = "\033[1;31m"
BLUE  = "\033[1;34m"
CYAN  = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD    = "\033[;1m"
REVERSE = "\033[;7m"
YELLOW = "\033[0;33m"

ADICIONAR = 'a'
REMOVER = 'r'
FAZER = 'f'
PRIORIZAR = 'p'
LISTAR = 'l'

# Imprime texto com cores. Por exemplo, para imprimir "Oi mundo!" em vermelho, basta usar
#
# printCores('Oi mundo!', RED)
# printCores('Texto amarelo e negrito', YELLOW + BOLD)

def printCores(texto, cor) :
  print(cor + texto + RESET)


def processarComandos(comandos) :
    if (comandos[1] == "a"):
        comandos.pop(0) # remove 'agenda.py'
        comandos.pop(0) # remove 'adicionar'
        itemParaAdicionar = organizar([' '.join(comandos)])[0]
        # itemParaAdicionar = (descricao, (prioridade, data, hora, contexto, projeto))
        adicionar(itemParaAdicionar[0], itemParaAdicionar[1]) # novos itens não têm prioridade
    elif (comandos[1] == "l"):
        listar()
    elif (comandos[1] == "r"):
        remover(comandos[2])
    elif comandos[1] == "f":
        fazer(comandos[2])
    elif comandos[1] == "p":
        priorizar(comandos[2],comandos[3])
    else :
        print("Comando inválido.")

def organizar(linhas):
    itens = []
    for x in range(0, len(linhas)):
        listaString = linhas[x].split()
        data = ""
        hora = ""
        pri = ""
        desc = ""
        contexto = ""
        projeto = ""
        if (dataValida(listaString[0])):
            data = listaString.pop(0)
        if (horaValida(listaString[0])):
            hora = listaString.pop(0)
        if (prioridadeValida(listaString[0])):
            pri = listaString.pop(0)
        while (projetoValido(listaString[-1])):
            projeto += listaString.pop(-1) + " "
        while (contextoValido(listaString[-1])):
            contexto += listaString.pop(-1) + " "
        for y in range(0, len(listaString)):
            desc += listaString[y] + " "
        itens.append((desc, (data, hora, pri, contexto, projeto)))

    # acima, função percorre todas as linhas do arquivo, e a cada linha ele testa a string para ver as informações "extras" são válidas e as adiciona nas variavéis locais
    # e na decrição  uso as strings restantes para formar a informação novamente e adiciono tudo na lista "itens"
    return itens



def criarListaLinhas():
    listaLinhas = [line.rstrip("\n") for line in open("todo.txt")]
    return listaLinhas

# (DESC, (DATA, HORA, PRI, CONTEXTO, PROJETO)).


def horaValida(string):
    if(len(string)!=4 or  not(str.isdigit(string)) or not(int(string[:2])>=0 and int(string[:2])<=23) or not(int(string[2:])>=0 and int(string[2:])<=59)):
        return False
    else:
        return True
    # primeiro vejo se a string tem 4 digitos, (str.isdigit) diz se a string é um dígito ou não, se não tiver 4 digitos e se não forem válidos retorna False
    # e também converte para inteiro e vê se o numero está entre 0 e 23 e para os minutos se está entre 0 e 59, se não satisfazer essa condição retorna False, de outra forma retorna True

def dataValida(string):
    if(len(string)!=8 or not(str.isdigit(string)) or not(int(string[4:])>=2018 and int(string[4:])<=2024)):
        return False
    # primeiro vejo se a string tem 8 digitos, (str.isdigit) diz se a string é um dígito ou não, se não tiver 8 digitos e não tiver entre o ano de 2018 até 2024 retorna False
    else:
        if (int(string[2:4])<=7):
            if (int(string[2:4])%2==1):
                if ((int(string[:2])>=1) and (int(string[:2])<=31)):
                    return True
                else:
                    return False
            elif (int(string[2:4])==2):
                if ((int(string[:2]) >= 1) and (int(string[:2]) <= 29)):
                    return True
                else:
                    return False
            else:
                if ((int(string[:2]) >= 1) and (int(string[:2]) <= 30)):
                    return True
                else:
                    return False
        else:
            if (int(string[2:4])%2==0):
                if ((int(string[:2])>=1) and (int(string[:2])<=31)):
                    return True
                else:
                    return False
            else:
                if ((int(string[:2]) >= 1) and (int(string[:2]) <= 30)):
                    return True
                else:
                    return False
    # No else eu trabalho os meses do ano, todos os meses impares até >=7 tem 31 dias, e os meses pares >=8 e <=12 também tem 31 dias.
    # de resto tirando o mês 2 todos os outros meses restantes tem 30 dias.

def projetoValido(string):
    if (len(string)>=2 and (string[0])=="+"):
        return True
    else:
        return False
#Acima ele vê se a string tem a string '+', se sim valida, se não retorna False

def contextoValido(string):
    if (len(string)>=2 and (string[0])=="@"):
        return True
    else:
        return False
    #Na função contexto ele lê as strings se achar o '@' ele valida, se não retorna False

def prioridadeValida(string):
    if(string[0]=="(" and string[2] ==")"):
        if(ord(string[1])>=ord("A") and ord(string[1])<= ord("Z")):
            return True
        else:
            return False
    else:
        return False

def adicionar(descricao,extras):
    if(descricao==''):
        print("Não foi possível escrever para o arquivo " + "todo.txt")
        return False
    else:
        desc = descricao
        data = ""
        hora = ""
        prioridade = ""
        contexto = ""
        projeto = ""
        finalform=""
        for x in range(0,len(extras)):
            if(not(extras[x]=="")):
                if(dataValida(extras[x])):
                    data=extras[x]
                if(horaValida(extras[x])):
                    hora=extras[x]
                if(prioridadeValida(extras[x])):
                    prioridade=extras[x]
                if(contextoValido(extras[x])):
                    contexto = extras[x]
                if (projetoValido(extras[x])):
                    projeto = extras[x]
        if(data!=""):
            finalform+=data+" "
        if(hora!=""):
            finalform+=hora+" "
        if(prioridade!=""):
            finalform+=prioridade+" "
        finalform+=desc+" "
        if(contexto!=""):
            finalform+=contexto+" "
        if(projeto!=""):
            finalform+=projeto
        with open("todo.txt", "r+") as f:
            d = f.readlines()
            f.seek(0)
            for x in range (0,len(d)):
                f.write(d[x])
            f.write(finalform+"\n")
            f.truncate()
            f.close()
    #Acima, eu crio as variáveis com string vazia, percorro o arquivo chamando cada função pra ver se as informações extras são válidas ou não,
    #e caso sejam eu as adiciono ao arquivo,e adiciono a descrição tbm, e exibo um erro caso a descrição, seja uma string vazia.

def listar():
    arquivo =open("todo.txt","r")
    linhas = criarListaLinhas()
#Crio uma lista de linhas do 'arquivo' completo.
    arquivo.close()
    organizada = organizar(linhas)
#evoco a função organizar na lista de linhas, devolvendo uma tupla no modelo pedido no projeto (desc, (data, hora, pri, contexto, projeto))
    ordenadaPorPrioridade=ordenarPorPrioridade(organizada)
#evoco a função ordenar por prioridade e retorno a tupla com a prioridade na frente, se houver a prioridade descrita.
    totalmenteOrdenada=ordenarPorDataHora(ordenadaPorPrioridade)
#evoco a função ordenar por hora e retorno a tupla com a hora na frente, se houver hora descrita.
    arquivo = open("todo.txt", "r")
    linhas = criarListaLinhas()
    arquivo.close()
    real = organizar(linhas)
    for x in range(0,len(totalmenteOrdenada)):
        formafinal=""
        for y in range(0,len(real)):
            if(totalmenteOrdenada[x][0]==real[y][0]):
                formafinal+=str(y)+" "
                break
    ###para cada elemento da lista ordenada acha a posição na agenda e adiciona na primeira posição da formafinal
    #######################
        if(totalmenteOrdenada[x][1][0]!=""):
            formafinal+=totalmenteOrdenada[x][1][0]+" "
    #CHECA SE EXISTE UMA DATA E SE HOUVER ADICIONA PRIMEIRA POSIÇÃO.
        if(totalmenteOrdenada[x][1][1] != ""):
            formafinal += totalmenteOrdenada[x][1][1] + " "
    #CHECA SE EXISTE UMA HORA E SE HOUVER ADICIONA PRIMEIRA POSIÇÃO.
        if(totalmenteOrdenada[x][1][2]!= ""):
            formafinal+=totalmenteOrdenada[x][1][2] + " "
    #CHECA SE EXITE UMA PRIORIDADE SE HOUVER, ADICIONA NA PRIMEIRA POSIÇÃO
        formafinal+=totalmenteOrdenada[x][0]+" "  #E FINALMENTE AO FINAL EU ADICIONO A INFORMAÇÃO EXISTENTE NA LISTAGEM NA PRIMEIRA POSIÇÃO
        if (totalmenteOrdenada[x][1][3] != ""):
            formafinal += totalmenteOrdenada[x][1][3] + " "
    #CHECA SE EXISTE O CONTEXTO E SE HOUVER ADICIONA NA POSIÇÃO POSTERIOR
        if (totalmenteOrdenada[x][1][4] != ""):
            formafinal += totalmenteOrdenada[x][1][4]
    #CHECA SE EXISTE UMA UM PROJETO E ADICIONA ELE NA POSIÇÃO POSTERIOR
        if(totalmenteOrdenada[x][1][2]=="A"):
            printCores(formafinal, RED + BOLD)
    # Defino as atividades com prioridade "A" em Vermelho
        elif(totalmenteOrdenada[x][1][2]=="B"):
            printCores(formafinal, YELLOW)
    # Defino as atividades com prioridade "B" em Amarelo
        elif (totalmenteOrdenada[x][1][2] == "C"):
            printCores(formafinal, GREEN)
    # Defino as atividades com prioridade "C" em Verde
        elif (totalmenteOrdenada[x][1][2] == "D"):
            printCores(formafinal, BLUE)
    # Defino as atividades com prioridade "D" em Azul
        else:
            print(formafinal)

def ordenarPorDataHora(listaDeTuplas):
    for l in range(0,len(listaDeTuplas)):
        atual = 0
        while atual < len(listaDeTuplas)-1:
            if(listaDeTuplas[atual][1][2]==listaDeTuplas[atual+1][1][2]):
                if(listaDeTuplas[atual][1][0]=="" and listaDeTuplas[atual+1][1][0]!=""):
                    temp = listaDeTuplas[atual]
                    listaDeTuplas[atual] = listaDeTuplas[atual + 1]
                    listaDeTuplas[atual + 1] = temp
                elif(listaDeTuplas[atual][1][0]==""):
                    nadaAconteceFeijoada=0
                elif(listaDeTuplas[atual+1][1][0]==""):
                    nadaAconteceFeijoada = 0
                elif(int(listaDeTuplas[atual][1][0][4:])>int(listaDeTuplas[atual+1][1][0][4:])):
                    temp = listaDeTuplas[atual]
                    listaDeTuplas[atual] = listaDeTuplas[atual + 1]
                    listaDeTuplas[atual + 1] = temp
                elif(int(listaDeTuplas[atual][1][0][4:])==int(listaDeTuplas[atual+1][1][0][4:])):
                    if(int(listaDeTuplas[atual][1][0][2:4])>int(listaDeTuplas[atual+1][1][0][2:4])):
                        temp = listaDeTuplas[atual]
                        listaDeTuplas[atual] = listaDeTuplas[atual + 1]
                        listaDeTuplas[atual + 1] = temp
                    elif(int(listaDeTuplas[atual][1][0][2:4])==int(listaDeTuplas[atual+1][1][0][2:4])):
                        if(int(listaDeTuplas[atual][1][0][:2])>int(listaDeTuplas[atual+1][1][0][:2])):
                            temp = listaDeTuplas[atual]
                            listaDeTuplas[atual] = listaDeTuplas[atual + 1]
                            listaDeTuplas[atual + 1] = temp
            if (listaDeTuplas[atual][1][2] == listaDeTuplas[atual + 1][1][2] and listaDeTuplas[atual][1][0]== listaDeTuplas[atual +1][1][0]):
                if (listaDeTuplas[atual][1][1] == "" and listaDeTuplas[atual + 1][1][1] != ""):
                    temp = listaDeTuplas[atual]
                    listaDeTuplas[atual] = listaDeTuplas[atual + 1]
                    listaDeTuplas[atual + 1] = temp
                elif (listaDeTuplas[atual][1][1] == ""):
                    nadaAconteceFeijoada = 0
                elif (listaDeTuplas[atual + 1][1][1] == ""):
                    nadaAconteceFeijoada = 0
                elif (int(listaDeTuplas[atual][1][1][:2]) > int(listaDeTuplas[atual + 1][1][1][:2])):
                    temp = listaDeTuplas[atual]
                    listaDeTuplas[atual] = listaDeTuplas[atual + 1]
                    listaDeTuplas[atual + 1] = temp
                elif (int(listaDeTuplas[atual][1][1][:2]) == int(listaDeTuplas[atual + 1][1][1][:2])):
                    if(int(listaDeTuplas[atual][1][1][2:]) > int(listaDeTuplas[atual + 1][1][1][2:])):
                        temp = listaDeTuplas[atual]
                        listaDeTuplas[atual] = listaDeTuplas[atual + 1]
                        listaDeTuplas[atual + 1] = temp
            atual=atual+1
    return listaDeTuplas



def ordenarPorPrioridade(listaDeTuplas):

    for l in range(0,len(listaDeTuplas)):
        atual = 0
        while atual < len(listaDeTuplas)-1:
            if(listaDeTuplas[atual][1][2]=="" and listaDeTuplas[atual+1][1][2]!=""):
                temp = listaDeTuplas[atual]
                listaDeTuplas[atual] = listaDeTuplas[atual + 1]
                listaDeTuplas[atual + 1] = temp
            elif (listaDeTuplas[atual][1][2] == ""):
                nadaAconteceFeijoada = 0
            elif(listaDeTuplas[atual+1][1][2]==""):
                nadaAconteceFeijoada=0
            elif(ord(listaDeTuplas[atual][1][2][1]) > ord(listaDeTuplas[atual + 1][1][2][1])):
                temp = listaDeTuplas[atual]
                listaDeTuplas[atual] = listaDeTuplas[atual + 1]
                listaDeTuplas[atual + 1] = temp
            atual = atual+1
    return listaDeTuplas

def remover(numero):
    num_linhas = sum(1 for line in open('todo.txt'))
    if(numero>num_linhas):
        print("erro")
    else:
        with open("todo.txt", "r+") as f:
            d = f.readlines()
            f.seek(0)
            for x in range (0,len(d)):
                if(x!=numero):
                    f.write(d[x])
            f.truncate()

def priorizar(numero,caractere):
    arquivo = open("todo.txt", "r+")
    linhas = criarListaLinhas()
    arquivo.close()
    real = organizar(linhas)
    num_linhas = sum(1 for line in open('todo.txt'))
    if (numero > num_linhas):
        print("erro")
    else:
        with open("todo.txt", "r+") as f:
            f.seek(0)
            for x in range (0,len(real)):
                if(x!=numero):
                    f.write((str(real[x][1][0] + " ") if (real[x][1][0] != "") else "") + (
                        str(real[x][1][1] + " ") if (real[x][1][1] != "") else "") + (
                                str(real[x][1][2] + " ") if (real[x][1][2] != "") else "") + str(real[x][0]) + " " + (
                                str(real[x][1][3] + " ") if (real[x][1][3] != "") else "") + (
                                str(real[x][1][4] + "") if (real[x][1][4] != "") else "") + "\n")

        # esse conjunto de ternário, não entrelaçados, checa se cada elemento opcional existe e o adiciona a linha a ser escrita, se não existir ignora a informação extra.
                else:
                    f.write((str(real[x][1][0] + " ") if (real[x][1][0] != "") else "") + (
                        str(real[x][1][1] + " ") if (real[x][1][1] != "") else "") + "(" + caractere + ") " + str(
                        real[x][0]) + " " + (str(real[x][1][3] + " ") if (real[x][1][3] != "") else "") + (
                               str(real[x][1][4] + "") if (real[x][1][4] != "") else "") + "\n")
        # Nesse else quando for a linha desugnada no primeiro parâmetro da função é feito a quase a mesma checagem, exceto pela prioridade que é modificada de acordo com a
        # entrada do segundo parâmetro da função ou adicionada a prioridade caso a mesma não exista.
            f.truncate()


def fazer(numero):
    num_linhas = sum(1 for line in open('todo.txt'))
    if (numero > num_linhas):
        print("erro")
    else:
        arquivo = open("todo.txt", "r+")
        linhas = criarListaLinhas()
        arquivo.close()
        file = open("done.txt","r+")
        file.write(linhas[numero] + "\n")
        file.close()
        remover(numero)

listar()