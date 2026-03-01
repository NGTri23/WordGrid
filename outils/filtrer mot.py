def quick_sort(words):
    if len(words) <= 1:
        return words

    pivot = words[len(words) // 2]
    pivot_len = len(pivot)

    left = []
    equal = []
    right = []

    for w in words:
        if len(w) < pivot_len:
            left.append(w)
        elif len(w) > pivot_len:
            right.append(w)
        else:
            equal.append(w)

    return quick_sort(left) + equal + quick_sort(right)


# Lecture du fichier
with open(f"c:/Users/ELEVE/Sac à dos 5eme1/3°/OneDrive/Sac à dos/Term/trophé/en_all.txt", 'r') as f:
    words = [line.strip() for line in f if line.strip()]

# # Tri rapide par taille croissante
sorted_words = quick_sort(words)

# Écriture du résultat
with open(f"c:/Users/ELEVE/Sac à dos 5eme1/3°/OneDrive/Sac à dos/Term/trophé/data/en_all.txt", "w") as f:
    for w in sorted_words:
      f.write(w + "\n")
