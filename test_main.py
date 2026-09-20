import os
import unittest
from qrcode.image.base import BaseImage
from qrcode.image.pil import PilImage
from main import (
    validar_dados,
    formatar_nome_arquivo,
    gerar_qrcode_imagem,
    salvar_qrcode
)

class TestGeradorQRCode(unittest.TestCase):

    def test_validar_dados_valido(self):
        """Teste 1: Garante que dados válidos (texto ou link) são aceitos."""
        resultado = validar_dados("https://github.com/guhscf")
        self.assertTrue(resultado)

    def test_validar_dados_vazio_ou_invalido(self):
        """Teste 2: Garante que dados vazios ou apenas espaços lançam ValueError."""
        with self.assertRaises(ValueError):
            validar_dados("")
        with self.assertRaises(ValueError):
            validar_dados("   ")
        with self.assertRaises(ValueError):
            validar_dados(None)

    def test_formatar_nome_arquivo_sem_extensao(self):
        """Teste 3: Garante que a extensão .png é adicionada quando omitida."""
        nome = formatar_nome_arquivo("meu_qr")
        self.assertEqual(nome, "meu_qr.png")

    def test_formatar_nome_arquivo_com_extensao(self):
        """Teste 4: Garante que a extensão .png não é duplicada se já fornecida."""
        nome = formatar_nome_arquivo("codigo_final.png")
        self.assertEqual(nome, "codigo_final.png")

    def test_formatar_nome_arquivo_padrao_se_vazio(self):
        """Teste 5: Garante que um nome padrão é atribuído quando o nome for vazio."""
        nome = formatar_nome_arquivo("")
        self.assertEqual(nome, "qrcode_gerado.png")

    def test_gerar_qrcode_imagem_valida(self):
        """Teste 6: Garante que a função retorna uma imagem válida com dimensões maiores que zero."""
        img = gerar_qrcode_imagem("Teste de Conteúdo")
        self.assertIsInstance(img, (BaseImage, PilImage))
        largura, altura = img.size
        self.assertGreater(largura, 0)
        self.assertGreater(altura, 0)

    def test_salvar_qrcode_cria_arquivo_fisico(self):
        """Teste 7: Garante que o arquivo de imagem é salvo corretamente no disco e depois limpo."""
        arquivo_teste = "teste_temporario_qr.png"
        
        # Garante que não existe antes
        if os.path.exists(arquivo_teste):
            os.remove(arquivo_teste)

        try:
            arquivo_salvo = salvar_qrcode("Conteudo de teste", arquivo_teste)
            self.assertEqual(arquivo_salvo, arquivo_teste)
            self.assertTrue(os.path.exists(arquivo_teste))
            self.assertGreater(os.path.getsize(arquivo_teste), 0)
        finally:
            if os.path.exists(arquivo_teste):
                os.remove(arquivo_teste)

if __name__ == "__main__":
    unittest.main()
