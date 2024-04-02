from jwcrypto import jwk

# jwkpair = jwk.JWK.generate(kty='RSA', size=2048) 
jwkpair = jwk.JWK.generate(kty='RSA', size=2048, kid='mykeyid123', use='sig', alg='RSA256')

# print(f'jwk=  {jwkpair}')

pubkey = jwkpair.export_public(as_dict=True)

privkey = jwkpair.export_private(as_dict=True)

print(f'public JWK= {pubkey}')
# {
#    "kty":"RSA",
#    "use":"sig",
#    "alg":"RSA256",
#    "kid":"mykeyid123",
#    "n":"v190o88vFKp9SaWEZcgzD1YYL_TtkmUEltd0v1gncBboY63cqkFJZ38XLgYt-HG2XmEcuLqpEOhoOlhipJokjqFbqVQFzYOXE6DKVKrkueUbSgxWGItcgfBQ2msoQ8HJSyxBrYwFJQUabGA1wc0C_9pcVm2aceJccjpH5Z5Utux0TKVgyAGFHAdWMIT89GT8Adeupatkagpi_bBAC7SBdBKbLVjsqwl_QIFe9iyOEGifsJKzDHz0TlDZie7SIimhCWpgBJLviHRIw5r2dOrtH2XWNWHyHtue1LhwNT7dO1R_53ft1yP8kqmEP9QhT7SIa0Lg4tZml2c6yYsMvz4ccw",
#    "e":"AQAB"
# }

print('---------------------------------------------')

print(f'private JWK= {privkey}')


# {
#    "kty":"RSA",
#    "use":"sig",
#    "alg":"RSA256",
#    "kid":"mykeyid123",
#    "n":"v190o88vFKp9SaWEZcgzD1YYL_TtkmUEltd0v1gncBboY63cqkFJZ38XLgYt-HG2XmEcuLqpEOhoOlhipJokjqFbqVQFzYOXE6DKVKrkueUbSgxWGItcgfBQ2msoQ8HJSyxBrYwFJQUabGA1wc0C_9pcVm2aceJccjpH5Z5Utux0TKVgyAGFHAdWMIT89GT8Adeupatkagpi_bBAC7SBdBKbLVjsqwl_QIFe9iyOEGifsJKzDHz0TlDZie7SIimhCWpgBJLviHRIw5r2dOrtH2XWNWHyHtue1LhwNT7dO1R_53ft1yP8kqmEP9QhT7SIa0Lg4tZml2c6yYsMvz4ccw",
#    "e":"AQAB",
#    "d":"Vb08ks-WNloT-9TuNnO1fJ-EAqhnb_lWTwaExd2G_c8lmtMgVB8f9gCYsAQQwIihvjMgHRtz96FIYSuMNlbhHg3o9Toxx1u3ahHV1I0kIK0mxsw0HpcBgS3b65-q0ICX4NgZLNnYzDc3GWsZapShTWPVjttYIMHbzUmTQKrpJXKQZwA560NFgfEizy-IKZyHwP32UyZMc_3Z5V2nDspfXSKiLLdE4yFb66w7YWAIP4uFjPOBfXhCwev0A08YtPkpcKvCkl_2sqcBMb0i0XllMfHEmdxrPYREXqDKRuCMn-hMKH_ZCZlo0nTNd1dhmhLN4Z960oNTwendNSR0Z6D1sQ",
#    "p":"4CngLlnVScVoOlD5Gd6RFGVsJLDMt876C-fNQJdxJi6AzrM2BUen_ePSMpVMJLHUagMS2w696Jn2uspt4cJydvA2G_-00j2Oz5X_91_LFELRScIJ3t63NaTBMwcdO6xh9I50tKbQqlYwTXuX8D3WCXUyJibgoOCRLT9MLdkJlKU",
#    "q":"2o1gslbC4pacjnPHmUefi6HhZ6opgIVr1fM-CQ7wUVqmyDXoglWaZQ1Osyx7ZkB3ZLPa2KC8nrN5VXS403Y-8loqdHoGiuqyPkkDqzzYXW1j7ZkfSgE_28diCSrCPB7VbFHGpkhZt5WMK08QrUgqfS3Io49RmIpN1rmkx4hB6Tc",
#    "dp":"tQ5dulJoyeseomugp9pzCCxbSs9aquQMZu1VhWRMyfAprcpmSaF0-Ma4ko6wL7tKvE27PyALGAKznG_AjOaHmbWvnrHMlTuPS-_2DRJcbwMBFDgbzN3K0RM_0T1fyUEU5Xjinr9WLx7qaMr5D9yCMqVsWhBwwsBfwlIr76Qr7tk",
#    "dq":"h9wDFFni5ECEKfnHRn3DrGWBXZPmIMLP-jwvgCoNMkWMEEGSvBLC27aeCbvJKhNBJRS5IpkpJ-6hqoHYs3t6PeXXJnkEwC6NhzKUWUqFpe5uhDD_xl1oeRNE2jX-cKkqOx_KwWuQehM5A2MvFskZwJ9JboOVUaIIKUdWK8OEVZk",
#    "qi":"3pMJnE-_M_0UCba9R6zL5UqqIBiQK_cvwzYohkaBb-lkrWI_qiGKNwGMxF1NsRZbAOoQVX0ReMhhB_QOIrgQBUYojRa2PAeH_uzzt98B0iCf9Y_SZH95I3OMoL3npnsi7yjNll1IFZcxSLL_1vTbTneIqitCrQphXii4MmznRNw"
# }