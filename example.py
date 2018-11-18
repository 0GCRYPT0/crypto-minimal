import crypto_minimal

# Test key 
key0 = '6b26e3fb05c9fea259714b32974e8626b28591c3087dd7c250ad8b4f2893ddff'

# Generates random key
kg = crypto_minimal.KeyGenerator()
kg.seed_input('Truly random string. I rolled a dice and got 4.')
key1 = kg.generate_key()

# Generate wallet address encoded in base58check format
address0 = crypto_minimal.TronWallet.generate_address(key0)
address1 = crypto_minimal.TronWallet.generate_address(key1)
print('SampleKey: ' + key0)
print('SampleKey wallet address: ' + address0)
print('')
print('RandomKey: ' + key1)
print('RandomKey wallet address: ' + address1)