Feature: Terminate SC_AAA_BBB Contract

  # Features foram mergeadas porque o background era o mesmo
  Background:
    Given a contratante "AAA Consultoria Empresarial Ltda"
    And a contratada "BBB Tecnologia Ltda"
    And data de criação do contrato "2026-06-20"
    And data de início do contrato "2026-07-05"
    And data de término do contrato "2026-08-04"
    And contratada tem obrigação "oblig1" de "Prestar os serviços contratados (cláusula 2.3.I)"
    And contratada tem obrigação "oblig2" de "Enviar fatura e relatório das horas prestadas (descrição detalhada das atividades e cronograma do projeto) (cláusula 2.3.VII)"
    And contratante tem obrigação "oblig3" de "Indicar um colaborador responsável pelos contatos de ordem técnica com a Contratada (cláusula 2.5.IV)"
    And contratante tem obrigação "oblig4" de "Realizar o pagamento de 50% do serviço desenvolvido na assinatura do contrato (cláusula 3.2)"
    And contratante tem obrigação "oblig5" de "Realizar o pagamento de 50% do serviço desenvolvido trinta dias após o início dos trabalhos (cláusula 3.2)"
    And contratante tem obrigação "oblig6" de "As parcelas não liquidadas nos respectivos vencimentos ficarão sujeitas à multa (cláusula 3.5)"
    And contratante tem obrigação "oblig7" de "Dispor para a contratada, após o período de garantia (90 dias após a entrega), um pacote de 20 horas mensais ao valor de 120 reais a hora"
    And o contrato é criado
    And o contrato é ativado

  @SuccessfullyTerminateContract
  Scenario: Successful termination #1 of SC_AAA_BBB contract
    When "oblig1" é satisfeita
    And "oblig4" é satisfeita
    And "oblig5" é satisfeita
    Then o contrato não está ativado
    And o estado do contrato é "Successful Termination"
    And "oblig7" está ativada

  # Foi utilizado scenario outline para evitar repetição de código
  @UnsuccessfullyTerminateContract
  Scenario Outline: Unsuccessful termination of SC_AAA_BBB contract
    When <oblig> não é satisfeita
    Then o contrato não está ativado
    And o estado do contrato é "Unsuccessful Termination"

    Examples:
      | oblig  |
      | oblig1 |
      | oblig2 |
      | oblig4 |
      | oblig5 |
