"""Accounts: a person's private home for saved conversations and tokens.

An account is optional. This package knows nothing about worlds, records,
voices, quotes or money: it holds a keyed hash of a sign-in address, the
sessions and codes that prove a person controls it. No
file it writes holds an address, a name or any conversation text. It imports
the standard library and itself, nothing else, and the conversation engine
imports nothing from it.

Two SQLite files of its own: a durable one (accounts and the deletion ledger)
and an ephemeral one (proof challenges, sessions, counters) that is never
backed up.
"""
