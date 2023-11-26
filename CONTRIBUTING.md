# Guia de Contribuição para o Projeto Connect CESAR

Se você está aqui, muito obrigado por demonstrar interesse em contribuir com o site do Connect CESAR! Para ajudar da melhor maneira possível, leia esse breve guia informando tudo que você deve saber sobre como enviar sua contribuição para a nossa equipe

## 1. Instruções

0. **Reporte uma Issue**
    - Se não deseja resolver uma issue encontrada, você pode simplesmente reportá-la na nossa página de [issues](https://github.com/caetrias/connectcesar/issues). Tente fornecer informações detalhadas sobre o problema encontrado, se possível com prints. Pode ser tanto um bug, que prejudica o uso do sistema, quanto uma issue, algo que pode ser melhorado, que a equipe tentará prontamente resolver. 

1. **Escolha uma Issue:**
   - Para encontrar um problema já existente em nosso site, olhe as nossas [issues](https://github.com/caetrias/connectcesar/issues) informadas e escolha uma que você tem interesse em resolver ou melhorar. Ou então, através do uso do site, você pode encontrar algum problema que não achamos. Nesse caso, sinta-se livre para escolher esse problema e tentar resolvê-lo. Lembrando que a issue escolhida pode tanto ser algo no html, encontrado na pasta de [templates](https://github.com/caetrias/connectcesar/tree/main/cesarconnect/templates), bem como problemas no código em Django, encontrado na pasta [CCapp](https://github.com/caetrias/connectcesar/tree/main/cesarconnect/ccapp).

2. **Fork do Repositório:**
   - Faça um fork do repositório para sua conta. Com isso, você conseguirá realizar as suas alterações sem modificar o repositório principal.

3. **Clone o Repositório**
    - Faça um clone do nosso repositório na sua máquina utilizando o seguinte comando:

    ```bash
    git clone https://github.com/caetrias/connectcesar.git
    ```

4. **Crie uma Branch:**
   - Crie a sua branch para trabalhar no desenvolvimento da feature contribuinte ao projeto. Lembre-se de sempre manter essa branch atualizada com a branch principal para evitar possíveis conflitos. Você consegue criar a sua branch com o seguinte comando:

   ```bash
    git checkout -b nome-da-sua-branch
    ```

5. **Desenvolva sua Contribuição:**
   - Desenvolva as alterações necessárias no código que resolvam a issue selecionada. Garanta que as boas práticas de programação sejam seguidas e que a segurança do site seja sempre mantida.

6. **Teste sua Contribuição:**
   - Antes de marcar a sua contribuição como finalizada, é importante testar as suas alterações localmente, de preferência com diferentes cenários de teste, a fim de garantir que não há problemas e que o seu código resolve a questão escolhida.

7. **Envie um Pull Request:**
   - Abra um pull request acessando essa [página](https://github.com/caetrias/connectcesar/pulls) explicando as mudanças que você realizou, bem como o problema que essas mudanças soluciona. Coloque um título sucinto e objetivo e forneça mais detalhes nos comentário do pull request. Se a equipe aceitar as mudanças, o seu pull request será aprovada, permitindo as suas alterações entrarem no repositório principal. Se não, negaremos  pull request, enviando uma mensagem de feedback do motivo de recusarmos. Sinta-se livre para enviar quantos pull requests desejar, bem como conversar com qualquer um dos membros sobre mais informações do projeto. 

## 2. Diretrizes de Código 

- Siga as boas práticas de codificação em Python, HTML e CSS.
  - Formatação correta do código.
  - Espaçamento adequado, nem ausente, nem excessivo
  - Utilize nomes de variáveis e funções adequados, que indiquem do que se trata
    - Dê preferência para nomes utilizando underline (_): nome_usuario, nome_grupo
  - Adicione comentários sempre que julgar necessário, evitando comentários óbvios
  - Escreva testes na pasta correta ([testes](https://github.com/caetrias/connectcesar/tree/main/cesarconnect/ccapp/tests)), cobrindo diferentes cenários de aceitação
  - Por tratar com informações de cadastro de usuários, priorize sempre a segurança, evitando vulnerabilidades no código
- Se essas diretrizes não forem seguidas, as chances da sua pull request ser aprovada são baixas, por isso tente sempre seguir essas instruções
- Em caso de dúvida, você pode olhar os códigos já desenvolvidos pela equipe, para saber como as suas alterações devem ser escritas


Se houver qualquer dúvida, sinta-se a vontade para enviar uma mensagem ao email jvmf@cesar.school, que a equipe responderá o mais rapidamente possível, ou envie uma mensagem a algum dos membros do grupo, procurando suas redes sociais em seus respectivos perfis. Muito obrigado por querer contribuir com o nosso projeto, a equipe do Connect CESAR encontra-se sempre a disposição!