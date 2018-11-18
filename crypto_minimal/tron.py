import base58
import codecs
import ecdsa
import random

from Crypto.Hash import keccak

class TronWallet:
    @staticmethod
    def generate_address(private_key):
        private_key_bytes = codecs.decode(private_key, 'hex')
        # Get ECDSA public key
        key = ecdsa.SigningKey.from_string(private_key_bytes, curve=ecdsa.SECP256k1).verifying_key
        key_bytes = key.to_string()
        key_hex = codecs.encode(key_bytes, 'hex')

        # Generate wallet address in hex
        public_key_bytes = codecs.decode(key_hex, 'hex')
        keccak_hash = keccak.new(digest_bits=256)
        keccak_hash.update(public_key_bytes)
        keccak_digest = keccak_hash.hexdigest()
        # Take the last 20 bytes
        wallet_len = 40
        wallet = '41' + keccak_digest[-wallet_len:]
        
        # Encode wallet address to base58check
        wallet_encoded = codecs.decode(base58.b58encode_check(bytes.fromhex(wallet)), 'UTF-8')
        return wallet_encoded