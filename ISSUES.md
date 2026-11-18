# Assigned issues

# Prevent duplicate postings

A merchant receives two copies of a capture notification, a partial refund and a settlement with a differently formatted reference. Show the finance team which balances agree and which records need investigation.

Expected behavior: Each tuple contains an event ID and signed integer paise. Return the sum of first occurrences. A repeated ID always has the same payload. Negative entries represent refunds.

Reproduce with python3 -m unittest -v from the track directory. Inspect the failing net examples and trace one input through demo.py. Add one fresh boundary regression and demonstrate the corrected output.


# Classify refunds and reversals

A merchant receives two copies of a capture notification, a partial refund and a settlement with a differently formatted reference. Show the finance team which balances agree and which records need investigation.

Expected behavior: Given a positive capture and cumulative refund in paise, return captured, partial, refunded or invalid for negative or excessive refunds. A full reversal uses the full refunded amount.

Reproduce with python3 -m unittest -v from the track directory. Inspect the failing state examples and trace one input through demo.py. Add one fresh boundary regression and demonstrate the corrected output.


# Reconcile settlement records

A merchant receives two copies of a capture notification, a partial refund and a settlement with a differently formatted reference. Show the finance team which balances agree and which records need investigation.

Expected behavior: For one merchant and currency, match the reference ignoring case, hyphens and outer whitespace. Sum distinct settlement rows supplied for that reference. Return missing, matched, short or excess. Inputs already have unique row IDs upstream.

Reproduce with python3 -m unittest -v from the track directory. Inspect the failing match examples and trace one input through demo.py. Add one fresh boundary regression and demonstrate the corrected output.


