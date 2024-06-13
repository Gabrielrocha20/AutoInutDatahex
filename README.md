# Projeto de Automação

Este projeto é uma automação que requer a execução de um script Python. Siga as instruções abaixo para configurar e executar o projeto.

## Como usar via terminal ou IDE

### 1. Criar o ambiente virtual

Para criar e ativar um ambiente virtual, execute os seguintes comandos no terminal:

```sh
python -m venv venv
venv/Scripts/activate
pip install -r requirements.txt
2. Executar o arquivo main.py
Após configurar o ambiente, rode o arquivo main.py. Ele solicitará as seguintes informações:

EMAIL
SENHA
SERIE FISCAL
O modelo será 65 por padrão.
```
3. Criar um executável
Para criar um executável do script, utilize o pyinstaller com o comando abaixo:

```sh
pyinstaller main.py --icon=icon.ico
```
4. Configurar os drivers
Após gerar o executável, siga estas etapas:

Vá até a pasta DRIVERS no repositório.
Navegue até a pasta onde o executável foi gerado.
Siga este caminho: nomedapasta\_internal\playwright\driver\package\.
Copie a pasta .local-browsers e cole-a dentro deste diretório.
Caso o driver seja antigo, substitua o driver dentro da pasta com a versão mais recente.

5. Executar o executável
Depois de configurar os drivers, você pode abrir o executável que ele será executado corretamente.

Contribuição
Sinta-se à vontade para abrir issues ou pull requests se desejar contribuir com este projeto.

Licença
Este projeto está licenciado sob a Licença XYZ. Consulte o arquivo LICENSE para obter mais informações.


