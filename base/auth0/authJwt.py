import http.client

conn = http.client.HTTPSConnection("dev-1zj6gvptfqijugj1.us.auth0.com")

payload = "{\"client_id\":\"OpuY7jP6eFbm7loz2xgRlMXCIOsh5bPF\",\"client_secret\":\"0u-hT8cgejCRGEuJ334jbCpLQs5QEEXOxwSxqzch7_beT3M0i1PMIfbXzQYI3kYD\",\"audience\":\"https://dev-1zj6gvptfqijugj1.us.auth0.com/api/v2/\",\"grant_type\":\"client_credentials\"}"

headers = { 'content-type': "application/json" }

conn.request("POST", "/oauth/token", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))