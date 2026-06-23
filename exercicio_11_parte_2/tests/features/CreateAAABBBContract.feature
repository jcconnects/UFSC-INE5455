Feature: Criação do contrato de prestação de serviços entre AAA e BBB

  Como contratante (AAA Consultoria Empresarial) e contratada (BBB Tecnologia),
  queremos registrar nosso acordo em um contrato inteligente
  para que cada parte saiba quais são suas obrigações e quando elas passam a valer.

  Background: As partes acordam os termos do contrato
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

  @CreateContract
  Scenario: O contrato é registrado, mas ainda não está valendo
    When as partes registram o contrato
    Then o contrato ainda não está em vigor
    And o contrato fica no estado "Created"
    And nenhuma das obrigações abaixo está valendo ainda:
      | obrigação                                                       |
      | prestar os serviços contratados                                 |
      | enviar a fatura com o relatório das horas trabalhadas           |
      | indicar um responsável técnico pelo contato com a contratada    |
      | pagar metade do serviço na assinatura do contrato               |
      | pagar a outra metade trinta dias após o início dos trabalhos    |
      | pagar multa sobre as parcelas não quitadas no vencimento        |
      | oferecer um pacote de manutenção após o período de garantia     |

  @ActivateContract
  Scenario: As partes colocam o contrato em vigor e as obrigações passam a valer
    Given as partes registraram o contrato
    When as partes colocam o contrato em vigor
    Then o contrato passa a estar em vigor
    And o contrato fica no estado "InEffect"
    And as seguintes obrigações passam a valer:
      | obrigação                                                       |
      | prestar os serviços contratados                                 |
      | enviar a fatura com o relatório das horas trabalhadas           |
      | indicar um responsável técnico pelo contato com a contratada    |
      | pagar metade do serviço na assinatura do contrato               |
      | pagar a outra metade trinta dias após o início dos trabalhos    |
      | pagar multa sobre as parcelas não quitadas no vencimento        |
    And a obrigação "oferecer um pacote de manutenção após o período de garantia" ainda não vale, pois só começa após a garantia
