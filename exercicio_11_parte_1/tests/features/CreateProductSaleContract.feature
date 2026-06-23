Feature: Create New Meat Contract
  Text...

  Background:
    Given the seller Seller01
    And the buyer Buyer01
    And the effective date of the contract 2020/2

  @CreateProductSaleContract
  Scenario: Create a product sale contract succeeding
    Given the contract title YYZ01
    And the currency BRL
    When the contract is created
    Then the contract seller must be Seller01
    And the contract buyer must be Buyer01
    And the contract title must be YYZ01
    And the currency must be BRL
    And the total price of the contract must be 0

  @CreateSeveralProductSaleContracts
  Scenario Outline: Create product sale contracts with different currencies
    Given the contract title <title>
    And the currency <currency>
    When the contract is created
    Then the contract seller must be <seller>
    And the contract buyer must be <buyer>
    And the contract title must be <title>
    And the currency must be <currency>
    And the total price of the contract must be 0

    Examples:
      | title | currency | seller   | buyer   |
      | YYZ01 | USD      | Seller01 | Buyer01 |
      | YYZ01 | CAN      | Seller01 | Buyer01 |
      | YYZ01 | BRL      | Seller01 | Buyer01 |

