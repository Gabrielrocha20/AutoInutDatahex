from time import sleep

from playwright.sync_api import TimeoutError, expect, sync_playwright


class AutoInutData:
    def __init__(self) -> None:
        self.email = input("Email: ")
        self.senha = input("Senha: ")
        self.serie = input("Serie: ")
        self.BadRequest = []
     
    def initialize(self):
        try:
            with sync_playwright() as p:
                # verifica se possui o navegador na máquina do usuário, se não tiver, executa o próprio navegador do playwright
                # try:
                #     navegador = p.chromium.launch_persistent_context(rf'C:\Users\{self.username}\AppData\Local\Google\Chrome\User Data', headless=False, executable_path=r"C:\Program Files\Google\Chrome\Application\chrome.exe")
                # except:
                #     navegador = p.chromium.launch(headless=False) # headless

                navegador = p.chromium.launch(headless=False)
                # navegador = p.chromium.launch_persistent_context(rf'C:\Users\{self.hostname}\AppData\Local\Google\Chrome\User Data', headless=False, executable_path=r"C:\Program Files\Google\Chrome\Application\chrome.exe")
                page = navegador.new_page()
                page.goto("https://app.datahex.com.br/login")
                page.get_by_placeholder("Email").fill(self.email)
                page.get_by_placeholder("Senha").fill(self.senha)
                page.get_by_role("button", name="Entrar").click()
                page.get_by_role("button", name="description Notas").click()
                page.get_by_role("button", name="Inutilização de números").click()
                page.get_by_label("Nova inutilização de números").click()
                
                with open('list.txt', 'r') as file:
                    for row in file:
                        row = row.replace('\n', '').split('/')
                        row = [i.replace(' ', '')[2:] for i in row]
                        if len(row) == 1:
                            if page.get_by_label("Modelo de nota"):
                                page.get_by_label("Modelo de nota").click()
                                page.get_by_role("option", name="- NFC-e").click()
                            page.get_by_label("Série").fill(self.serie)
                            page.get_by_label("Início da faixa").fill(str(row[0]))
                            page.get_by_label("Fim da faixa").fill(str(row[0]))
                            page.get_by_label("Inutilizar numeração").click()
                            page.get_by_role("button", name="Continuar").click()
                            sleep(2)
                            if page.get_by_label("OK", exact=True).is_visible():
                                page.get_by_label("OK", exact=True).click()
                                self.BadRequest.append(str(row[0]))
                            else:
                                page.get_by_role("button", name="Sim").click()
                        else:
                            for i in range(int(row[0]), int(row[1]) + 1):
                                if page.get_by_label("Modelo de nota"):
                                    page.get_by_label("Modelo de nota").click()
                                    page.get_by_role("option", name="- NFC-e").click()
                                page.get_by_label("Série").fill(self.serie)
                                page.get_by_label("Início da faixa").fill(str(i))
                                page.get_by_label("Fim da faixa").fill(str(i))
                                page.get_by_label("Inutilizar numeração").click()
                                page.get_by_role("button", name="Continuar").click()
                                sleep(2)
                                # page.pause()
                                if page.get_by_label("OK", exact=True).is_visible():
                                    page.get_by_label("OK", exact=True).click()
                                    self.BadRequest.append(str(i))
                                else:
                                    page.get_by_role("button", name="Sim").click()
                with open('listErros.txt', 'w') as listErro:
                    for item in self.BadRequest:
                        listErro.write(item + '\n')
                       
        except TimeoutError:
            with open('listErros.txt', 'w') as listErro:
                for item in self.BadRequest:
                    listErro.write(item + '\n')
        except ValueError as e:
            # Código a ser executado para a exceção específica ValueError
            print(f"Erro de valor: {e}")
            with open('listErros.txt', 'w') as listErro:
                for item in self.BadRequest:
                    listErro.write(item + '\n')
        except Exception as e:
            # Código a ser executado para qualquer outra exceção
            print(f"Ocorreu um erro: {e}")
            with open('listErros.txt', 'w') as listErro:
                for item in self.BadRequest:
                    listErro.write(item + '\n')

    def ListNumber(self):
            with open('list.txt', 'r') as file:
                for row in file:
                    row = row.replace('\n', '').split('/')
                    row = [i.replace(' ', '')[2:] for i in row]
                    if len(row) == 1:
                        print(row[0])
                    else:
                        for i in range(int(row[0]), int(row[1]) + 1):
                            print(i)


if __name__ == '__main__':
    a = AutoInutData()
    a.initialize()