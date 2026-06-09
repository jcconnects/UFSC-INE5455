Feature: Cadastrar Usuario
  Cadastrar usuarios

Scenario Outline: Cadastrar Usuario com Sucesso
Given o nome de usuario <nome>
  And o CPF <cpf>
  And o endereco <end>
  And o e-mail <email>
When cadastra o usuario
Then o sistema retorna a mensagem <mensagem>

Examples:
  | nome         | cpf            | end   | email                       | mensagem                       |
  | Ernani Cesar | 055.761.919-00 | UFSC  | ernani@posgrad.ufsc.br      | Usuario cadastrado com sucesso |
  | Ernani Cesar | 055.761.919-99 | UFSC  | ernani@posgrad.ufsc.br      | CPF invalido: 055.761.919-99   |
  | Patricia     | 447.115.568-77 | UFSC  | patricia@posgrad.ufsc.br    | Usuario cadastrado com sucesso |
