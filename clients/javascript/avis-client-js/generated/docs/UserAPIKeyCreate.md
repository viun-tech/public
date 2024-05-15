# ViunAvisClientJs.UserAPIKeyCreate

## Properties

| Name           | Type        | Description                                                              | Notes      |
| -------------- | ----------- | ------------------------------------------------------------------------ | ---------- |
| **key**        | **String**  |                                                                          | [readonly] |
| **created**    | **Date**    |                                                                          | [readonly] |
| **name**       | **String**  | A free-form name for the API key. Need not be unique. 50 characters max. | [optional] |
| **expiryDate** | **Date**    | Once API key expires, clients cannot use it anymore.                     | [readonly] |
| **revoked**    | **Boolean** |                                                                          | [readonly] |
| **message**    | **String**  |                                                                          | [readonly] |
