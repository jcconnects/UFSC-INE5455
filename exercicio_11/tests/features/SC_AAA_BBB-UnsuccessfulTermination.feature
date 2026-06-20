Feature: Terminate Unsuccessfully SC_AAA_BBB Contract
  Text...

  Background:
    Given <smart contract setup, including participants>
    And <all information about the smart contract>
    And <the contract is created and activated>

  @UnsuccessfullyTerminateContract
  Scenario: Unsuccessful termination #1 of SC_AAA_BBB contract
    Given <information necessary to the scenario>
    When <~oblig 1>
    Then <assure that the contract is terminated>

  @UnsuccessfullyTerminateContract
  Scenario: Unsuccessful termination #2 of SC_AAA_BBB contract
    Given <information necessary to the scenario>
    When <~oblig 2>
    Then <assure that the contract is terminated>

  Scenario: Unsuccessful termination #3 of SC_AAA_BBB contract
    Given <information necessary to the scenario>
    When <~oblig 4>
    Then <assure that the contract is terminated>

  Scenario: Unsuccessful termination #4 of SC_AAA_BBB contract
    Given <information necessary to the scenario>
    When <~oblig 5>
    Then <assure that the contract is terminated>
