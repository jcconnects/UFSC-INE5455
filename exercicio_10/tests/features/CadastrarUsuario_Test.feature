Feature: Cadastrar Usuario
  Cadastrar usuarios

Scenario: Cadastrar Usuario com Sucesso
Given o nome de usuario Ernani Cesar
  And o endereco Campus Universitario
  And o CPF 055.761.919-00
  And o e-mail ernani.santos@posgrad.ufsc.br
When O usuario eh cadastrado
Then O sistema deve possuir usuarios
