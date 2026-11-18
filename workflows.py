def net(events):
    return sum(amount for key,amount in events)

def state(capture, refund):
    return "refunded" if refund else "captured"

def match(ref, expected, rows):
    return "matched" if (ref,expected) in map(tuple,rows) else "missing"
