#Criando a função principal da lógica do programa

def validar_questao(questao):
    campos_obrigatorios = [
        "id",
        "dificuldade",
        "categoria",
        "questao",
        "alternativas",
        "correta",
        "explicacao"
    ]
    
    for campo in campos_obrigatorios:
        if campo not in questao:
            return False
        
    if questao["dificuldade"] not in {"Fácil", "Média", "Difícil"}:
        return False
    if len(questao["alternativas"]) != 4:
        return False
    if questao["correta"] not in questao["alternativas"]:
        return False
    
    return True

def validar_id_unico(questoes):
    ids = [questao["id"] for questao in questoes]
    return len(ids) == len(set(ids))

def validar_texto(questao):
    if not questao["questao"].strip():
        return False
    if not questao["explicacao"].strip():
        return False
    
    return all(
        texto.strip()
        for texto in questao["alternativas"].values()
    )
