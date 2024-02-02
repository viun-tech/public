# AVIS RESTful API

## Introduction

The AVIS API is RESTful. Our API has predictable resource-oriented URLs, accepts JSON-encoded request bodies, returns
JSON-encoded responses, and uses standard HTTP response codes, authentication, and verbs.

The API is organized around the following resources:

Coming soon...

## API conventions

Coming soon...

## Authentication

The API supports two authentication methods:

* [API keys](#api-keys): for authenticating requests programmatically from your application
* [Session cookies](#session-cookies): for authenticating requests from your browser when you're logged in to the AVIS
  web UI

### API Keys

#### Create

API keys are used to authenticate requests made by your application to the AVIS API. To create an API key make a POST
request to the `/api/api-keys` endpoint:

```bash title="Create an API key"

curl -X 'POST' 'http://localhost:8000/api/api-keys/' \
  -H 'accept: */*' \
  -H 'Content-Type: application/json' \
  -d '{
      "username": "your.email@mail.com",
      "password": "*********************"
  }'
```

This will return a JSON response containing your API key:

```json
{
  "key": "dIc9aNAo.AMhal3Ab7ggeEySCwnUpSptp4QKA6BCt",
  "created": "2024-01-24T05:16:31.894775Z",
  "name": "Zygz3GsXnBSHBr6nDkb4Fh",
  "expiry_date": "2024-01-31T05:16:31.887783Z",
  "revoked": false,
  "message": "Save this key somewhere safe - you will only see it once!"
}
```

You can use this key to authenticate your requests using the `X-Api-Key` header:

```bash title="Use the API key to query the API"
curl -X 'GET' 'http://localhost:8000/api/case/' \
  -H 'accept: application/json' \
  -H 'X-Api-Key: 8dbMsjJ1.1P9m9V0w7Kp9KmE3XZ6LdzY5kdHxO2wT'
```

#### Revoke

To revoke an API key make a PATCH request to the `/api/api-keys/{name}/revoke` endpoint where `{name}` is the name of
the
API key you want to revoke:

```bash title="Revoke an API key"
curl -X 'PATCH' 'http://localhost:8000/api/api-keys/Zygz3GsXnBSHBr6nDkb4Fh/revoke' \
  -H 'accept: */*' \
  -H 'Content-Type: application/json' \
  -d '{
      "username": "your.email@mail.com",
      "password": "*********************"
  }'
```

### Session Cookies

This requires the user to authenticate with username and password using the `/accounts/login/` endpoint **in their
browser**. The browser will store the session id in a cookie called `sessionid`.

A CSRF token needs be passed as well to protect against cross-site request forgery attacks. This is the default
authentication mechanism used for the AVIS web interface.

You can get the `csrftoken` cookie by making a unauthenticated request to any `/accounts` endpoint:

```bash title="Get the csrftoken cookie"
curl -c cookies.txt -s -X 'GET' 'http://localhost:8000/accounts/login/' \
  -H 'accept: */*' > /dev/null
```

The sessionid will be in the cookies.txt file:

```bash title="Get the sessionid cookie"
cat cookies.txt
```

The REST API can also be used with this authentication mechanism: just pass the `sessionid` and `csrftoken` cookies
with the request:

```bash title="Use the sessionid and csrftoken cookies to authenticate"
curl -X GET 'http://localhost:8000/api/cases/' \
  -H 'accept: application/json' \
  -H 'Cookie: sessionid=...; csrftoken=...'
```

The swagger UI can also be used with this authentication mechanism: just login normally with
the `/accounts/login/` endpoint in your browser and then use the swagger UI to make requests to the API.
