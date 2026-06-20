Feature: Create SC_AAA_BBB Contract
  Text...

  Background:
    Given <smart contract setup, including participants>

  @CreateContract
  Scenario: Create the SC_AAA_BBB contract
    Given <all information about the smart contract>
    When <the contract is created>
    Then <assure that the contract is correctly initialized and not activated>

  @ActivateContract
  Scenario: Activate the SC_AAA_BBB contract
    Given <all information about the smart contract>
    And <the contract is created>
    When <the contract is activated>
    Then <assure that the contract is correctly initialized and activated>
