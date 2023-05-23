from pyknow import *
import difflib


class Command(Fact):
    pass


class InferenceEngine(KnowledgeEngine):
    @Rule(Command(action="turn_on_light"))
    def rule_turn_on_light(self):
        print("Prendiendo las luces")

    @Rule(Command(action="play_music"))
    def rule_play_music(self):
        print("Reproduciendo música")


# Creando instancia del motor de inferencia
engine = InferenceEngine()

# Obteniendo comando de entrada
command = input("Di un comando: ")

# Definiendo palabras clave y acciones asociadas
keywords = [
    (["Prende la luz", "enciende la luz", "activa la luz"], "turn_on_light"),
    (
        [
            "Reproduce musica",
            "reproduce una cancion",
            "encuentra cancion a reproducir",
        ],
        "play_music",
    ),
]

# Buscando palabras clave en el comando
matched_action = None
max_similarity = 0
for keyword_list, action in keywords:
    for keyword in keyword_list:
        similarity = difflib.SequenceMatcher(None, keyword, command.lower()).ratio()
        if similarity > max_similarity:
            max_similarity = similarity
            matched_action = action

# Estableciendo hecho y realizando inferencia
if matched_action and max_similarity >= 0.8:
    engine.reset()
    engine.declare(Command(action=matched_action))
    engine.run()
else:
    print(
        "No se encontró ninguna acción correspondiente o la similitud es menor al 80%"
    )
