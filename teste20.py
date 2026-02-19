#Desafio final
#Criar sistema de cadastro de alunos.
#Pedir:
#• nome
#• idade
#• 2 notas
#Regras:
#• validar tudo
#• calcular média
#• mostrar situação


while True:
    try: 
        nome = input("Digite o seu nome: ")
        
        idade = int(input("Digite a sua idade: "))
        if not (0 < idade < 110):
            print("Erro: Idade inválida (deve ser entre 1 e 109).")
            

        nota1 = float(input("Digite a nota 1: "))
        if not (0 <= nota1 <= 10):
            print("Erro: A nota deve ser entre 0 e 10.")
            

        nota2 = float(input("Digite a nota 2: "))
        if not (0 <= nota2 <= 10):
            print("Erro: A nota deve ser entre 0 e 10.")
            

        # Se chegou aqui, tudo está correto
        media = (nota1 + nota2) / 2
        print("\n--- Resultado ---")
        print("Nome: ", nome)
        print("Idade: ", idade)
        print("Média: ", media)
        
        break
        
    except ValueError:
        print("Erro: Digite valores numéricos válidos para idade e notas.")