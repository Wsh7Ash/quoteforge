from decimal import Decimal, ROUND_HALF_UP

def money(x):
    return Decimal(str(x)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

def line_total(item):
    qty = Decimal(str(item['qty']))
    price = Decimal(str(item['price']))
    return money(qty * price)

def build_quote(items, tax_rate=0.0, discount=0.0):
    sub = sum(line_total(i) for i in items)
    disc = money(Decimal(str(sub)) * Decimal(str(discount)))
    taxable = sub - disc
    tax = money(Decimal(str(taxable)) * Decimal(str(tax_rate)))
    total = money(taxable + tax)
    return {
        'lines': [{'desc': i['desc'], 'qty': i['qty'], 'price': str(money(i['price'])),
                   'total': str(line_total(i))} for i in items],
        'subtotal': str(money(sub)),
        'discount': str(disc),
        'tax': str(tax),
        'total': str(total),
    }

def render_text(quote, title='Quote'):
    out = [f'=== {title} ===', '']
    for l in quote['lines']:
        out.append(f"  {l['qty']} x {l['desc']} @ {l['price']} = {l['total']}")
    out += ['', f"Subtotal: {quote['subtotal']}",
            f"Discount: {quote['discount']}",
            f"Tax:      {quote['tax']}",
            f"TOTAL:    {quote['total']}"]
    return '\n'.join(out)
