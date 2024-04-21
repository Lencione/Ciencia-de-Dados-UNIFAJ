from sklearn.neural_network import MLPClassifier
from coffees_db import roast as roast_db
from coffees_db import harvest as harvest_db
from coffees_db import localization as localization_db
from coffees_db import coffee as coffee_db
from coffees_db import coffee_images as images
from PIL import Image
import matplotlib.pyplot as plt


def train_model(model_conditions, db):
    x = []
    y = []
    for model in db:
        for condition in model["conditions"]:
            x.append([condition[model_condition] for model_condition in model_conditions])
            y.append(model["quality"])
    model = MLPClassifier(alpha=1e-8, hidden_layer_sizes=(450, 450), random_state=1)
    model.fit(x, y)
    return model


def get_answers(conditions):
    return [int(input(f"What is {condition}? (Min: 1 / Max: 7)")) for condition in conditions]


def predict_model(model, answers):
    return model.predict([answers])[0]


def printImage(index):
    image = Image.open(images[index])
    plt.imshow(image)
    plt.axis('off')  # Hide axis
    plt.show()


harvest_conditions = ["height", "maturity"]
roast_conditions = ["size", "temperature", "time"]
localization_conditions = ["latitude", "longitude"]
coffee_conditions = ["roast", "harvest", "localization"]

harvest_model = train_model(harvest_conditions, harvest_db)
roast_model = train_model(roast_conditions, roast_db)
localization_model = train_model(localization_conditions, localization_db)
coffee_model = train_model(coffee_conditions, coffee_db)

print("Answer the questions about the Harvest of coffee:")
harvest_answer = predict_model(harvest_model, get_answers(harvest_conditions))

print("\n\nAnswer the questions about the Roast of coffee:")
roast_answer = predict_model(roast_model, get_answers(roast_conditions))

print("\n\nAnswer the questions about the Localization of coffee:")
localization_answer = predict_model(localization_model, get_answers(localization_conditions))

coffee_answer = predict_model(coffee_model, [harvest_answer, roast_answer, localization_answer])

print("\n\nThe quality of the coffee is: (MAX: 7 | MIN:1)")
print(coffee_answer)
printImage(coffee_answer)
