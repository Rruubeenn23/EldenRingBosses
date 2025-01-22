from flask import Flask, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Permitir CORS para permitir solicitudes desde el frontend


@app.route('/dlc/api', methods=['GET'])
def dlc_api():
    data = [
        {"id": 1, "name": "Bestia divina León Danzante", "ubicacion": "Belurat, asentamiento de la torre", "region": "Belurat, asentamiento de la torre", "descripcion": "Divine Beast Dancing Lion is a Legend Boss in Elden Ring. Divine Beast Dancing Lion is a powerful and fast boss that uses diverse elemental attacks and is found in Belurat, the Tower Settlement.", "suelta": ["120.000 Runes", "Rememberance of the Dancing Lion", "Divine Beast Head"], "hp": 22.571, "image" : "https://eldenring.wiki.fextralife.com/file/Elden-Ring/divine_beast_dancing_lion_bosses_elden_ring_wiki_300px.jpg"},
        {"id": 2, "name": "Rellana, Caballera de la Luna Gemela", "ubicacion": "Castillo de Ensis", "region": "Castillo de Ensis", "descripcion": "Rellana, Twin Moon Knight is a Legend Boss in Elden Ring. A former princess of the Carian Royal family, she is the younger sister of Rennala, Queen of the Full Moon. Wielding her signature Twin Blades that she can infuse with Glintstone magic and Messmer's Flame respectively.", "suelta": ["240.000 Runes", "Rememberance of the Twin Moon Knight"], "hp": 29.723, "image" : "https://eldenring.wiki.fextralife.com/file/Elden-Ring/rellana_twin_moon_knight2_300px.jpg"},
        {"id": 3, "name": "Hipopótoma Dorado", "ubicacion": "Fortaleza sombría", "region": "Fortaleza sombría", "descripcion": "Golden Hippopotamus is a Great Enemy Boss in Elden Ring. Golden Hippopotamus can be found resting near the foot of the giant Marika Statue in Shadow Keep.", "suelta": ["200.000 Runes", "Aspects of the Crucible: Thorns", "Scadutree Fragment x2"], "hp": 33.866, "image" : "https://eldenring.wiki.fextralife.com/file/Elden-Ring/golden-hippopotamus-elden-ring-wiki-300px.jpg"},
        {"id": 4, "name": "Messmer el Empalador", "ubicacion": "Fortaleza sombría, en el Almacén de especímenes", "region": "Fortaleza sombría, en el Almacén de especímenes", "descripcion": "Messmer the Impaler is a Demigod Boss in Shadow of the Erdtree. He fights alongside the two-headed abyssal serpent and uses fire-based spells to attack the player, as well as a long-reaching spear. He is revealed to be Queen Marika's son, hidden away and abandoned in the Land of Shadow.", "suelta": ["400.000 Runes", "Rememberance of the Impaler Messmer's Kindling"], "hp": 38.981, "image" : "https://eldenring.wiki.fextralife.com/file/Elden-Ring/messmer_the_impaler_bosses_elden_ring_wiki_300px.jpg"},
        {"id": 5, "name": "Romina, la santa del brote", "ubicacion": "Iglesia del Brote, en las Antiguas ruinas de Rauh", "region": "Iglesia del Brote, en las Antiguas ruinas de Rauh", "descripcion": "Romina, Saint of the Bud is a Legend Boss in Elden Ring. Romina, Saint of the Bud is an amalgamation of various creatures, such as a scorpion, centipede, butterfly, and humanoid creature.", "suelta": ["380.000 Runes", "Rememberance of the Saint of the Bud"], "hp": 35.798, "image" : "https://eldenring.wiki.fextralife.com/file/Elden-Ring/romina_saint_of_the_bud_bosses_elden_ring_wiki_300px.jpg"},
        {"id": 6, "name": "Radahn, consorte prometido", "ubicacion": "Enir-Ilim", "region": "Enir-Ilim", "descripcion": "Promised Consort Radahn is a God Boss in Shadow of the Erdtree. He is an imposing, fully armored humanoid enemy adorned in red and gold with a lion-shaped helmet, wielding two colossal swords, and is found in Enir-Ilim. The second phase of this boss is called Radahn, Consort of Miquella.", "suelta": ["500.000 Runes", "Rememberance of a God and a Lord"], "hp": 46.134, "image" : "https://eldenring.wiki.fextralife.com/file/Elden-Ring/radahn_consort_of_miquella_bosses_elden_ring_wiki_600px.jpg"},
        {"id": 7, "name": "Dragón de la llama espectral", "ubicacion": "Llanura de las Tumbas", "region": "Llanura de las Tumbas", "descripcion": "Ghostflame Dragon is a Field Boss in Elden Ring. Ghostflame Dragon is a massive dragon with withered wings and exposed bones.", "suelta": ["100.000 Runes", "Dragon Heart", "Somber Ancient Dragon Smithing Stone"], "hp": 31.518, "image" : "https://eldenring.wiki.fextralife.com/file/Elden-Ring/ghostflame-dragon-gravesite-plain-elden-ring-wiki-600px.jpg"},
        {"id": 8, "name": "Caballero Negro Edredd", "ubicacion": "Fuerte de la reprimenda", "region": "Fuerte de la reprimenda", "descripcion": "Black Knight Edredd is a Field Boss in Elden Ring. Black Knight Edredd is a winged knight armed with a double-ended sword and is found in Fort of Reprimand.", "suelta": ["80.000 Runes", "Ash of War: Aspects of the Crucible: Wings"], "hp": 9.792, "image" : "https://eldenring.wiki.fextralife.com/file/Elden-Ring/edreed.png"},
        {"id": 9, "name": "Ralva, el Gran Oso Rojo", "ubicacion": "Altiplano Sombrío", "region": "Altiplano Sombrío", "descripcion": "Ralva the Great Red Bear is a Field Boss in Elden Ring. Ralva the Great Red Bear is a ferocious boss that fights with the strength of its limbs and is found in Scadu Altus.", "suelta": ["180.000 Runes", "Pelt of Ralva"], "hp": 29.606, "image" : "https://eldenring.wiki.fextralife.com/file/Elden-Ring/ralva.png"},
        {"id": 10, "name": "Caballero de la Muerte", "ubicacion": "Catacumbas del río Escorpión", "region": "Catacumbas del río Escorpión", "descripcion": "Death Knight is a Field Boss in Elden Ring. Death Knight is a repeat boss that wields various weapons that can conjure lightning and is found standing guard in the catacombs.", "suelta": ["110.000 Runes", "Death Knight's Twin Axes", "Crimson Amber Medallion +3"], "hp": 9.642, "image" : "https://eldenring.wiki.fextralife.com/file/Elden-Ring/death-knight-fog-rift-elden-ring-wiki-600px.jpg"},
        {"id": 11, "name": "Avatar del Árbol Umbrío", "ubicacion": "Nord-Este de la Fortaleza Sombría", "region": "Nord-Este de la Fortaleza Sombría", "descripcion": "Scadutree Avatar is a Legend Boss in Elden Ring. Scadutree Avatar is the Realm of Shadow's equivalent of the Erdtree Avatar, but in design it resembles an enlarged Shadow Sunflower with two massive roots for arms and can summon thorns and conjure the Scadutree's light for offense. It is found in the Scadutree Base, accessible through a hidden path in the Shadow Keep.", "suelta": ["260.000 Runes", "Rememberance of the Shadow Sunflower", "Miquella's Great Rune"], "hp": [7.650, 13.608, 13.608], "image" : "https://eldenring.wiki.fextralife.com/file/Elden-Ring/scadutree_avatar_bosses_elden_ring_wiki_300px.jpg"},
        {"id": 12, "name": "Jori, inquisidor anciano", "ubicacion": "Catacumbas de Luz Oscura", "region": "Catacumbas de Luz Oscura", "descripcion": "Jori, Elder Inquisitor is a Boss in Elden Ring. Jori, Elder Inquisitor is a hornsent summoner who wields the Barbed Staff-Spear and is found as the boss of the Darklight Catacombs.", "suelta": ["260.000 Runes", "Barbed Staff-Spear"], "hp": 30.506, "image" : "https://eldenring.wiki.fextralife.com/file/Elden-Ring/jori-elder-inquisitor-elden-ring-wiki-300px.jpg"},
        {"id": 13, "name": "Midra, Señor de la Llama Frenética", "ubicacion": "Casa Parroquial de Midra", "region": "Casa Parroquial de Midra", "descripcion": "Midra, Lord of Frenzied Flame is a Legend Boss in Elden Ring. He is the embodiment of the Frenzied Flame found in Midra's Manse.", "suelta": ["410.000 Runes", "Rememberance of the Lord of Frienzied Flame"], "hp": 47.171, "image" : "https://eldenring.wiki.fextralife.com/file/Elden-Ring/midra_lord_of_frenzied_flame_bosses_elden_ring_wiki_300px.jpg"},
        {"id": 14, "name": "Caballero Putrefacto", "ubicacion": "Fisura en ataúd de piedra", "region": "Fisura en ataúd de piedra", "descripcion": "Putrescent Knight is a Legend Boss in Shadow of the Erdtree. The Putrescent Knight is a large decrepit skeleton wielding a cleaver and riding a steed. It is found guarding the entrance to St. Trina's cave at the end of Stone Coffin Fissure.", "suelta": ["220.000 Runes", "Rememberance of Putrescence"], "hp": 20.612, "image" : "https://eldenring.wiki.fextralife.com/file/Elden-Ring/putrescent_knight_bosses_elden_ring_wiki_300px.jpg"},
        {"id": 15, "name": "Dragón de pico escarpado", "ubicacion": "Camino a la Rumba oculta de Charo", "region": "Camino a la Rumba oculta de Charo", "descripcion": "Jagged Peak Drake is a Boss in Elden Ring. They are large dragons said to have come from the bloodline of Bayle, and in turn have inherited his power to conjure flame lightning. The first Drake is fought at the foothills of the Jagged Peak, while two others are fought on the way upwards. ", "suelta": ["120.000 Runes", "Dragon Heart", "Dragonscale Flesh"], "hp": 39.377, "image" : "https://eldenring.wiki.fextralife.com/file/Elden-Ring/jagged-peak-drake-1-elden-ring-wiki-600px.jpg"},
        {"id": 16, "name": "Dragón antiguo Senessax", "ubicacion": "Pico Escarpado", "region": "Pico Escarpado", "descripcion": "Ancient Dragon Senessax is a Great Enemy Boss in Elden Ring. Senessax is an ancient dragon that guards the path to the summit. They are found in Jagged Peak, West side which is also near Bayle the Dread.", "suelta": ["200.000 Runes", "Ancient Dragon Smithing Stone", "Somber Ancient Dragon Smithing Stone"], "hp": 45.551,  "image" : "https://eldenring.wiki.fextralife.com/file/Elden-Ring/senessax.png"},
        {"id": 17, "name": "Bayle el Temible", "ubicacion": "Pico Escarpado", "region": "Pico Escarpado", "descripcion": "Bayle the Dread is a Legend Boss in Elden Ring. Bayle is the forefather of the drakes, a sworn enemy of the ancient dragons, and the target of Igon's vengeance. He is found at the summit of the Jagged Peak.", "suelta": ["490.000 Runes", "Heart of Bayle"], "hp": 41.612, "image" : "https://eldenring.wiki.fextralife.com/file/Elden-Ring/bayle_the_dread_bosses_elden_ring_wiki_300px.jpg"},
        {"id": 18, "name": "Comandante Gaius", "ubicacion": "Vista Sombría", "region": "Vista Sombría", "descripcion": "Commander Gaius is a Legend Boss in Elden Ring. Commander Gaius rides a boar into battle and uses several magic attacks and is found at the back of the Shadow Keep Legacy Dungeon.", "suelta": ["230.000 Runes", "Rememberance of the Wild Boar Rider"], "hp": 33.871,  "image" : "https://eldenring.wiki.fextralife.com/file/Elden-Ring/commander_gaius_bosses_elden_ring_wiki_300px.jpg"},
        {"id": 19, "name": "Metyr, madre de Dedos", "ubicacion": "Ruinas del Dedo de Miyr", "region": "Ruinas del Dedo de Miyr", "descripcion": "Metyr, Mother of Fingers is a Legend Boss in Elden Ring. Metyr, Mother of Fingers is a large monster that is composed of several fingers with two arms in front, and has a stomach made of smaller fingers, and is found in the Finger Ruins of Miyr.", "suelta": ["420 Runes", "rememberance of the Mother of Fingers"], "hp": 43.296, "image" : "https://eldenring.wiki.fextralife.com/file/Elden-Ring/metyr_mother_of_fingers_bosses_elden_ring_wiki_300px.jpg"},
        {"id": 20, "name": "Caballera de la aguja Leda", "ubicacion": "Enir-Ilim", "region": "Enir-Ilim", "descripcion": "Leda and Allies is an NPC battle in Elden Ring exclusive to the Shadow of the Erdtree DLC. Needle Knight Leda leads a band of Miquella's faithful to prevent you from stopping him from becoming a god.", "suelta": ["300.000 Runes", "Leda's Sword"], "hp": [15.101, 9.992, 14.615, 15.911, 17.256], "image" : "https://eldenring.wiki.fextralife.com/file/Elden-Ring/elden-ring-player-speaking-to-leda-the-needle-knight.png"},
    ]
    return jsonify(data)
@app.route("/")
def index():
    return render_template("base.html")

@app.route("/dlc")
def dlc():
    return render_template("dlc.html")

if __name__ == '__main__':
    app.run(debug=True)
