from quoteforge.calc import build_quote, line_total, money
def test_line_total():
    assert line_total({'desc':'a','qty':2,'price':'10.00'}) == money('20.00')
def test_tax_and_total():
    q = build_quote([{'desc':'a','qty':1,'price':'100.00'}], tax_rate=0.1)
    assert q['subtotal'] == '100.00'
    assert q['tax'] == '10.00'
    assert q['total'] == '110.00'
def test_discount_before_tax():
    q = build_quote([{'desc':'a','qty':1,'price':'100.00'}], tax_rate=0.1, discount=0.2)
    assert q['discount'] == '20.00'
    assert q['tax'] == '8.00'
    assert q['total'] == '88.00'
def test_money_rounding():
    assert money('10.005') == money('10.01')
