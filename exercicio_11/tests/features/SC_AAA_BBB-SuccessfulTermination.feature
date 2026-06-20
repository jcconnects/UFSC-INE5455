Feature: Terminate Successfully SC_AAA_BBB Contract
  Text...

  Background:
    Given <smart contract setup, including participants>
    And <all information about the smart contract>
    And <the contract is created and activated>

  @SuccessfullyTerminateContract
  Scenario: Successful termination #1 of SC_AAA_BBB contract
    Given <information necessary to the scenario>
    When <oblig 1 is fulfilled>
    And <oblig 4 is fulfilled>
    And <oblig 5 is fulfilled>
    Then <assure that the contract is successfully terminated>
    Then <assure that the surviving obligations are activated>
