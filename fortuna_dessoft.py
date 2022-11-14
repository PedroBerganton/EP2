n=input("Qual é seu nome?")
print()




quest = [{'titulo': 'Qual o resultado da operação 57 + 32?',
          'nivel': 'facil',
          'opcoes': {'A': '-19', 'B': '85', 'C': '89', 'D': '99'},
          'correta': 'C'},

         {'titulo': 'Qual a capital do Brasil?',
          'nivel': 'facil',
          'opcoes': {'A': 'Brasília', 'B': 'Rio de janeiro', 'C': 'São Paulo', 'D': 'Osasco'},
          'correta': 'A'},

         {'titulo': 'Quando é o feriado da Independência do Brasil?',
          'nivel': 'facil',
          'opcoes': {'A': '21 de Abril', 'B': '12 de Outubro', 'C': '07 de Setembro', 'D': '15 de Novembro'},
          'correta': 'C'},

         {'titulo': '_________ é um conjunto de particularidades que caracterizam um grupo de pessoas, uma família ou uma sociedade. É formada por princípios morais, hábitos, costumes, histórias, manifestações religiosas, entre outros. Qual palavra melhor completa o início da frase?',
          'nivel': 'facil',
          'opcoes': {'A': 'Missão', 'B': 'Cultura', 'C': 'Curso superior', 'D': 'Culinária'},
          'correta': 'B'},

         {'titulo': 'Qual destes termos menos tem relação com o fenômeno da globalização?',
          'nivel': 'facil',
          'opcoes': {'A': 'Aculturação', 'B': 'Neoliberalismo', 'C': 'União Europeia', 'D': 'Caldeirão do Huck'},
          'correta': 'D'},

         {'titulo': 'Qual o feriado do aniversário da cidade de São Paulo?',
          'nivel': 'facil',
          'opcoes': {'A': '25 de Janeiro', 'B': '24 de Março', 'C': '9 de Julho', 'D': '12 de Novembro'},
          'correta': 'A'},

         {'titulo': 'Qual destas não é uma fruta?',
          'nivel': 'facil',
          'opcoes': {'A': 'Laranja', 'B': 'Maça', 'C': 'Tomate', 'D': 'Abacate'},
          'correta': 'B'},

         {'titulo': 'Em qual ano o TikTok atingiu 1 bilhão de usuários?',
          'nivel': 'facil',
          'opcoes': {'A': '2019', 'B': '2021', 'C': '2015', 'D': '2018'},
          'correta': 'B'},
         
         {'titulo': 'Qual destes não é um app com foco em streaming de vídeo?',
          'nivel': 'facil',
          'opcoes': {'A': 'Netflix', 'B': 'Disney Plus', 'C': 'TIDAL', 'D': 'HBO Max'},
          'correta': 'C'},

         {'titulo': 'Qual destes parques não se localiza em São Paulo?!',
          'nivel': 'facil',
          'opcoes': {'A': 'Ibirapuera', 'B': 'Parque do Carmo', 'C': 'Parque Villa Lobos', 'D': 'Morro da Urca'},
          'correta': 'D'},

         {'titulo': 'Qual destas não é uma linguagem de programação?',
          'nivel': 'facil',
          'opcoes': {'A': 'Miratdes', 'B': 'Python', 'C': 'Lua', 'D': 'C++'},
          'correta': 'A'},

         {'titulo': 'Dentre os listados, qual destes esportes é menos praticado no Brasil?',
          'nivel': 'facil',
          'opcoes': {'A': 'Natação', 'B': 'Vôlei', 'C': 'Ski Cross Country', 'D': 'Futebol'},
          'correta': 'C'},
         
         {'titulo': 'Qual o resultado da operação 5 + 2 * 3?',
          'nivel': 'medio',
          'opcoes': {'A': '21', 'B': '11', 'C': '30', 'D': '10'},
          'correta': 'B'},

         {'titulo': 'Qual destas é uma pseudociência que estuda os corpos celestes e as prováveis relações que possuem com a vida das pessoas e os acontecimentos na Terra?',
          'nivel': 'medio',
          'opcoes': {'A': 'Astronomia', 'B': 'Física quântica', 'C': 'Astrologia', 'D': 'Computação'},
          'correta': 'C'},

         {'titulo': 'Qual destas não foi considerada em 2007 uma das sete maravilhas do mundo moderno?',
          'nivel': 'medio',
          'opcoes': {'A': 'Muralha da China', 'B': 'Machu Picchu', 'C': 'Cristo Redentor', 'D': 'Torre Eiffel'},
          'correta': 'D'},

         {'titulo': 'Qual destas pessoas conduziu importantes estudos sobre radioatividade, sendo ganhadora de dois prêmios Nobel?',
          'nivel': 'medio',
          'opcoes': {'A': 'Marie Curie', 'B': 'Paul Erdős', 'C': 'Clive W.J. Granger', 'D': 'Maria Ressa'},
          'correta': 'A'},

         {'titulo': 'Quem é considerada a primeira pessoa programadora do mundo?!',
          'nivel': 'medio',
          'opcoes': {'A': 'Marie Curie', 'B': 'Alan Turing', 'C': 'Ada Lovelace', 'D': 'Edsger Dijkstra'},
          'correta': 'C'},

         {'titulo': 'Qual destes números é primo?',
          'nivel': 'medio',
          'opcoes': {'A': '259', 'B': '85', 'C': '49', 'D': '19'},
          'correta': 'D'},

         {'titulo': 'Na Conjectura de _______, escolhendo-se um número natural inicial n, onde n > 0, os seguintes critérios serão obedecidos: Se n for par o seu sucessor será a metade e se n for ímpar o seu sucessor será o triplo mais um, gerando então um novo número. Qual o nome da conjectura?',
          'nivel': 'medio',
          'opcoes': {'A': 'Collatz', 'B': 'Goldbach', 'C': 'Poincaré', 'D': 'Hodge'},
          'correta': 'A'},

         {'titulo': 'Como faço para chamar o SAMU?',
          'nivel': 'medio',
          'opcoes': {'A': 'Ligue 101', 'B': 'Ligue 192', 'C': 'Ligue 109', 'D': 'Ligue 122'},
          'correta': 'B'},

         {'titulo': 'Qual a segunda pessoa mais seguida no Instagram?',
          'nivel': 'medio',
          'opcoes': {'A': 'Cristiano Ronaldo', 'B': 'Dwayne Johnson', 'C': 'Kim Kardashian', 'D': 'Kylie Jenner'},
          'correta': 'D'},

         {'titulo': 'Qual a pessoa mais seguida no Instagram?',
          'nivel': 'medio',
          'opcoes': {'A': 'Cristiano Ronaldo', 'B': 'Dwayne Johnson', 'C': 'Kim Kardashian', 'D': 'Lionel Messi'},
          'correta': 'A'},

         {'titulo': 'A reprodução dos seres vivos é um processo biológico através do qual os organismos geram descendência. Qual desta não é uma forma de reprodução assexuada?',
          'nivel': 'dificil',
          'opcoes': {'A': 'Autogamia', 'B': 'Esporulação', 'C': 'Partenogênese', 'D': 'Divisão binária'},
          'correta': 'A'},

         {'titulo': 'Qual o resultado da operação 5 + 2 * 3 ^ 2, onde ^ representa potenciação?',
          'nivel': 'dificil',
          'opcoes': {'A': '441', 'B': '86', 'C': 'Nenhuma das outras respostas', 'D': '23'},
          'correta': 'D'},

         {'titulo': 'Quem é Oxóssi?!',
          'nivel': 'dificil',
          'opcoes': {'A': 'Rede de mercados', 'B': 'Tipo de poema Dissílabo', 'C': 'Divindade das religiões africanas', 'D': 'Trapper brasileiro'},
          'correta': 'C'},

         {'titulo': 'Qual a altura do Cristo Redentor?',
          'nivel': 'dificil',
          'opcoes': {'A': 'entre 0 e 20 metros', 'B': 'Entre 21 e 40 metros', 'C': 'Entre 41 e 60 metros', 'D': 'Mais que 60 metros'},
          'correta': 'B'},

         {'titulo': 'Em que ano faleceu Charles Babbage?',
          'nivel': 'dificil',
          'opcoes': {'A': '2022', 'B': '1791', 'C': '1935', 'D': '1871'},
          'correta': 'A'},

         {'titulo': 'Einstein foi Nobel de física em qual ano?',
          'nivel': 'dificil',
          'opcoes': {'A': '1906', 'B': '1905', 'C': '1920', 'D': '1921'},
          'correta': 'D'},

         {'titulo': 'Qual o número atômico do nitrogênio?',
          'nivel': 'dificil',
          'opcoes': {'A': '9', 'B': '7', 'C': '6', 'D': '8'},
          'correta': 'B'},

         {'titulo': 'Qual o ponto de fusão do nitrogênio?',
          'nivel': 'dificil',
          'opcoes': {'A': '120º C', 'B': '15º C', 'C': '-210º C', 'D': '-180º C'},
          'correta': 'C'},
         
         {'titulo': 'Quantos gols Pelé fez oficialmente?',
          'nivel': 'dificil',
          'opcoes': {'A': '815', 'B': '762', 'C': '1100', 'D': '1057'},
          'correta': 'B'},

         {'titulo': 'O que é Necrose?',
          'nivel': 'dificil',
          'opcoes': {'A': 'Uma banda de Rock', 'B': 'Uma marca de luxo', 'C': 'Cidade Francesa', 'D': 'Morte de tecido orgânico'},
          'correta': 'D'},

          {'titulo': 'Quem era o presidente do Brasil em 1953?',
          'nivel': 'medio',
          'opcoes': {'A': 'Dilma', 'B': 'JK', 'C': 'Getulio Vargas', 'D': 'FHC'},
          'correta': 'C'},

          {'titulo': 'O que é Necrose?',
          'nivel': 'dificil',
          'opcoes': {'A': 'Uma banda de Rock', 'B': 'Uma marca de luxo', 'C': 'Cidade Francesa', 'D': 'Morte de tecido orgânico'},
          'correta': 'D'},

         {'titulo': 'Quem era o presidente do Brasil em 1953?',
         'nivel': 'medio',
        'opcoes': {'A': 'Dilma', 'B': 'JK', 'C': 'Getulio Vargas', 'D': 'FHC'},
        'correta': 'C'},

        {'titulo': 'Onde fica o Egito?',
        'nivel': 'facil',
        'opcoes': {'A': 'Norte da Africa', 'B': 'Oeste Europeu', 'C': 'Sul da Afica', 'D': 'Nordeste Asiatico'},
        'correta': 'A'},

        {'titulo': 'Há quantos anos terminou a segunda Guerra Mundial?',
        'nivel': 'facil',
        'opcoes': {'A': '70 anos', 'B': '77 anos', 'C': '65 anos', 'D': '34 anos'},
        'correta': 'B'},

        {'titulo': 'Qual é o ano da Independência do Brasil?',
        'nivel': 'media',
        'opcoes': {'A': '1822', 'B': '1877', 'C': '1865', 'D': '1910'},
        'correta': 'A'},

        {'titulo': 'Qual é a capital da Espanha?',
        'nivel': 'facil',
        'opcoes': {'A': 'Barcelona', 'B': 'Madri', 'C': 'Amsterdam', 'D': 'Valencia'},
        'correta': 'B'},

        {'titulo': 'Quem descobriu as Américas?',
        'nivel': 'facil',
        'opcoes': {'A': 'Donald Trump', 'B': 'Pedro Alvares Cabral', 'C': 'Cristóvão Colombo', 'D': 'Gandhi'},
        'correta': 'C'},

        {'titulo': 'Em que ano iniciou a Revolução Francesa?',
        'nivel': 'medio',
        'opcoes': {'A': '1799', 'B': '1823', 'C': '1917', 'D': '1888'},
        'correta': 'A'},

        {'titulo': 'Qual o nome dos protagonistas do jogo The Last Of Us?',
        'nivel': 'medio',
        'opcoes': {'A': 'Joseph e Elliot', 'B': 'Joel e Ellie', 'C': 'Jonathan e Ellen', 'D': 'Juca e Lucia'},
        'correta': 'B'},

        {'titulo': 'Qual o nome do rival do personagem Bob Esponja?',
        'nivel': 'facil',
        'opcoes': {'A': 'Pedro', 'B': 'Plonquion', 'C': 'Plancton', 'D': 'Pinoquio'},
        'correta': 'C'},

        {'titulo': 'Qual a sigla do vestibular estudantil estaduniense?',
        'nivel': 'facil',
        'opcoes': {'A': 'ENEM', 'B': 'MET', 'C': 'YONG', 'D': 'SAT'},
        'correta': 'D'},

        {'titulo': 'Quanto vale 513x890?',
        'nivel': 'dificil',
        'opcoes': {'A': '100000', 'B': '456570', 'C': '500000', 'D': '789654'},
        'correta': 'B'},

        {'titulo': 'Quem foi Pablo Escobar?',
        'nivel': 'facil',
        'opcoes': {'A': 'Educador brasileiro?', 'B': 'Narcotraficante', 'C': 'Policial Federal', 'D': 'Estudante do Insper'},
        'correta': 'B'},

        {'titulo': 'Onde fica o Monte Everest?',
        'nivel': 'dificil',
        'opcoes': {'A': 'Espanha', 'B': 'Asia', 'C': 'Sudeste dos EUA', 'D': 'Holanda'},
        'correta': 'B'},

        {'titulo': 'Quem é o personagem principal de Velozes e Furiosos?',
        'nivel': 'facil',
        'opcoes': {'A': 'Vin Diesel', 'B': 'Giulia', 'C': 'Gabriel Burher', 'D': 'Pinoquio'},
        'correta': 'A'},

        {'titulo': 'Qual é o nome da boneca Barbie?',
        'nivel': 'medio',
        'opcoes': {'A': 'Barbara Millicent Roberts', 'B': 'Bella gonsalvez', 'C': 'Beatriz Angela', 'D': 'Bianca Alvargaz'},
        'correta': 'A'},

        {'titulo': 'Quem inventou a lata de conservar alimentos em 1810?',
        'nivel': 'dificil',
        'opcoes': {'A': 'Pedro Calleri', 'B': 'Pedro Berganton', 'C': 'Pedro Aguiar', 'D': 'Pedro Durant'},
        'correta': 'D'},

        {'titulo': 'Quantos jogadores há em uma equipe de polo aquático??',
        'nivel': 'medio',
        'opcoes': {'A': '!7', 'B': 'Tres', 'C': 'Doze', 'D': 'Sete'},
        'correta': 'D'},

        {'titulo': 'Qual a temperatura média de Vênus?',
        'nivel': 'dificil',
        'opcoes': {'A': '25 C', 'B': '150 C', 'C': '460 C', 'D': '800 C'},
        'correta': 'C'},

        {'titulo': 'Em qual país encontra-se o Coliseu?',
        'nivel': 'facil',
        'opcoes': {'A': 'Espanha', 'B': 'Italia', 'C': 'Holanda', 'D': 'Alemanha'},
        'correta': 'B'},

        {'titulo': 'Quem é o atual presidente dos EUA?',
        'nivel': 'facil',
        'opcoes': {'A': 'Joe Biden', 'B': 'Donald Trump', 'C': 'Getulio VArgas', 'D': 'Bolsonaro'},
        'correta': 'A'}]














def transforma_base(lista):

    lista_faceis=[]
    lista_medios=[]
    lista_dificeis=[]

    dicio={}

    for dicionarios in lista:
        if dicionarios["nivel"]=='facil':
            lista_faceis.append(dicionarios)
            dicio["facil"]= lista_faceis

        if dicionarios["nivel"]=='medio':
            lista_medios.append(dicionarios)
            dicio["medio"]=lista_medios

        if dicionarios["nivel"]=='dificil':
            lista_dificeis.append(dicionarios)
            dicio["dificil"]=lista_dificeis



    if lista==[]:
        dicio={}

    return dicio

def valida_questao(questao):

    dicio = {}
    chaves = ["titulo", "nivel", "opcoes", "correta"]
    nivels = ["facil", "medio", "dificil"]
    letras = ["A", "B", "C", "D"]


    for chave in chaves:

        if chave not in questao:
            dicio[chave] = "nao_encontrado"

    if len(questao) != 4:
        dicio["outro"] = "numero_chaves_invalido"

    if chaves[0] in questao:
        
        if questao["titulo"].strip() == "":

            dicio["titulo"] = "vazio"
    if chaves[1] in questao:
        if questao["nivel"] not in nivels:

            dicio["nivel"] = 'valor_errado'
    if chaves[2] in questao:

        if len(questao["opcoes"]) != 4:
            dicio["opcoes"] = 'tamanho_invalido'
        else:

            for option in letras:
                if option not in questao["opcoes"]:

                    dicio["opcoes"] = "chave_invalida_ou_nao_encontrada"
            
            for option in letras:

                if questao["opcoes"][option].strip() == "":

                    if "opcoes" not in dicio: 

                        dicio["opcoes"] = {f'{option}': 'vazia'}
                    else:
                        dicio["opcoes"][option]  = "vazia"
    if chaves[3] in questao:

        if questao["correta"] not in letras: 

            dicio["correta"] = 'valor_errado'

    return dicio

def valida_questoes(lista):
    p_identificado = []
    for questao in lista:
        p_ident = valida_questao(questao)
        p_identificado.append(p_ident)
    return p_identificado

import random
def sorteia_questao(dicionario, nivel):
    lista=dicionario[nivel]
    s = random.choice(lista)
    return s 

def sorteia_questao_inedita (dicionario, nivel, lista):
    maxi = len(dicionario[nivel])
    num = random.randint(0,max-1)
    sorteada = dicionario[nivel][num]
    while sorteada in lista:
        num = random.randint(0,max-1)
        sorteada = dicionario[nivel][num]
    lista.append(sorteada)
    return sorteada
def questao_para_texto(dicio,n):

    item = 0
    rpts = 0
    num = str(n)
    A = 0
    B = 0
    C = 0
    D = 0

    for item in dicio:
        if item == "titulo":
            titulo = dicio[item]
        if item == 'opcoes':
            rpts = dicio[item]

    for letra in rpts:
        if letra == "A":
            A = rpts[letra]
        elif letra == "B":
            B = rpts[letra]
        elif letra == "C":
            C = rpts[letra]
        elif letra == "D":
            D = rpts[letra]
        

    final = "----------------------------------------\nQUESTAO {0}\n\n{1}\n\nRESPOSTAS:\nA: {2}\nB: {3}\nC: {4}\nD: {5}".format(num,titulo,A,B,C,D)

    return final
import random
def gera_ajuda(questao):
    lista = [ "A", "B", "C", "D"]
    lista.remove(questao["correta"])
    n = 1
    ajuda = []
    max = 3
    qtsorteio = random.randint(1,2)
    sor_per = random.randint(1,max-1)
    while qtsorteio >= n:
        sor_per = random.randint(0,max-1)
        if questao["opcoes"][lista[sor_per]] not in ajuda:
            ajuda.append(questao["opcoes"][lista[sor_per]])
            n = n + 1
    ajudas = " | ".join(ajuda)
    return f"DICA:\nOpções certamente erradas: {ajudas}" 
