from movies_db import movies
from sklearn.neural_network import MLPClassifier


# Função para treinar o modelo
def train_model(movies_arr):
    x = []
    y = []
    for movie in movies_arr:
        x.append([movie["score"][score_type] for score_type in score_types])
        y.append(movie["title"])

    rover = MLPClassifier(solver='lbfgs', activation='logistic', alpha=1e-8, hidden_layer_sizes=(450, 450),random_state=1, verbose=False)
    rover.fit(x, y)
    # print(rover.get_params())
    return rover


# Função para fazer a previsão do filme
def predict_movie(_trained_model, _score_types):
    while True:
        print("Answer the following questions to find a movie:")

        answers = [float(input(f"What is your rating for '{score_type}' (0-10)? ")) for score_type in _score_types]
        predicted_movie = _trained_model.predict([answers])
        print(f"The predicted movie is: {predicted_movie[0]}")

        if int(input("Continue? (1 = yes / 0 = no): ")) == 0:
            break


# Pontuações a serem consideradas
score_types = ["story", "acting", "soundtrack", "visuals", "special_effects"]

# Treinamento do modelo
trained_model = train_model(movies)

# Previsão do filme
predict_movie(trained_model, score_types)
