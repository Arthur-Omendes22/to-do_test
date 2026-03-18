import json

ARQUIVO = "tarefas.json"

def carregar_tarefas():
    try:
        with open(ARQUIVO, "r") as f:
            return json.load(f)
    except:
        return []

def salvar_tarefas(tarefas):
    with open(ARQUIVO, "w") as f:
        json.dump(tarefas, f, indent=4)

def adicionar_tarefa(tarefas):
    titulo = input("Digite a tarefa: ")
    tarefas.append({"titulo": titulo, "concluida": False})
    salvar_tarefas(tarefas)
    print("✅ Tarefa adicionada!")

def listar_tarefas(tarefas):
    if not tarefas:
        print("Nenhuma tarefa encontrada.")
        return

    for i, tarefa in enumerate(tarefas):
        status = "✔" if tarefa["concluida"] else "✘"
        print(f"{i} - {tarefa['titulo']} [{status}]")

def concluir_tarefa(tarefas):
    listar_tarefas(tarefas)
    try:
        indice = int(input("Digite o número da tarefa: "))
        tarefas[indice]["concluida"] = True
        salvar_tarefas(tarefas)
        print("🎉 Tarefa concluída!")
    except:
        print("Erro ao concluir tarefa.")

def remover_tarefa(tarefas):
    listar_tarefas(tarefas)
    try:
        indice = int(input("Digite o número da tarefa para remover: "))
        tarefas.pop(indice)
        salvar_tarefas(tarefas)
        print("🗑 Tarefa removida!")
    except:
        print("Erro ao remover tarefa.")

def menu():
    tarefas = carregar_tarefas()

    while True:
        print("\n==== GERENCIADOR DE TAREFAS ====")
        print("1 - Adicionar tarefa")
        print("2 - Listar tarefas")
        print("3 - Concluir tarefa")
        print("4 - Remover tarefa")
        print("5 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_tarefa(tarefas)
        elif opcao == "2":
            listar_tarefas(tarefas)
        elif opcao == "3":
            concluir_tarefa(tarefas)
        elif opcao == "4":
            remover_tarefa(tarefas)
        elif opcao == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

#  TESTE PRA VER SE ESTÁ RODANDO CERTO
print("INICIOU O PROGRAMA")
input("Pressione ENTER para continuar...")

# INICIA O SISTEMA
menu()