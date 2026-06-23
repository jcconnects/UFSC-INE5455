Feature: Encerramento do contrato de prestação de serviços entre AAA e BBB

  Como contratante (AAA Consultoria Empresarial) e contratada (BBB Tecnologia),
  queremos que o contrato inteligente saiba reconhecer quando o acordo terminou,
  para distinguir um encerramento bem-sucedido de um encerramento por descumprimento.

  Background: O contrato já está assinado e em vigor
    Given a AAA Consultoria Empresarial é a contratante
    And a BBB Tecnologia é a contratada
    And o contrato é assinado no dia 10
    And o projeto começa no dia 25
    And o projeto termina no dia 55
    And a contratada se compromete a prestar os serviços contratados
    And a contratada se compromete a enviar a fatura com o relatório das horas trabalhadas
    And a contratante se compromete a indicar um responsável técnico pelo contato com a contratada
    And a contratante se compromete a pagar metade do serviço na assinatura do contrato
    And a contratante se compromete a pagar a outra metade trinta dias após o início dos trabalhos
    And a contratante se compromete a pagar multa sobre as parcelas não quitadas no vencimento
    And a contratante se compromete a oferecer um pacote de manutenção após o período de garantia
    And as partes registraram o contrato
    And as partes colocaram o contrato em vigor

  @SuccessfullyTerminateContract
  Scenario: O contrato termina bem porque as partes cumpriram suas obrigações
    When a contratada presta os serviços contratados
    And a contratante paga metade do serviço na assinatura do contrato
    And a contratante paga a outra metade trinta dias após o início dos trabalhos
    Then o contrato deixa de estar em vigor
    And o contrato fica no estado "SuccessfulTermination"
    And a obrigação "oferecer um pacote de manutenção após o período de garantia" passa a valer

  # Basta uma única obrigação essencial não ser cumprida para o contrato terminar mal.
  # Cada linha abaixo conta a mesma história com uma obrigação diferente sendo descumprida.
  @UnsuccessfullyTerminateContract
  Scenario Outline: O contrato termina mal porque uma obrigação não foi cumprida
    When a parte responsável não cumpre a obrigação de "<obrigação>"
    Then o contrato deixa de estar em vigor
    And o contrato fica no estado "UnsuccessfulTermination"

    Examples:
      | obrigação                                                    |
      | prestar os serviços contratados                              |
      | enviar a fatura com o relatório das horas trabalhadas        |
      | pagar metade do serviço na assinatura do contrato            |
      | pagar a outra metade trinta dias após o início dos trabalhos |
