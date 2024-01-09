from transformers import AutoTokenizer, AutoModel
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import DBSCAN
from nltk.tokenize import word_tokenize
import morfeusz2

# Pobieranie polskiego modelu BERT oraz tokienizera
tokenizer = AutoTokenizer.from_pretrained("allegro/herbert-base-cased")
model_bert = AutoModel.from_pretrained("allegro/herbert-base-cased")

# Inicjalizacja Morfeusz2, narzędzia do analizy języka polskiego
morfeusz = morfeusz2.Morfeusz()

# Funkcja generująca BERT embeddings dla tekstu w języku polskim
def bert_embeddings_pl(text):
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True, max_length=512)
    outputs = model_bert(**inputs)
    return outputs.last_hidden_state.mean(dim=1).squeeze().detach().numpy()

# Funkcja do ekstrakcji nazw własnych dla tekstu w języku polskim
def extract_named_entities_pl(text):
    analysis = morfeusz.analyse(text)
    named_entities = []
    for word, interp in analysis:
        if 'nazwa_pospolita' not in interp[2] and interp[2] != 'ign':
            named_entities.append(interp[1].split(':')[0])
    return named_entities

# Przykładowe opisy książek w języku polskim
book_descriptions_pl = [
    "Epicka powieść fantasy, która śledzi losy grupy bohaterów próbujących uratować swoje królestwo przed ciemnością.",
    "Opowieść science fiction rozgrywająca się w dystopijnym świecie, gdzie ludzkość walczy o przetrwanie pod rządami totalitarnego reżimu.",
    "Romans historyczny osadzony w epoce wiktoriańskiej, pełen dramatów i nacisków społecznych.",
    # ... więcej opisów ...
]

# Generowanie embeddings dla opisów książek w języku polskim
embeddings_pl = np.array([bert_embeddings_pl(desc) for desc in book_descriptions_pl])

# Skalowanie embeddings przed grupowaniem
scaler_pl = StandardScaler()
scaled_embeddings_pl = scaler_pl.fit_transform(embeddings_pl)

# Grupowanie z użyciem DBSCAN
dbscan_pl = DBSCAN(eps=0.5, min_samples=2).fit(scaled_embeddings_pl)
labels_pl = dbscan_pl.labels_

# Ekstrakcja nazw własnych z opisów w języku polskim
named_entities_per_description_pl = [extract_named_entities_pl(desc) for desc in book_descriptions_pl]

# Wyświetlenie wyników
for i, (cluster, named_entities) in enumerate(zip(labels_pl, named_entities_per_description_pl)):
    print(f"Opis {i+1}:")
    print(f"Klaster - {cluster}")
    print(f"Byty nazwane - {', '.join(named_entities)}")
    print("--------------")


# Przykładowy opis książki w języku polskim
single_description_pl = "Mroczna opowieść fantasy o losach młodego maga, który musi stawić czoła dawnej przepowiedni i ocalić świat przed nadchodzącym złem."

# Generowanie embeddings dla pojedynczego opisu
single_embedding_pl = bert_embeddings_pl(single_description_pl)

# Skalowanie embeddings
single_scaled_embedding_pl = scaler_pl.transform([single_embedding_pl])

# Grupowanie z użyciem DBSCAN
single_label_pl = dbscan_pl.fit_predict(single_scaled_embedding_pl)

# Ekstrakcja nazw własnych z pojedynczego opisu
single_named_entities_pl = extract_named_entities_pl(single_description_pl)

# Wynik dla pojedynczego opisu
print(f"Opis: {single_description_pl}")
print(f"Klaster - {single_label_pl[0]}")
print(f"Byty nazwane - {', '.join(single_named_entities_pl)}")
