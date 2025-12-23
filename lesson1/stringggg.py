# Lesson 1: String Handling Demonstrations

"""This script demonstrates various ways to work with strings in Python, including
multi‑line strings, raw strings, slicing, and common string methods.
"""

# Simple print statement
print("Selam, Dünya! Bu bir örnek.")

# Variable assignments with different string literals
kadir = "Merhaba Dünyakkkkk"
kadirr = "Merhaba \nDünya"
mesaj = "Merhaba \tDünya"
mesaj2 = """Merhaba Dünya"""

# Multi‑line string example using triple quotes
print("""
      Bu bir örnek çok satırlı string.
      Python ile kod yazıyoruz.
      
      Merhaba Dünya
      Merhaba \tDünya
      """, kadir + " " + kadirr)

# ---------------------------------------------------------------------
# String slicing examples
# ---------------------------------------------------------------------
print(mesaj[1:7])          # erhaba
print(mesaj2[0:7])         # Merhaba
print(mesaj2[0:7:2])       # Mrba
print(mesaj2[:])           # Merhaba Dünya
print(mesaj2[::-1])        # ayñuD abahreM (reversed)
print(mesaj2[::-2])        # abahreM (every second char from end)
print(mesaj2[::2])         # Mrba üa
print(mesaj2[::3])         # Mhaa

# ---------------------------------------------------------------------
# Common string methods
# ---------------------------------------------------------------------
print(mesaj2.upper())
print(mesaj2.lower())
print(mesaj2.title())
print(mesaj2.capitalize())
print(mesaj2.strip())
print(mesaj2.replace("Dünya", "Kadir"))
print(mesaj2.split())
print("Dünya" in mesaj2)
print("Kadir" in mesaj2)
print(mesaj2.find("Dünya"))
print(mesaj2.find("Kadir"))
print(mesaj2.index("Dünya"))
print(mesaj2.count("a"))
print(mesaj2.count("z"))
print(mesaj2.startswith("Merhaba"))
print(mesaj2.endswith("a"))
print(mesaj2.isalpha())
print(mesaj2.isdigit())
print(mesaj2.isspace())
print(mesaj2.islower())
print(mesaj2.isupper())

# ---------------------------------------------------------------------
# Alignment and length utilities
# ---------------------------------------------------------------------
print(mesaj2.center(30, "*"))
print(mesaj2.ljust(30, "-"))
print(len(mesaj2))

# ---------------------------------------------------------------------
# f‑string example
# ---------------------------------------------------------------------
yaş = 25
isim = "Kadir"
print(f"{isim}, {yaş} yaşındadır.")
