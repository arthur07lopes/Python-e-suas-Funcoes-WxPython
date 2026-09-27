#Criando a função principal da lógica do programa

def validar_questao(questao):
    campos_obrigatorios = [
        "id",
        "pergunta",
        "categoria",
        "alternativas",
        "resposta",
        "explicacao"
    ]
    
    for campo in campos_obrigatorios:
        if campo not in questao:
            return False
        
    if questao["categoria"] not in [1, 2, 3]:
        return False
    if len(questao["alternativas"]) != 4:
        return False
    if questao["resposta"] not in questao["alternativas"]:
        return False
    
    return True

def validar_id_unico(questoes):
    ids = [questao["id"] for questao in questoes]
    return len(ids) == len(set(ids))

def validar_texto(questao):
    if not questao["pergunta"].strip():
        return False
    if not questao["explicacao"].strip():
        return False
    
    return all(
        texto.strip()
        for texto in questao["alternativas"].values()
    )
