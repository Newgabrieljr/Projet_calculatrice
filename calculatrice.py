# calculatrice.py

def addition(a, b):
    return a + b

def soustraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Erreur: Division par zéro"

def calculatrice():
    print("Sélectionnez l'opération:")
    print("1. Addition")
    print("2. Soustraction")
    print("3. Multiplication")
    print("4. Division")

    choix = input("Entrez le choix (1/2/3/4): ")

    num1 = float(input("Entrez le premier nombre: "))
    num2 = float(input("Entrez le deuxième nombre: "))

    if choix == '1':
        print(f"Résultat: {num1} + {num2} = {addition(num1, num2)}")
    elif choix == '2':
        print(f"Résultat: {num1} - {num2} = {soustraction(num1, num2)}")
    elif choix == '3':
        print(f"Résultat: {num1} * {num2} = {multiplication(num1, num2)}")
    elif choix == '4':
        print(f"Résultat: {num1} / {num2} = {division(num1, num2)}")
    else:
        print("Erreur: Choix invalide")

if __name__ == "__main__":
    calculatrice()