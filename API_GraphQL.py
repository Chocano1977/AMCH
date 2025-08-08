from azure.identity import InteractiveBrowserCredential
import requests
import json

# Acquire a token
# DO NOT USE IN PRODUCTION.
# Below code to acquire token is for development purpose only to test the GraphQL endpoint
# For production, always register an application in a Microsoft Entra ID tenant and use the appropriate client_id and scopes
# https://learn.microsoft.com/en-us/fabric/data-engineering/connect-apps-api-graphql#create-a-microsoft-entra-app

app = InteractiveBrowserCredential()
scp = 'https://analysis.windows.net/powerbi/api/user_impersonation'
result = app.get_token(scp)

if not result.token:
    print('Error:', "Could not get access token")

# Prepare headers
headers = {
    'Authorization': f'Bearer {result.token}',
    'Content-Type': 'application/json'
}

endpoint = 'https://aa26475996e2454183ef23e2949a4340.zaa.graphql.fabric.microsoft.com/v1/workspaces/aa264759-96e2-4541-83ef-23e2949a4340/graphqlapis/c4bfb983-6931-49a8-909c-458cdf65d3c8/graphql'
query = """
    query {
  libros(first: 10) {
     items {
        nombre
     }
  }
}
"""

variables = {

  }
  

# Issue GraphQL request
try:
    response = requests.post(endpoint, json={'query': query, 'variables': variables}, headers=headers)
    response.raise_for_status()
    data = response.json()
    print(json.dumps(data, indent=4))
except Exception as error:
    print(f"Query failed with error: {error}")
