# Gerenciamento de Usuários no Linux

Este documento apresenta os principais comandos e práticas para gerenciar usuários em sistemas Linux, incluindo criação, modificação, remoção e permissões.

## Comandos Básicos

- **Adicionar novo usuário:**
  ```bash
  sudo adduser <nome_do_usuario>
  ```
- **Remover usuário e seu diretório home:**
  ```bash
  sudo deluser --remove-home <nome_do_usuario>
  ```
- **Alterar senha do usuário:**
  ```bash
  sudo passwd <nome_do_usuario>
  ```
- **Listar todos os usuários:**
  ```bash
  cut -d: -f1 /etc/passwd
  ```

## Gerenciamento de Grupos

- **Adicionar usuário a um grupo:**
  ```bash
  sudo usermod -aG <grupo> <nome_do_usuario>
  ```
- **Listar grupos de um usuário:**
  ```bash
  groups <nome_do_usuario>
  ```

## Permissões e Sudo

- **Adicionar usuário ao grupo sudo:**
  ```bash
  sudo usermod -aG sudo <nome_do_usuario>
  ```
- **Verificar se o usuário tem sudo:**
  ```bash
  groups <nome_do_usuario>
  ```

## Arquivos Importantes

- `/etc/passwd`: Informações dos usuários.
- `/etc/shadow`: Senhas dos usuários (criptografadas).
- `/etc/group`: Informações dos grupos.

## Exemplos

- Criar usuário com diretório home e shell bash:
  ```bash
  sudo adduser --shell /bin/bash <nome_do_usuario>
  ```
- Bloquear usuário:
  ```bash
  sudo usermod -L <nome_do_usuario>
  ```
- Desbloquear usuário:
  ```bash
  sudo usermod -U <nome_do_usuario>
  ```

## Dicas

- Sempre use `sudo` para tarefas administrativas.
- Remova usuários inativos para aumentar a segurança.
- Revise permissões de grupos regularmente.

## Referências

- [Documentação Oficial do Ubuntu sobre usuários](https://help.ubuntu.com/community/AddUsersHowto)
- [Linux User Management - DigitalOcean](https://www.digitalocean.com/community/tutorials/how-to-create-a-new-user-and-grant-permissions-in-linux)

---
Sinta-se à vontade para contribuir com sugestões ou melhorias!