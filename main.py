import qrcode

def criar_qrcode():
    print("=== Gerador de QR Code ===")
    dados = input("Digite o link ou texto para o QR Code: ")
    nome_arquivo = input("Digite o nome do arquivo para salvar (ex: meu_codigo.png): ")

    # Garante que o arquivo tenha a extensão correta
    if not nome_arquivo.endswith('.png'):
        nome_arquivo += '.png'

    try:
        # Configuração do QR Code
        qr = qrcode.QRCode(
            version=1, 
            error_correction=qrcode.constants.ERROR_CORRECT_H, # Alta correção de erro
            box_size=10, 
            border=4, 
        )
        
        qr.add_data(dados)
        qr.make(fit=True)

        # Gera e salva a imagem
        img = qr.make_image(fill_color="black", back_color="white")
        img.save(nome_arquivo)
        
        print(f"\n✅ Sucesso! Seu QR Code foi gerado e salvo como '{nome_arquivo}'.")
    except Exception as e:
        print(f"\n❌ Ocorreu um erro ao gerar o QR Code: {e}")

if __name__ == "__main__":
    criar_qrcode()