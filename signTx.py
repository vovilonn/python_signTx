# from web3 import Web3
import json

import sys
sys.path.append('path')

with open('abi.json') as json_file:
    data = json.load(json_file)

    print(data)

contract = '0xf8e81D47203A594245E36C48e151709F0C19fBe8'
private_key = ''
nonce = 1


# def to_32byte_hex(val):
#     return Web3.toHex(Web3.toBytes(val).rjust(32, b'\0'))


# def sign_confirmation(nonce, contractaddr, private_key):
#     print('Signing data with settlementid, contractaddr...')
#     base_message = Web3.soliditySha3(['uint256', 'address'],
#                                      [nonce, Web3.toChecksumAddress(contractaddr)])
#     msg_hash = encode_defunct(base_message)
#     signed_msg = w3.eth.account.sign_message(msg_hash, private_key=private_key)
#     print(signed_msg.signature)
#     return signed_msg.signature
