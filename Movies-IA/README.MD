## <center>Avaliacao 1 bimestre PARTE I</center>
#### <center>Prof: Andre Mendeleck</center>

**Tema:** Previsao de Filmes

**Banco de dados:** movies_db.py

### Inputs

Os inputs para treinamento foram feitos atraves da funcao train_model
onde os dados do banco foram iterados e inseridos nas variaveis x e y, 
sendo x os valores para as buscas e y para as respostas a esses valores

Tambem ficou definido dentro de uma variavel (poderia tambem ter sido colocada dentro do db)
 os tipos de verificacao, sendo assim, para os mesmos dados que vamos prever posteriormente

Depois do modelo ter sido treinado, vamos prever o filme assistido pelo usuario
baseado nas notas dos filmes
Entao perguntamos ao usuario qual nota ele da para cada tipo de pontuacao definida anteriomente na variavel
**score_types**

Aplicacao simples, mas vai direto ao ponto.<br>
Nao fiz nenhum tipo de validacao para as entradas do usuario
considerando que o intuito da aplicacao nao seria essa

    Wesley Lencione de Oliveira
    RA 12225140