"""Additional contract cases with passing controls for each tagged workflow."""

import unittest

import workflows


def scenarios(i):
    amount = 1000 + 17 * i
    refund = i + 1
    events = [("sale", amount), ("refund", -refund)]
    if i >= 5:
        events += [events[i % 2]] * (1 + i % 4)
    yield "net", (events,), amount - refund
    cumulative = amount if i < 5 else (refund, -refund, amount + refund)[i % 3]
    yield "state", (amount, cumulative), "refunded" if i < 5 else ("partial" if i % 3 == 0 else "invalid")
    ref = f"pay-{i}"
    rows = [(ref, amount)] if i < 5 else [(f" PAY{i} ", amount - refund), (f"Pay-{i}", refund)]
    yield "match", (ref, amount, rows), "matched"

def load_tests(loader, standard_tests, pattern):
    suite = unittest.TestSuite()
    for index in range(50):
        for operation, arguments, expected in scenarios(index):
            def check(operation=operation, arguments=arguments, expected=expected):
                actual = getattr(workflows, operation)(*arguments)
                unittest.TestCase().assertEqual(actual, expected, f"{operation}{arguments!r}")

            suite.addTest(unittest.FunctionTestCase(check, description=f"{operation}_scale_{index + 1:02d}"))
    return suite
