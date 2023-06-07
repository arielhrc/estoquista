import os
import datetime #eu odeio essa biblioteca
import shutil


def renamer(file, filepath, whitelist, extension2):
    recentdata = datetime.date(2000, 1, 1)
    for whitelisted in whitelist:
        if file.upper()[:len(whitelisted)] == whitelisted.upper() and extension == extension2:
            filedata = datetime.date.fromtimestamp(os.path.getmtime(filepath))
            os.rename(filepath, path + whitelisted + ' ' + str(filedata) + extension)
            if filedata > recentdata:
                recentdata = filedata
                        


def packer():
    pass


pathOriginal = 'C:/Users/ariel/OneDrive/Área de Trabalho/MAXXIVAREJO/'
path = 'C:/Users/ariel/OneDrive/Área de Trabalho/MAXXIVAREJO2/'
#SE NAO SABE AUTOMATIZAR NAO AUTOMATIZA ARIEL

lista = os.listdir(path)
for file in lista:
    filepath = path + file
    extension = file[-4:]
    obj = ['MaxxiVarejo', 'MaxxiRestaurante', 'PDV20', 'MaxxiPDV', 'ServidorMobile', 'APINFe_Servidor', 'ServidorMobile', 'Atendimento', 'Recepcao']
    renamer(file, filepath, obj, '.exe')
lista = os.listdir(path)
