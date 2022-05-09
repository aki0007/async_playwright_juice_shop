import allure


def test_update_company(page, successful_login) -> None:
    # Click text=Apple Juice (1000ml) 1.99¤Add to Basket
    page.locator("text=Apple Juice (1000ml) 1.99¤Add to Basket >> [aria-label=\"Click\\ for\\ more\\ information\\ about\\ the\\ product\"]").click()
    # Click text=Write a review
    page.locator("text=Write a review").click()
    # Click [aria-label="Text\ field\ to\ review\ a\ product"]
    page.locator("[aria-label=\"Text\\ field\\ to\\ review\\ a\\ product\"]").click()
    # Fill [aria-label="Text\ field\ to\ review\ a\ product"]
    page.locator("[aria-label=\"Text\\ field\\ to\\ review\\ a\\ product\"]").fill("Automated review")
    # Click [aria-label="Send\ the\ review"]
    page.locator("[aria-label=\"Send\\ the\\ review\"]").click()

    # TODO page.pause()
    # page.pause()

    # Click [aria-label="Close\ Dialog"]
    page.locator("[aria-label=\"Close\\ Dialog\"]").click()
    # Click text=Apple Juice (1000ml) 1.99¤Add to Basket >>
    page.locator("text=Apple Juice (1000ml) 1.99¤Add to Basket >> [aria-label=\"Click\\ for\\ more\\ information\\ about\\ the\\ product\"]").click()
    # Click mat-expansion-panel-header[role="button"]:has-text("Reviews")
    page.locator("//span[text()='Reviews']").click()
    # Click [aria-label="Close\ Dialog"]
    page.locator("[aria-label=\"Close\\ Dialog\"]").click()


#def test_validate_banana_description(page, successful_login):
 #   # Click text=Banana Juice (1000ml)
  #  page.locator("text=Banana Juice (1000ml)").click()
   # # Click text=Monkeys love it the most.
   # assert page.locator("text=Monkeys love it the most.")
   # # Click [aria-label="Close\ Dialog"]
   # page.locator("[aria-label=\"Close\\ Dialog\"]").click()


def test_add_apple_pomace_to_basket(page, successful_login):
    # Click text=Me want it!
    page.locator("text=Me want it!").click()
    # Click text=Apple Pomace 0.89¤Add to Basket >> [aria-label="Add\ to\ Basket"]
    page.locator("text=Apple Pomace 0.89¤Add to Basket >> [aria-label=\"Add\\ to\\ Basket\"]").click()
    # Click [aria-label="Show\ the\ shopping\ cart"]
    page.locator("[aria-label=\"Show\\ the\\ shopping\\ cart\"]").click()
    assert page.url == "https://juice-shop.herokuapp.com/login#/basket"
    # Click text=Apple Pomace
    assert page.locator("text=Apple Pomace")


def test_fail_on_purpose(page, successful_login):
    # Click text=Monkeys love it the most.
    assert page.locator("text=Cows love it the most.")
