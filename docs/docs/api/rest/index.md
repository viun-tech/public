# AVIS RESTful API

## Introduction

The AVIS API is RESTful. Our API has predictable resource-oriented URLs, accepts JSON-encoded request bodies, returns
JSON-encoded responses, and uses standard HTTP response codes, authentication, and verbs.

The API is organized around resources. A non-exhaustive list of the main resources are:

* Case
* Image
* Inspection object
* Inspection result
* User, Team and Membership

See the [Swagger UI](https://docs.vu.engineering/api/rest/swagger/) for a complete list of resources and their endpoints.

## API conventions

### Resources

Resources names are lowercase, singular with no spaces in the API. For example, an Inspection Object will be named
as `inspectionobject`.

### Relationships

Resources are related to each other using foreign keys. For example, a `Case` resource has a foreign key to the
`InspectionObject` resource. This relationship is represented in the API's requests and responses as the ID of the
related resource.

For example to create a new case linked to the inspection object with ID 5, you would make a POST request to the
`/api/case/` endpoint with the following request body:

```json
{
  ...
  "inspection_object": 5,
  ...
}
```

Some resources support multiple relationships. For example, a `Case` resource can have multiple images. In this case,

```json
{
  ...
  "images": [
    1,
    2,
    3
  ],
  ...
}
```

### HTTP Verbs and actions

Each resource supports the following actions:

| Action         | Method | Endpoint              | Description                        |
|----------------|--------|-----------------------|------------------------------------|
| list           | GET    | /api/{resource}/      | List all resources of a given type |
| retrieve       | GET    | /api/{resource}/{id}/ | Retrieve a single resource  by id  |
| create         | POST   | /api/{resource}/      | Create a new resource              |
| update         | PUT    | /api/{resource}/{id}/ | Update a resource by id            |
| partial update | PATCH  | /api/{resource}/{id}/ | Partially update a resource by id  |
| delete         | DELETE | /api/{resource}/{id}/ | Delete a resource by id            |

#### Listing all existing resources

To list all existing resources of a given type, make a GET request to the resource's endpoint.

```bash title="List all cases"
curl -X 'GET' 'http://localhost:8000/api/case/' \
  -H 'accept: application/json' \
  -H 'X-Api-Key: <redacted>'
```

#### Retrieving a single resource

To retrieve a single resource, make a GET request to the resource's endpoint with the resource's ID.

```bash title="Retrieve a case"
curl -X 'GET' 'http://localhost:8000/api/case/1/' \
  -H 'accept: application/json' \
  -H 'X-Api-Key: <redacted>'
```

#### Creating a new resource

To create a new resource, make a POST request to the resource's endpoint with the resource's data required in the
request body.

```bash title="Create a new case"
curl -X 'POST' 'http://localhost:8000/api/case/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -H 'X-Api-Key: <redacted>' \
  -d '{
        "inspection_object": 5
        "opened_by": 45,
        "images": [],
        "team": 3
}'
```

#### Updating a resource

To update a resource, make a PUT request to the resource's endpoint with the resource's data required in the request

```bash title="Update a case"
curl -X 'PUT' 'http://localhost:8000/api/case/1/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -H 'X-Api-Key: <redacted>' \
  -d '{
        "inspection_object": 5
        "opened_by": 45,
        "images": [],
        "team": 3
}'
```

Please note that all the resource's required fields are required in the request body when updating a resource.

#### Partially updating a resource

To partially update a resource, make a PATCH request to the resource's endpoint with the resource's data required in the
request body.

```bash title="Partially update a case"
curl -X 'PATCH' 'http://localhost:8000/api/case/1/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -H 'X-Api-Key: <redacted>' \
  -d '{
        "inspection_object": 5
}'
```

In this case, only the fields that are required to be updated are passed in the request body.

#### Deleting a resource

To delete a resource, make a DELETE request to the resource's endpoint.

```bash title="Delete a case"
curl -X 'DELETE' 'http://localhost:8000/api/case/1/' \
  -H 'X-Api-Key: <redacted>' \
  -H 'accept: application/json'
```

### HTTP codes

The API uses standard HTTP response codes to indicate the success or failure of an API request. In general, codes in the
2xx range indicate success, codes in the 4xx range indicate an error that failed given the information provided, and
codes in the 5xx range indicate an error with AVIS's
servers.

#### Error codes

Most common error codes:

* 400 Bad Request: The request was invalid or cannot be otherwise served. An accompanying error message will explain
  further.
* 401 Unauthorized: The request requires user authentication.
* 403 Forbidden: The server understood the request, but is refusing to fulfill it. You might not have enough permissions
  to access the resource.
* 404 Not Found: The requested resource could not be found or does not exist.

## Authentication

The API supports two authentication methods:

* [API keys](#api-keys): for authenticating requests programmatically from your application
* [Session cookies](#session-cookies): for authenticating requests from your browser when you're logged in to the AVIS
  web UI

### API Keys

#### Create

!!! info

    The preferred way to create an API key is to use the AVIS web interface. The following instructions are for
    the rare case where you need to create a new API key programmatically using an existing API key.

API keys are used to authenticate requests made by your application to the AVIS API. To create an API key make a POST
request to the `/api/api-keys` endpoint:

```bash title="Create an API key"
curl -X 'POST' 'http://localhost:8000/api/keys/' \
        -H 'accept: */*' \
        -H 'Content-Type: application/json' \
        -H 'Cookie: sessionid=...; csrftoken=...'
```

This will return a JSON response containing your API key:

```json
{
  "key": "<redacted>",
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
  -H 'X-Api-Key: <redacted>'
```

#### Revoke

To revoke an API key make a POST request to the `/api/api-keys/{name}/revoke` endpoint where `{name}` is the name of
the
API key you want to revoke:

```bash title="Revoke an API key"
curl -X 'POST' 'http://localhost:8000/api/api-keys/Zygz3GsXnBSHBr6nDkb4Fh/revoke' \
        -H 'accept: */*' \
        -H 'Content-Type: application/json' \
        -H 'Cookie: sessionid=...; csrftoken=...'
```

### Session Cookies

!!! warning

    This authentication method is used for the AVIS web interface. It is not recommended to use it for programmatic
    access to the API.

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
