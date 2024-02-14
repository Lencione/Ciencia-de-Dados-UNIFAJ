# Wesley Lencione de Oliveira
# 12225140
# Nao tratei os possiveis erros de entrada pois acredito que nao seja esse o intuito agora no inicio

# Inicializacao do "banco de dados"
# Nao alterei pra manter as mesmas entradas de dados
BD = [ 
    {"DOENCA":"GRIPE","SINTOMAS":{"TOSSE":5,"FEBRE":7,"DOR GARGANTA":8,"CORIZA":6,"FADIGA":3},"OCORRENCIAS": 0,"PERCENTUAL":0},
    {"DOENCA":"DENGUE","SINTOMAS": {"FEBRE":9,"DOR CORPO":8,"MANCHAS CORPO":5},"OCORRENCIAS": 0,"PERCENTUAL":0},   
    {"DOENCA":"COVID","SINTOMAS": {"FEBRE":9,"TOSSE":9,"CORIZA":4,"CANSACO":8,"PERDA PALADAR":7},"OCORRENCIAS": 0,"PERCENTUAL":0},
    {"DOENCA":"DIABETES","SINTOMAS": {"DOR CORPO":5,"MANCHAS CORPO":3,"PERDA PESO":6,"SEDE":9,"FADIGA":8},"OCORRENCIAS": 0,"PERCENTUAL":0}
]

# Transformei a consulta do paciente em uma funcao, facilitando a consulta de mais pacientes
def consultar_paciente(qtde_sintomas, tipo_calculo):
  # Inicializando a variavel com os sintomas do paciente
  sintomas_paciente = []
  #loop para resetar o banco
  for doenca in BD:
    doenca["OCORRENCIAS"] = 0
    doenca["PERCENTUAL"] = 0
  
  # Loop para recuperar os sintomas do cliente
  # Inicializando um dicionario conforme o tipo de calculo
  for num_sintoma in range(0,qtde_sintomas):
    sintoma = {}
    sintoma["sintoma"] = input(f"INDIQUE O SINTOMA NUMERO {num_sintoma + 1}: ")
    if tipo_calculo == 1:
      while True:
        sintoma["grau"] = int(input("INDIQUE O GRAU DO SINTOMA (0 A 10): "))
        if sintoma["grau"] in range(0,10):
          break
        print("Numero invalido...\n")
    sintomas_paciente.append(sintoma)

  # loop para calcular as ocorrencias dos sintomas no cliente
  # baseado no tipo de calculo
  for doenca in BD:
    nome = doenca["DOENCA"]
    sintomas = doenca["SINTOMAS"]
    for sintoma_paciente in sintomas_paciente:
      if sintoma_paciente["sintoma"] in sintomas:
        if tipo_calculo == 1:
          doenca["OCORRENCIAS"] += sintomas[sintoma_paciente["sintoma"]] * float(sintoma_paciente["grau"]/ 10) 
        else:
          doenca["OCORRENCIAS"] += sintomas[sintoma_paciente["sintoma"]]
    total = sum(sintomas.values())
    doenca["PERCENTUAL"] = float(doenca["OCORRENCIAS"]) / total * 100

  # ordenacao e filtro para trazer apenas doencas em que existam chances de ser diagnosticada
  ordenado = sorted(BD,key=lambda x: x["PERCENTUAL"],reverse = True)
  filtrado = list(filter(lambda x: x["PERCENTUAL"] > 0,ordenado))
  
  # Exibicao dos resultados ordenados e filtrados
  print("\nRESULTADOS: ")
  for doenca in filtrado:
    percentual_formatado = format(doenca["PERCENTUAL"], ".2f")
    nome = doenca["DOENCA"]
    print(f"A DOENÇA: {nome} TEM {percentual_formatado}% DE PROBABILIDADE DE ATENDER AOS SINTOMAS ESPECIFICADOS")
  print("\n")

#main
# Recebe uma variavel com a quantidade de sintomas que o paciente tem
# Caso o valor seja zero, finaliza o processamento do programa
# Dessa forma podemos consultar n pacientes
while True:
  while True:
    tipo_calculo = int(input("Digite 1 para calculo ponderado ou 2 para calculo simples:"))
    if tipo_calculo == 1 or tipo_calculo == 2:
      break
    
  qtde_sintomas = int(input("QUANTOS SINTOMAS O PACIENTE TEM? (0) para sair"))
  if qtde_sintomas == 0:
    print("Encerrando aplicacao!")
    break
  consultar_paciente(qtde_sintomas, tipo_calculo)