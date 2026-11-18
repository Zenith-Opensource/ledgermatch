# LedgerMatch

A merchant receives two copies of a capture notification, a partial refund and a settlement with a differently formatted reference. Show the finance team which balances agree and which records need investigation.

Run these commands inside this folder (Python 3.9+, standard library only).

```sh
python3 demo.py
python3 -m unittest -v
```

The demo reads 6,000 synthetic JSONL records. Each record names an operation and its positional inputs. Edit the existing workflow module, keep passing cases green, and add a useful report of your choice. Demonstrate one record before and after your fix.

## Issue 1 · Prevent duplicate postings

Each tuple contains an event ID and signed integer paise. Return the sum of first occurrences. A repeated ID always has the same payload. Negative entries represent refunds.

## Issue 2 · Classify refunds and reversals

Given a positive capture and cumulative refund in paise, return captured, partial, refunded or invalid for negative or excessive refunds. A full reversal uses the full refunded amount.

## Issue 3 · Reconcile settlement records

For one merchant and currency, match the reference ignoring case, hyphens and outer whitespace. Sum distinct settlement rows supplied for that reference. Return missing, matched, short or excess. Inputs already have unique row IDs upstream.

## How to contribute

See [CONTRIBUTING.md](CONTRIBUTING.md) for the fork, branch and pull request workflow.

Complete [approach.md](approach.md), [challenges.md](challenges.md) and [optimizations.md](optimizations.md).
