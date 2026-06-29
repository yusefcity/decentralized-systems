# Simple Contract Signing Demo
import hashlib
import time
import json

class Contract:
    def __init__(self, party_a, party_b, terms):
        self.party_a = party_a
        self.party_b = party_b
        self.terms = terms
        self.timestamp = time.time()
        self.signature = None

    def to_payload(self):
        payload = {
            "party_a": self.party_a,
            "party_b": self.party_b,
            "terms": self.terms,
            "timestamp": self.timestamp
        }
        return json.dumps(payload, sort_keys=True)

    def generate_hash(self):
        data = self.to_payload().encode("utf-8")
        return hashlib.sha256(data).hexdigest()

    def sign(self, private_key):
        base = self.generate_hash()
        combined = f"{base}:{private_key}"
        self.signature = hashlib.sha256(combined.encode()).hexdigest()
        return self.signature

    def verify(self, signature):
        return signature == self.signature

def create_contract():
    print("Creating contract...")
    return Contract("Alice", "Bob", "Transfer of digital asset rights")

def sign_flow(contract):
    key = "demo_private_key_123"
    sig = contract.sign(key)
    print("Contract signed:", sig)
    return sig

def verify_flow(contract, sig):
    result = contract.verify(sig)
    print("Verification result:", result)
    return result

def print_summary(contract):
    print("---- Contract Summary ----")
    print(contract.to_payload())
    print("--------------------------")

def audit_log(contract, sig):
    log = {
        "hash": contract.generate_hash(),
