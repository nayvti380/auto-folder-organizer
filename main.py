import os
from tkinter.filedialog import askdirectory

caminho = askdirectory(title='Selecione uma pasta')
print(f'Caminho selecionado: {caminho}')

lista_arquivos = os.listdir(caminho)

locais = {
    'imagens': ['.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff', '.webp','.dng'],
    'planilhas': ['.xlsx', '.xls'],
    'pdfs': ['.pdf'],
    'csv': ['.csv'],
    'musicas': ['.mp3', '.wav', '.flac', '.aac', '.ogg', '.wma', '.m4a'],
    'videos': ['.mp4', '.mkv', '.avi', '.mov', '.wmv', '.flv', '.webm'],
    'documentos': ['.doc', '.docx', '.txt', '.odt', '.rtf', '.xml', '.ics'],
    'aplicativos': ['.apk'],
    'programas': ['.exe', '.msi', '.bat', '.sh', '.jar', '.py', '.pkt','.php','.md','.crdownload','.webmanifest'],
    'jogos': ['.iso', '.bin', '.rom', '.cue', '.nrg'],
    'compactados': ['.zip', '.rar', '.7z', '.tar', '.gz']
}

for arquivo in lista_arquivos:
    caminho_arquivo = os.path.join(caminho, arquivo)
    if not os.path.isfile(caminho_arquivo):
        continue

    nome, extensao = os.path.splitext(arquivo)
    extensao = extensao.lower()
    movido = False

    for pasta, extensoes in locais.items():
        if extensao in extensoes:
            pasta_destino = os.path.join(caminho, pasta)
            if not os.path.exists(pasta_destino):
                os.mkdir(pasta_destino)
            novo_caminho = os.path.join(pasta_destino, arquivo)
            os.rename(caminho_arquivo, novo_caminho)
            print(f'Movido: {arquivo} → {pasta}')
            movido = True
            break

    if not movido:
        print(f'Arquivo {arquivo} não se encaixa em nenhuma categoria.')

print('Organização concluída.')