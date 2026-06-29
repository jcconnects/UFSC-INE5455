Feature: Criação do contrato de prestação de serviços entre AAA e BBB

  Como contratante (AAA Consultoria Empresarial) e contratada (BBB Tecnologia),
  queremos registrar nosso acordo em um contrato inteligente
  para que cada parte saiba quais são suas obrigações e quando elas passam a valer.

  Background: As partes acordam os termos do contrato
    Given a AAA Consultoria Empresarial é a contratante
    And a BBB Tecnologia é a contratada
    And o contrato é assinado no dia 10

  @CreateContract
  Scenario: O contrato é registrado, mas ainda não está valendo
    When o contrato passa a existir
    Then o contrato não está ativo
    And o estado do contrato é "Created"

  @ActivateContract
  Scenario: As partes colocam o contrato em vigor e as obrigações passam a valer
    Given o contrato existe
    When o contrato é ativado
    Then o contrato está ativo
    And o estado do contrato é "InEffect"
