from rembg import remove
from PIL import Image 
import sys

def tirarFundoImagem(caminhoImagemOriginal, caminhoImagemSemFundo):
    imagemOriginal = Image.open(caminhoImagemOriginal)
    imageSemFundo = remove(imagemOriginal)
    imageSemFundo.save(caminhoImagemSemFundo)


caminhoImagemOriginal = sys.argv[1]
print(caminhoImagemOriginal)
caminhoImagemSemFundo = sys.argv[2]
print(caminhoImagemSemFundo)

tirarFundoImagem(caminhoImagemOriginal, caminhoImagemSemFundo)
