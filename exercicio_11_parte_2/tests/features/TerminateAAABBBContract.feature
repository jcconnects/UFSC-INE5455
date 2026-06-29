Feature: Encerramento do contrato de prestação de serviços entre AAA e BBB

  Como contratante (AAA Consultoria Empresarial) e contratada (BBB Tecnologia),
  queremos que o contrato inteligente reconheça quando o acordo terminou
  para distinguir um encerramento bem-sucedido de um encerramento por descumprimento.

  Background: As partes acordam os termos do contrato
    Given a AAA Consultoria Empresarial é a contratante
    And a BBB Tecnologia é a contratada
    And o contrato é assinado no dia 10

  @SuccessfullyTerminateContract
  Scenario: O contrato termina bem porque as partes cumpriram suas obrigações
    Given o contrato existe
    And o contrato está ativo
    When a contratada presta os serviços contratados
    And a contratante paga metade do serviço na assinatura do contrato
    And a contratante paga a outra metade trinta dias após o início dos trabalhos
    Then o contrato não está ativo
    And o estado do contrato é "SuccessfulTermination"

  @UnsuccessfullyTerminateContract
  Scenario Outline: O contrato termina mal porque uma obrigação não foi cumprida
    Given o contrato existe
    And o contrato está ativo
    When a parte responsável não cumpre sua obrigação
    Then o contrato não está ativo
    And o estado do contrato é "UnsuccessfulTermination"

