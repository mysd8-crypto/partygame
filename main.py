from pyscript import web, when
from js import CustomEvent, document
import secrets


tracks = [
    "spotify:track:6raLQ9U8Ra2rW7fOp3pPC0",
    "spotify:track:4mruI5Nfkjrx5ZDupW6HAi",
    "spotify:track:5zvZCnozZFaVTH5FI07In3",
    "spotify:track:5zvZCnozZFaVTH5FI07In3",
    "spotify:track:2oBd6KgXMeh0alqHHli0J4",
    "spotify:track:40TZnaw4eDPChJNHw2Swf3",
    "spotify:track:35DN4PTg8APLJlgXdc2Qeu",
    "spotify:track:0Li1OuXXfi7950ilZUFGkF",
    "spotify:track:7AzlLxHn24DxjgQX73F9fU",
    "spotify:track:7GBN1M5T3wF901JTiIDxwb",
    "spotify:track:0OA00aPt3BV10qeMIs3meW",
    "spotify:track:4AE7Lj39VnSZNOmGH2iZaq",
    "spotify:track:7DbdUf8aHSYoliSjO6LZv6",
    "spotify:track:4XvcHTUfIlWfyJTRG0aqlo",
]

truths = [
    # Harmlos / Deep / Lustig (~33%)
    "Wen im Kreis findest du am attraktivsten? (allein mit deinem anziehenden Sex, der die 3. Person links von dir ist, sonst links daneben)",
    "Wer hier wäre dein Notfall-Date? (allein mit deinem anziehenden Sex, der die 5. Person links von dir ist, sonst links daneben)",
    "Was war dein peinlichster Flirt-Versuch? (vor der Gruppe, nur mit deinem anziehenden Sex, der die 6. Person rechts von dir ist, sonst links daneben)",
    "Mit wem hier würdest du am wenigsten gern im Aufzug stecken bleiben? (allein mit deinem anziehenden Sex, der die 8. Person links von dir ist, sonst links daneben)",
    "Hast du schon mal jemanden im Kreis gestalkt? (vor der Gruppe, nur mit deinem anziehenden Sex, der die 10. Person links von dir ist, sonst links daneben)",
    "Was war dein unangenehmster Betrunken-Moment? (allein mit deinem anziehenden Sex, der die 2. Person rechts von dir ist, sonst links daneben)",
    "Wer hier nervt dich manchmal, auch wenn du es nicht sagst? (vor der Gruppe, nur mit deinem anziehenden Sex, der die 4. Person links von dir ist, sonst links daneben)",
    "Wer hier wäre die schlechteste Person für einen Roadtrip? (allein mit deinem anziehenden Sex, der die 7. Person links von dir ist, sonst links daneben)",
    "Hast du schon mal jemanden im Kreis angelogen? Wobei? (vor der Gruppe, nur mit deinem anziehenden Sex, der die 9. Person links von dir ist, sonst links daneben)",
    "Was war dein unangenehmstes erstes Date? (allein mit deinem anziehenden Sex, der die 6. Person links von dir ist, sonst links daneben)",
    "Wer hier hat den besten Körper? (vor der Gruppe, nur mit deinem anziehenden Sex, der die 3. Person rechts von dir ist, sonst links daneben)",
    "Wer hier wäre dein heimlicher Crush? (allein mit deinem anziehenden Sex, der die 4. Person links von dir ist, sonst links daneben)",
    "Was ist dein größter Turnoff? (vor der Gruppe, nur mit deinem anziehenden Sex, der die 5. Person rechts von dir ist, sonst links daneben)",
    "Wer hier hat den schlechtesten Modegeschmack? (allein mit deinem anziehenden Sex, der die 2. Person links von dir ist, sonst links daneben)",
    "Mit wem hier würdest du am ehesten tauschen wollen? (vor der Gruppe, nur mit deinem anziehenden Sex, der die 6. Person rechts von dir ist, sonst links daneben)",
    "Was ist dein schlimmster Spitzname? (allein mit deinem anziehenden Sex, der die 7. Person links von dir ist, sonst links daneben)",
    "Was ist etwas, das du Angst hast, dass andere über dich herausfinden? (vor der Gruppe, nur mit deinem anziehenden Sex, der die 8. Person rechts von dir ist, sonst links daneben)",
    "Wann hast du dich das letzte Mal wirklich einsam gefühlt? (allein mit deinem anziehenden Sex, der die 9. Person links von dir ist, sonst links daneben)",
    "Welche Person in deinem Leben bedeutet dir mehr, als du zeigst? (vor der Gruppe, nur mit deinem anziehenden Sex, der die 10. Person rechts von dir ist, sonst links daneben)",
    "Was war der Moment, der dich am meisten verändert hat? (allein mit deinem anziehenden Sex, der die 3. Person links von dir ist, sonst links daneben)",

    # Sexy / Provokant / Flirty (~66%)
    "Wen hier würdest du am ehesten küssen? (allein mit deinem anziehenden Sex, der die 3. Person rechts von dir ist, sonst links daneben)",
    "Mit wem hier hättest du am meisten Spannung? (vor der Gruppe, nur mit deinem anziehenden Sex, der die 5. Person links von dir ist, sonst links daneben)",
    "Wer hier hat die heißeste Ausstrahlung? (allein mit deinem anziehenden Sex, der die 6. Person rechts von dir ist, sonst links daneben)",
    "Wenn du mit einer Person hier rummachen müsstest, wer wäre es? (vor der Gruppe, nur mit deinem anziehenden Sex, der die 7. Person links von dir ist, sonst links daneben)",
    "Wer hier wäre dein One-Night-Stand? (allein mit deinem anziehenden Sex, der die 8. Person links von dir ist, sonst links daneben)",
    "Wessen Lippen im Kreis findest du am schönsten? (vor der Gruppe, nur mit deinem anziehenden Sex, der die 9. Person rechts von dir ist, sonst links daneben)",
    "Mit wem hier würdest du ein Bett teilen? (allein mit deinem anziehenden Sex, der die 10. Person links von dir ist, sonst links daneben)",
    "Wer hier wirkt am besten beim Küssen? (vor der Gruppe, nur mit deinem anziehenden Sex, der die 2. Person rechts von dir ist, sonst links daneben)",
    "Wen hier würdest du gerne oben ohne sehen? (allein mit deinem anziehenden Sex, der die 3. Person links von dir ist, sonst links daneben)",
    "Wer hier hätte dich am schnellsten rumgekriegt? (vor der Gruppe, nur mit deinem anziehenden Sex, der die 5. Person rechts von dir ist, sonst links daneben)",
    "Wenn du jemanden daten müsstest: wer? (allein mit deinem anziehenden Sex, der die 6. Person links von dir ist, sonst links daneben)",
    "Wer hier ist am ehesten dein verbotener Crush? (vor der Gruppe, nur mit deinem anziehenden Sex, der die 4. Person links von dir ist, sonst links daneben)",
    "Wen hier würdest du auf einer Party zuerst anflirten? (allein mit deinem anziehenden Sex, der die 7. Person rechts von dir ist, sonst links daneben)",
    "Wer hier hat den sexiesten Blick? (vor der Gruppe, nur mit deinem anziehenden Sex, der die 2. Person links von dir ist, sonst links daneben)",
    "Mit wem hier wär ein F+ am wahrscheinlichsten? (allein mit deinem anziehenden Sex, der die 8. Person rechts von dir ist, sonst links daneben)",
    "Wen hier würdest du bei einem Kuss nicht stoppen? (vor der Gruppe, nur mit deinem anziehenden Sex, der die 3. Person links von dir ist, sonst links daneben)",
    "Zeig der 3. Person links, wen du am heißesten findest (allein, nur anziehender Sex, sonst links daneben)",
    "Erzähl der 7. Person deinen letzten Traum, der dich sexuell verwirrt hat (allein, nur anziehender Sex, sonst links daneben)",
    "Sag der 8. Person gegenüber, wen du heimlich anziehend findest (allein, nur anziehender Sex, sonst links daneben)",
    "Flüstere der 2. Person rechts, was du am meisten an ihr magst (allein, nur anziehender Sex, sonst links daneben)",
    "Beschreibe der 10. Person, welchen Crush aus dem Kreis du am meisten willst (allein, nur anziehender Sex, sonst links daneben)",
    "Erzähl der 5. Person links, wann du dich das letzte Mal sehr flirtig gefühlt hast (allein, nur anziehender Sex, sonst links daneben)",
    "Zeig der 6. Person rechts, wen du am liebsten küssen würdest (allein, nur anziehender Sex, sonst links daneben)",
    "Erzähl der 9. Person gegenüber eine deiner peinlichsten Fantasien (PG-13) (allein, nur anziehender Sex, sonst links daneben)",
    "Flirte spielerisch mit der 6. Person für 30 Sekunden (vor der Gruppe, nur mit deinem anziehenden Sex, sonst links daneben)",
    "Erzähl der 1. Person, wer aus der Runde dich am meisten nervös macht (allein, nur anziehender Sex, sonst links daneben)",
    "Sag der 9. Person, was dich sexuell am meisten reizt (allein, nur anziehender Sex, sonst links daneben)",
    "Flirte mit der Person deiner Wahl aus dem Kreis für 20 Sekunden (vor der Gruppe, nur mit deinem anziehenden Sex, sonst links daneben)",

    # Neue Massage-Truths (leicht sexy)
    "Wem würdest du am liebsten eine Schulter- oder Nackenmassage geben? (vor der Gruppe, nur mit deinem anziehenden Sex, sonst links daneben)",
    "Wer hier würde am meisten genießen, wenn du ihm/ihr den Rücken massierst? (allein mit deinem anziehenden Sex, sonst links daneben)",
    "Wem würdest du am liebsten eine entspannende Hand- oder Fußmassage geben? (vor der Gruppe, nur mit deinem anziehenden Sex, sonst links daneben)",

    # Neue Musik-Truths
    "Welches Lied würdest du am liebsten mit der Person links von dir gemeinsam hören? (allein, nur mit deinem anziehenden Sex, sonst links daneben)",
    "Wer hier hat den besten Musikgeschmack? (vor der Gruppe, nur mit deinem anziehenden Sex, sonst links daneben)"
]


dares = [
    # Harmlos / Lustig (~33%)
    "Die Person rechts von dir darf dir eine neue Frisur machen (allein mit deinem anziehenden Sex, der die 4. Person links von dir ist, sonst links daneben)",
    "Die 2. Person links von dir bekommt dein Handy und darf ein Selfie posten (allein mit deinem anziehenden Sex, der die 6. Person rechts von dir ist, sonst links daneben)",
    "Bell wie ein Hund für 20 Sekunden (vor der Gruppe, nur mit deinem anziehenden Sex, der die 3. Person links von dir ist, sonst links daneben)",
    "Umarme die 3. Person rechts (allein mit deinem anziehenden Sex, der die 7. Person links von dir ist, sonst links daneben)",
    "Tanze ohne Musik für 30 Sekunden (vor der Gruppe, nur mit deinem anziehenden Sex, der die 5. Person rechts von dir ist, sonst links daneben)",
    "Die Person gegenüber darf ein Wort bestimmen, das du 2 Minuten lang nicht sagen darfst (allein mit deinem anziehenden Sex, der die 2. Person links von dir ist, sonst links daneben)",
    "Lass dich von der Person links schminken (vor der Gruppe, nur mit deinem anziehenden Sex, der die 8. Person rechts von dir ist, sonst links daneben)",

    # Sexy / Provokant / Flirty (~66%)
    "Setz dich für eine Runde auf den Schoß der 5. Person (vor der Gruppe, nur mit deinem anziehenden Sex, sonst links daneben)",
    "Flüstere der 6. Person rechts, was du gerade an ihr am attraktivsten findest (allein, nur mit deinem anziehenden Sex, sonst links daneben)",
    "Schau der 7. Person gegenüber so lange in die Augen, bis jemand eingreift (vor der Gruppe, nur mit deinem anziehenden Sex, sonst links daneben)",
    "Zieh jemanden deiner Wahl nah zu dir und halte ihn/sie 20 Sekunden fest (allein, nur mit deinem anziehenden Sex, sonst links daneben)",
    "Mach der 8. Person links ein langsames, intensives Kompliment von Kopf bis Fuß (vor der Gruppe, nur mit deinem anziehenden Sex, sonst links daneben)",
    "Lehn deine Stirn an die 9. Person gegenüber und bleib so für 15 Sekunden (allein, nur mit deinem anziehenden Sex, sonst links daneben)",
    "Setz dich zwischen die 4. und 6. Person und tu so, als würdest du kuscheln (vor der Gruppe, nur mit deinem anziehenden Sex, sonst links daneben)",
    "Halte Blickkontakt mit der 3. Person für 20 Sekunden, während die Gruppe zuschaut (vor der Gruppe, nur mit deinem anziehenden Sex, sonst links daneben)",
    "Lehn dich eng an die 2. Person links, tu so, als würdest du sie verführen (vor der Gruppe, nur mit deinem anziehenden Sex, sonst links daneben)",
    "Mach der 7. Person ein intensives Kompliment über den Körper, während alle schauen (vor der Gruppe, nur mit deinem anziehenden Sex, sonst links daneben)",

    # Musik-Dares (~10%)
    "Spiele das letzte Lied, das du in deiner Playlist abgespielt hast, vor allen (vor der Gruppe, nur mit deinem anziehenden Sex, sonst links daneben)",
    "Tanze 30 Sekunden zu deinem Lieblingssong, den die 3. Person rechts von dir ausgesucht hat (vor der Gruppe, nur mit deinem anziehenden Sex, sonst links daneben)",
    "Sing den Refrain deines letzten gespielten Liedes laut für alle (vor der Gruppe, nur mit deinem anziehenden Sex, sonst links daneben)",
    "Zeig der 5. Person links deinen besten Tanzmove zu deinem aktuellen Lieblingssong (allein, nur mit deinem anziehenden Sex, sonst links daneben)",
    "Lass die 6. Person dein Handy nehmen und den nächsten Song in deiner Playlist abspielen, zu dem du tanzen musst (vor der Gruppe, nur mit deinem anziehenden Sex, sonst links daneben)",
    "Spiele ein Lied aus deiner Playlist ab, das dich zuletzt sehr glücklich gemacht hat, und tanze dazu (vor der Gruppe, nur mit deinem anziehenden Sex, sonst links daneben)",
    "Tanze 20 Sekunden improvisiert zu dem Song, der gerade auf deinem Handy läuft (allein, nur mit deinem anziehenden Sex, sonst links daneben)",
    "Die 7. Person darf dein Handy nehmen und dein zuletzt gespieltes Lied abspielen; du musst dazu performen (vor der Gruppe, nur mit deinem anziehenden Sex, sonst links daneben)",
    "Zeig der 4. Person links, wie du zu deinem Lieblingslied tanzt (allein, nur mit deinem anziehenden Sex, sonst links daneben)",

    # Massage-Dares (neu, leicht sexy)
    "Gib der Person rechts von dir eine 30-Sekunden-Schulter- oder Nackenmassage (vor der Gruppe, nur mit deinem anziehenden Sex, sonst links daneben)",
    "Massiere 20 Sekunden lang die Hände der Person links von dir (allein, nur mit deinem anziehenden Sex, sonst links daneben)",
    "Gib der Person gegenüber eine sanfte Rückenmassage für 30 Sekunden (vor der Gruppe, nur mit deinem anziehenden Sex, sonst links daneben)",
    "Massiere 15 Sekunden die Füße der Person rechts von dir (allein, nur mit deinem anziehenden Sex, sonst links daneben)",
    "Massiere 30 Sekunden die Arme der Person links von dir, während ihr euch anseht (vor der Gruppe, nur mit deinem anziehenden Sex, sonst links daneben)"
]


class Player:
    def __init__(self, name: str):
        self.name = name
    def __repr__(self):
        return str(self.name)

class PartyGame:
    def __init__(self, group_size: int):
        self.group_size = group_size
        self.players = []
        self.positions = {}

    def create_players(self, name: str):
        self.players.append(Player(name))

    def randomize_players(self):
        import copy
        remaining = copy.copy(self.players)
        self.positions = {}
        for position in range(self.group_size):
            random_player = secrets.choice(remaining)
            remaining.remove(random_player)
            self.positions[position] = random_player
        return self.positions

    def pick_random_truth_or_dare(self):
        if secrets.choice([0,1]) == 0:
            return {"truth": secrets.choice(truths)}
        else:
            return {"dare": secrets.choice(dares)}

party_game = None

# --- Event-Handler ---
@when("click", "#group-confirm-button")
def create_party_game(event):
    global party_game
    group_size = int(web.page["group"].value)
    party_game = PartyGame(group_size)
    web.page["group-size-output"].innerText = f"Gruppengröße: {group_size}"

@when("click", "#player-confirm-button")
def append_player_name_position(event):
    player_names = web.page["individual"].value.split(", ")
    for name in player_names:
        party_game.create_players(name)
    positions = party_game.randomize_players()
    listings = "\n".join(f"Name: {name}, Position: {pos+1}" for pos, name in positions.items())
    web.page["player-name-position-output"].innerText = f"Spieler und Positionen:\n{listings}"

@when("click", "#randomize-button")
def randomize_and_play(event):
    # Track zufällig auswählen
    track_uri = secrets.choice(tracks)

    # Erstelle ein CustomEvent mit dem Track-URI im 'detail' Feld
    event_data = {"detail": track_uri}
    js_event = CustomEvent.new("play-track", eval(str(event_data)))
    
    # Event abschicken
    document.dispatchEvent(js_event)

    # Zufällige Aufgabe auswählen
    choice = party_game.pick_random_truth_or_dare()
    text = choice.get("truth") or choice.get("dare")
    
    # Anzeige aktualisieren
    web.page["truth-dare-output"].innerText = f"Aufgabe: \n{text}"
