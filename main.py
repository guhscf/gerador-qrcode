import qrcode
from qrcode.image.base import BaseImage

def validar_dados(dados: str) -> bool:
    """Valida se os dados para o QR Code são válidos (não vazios)."""
    if not isinstance(dados, str) or not dados.strip():
        raise ValueError("Os dados para gerar o QR Code não podem ser vazios.")
    return True

def formatar_nome_arquivo(nome_arquivo: str) -> str:
    """Garante que o arquivo tenha a extensão .png e um nome válido."""
    if not isinstance(nome_arquivo, str) or not nome_arquivo.strip():
        nome_arquivo = "qrcode_gerado.png"
    
    nome_arquivo = nome_arquivo.strip()
    if not nome_arquivo.lower().endswith('.png'):
        nome_arquivo += '.png'
    return nome_arquivo

def gerar_qrcode_imagem(dados: str, box_size: int = 10, border: int = 4) -> BaseImage:
    """Gera o objeto de imagem do QR Code a partir dos dados fornecidos."""
    validar_dados(dados)
    
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H, # Alta correção de erro
        box_size=box_size,
        border=border,
    )
    qr.add_data(dados)
    qr.make(fit=True)
    return qr.make_image(fill_color="black", back_color="white")

def salvar_qrcode(dados: str, nome_arquivo: str) -> str:
    """Gera e salva o QR Code no disco com o nome de arquivo especificado."""
    validar_dados(dados)
    nome_formatado = formatar_nome_arquivo(nome_arquivo)
    
    img = gerar_qrcode_imagem(dados)
    img.save(nome_formatado)
    return nome_formatado

def criar_qrcode():
    """Interface interativa de linha de comando para gerar QR Code."""
    print("=== Gerador de QR Code ===")
    dados = input("Digite o link ou texto para o QR Code: ")
    nome_arquivo = input("Digite o nome do arquivo para salvar (ex: meu_codigo.png): ")

    try:
        arquivo_final = salvar_qrcode(dados, nome_arquivo)
        print(f"\n✅ Sucesso! Seu QR Code foi gerado e salvo como '{arquivo_final}'.")
    except Exception as e:
        print(f"\n❌ Ocorreu um erro ao gerar o QR Code: {e}")

if __name__ == "__main__":
    criar_qrcode()