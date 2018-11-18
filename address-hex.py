import base58
import codecs
import ecdsa

from Crypto.Hash import keccak

# Private key used for testing
private_key = 'fa6a7b3c18af932b85183391702c172eefa512566ea08b178abb73a987e9571a'

private_key_bytes = codecs.decode(private_key, 'hex')
# Get ECDSA public ket
key = ecdsa.SigningKey.from_string(private_key_bytes, curve=ecdsa.SECP256k1).verifying_key
key_bytes = key.to_string()
key_hex = codecs.encode(key_bytes, 'hex')
# print (key_hex)

public_key_bytes = codecs.decode(key_hex, 'hex')
keccak_hash = keccak.new(digest_bits=256)
keccak_hash.update(public_key_bytes)
keccak_digest = keccak_hash.hexdigest()
# Take the last 20 bytes
wallet_len = 40
wallet = '41' + keccak_digest[-wallet_len:]
# print(wallet)

unencoded_string = bytes.fromhex(wallet)
encoded_string = base58.b58encode_check(unencoded_string)
print(encoded_string)