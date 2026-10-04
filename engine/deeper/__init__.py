"""Go Deeper: pay-as-you-go conversation codes.

A code a participant holds buys more tokens. This package knows nothing
about worlds, records, voices or quotes, and imports nothing from the
conversation engine. It keeps two small SQLite files of its own: the meter
(a hash of each code, its balance, the Stripe payment id) and the claim table
(a purchase reference and the plain code, for one hour).
"""
