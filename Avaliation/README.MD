## <center>Avalicao Parte II</center>

Criei o "banco de dados" em um arquivo separado
**coffees_db.py** e nele estao contidos as 4 propriedades
para treinar o modelo de cada uma das partes

Primeiramente, criei a funcao de treinar um modelo e 
retornar o modelo treinado, dessa forma evitando a repeticao de codigo

**train_model(model_conditions, db)**<br>
Nela recebemos 2 parametros, sendo model_conditions um array com os indices
do banco onde estao contidos os parametros de treinamento<br>
e **db** que recebe a referencia do banco

Fiz uma iteracao em cada linha do banco e inclui dentro de um array
as condicoes de treinamento, gerando assim, um array e em seguida,
insiro o indice "quality" do banco, indicando a qualidade do cafe (colhido, torrado, localizado)

Apos isso, crio um novo modelo treinado e o retorno na funcao.


**get_answers(conditions)**<br>
Uma funcao simples que recebe como parametro as condicoes do banco para questionar o usuario,e que me retorna um array com as respostas do usuario
pra usar como parametro para prever a resposta do modelo

**predict_model(model, answers)**<br>
Uma funcao simples tambem, que recebe o modelo treinado e as respostas do usuario pra
prever a resposta do modelo

O restante de torna intuitivo, depois de bem estruturada as funcoes e banco de dados
Resta treinar os 4 modelos, questionar o usuario a respeito da qualidade da colheita, torra e localizacao do cafe, para
retornar a qualidade do cafe para o mesmo.
