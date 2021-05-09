
texte = """Oceano Nox

Victor Hugo

Oh ! combien de marins, combien de capitaines
Qui sont partis joyeux pour des courses lointaines,
Dans ce morne horizon se sont évanouis ?
Combien ont disparu, dure et triste fortune ?
Dans une mer sans fond, par une nuit sans lune,
Sous l’aveugle océan à jamais enfoui ?

Combien de patrons morts avec leurs équipages ?
L’ouragan de leur vie a pris toutes les pages
Et d’un souffle il a tout dispersé sur les flots !
Nul ne saura leur fin dans l’abîme plongée,
Chaque vague en passant d’un butin s’est chargée ;
L’une a saisi l’esquif, l’autre les matelots !
"""

print(texte)

lignes = texte.splitlines()
print(lignes)
print(type(lignes))

# #for ligne in lignes:
    # #if ligne:
        # #print(ligne)

# Remplacement
mon_texte = texte.replace("combien de ", "pauvres ")
print(mon_texte)

# Trouver un truc fun
texte = texte.replace("a", "o")
texte = texte.replace("i", "a")
print(texte)
