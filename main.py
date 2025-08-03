"""
Project Level 1: Beginner

This project is designed for beginner learners who are still learning and practicing Python fundamentals.

Project Description
This program defines a string, counts how many uppercase and lowercase letters are present, and displays both counts.

Autor: Juan Sebastian Valencia Londoño
"""

def verificar_letras():
    entrada = str(input('Ingrese una frase:\n'))
    may, min = 0, 0
    try:
        for letra in entrada:
            if letra.islower():
                min += 1
            elif letra.isupper():
                may += 1
    except Exception as e:
        print(e)

    print(f'The number of uppercase is: {may}\nThe number of lowercase is: {min}')

if __name__ == "__main__":
    verificar_letras()

