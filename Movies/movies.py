# Wesley Lencione de Oliveira
# 12225140
# https://github.com/Lencione/Ciencia-de-Dados-UNIFAJ/tree/master/Movies
from movies_db import movies


# Ler a quantidade e quais os nomes do atores que devem estar no filme
def get_actors():
    quantity = int(input("Quantos atores voce quer ver no filme? "))
    actors = []
    for i in range(quantity):
        actor = {"name": input("Nome: ")}
        actors.append(actor)
    return actors


# Ler o tipo de score que deve ser considerado no filme
def get_by_score():
    score_types = {
        1: ["Historia", "story"],
        2: ["Atuacao", "acting"],
        3: ["Trilha Sonora", "soundtrack"],
        4: ["Visualizacao", "visuals"],
        5: ["Efeitos Especiais", "special_effects"]
    }
    score_types_array = []

    while True:
        print("Qual tipo de score voce quer? ")
        for key, value in score_types.items():
            print(f"{key} - {value[0]}")
        score_type = int(input("Qual tipo de score voce quer? "))
        if score_type not in score_types:
            print("Tipo de score invalido.")
            continue
        score_types_array.append(score_types[score_type][1])
        score_types.pop(score_type)
        if len(score_types) == 0:
            break
    return score_types_array


# Ler o nome do diretor que deve estar no filme
def get_director():
    director = input("Qual diretor voce quer? ")
    return director


# Ler a quantidade e quais os generos do filme
def get_genres():
    genres = []
    quantity = int(input("Quantos generos voce quer? "))
    for i in range(quantity):
        genre = input("Qual genero voce quer? ")
        genres.append(genre)
    return genres


# Filtrar os filmes baseado nos dados inseridos pelo usuario
def get_movies(actors, score_types, director, genres):
    movies_filtered = []
    for movie in movies:
        points = 0
        for actor in actors:
            if actor["name"] in movie["cast"]:
                points += 1
        if director in movie["director"]:
            points += 1
        for genre in genres:
            if genre in movie["genre"]:
                points += 1
        if points > 0:
            movies_filtered.append((movie, points))

    movies_filtered.sort(key=lambda x: (x[1], x[0]["score"][score_types[0]][0]), reverse=True)
    return movies_filtered


#  Imprimir os filmes filtrados e suas informacoes
def print_movies(suggested_movies_data):
    for movie in suggested_movies_data:
        print(f"Pontuacao: {movie[1]}")
        print(f"Titulo: {movie[0]['title']}")
        print(f"Diretor: {movie[0]['director']}")
        print(f"Generos:")
        for genre in movie[0]["genre"]:
            print(genre)
        print(f"Score: {movie[0]['score']}")
        print("Atores:")
        for actor in movie[0]["cast"]:
            print(actor)
        print("-------------------------------------------------")
        print()


# main
print("Bem vindo ao sistema de filtro de filmes!")
print("Escolha um filme para filtrar:")
suggested_movies = get_movies(get_actors(), get_by_score(), get_director(), get_genres())
print_movies(suggested_movies)
