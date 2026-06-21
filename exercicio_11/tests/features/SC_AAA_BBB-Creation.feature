Feature: Create SC_AAA_BBB Contract

  # Não consegui achar os "poderes" do contrato
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

  @CreateContract
  Scenario: Create the SC_AAA_BBB contract
    When o contrato é criado
    Then o contrato não está ativado
    And o estado do contrato é "Created"
    And "oblig1" existe
    And "oblig1" não está ativada
    And "oblig2" existe
    And "oblig2" não está ativada
    And "oblig3" existe
    And "oblig3" não está ativada
    And "oblig4" existe
    And "oblig4" não está ativada
    And "oblig5" existe
    And "oblig5" não está ativada
    And "oblig6" existe
    And "oblig6" não está ativada
    And "oblig7" existe
    And "oblig7" não está ativada

  @ActivateContract
  Scenario: Activate the SC_AAA_BBB contract
    Given o contrato é criado
    When o contrato é ativado
    Then o contrato está ativado
    And o estado do contrato é "InEffect"
    And "oblig1" está ativada
    And "oblig2" está ativada
    And "oblig3" está ativada
    And "oblig4" está ativada
    And "oblig5" está ativada
    And "oblig6" está ativada
    And "oblig7" não está ativada
