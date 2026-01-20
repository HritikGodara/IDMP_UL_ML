# plant_info.py
# Database of medicinal plants corresponding to the "Indian Medicinal Leaves Dataset"
# Keys match the dataset folder names exactly (including typos).

plant_data = {
    # --- A ---
    "Aloevera": {
        "Scientific Name": "Aloe barbadensis miller",
        "Uses": "Treats skin burns, digestive health, immunity booster.",
        "Ayurvedic": "Ghritkumari - Cooling (Sheetala), Rejuvenating (Rasayana)"
    },
    "Amla": {
        "Scientific Name": "Phyllanthus emblica",
        "Uses": "High Vitamin C, boosts immunity, hair growth.",
        "Ayurvedic": "Amalaki - Tridoshashamak (Balances all 3 doshas)"
    },
    "Amruta_Balli": {
        "Scientific Name": "Tinospora cordifolia",
        "Uses": "Immunity booster, chronic fever, dengue recovery.",
        "Ayurvedic": "Guduchi - Amrit (Nectar), antipyretic (Jwaraghna)"
    },
    "Arali": {
        "Scientific Name": "Nerium oleander",
        "Uses": "External use for swellings/lepam. (Toxic if ingested).",
        "Ayurvedic": "Karavira - Used in skin diseases (Kustha) externally."
    },
    "Ashoka": {
        "Scientific Name": "Saraca asoca",
        "Uses": "Gynaecological health, menstrual pain relief.",
        "Ayurvedic": "Ashoka - 'Remover of Sorrow', Uterine tonic."
    },
    "Ashwagandha": {
        "Scientific Name": "Withania somnifera",
        "Uses": "Reduces stress, improves energy and concentration.",
        "Ayurvedic": "Ashwagandha - Balya (Strengthening), Rasayana"
    },
    "Avacado": {
        "Scientific Name": "Persea americana",
        "Uses": "Heart health, rich in healthy fats, skin nourishment.",
        "Ayurvedic": "Butter Fruit - Nourishing (Brimhana), Balances Vata."
    },

    # --- B ---
    "Bamboo": {
        "Scientific Name": "Bambusa vulgaris",
        "Uses": "Silica rich (Vanshalochan), joint health, cooling.",
        "Ayurvedic": "Vanshalochana - Strengthening, Cooling."
    },
    "Basale": {
        "Scientific Name": "Basella alba",
        "Uses": "Cooling vegetable, mouth ulcers, digestion.",
        "Ayurvedic": "Upodika - Cooling, mild laxative, rich in iron."
    },
    "Betel": {
        "Scientific Name": "Piper betle",
        "Uses": "Digestion, oral health, analgesic.",
        "Ayurvedic": "Tambula - Pacifies Kapha and Vata, digestive."
    },
    "Betel_Nut": {
        "Scientific Name": "Areca catechu",
        "Uses": "Stimulant, digestive, strengthens gums.",
        "Ayurvedic": "Puga - Astringent, removes excess Kapha."
    },
    "Bhrami": {
        "Scientific Name": "Bacopa monnieri",
        "Uses": "Memory enhancer, reduces anxiety, hair growth.",
        "Ayurvedic": "Brahmi - Medhya (Brain tonic)."
    },
    "Brahmi": { # Handling duplicate spelling
        "Scientific Name": "Bacopa monnieri",
        "Uses": "Memory enhancer, reduces anxiety, hair growth.",
        "Ayurvedic": "Brahmi - Medhya (Brain tonic)."
    },

    # --- C ---
    "Castor": {
        "Scientific Name": "Ricinus communis",
        "Uses": "Laxative (oil), joint pain relief (leaves).",
        "Ayurvedic": "Eranda - Vatahara (Best for Vata disorders)."
    },
    "Catharanthus": {
        "Scientific Name": "Catharanthus roseus (Periwinkle)",
        "Uses": "Source of cancer drugs (Vincristine), diabetes management.",
        "Ayurvedic": "Sadapushpa - Antitumour, antidiabetic."
    },
    "Coriender": { # Typo in dataset
        "Scientific Name": "Coriandrum sativum",
        "Uses": "Digestion, cooling, kidney detox.",
        "Ayurvedic": "Dhanyaka - Digestive, tridosha sedative."
    },
    "Curry": {
        "Scientific Name": "Murraya koenigii",
        "Uses": "Flavoring, hair health, digestion, diabetes control.",
        "Ayurvedic": "Kaidarya - Appetizer, improves taste."
    },
    "Curry_Leaf": { # Handling duplicate
        "Scientific Name": "Murraya koenigii",
        "Uses": "Flavoring, hair health, digestion, diabetes control.",
        "Ayurvedic": "Kaidarya - Appetizer, improves taste."
    },

    # --- D ---
    "Doddapatre": {
        "Scientific Name": "Plectranthus amboinicus (Indian Borage)",
        "Uses": "Cough, cold, respiratory congestion.",
        "Ayurvedic": "Parnayavani - Deepana (Digestive), treats respiratory issues."
    },
    "Doddpathre": { # Typo in dataset
        "Scientific Name": "Plectranthus amboinicus (Indian Borage)",
        "Uses": "Cough, cold, respiratory congestion.",
        "Ayurvedic": "Parnayavani - Deepana (Digestive), treats respiratory issues."
    },

    # --- E ---
    "Ekka": {
        "Scientific Name": "Calotropis gigantea",
        "Uses": "Latex used for purgation, leaves for joint pain.",
        "Ayurvedic": "Arka - Bhedana (Purgative), treats skin diseases."
    },

    # --- G ---
    "Ganike": {
        "Scientific Name": "Solanum nigrum",
        "Uses": "Liver tonic, stomach ulcers, skin ailments.",
        "Ayurvedic": "Kakamachi - Hepato-protective, Tridoshahara."
    },
    "Gauva": { # Typo in dataset
        "Scientific Name": "Psidium guajava",
        "Uses": "Digestive health, Vitamin C, leaf tea for blood sugar.",
        "Ayurvedic": "Amrud - Astringent, cooling."
    },
    "Guava": {
        "Scientific Name": "Psidium guajava",
        "Uses": "Digestive health, Vitamin C, leaf tea for blood sugar.",
        "Ayurvedic": "Amrud - Astringent, cooling."
    },
    "Geranium": {
        "Scientific Name": "Pelargonium graveolens",
        "Uses": "Aromatherapy, skin care, stress relief.",
        "Ayurvedic": "Used in essential oils for calming Pitta."
    },

    # --- H ---
    "Henna": {
        "Scientific Name": "Lawsonia inermis",
        "Uses": "Natural dye, cooling, antifungal for skin.",
        "Ayurvedic": "Madayantika - Raktapitta (Bleeding disorders), cooling."
    },
    "Hibiscus": {
        "Scientific Name": "Hibiscus rosa-sinensis",
        "Uses": "Hair growth, heart health, blood pressure.",
        "Ayurvedic": "Japa - Keshya (Good for hair), Stambhana."
    },
    "Honge": {
        "Scientific Name": "Pongamia pinnata",
        "Uses": "Skin diseases, wound healing, biodiesel source.",
        "Ayurvedic": "Karanja - Kushtaghna (Cures skin diseases)."
    },

    # --- I, J, L ---
    "Insulin": {
        "Scientific Name": "Costus igneus",
        "Uses": "Traditionally used to manage blood sugar levels.",
        "Ayurvedic": "Insulin Plant - Diabetes management."
    },
    "Jackfruit": {
        "Scientific Name": "Artocarpus heterophyllus",
        "Uses": "Fruit is nutritious; leaves used in skin ailments.",
        "Ayurvedic": "Panasa - Nutritious (Brimhana), difficult to digest."
    },
    "Jasmine": {
        "Scientific Name": "Jasminum",
        "Uses": "Aromatherapy, wound healing (leaves), cooling.",
        "Ayurvedic": "Jati - Heals wounds, antimicrobial."
    },
    "Lemon": {
        "Scientific Name": "Citrus limon",
        "Uses": "Vitamin C, immunity, digestive.",
        "Ayurvedic": "Nimbuka - Digestive stimulant, acidic."
    },
    "Lemon_grass": {
        "Scientific Name": "Cymbopogon citratus",
        "Uses": "Tea for stress, digestion, mosquito repellent.",
        "Ayurvedic": "Bhustrina - Febrifuge (Treats fever), aromatic."
    },

    # --- M, N ---
    "Mango": {
        "Scientific Name": "Mangifera indica",
        "Uses": "Leaves used for oral health (gums), fruit is nutritious.",
        "Ayurvedic": "Amra - Leaves are astringent (Kashaya)."
    },
    "Mint": {
        "Scientific Name": "Mentha",
        "Uses": "Digestion, cooling, headache relief.",
        "Ayurvedic": "Pudina - Rochana (Improves taste), relieves gas."
    },
    "Nagadali": {
        "Scientific Name": "Ruta graveolens (Common Rue)",
        "Uses": "Anti-inflammatory, insect repellent, medicinal tea.",
        "Ayurvedic": "Sitaba - Pacifies Vata and Kapha."
    },
    "Neem": {
        "Scientific Name": "Azadirachta indica",
        "Uses": "Antibacterial, blood purifier, skin health.",
        "Ayurvedic": "Nimba - Bitter tonic, Grahi, Sheeta."
    },
    "Nithyapushpa": {
        "Scientific Name": "Catharanthus roseus",
        "Uses": "Cancer treatment (Vinca alkaloids), diabetes.",
        "Ayurvedic": "Sadapushpa - Toxic in high dose, medicinal."
    },
    "Nooni": { # Noni
        "Scientific Name": "Morinda citrifolia",
        "Uses": "Immunity booster, antioxidant, arthritis pain.",
        "Ayurvedic": "Achuka - General tonic, Rasayana."
    },

    # --- P ---
    "Palak(Spinach)": {
        "Scientific Name": "Spinacia oleracea",
        "Uses": "Rich in Iron, Vitamins, general nutrition.",
        "Ayurvedic": "Palakya - Laxative, nutritious."
    },
    "Papaya": {
        "Scientific Name": "Carica papaya",
        "Uses": "Digestion (Papain enzyme), dengue (platelets).",
        "Ayurvedic": "Erandakarkati - Pacifies Kapha, digestive."
    },
    "Pappaya": { # Typo in dataset
        "Scientific Name": "Carica papaya",
        "Uses": "Digestion (Papain enzyme), dengue (platelets).",
        "Ayurvedic": "Erandakarkati - Pacifies Kapha, digestive."
    },
    "Pepper": {
        "Scientific Name": "Piper nigrum",
        "Uses": "Spice, bio-enhancer (increases absorption of turmeric).",
        "Ayurvedic": "Maricha - Pramathi (Clears channels), deepana."
    },
    "Pomegranate": {
        "Scientific Name": "Punica granatum",
        "Uses": "Antioxidant, heart health, digestive.",
        "Ayurvedic": "Dadima - Hridya (Good for heart), Grahi."
    },

    # --- R, S ---
    "Raktachandini": {
        "Scientific Name": "Pterocarpus santalinus (Red Sandalwood)",
        "Uses": "Skin care, cooling, blood purification.",
        "Ayurvedic": "Rakta Chandana - Cooling, Pitta-shamaka."
    },
    "Rose": {
        "Scientific Name": "Rosa",
        "Uses": "Skin care (Rose water), stress relief, cooling.",
        "Ayurvedic": "Shatapatri - Cooling, heart tonic."
    },
    "Sapota": {
        "Scientific Name": "Manilkara zapota",
        "Uses": "Energy boosting, rich in antioxidants.",
        "Ayurvedic": "Nutritious, high sugar content."
    },
    "Seethapala": {
        "Scientific Name": "Annona squamosa (Custard Apple)",
        "Uses": "Cooling, nutritious, leaves are insecticidal.",
        "Ayurvedic": "Sitaphala - Cooling, increases Kapha."
    },

    # --- T, W ---
    "Tamarind": {
        "Scientific Name": "Tamarindus indica",
        "Uses": "Cooking acidulant, digestive, laxative.",
        "Ayurvedic": "Amlika - Sour, increases Pitta, mild laxative."
    },
    "Tulasi": {
        "Scientific Name": "Ocimum tenuiflorum",
        "Uses": "Cough, cold, immunity, stress relief.",
        "Ayurvedic": "Tulsi - Adaptogen, Kapha-Vatahara."
    },
    "Tulsi": {
        "Scientific Name": "Ocimum tenuiflorum",
        "Uses": "Cough, cold, immunity, stress relief.",
        "Ayurvedic": "Tulsi - Adaptogen, Kapha-Vatahara."
    },
    "Wood_sorel": {
        "Scientific Name": "Oxalis corniculata",
        "Uses": "Digestive, rich in Vitamin C, treats scurvy.",
        "Ayurvedic": "Changeri - Sour, appetizer, digestive."
    },

    "Default": {
        "Scientific Name": "Unknown Specimen",
        "Uses": "Information not available in database.",
        "Ayurvedic": "Consult an expert."
    }
}