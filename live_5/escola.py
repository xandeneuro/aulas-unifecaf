def calcular_media(nota1, nota2):
    return (nota1 + nota2) / 2

def verificar_aprovacao(media):
    if media >= 7.0:
        return "Aprovado"
    else:
        return "Reprovado"
    
def calcularMediaTurma(medias):
    total_media = 0
    for media in medias:
        total_media += media
    return total_media / len(medias)