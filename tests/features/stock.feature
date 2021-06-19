Feature: Stock management
    A site where you save your products

    Scenario: Adding new products to the stock
        Given We have a stock with <products> products

        When I add <extra_products> to the stock

        Then I should now have <new_count> products

        Examples:
        | products | extra_products | new_count |
        |  5       |  5             |  10       |
        |  0       |  3             |  3        |
