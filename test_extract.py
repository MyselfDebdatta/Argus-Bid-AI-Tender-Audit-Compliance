import os
import traceback
from tender_audit_platform import get_engine

engine = get_engine()

# Read the actual master bid text from somewhere?
# I don't have the user's master bid. But I can create a mock one.
bid_text = "Master Bid Document\n" * 1000

# Let's bypass the vectorstore to force it into fallback context or just let it run.
try:
    print("Running parse_master_bid...")
    result = engine.parse_master_bid(bid_text)
    print("Success:", result)
except Exception as e:
    print("Outer Error:", traceback.format_exc())
