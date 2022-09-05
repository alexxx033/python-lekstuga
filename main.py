### Reverse string ###

rev = "Hej på dig lille tjej"
print(rev[::-1] + rev)

### Reverse string ###

###############################

### Negativ rounding ###

print(round(1866.685, -1))  # Närmaste 10-tal
print(round(1866.685, -2))  # Närmaste 100-tal
print(round(1866.685, -3))  # Närmaste 1000-tal

### Negative rounding ###

################################

### Joining strings ###

words = ["PYTHON", "IS", "SO", "FUN"]
mening = " ".join(words)  # Joinar varje ord med " " <-- mellanrum
print(mening)

### Joining strings ###

################################

### Joining strings WITH FILTER ###

words = ["PYTHON", "IS", "NOT", "SO", "FUN"]
# Filtret kommer filtrera bort NOT från listan
mening = " ".join(filter(lambda x: x != "NOT", words))
print(mening)

### Joining strings WITH FILTER ###

################################

### Open a URL ###

# Har komenterat ut koden så den inte körs nu...

# import webbrowser
# webbrowser.open("http://www.gooogle.com/")

### Open a URL ###

################################

### Chaining comparison ###

n = 10
resultat = 1 < n < 20
print(resultat)  # Resultatet blir ett Boolean värde (TRUE or FALSE)

### Chaining comparison ###

################################

###
