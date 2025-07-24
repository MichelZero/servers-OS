#
porque o comando `yes | scp ...` não funciona no PowerShell e como fazer isso corretamente
```powershell
scp .\5.3.11.zip root@192.168.0.8:/tmp/ | yes
```
Aqui está o porquê o seu comando não funciona e quais são as maneiras corretas de fazer isso no PowerShell.

Por que | yes não funciona no PowerShell?

Pipeline de Objetos vs. Pipeline de Texto: No Linux/Bash, o pipe (|) conecta a "saída de texto padrão" (stdout) de um comando à "entrada de texto padrão" (stdin) do próximo. É um fluxo de texto simples. No PowerShell, o pipe passa objetos .NET completos de um cmdlet para o outro. Embora ele possa interagir com o stdin/stdout de programas externos como scp.exe, nem sempre funciona como esperado para prompts interativos.

O Comando yes não existe: yes é um utilitário padrão do GNU/Linux. Ele não existe nativamente no Windows ou no PowerShell.

Prompts Interativos: Muitos programas como ssh e scp não leem prompts de confirmação do stdin padrão. Em vez disso, eles se conectam diretamente ao terminal (TTY) para garantir que um usuário real esteja respondendo.

A Forma Correta de Fazer no PowerShell

A solução não é tentar imitar o yes, mas sim usar as opções que o próprio comando scp (e ssh) oferece para automação.

Método 1: A Solução Rápida e Direta (Recomendado)

Use as opções -o para modificar o comportamento do SSH e desativar a verificação interativa da chave do host.

```powershell
scp -o "StrictHostKeyChecking=no" -o "UserKnownHostsFile=nul" .\5.3.11.zip root@192.168.0.8:/tmp/
```

Vamos analisar o que isso faz:

-o "StrictHostKeyChecking=no": Esta é a opção chave. Ela diz ao scp para nunca perguntar sobre a chave do host. Ele irá adicioná-la automaticamente se for nova.

-o "UserKnownHostsFile=nul": Este é um truque útil no Windows (/dev/null no Linux). Ele diz ao scp para usar um arquivo de "hosts conhecidos" vazio e descartável. Isso evita que a chave do novo host seja salva permanentemente no seu arquivo C:\Users\SeuUsuario\.ssh\known_hosts, o que é bom para scripts que rodam contra máquinas temporárias (como em laboratórios).

Este é o método mais robusto e padrão para automação.

Método 2: A Forma Mais Segura para Scripts (Melhor Prática)

Se você estiver escrevendo um script que será reutilizado e a segurança é uma preocupação (para evitar ataques Man-in-the-Middle), a melhor prática é adicionar a chave do host ao seu arquivo known_hosts antes de executar o scp.

Passo 1: Adicionar a chave do host ao seu arquivo de hosts conhecidos.

Generated powershell
ssh-keyscan 192.168.0.8 >> $env:USERPROFILE\.ssh\known_hosts
IGNORE_WHEN_COPYING_START
content_copy
download
Use code with caution.
Powershell
IGNORE_WHEN_COPYING_END

ssh-keyscan 192.168.0.8: Este comando se conecta ao servidor e apenas captura sua chave pública.

>>: Este operador de redirecionamento adiciona a saída ao final de um arquivo.

$env:USERPROFILE\.ssh\known_hosts: Este é o caminho padrão para o arquivo known_hosts do usuário atual no Windows.

Passo 2: Executar o comando scp normalmente.

Generated powershell
scp .\5.3.11.zip root@192.168.0.8:/tmp/
IGNORE_WHEN_COPYING_START
content_copy
download
Use code with caution.
Powershell
IGNORE_WHEN_COPYING_END

Agora, o scp não fará a pergunta porque, ao verificar o arquivo known_hosts, ele encontrará uma chave correspondente para 192.168.0.8 e confiará na conexão.

Resumo
Método	Comando de Exemplo	Vantagens	Desvantagens
1. Rápido e Direto (Recomendado)	scp -o "StrictHostKeyChecking=no" -o "UserKnownHostsFile=nul" ...	Rápido, funciona em uma única linha, ótimo para labs.	Ignora a verificação de segurança da chave, vulnerável a MITM.
2. Mais Seguro (Melhor Prática)	ssh-keyscan <host> >> <known_hosts_file> <br> scp ...	Seguro, evita ataques MITM, ideal para automação.	Requer dois passos, um pouco mais complexo.

Para o seu caso, que parece ser um laboratório com PNETLab, o Método 1 é perfeitamente adequado e o mais prático.