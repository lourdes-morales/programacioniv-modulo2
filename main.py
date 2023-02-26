from base import engine, Session, Base
from diccionario import Diccionario
import sys

Base.metadata.create_all(engine)

session = Session()

try:

    def principal():
        menu = """
    \n__________________________________________
            DICCIONARIO DE SLANG PANAMEÑO
    a) Agregar nueva palabra
    b) Editar palabra existente
    c) Eliminar palabra existente
    d) Ver listado de palabras
    e) Buscar significado de palabra
    f) Salir
    __________________________________________
    Selecciona una opción: """

        option = ""
        while option != "f":
            option = input(menu).lower()
            if option == "a":
                word = input("Ingresa la palabra: ")
                # Comprobar si la palabra ya existe
                possibleMeaning = getMeaning(word)
                if possibleMeaning:
                    print(f"La palabra '{word}' ya existe")
                # Si no existe:
                else:
                    meaning = input("Ingresa el significado: ")
                    addWord (word, meaning)
            if option == "b":
                word = input("Ingresa la palabra que quieres editar: ")
                newMeaning = input("Ingresa el nuevo significado: ")
                editWord (word, newMeaning)
            if option == "c":
                word = input("Ingresa la palabra a eliminar: ")
                removeWord(word)
            if option == "d":
                words = getWords()
                print("=== Lista de palabras ===")
                for word in words:
                    print(word)
            if option == "e":
                word = input("Ingresa la palabra de la cual quieres saber el significado: ")
                meaning = getMeaning(word)
                if meaning:
                    print(f"El significado de '{word}' es: {meaning}")
                else:
                    print(f"Palabra '{word}' no encontrada")
        else:
            print("\nEl programa ha finalizado")
            sys.exit()

    #MÉTODO PARA AGREGAR PALABRA
    def addWord(word, meaning):
        new_word = Diccionario(word=word, meaning=meaning)
        session.add(new_word)
        session.commit()
        print(f"Palabra agregada: {word}")


    #MÉTODO PARA EDITAR PALABRA
    def editWord(word, newMeaning):
        word_obj = session.query(Diccionario).filter_by(word=word).first()
        if word_obj:
            word_obj.meaning = newMeaning
            session.commit()
            print(f"Palabra actualizada: {word}")
        else:
            print(f"Palabra '{word}' no encontrada")


    #MÉTODO PARA ELIMINAR PALABRA
    def removeWord(word):
        word_obj = session.query(Diccionario).filter_by(word=word).first()
        if word_obj:
            session.delete(word_obj)
            session.commit()

    #MÉTODO PARA OBTENER PALABRAS
    def getWords():
        words = session.query(Diccionario.word).all()
        return [word for (word,) in words]

    #MÉTODO PARA OBTENER SIGNIFICADO DE UNA PALABRA
    def getMeaning(word):
        word_obj = session.query(Diccionario).filter_by(word=word).first()
        if word_obj:
            return word_obj.meaning
        else:
            return None


    #GARANTIZAR QUE LA FUNCIÓN 'principal' SOLO SE EJECUTE CUANDO EL ARCHIVO SE EJECUTA COMO PROGRAMA PRINCIPAL Y NO CUANDO SE IMPORTA COMO MÓDULO
    if __name__ == '__main__':
        principal()

#MANEJO DE EXCEPCIONES
except ValueError:
    print("ExceptionError - ValueError: Database not connected")
except TypeError:
    print("ExceptionError - TypeError: Database not connected")
except TimeoutError:
    print("ExceptionError - Timeout: Database not connected")

finally:
    session.commit()
    session.close()