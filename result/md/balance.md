# balance API documentation
http://heidianapi.com

---

## Models

### OrderSerializer

| Field | Type | Pattern | Required |
| ----- | ---- | ------- | -------- |
| `image` | string | ` ` | no |
| `id` | integer | ` ` | no |
| `title` | string | ` ` | no |

### BalanceOutSerializer

| Field | Type | Pattern | Required |
| ----- | ---- | ------- | -------- |
| `` |  | ` ` | no |
| `` |  | ` ` | no |
| `` |  | ` ` | no |
| `` |  | ` ` | no |
| `` |  | ` ` | no |
| `` |  | ` ` | no |
| `` |  | ` ` | no |
| `` |  | ` ` | no |
| `` |  | ` ` | no |
| `` |  | ` ` | no |

### WalletSerializer

| Field | Type | Pattern | Required |
| ----- | ---- | ------- | -------- |
| `` |  | ` ` | no |
| `` |  | ` ` | no |
| `` |  | ` ` | no |
| `` |  | ` ` | no |

### BalanceInSerializer

| Field | Type | Pattern | Required |
| ----- | ---- | ------- | -------- |
| `` |  | ` ` | no |
| `` |  | ` ` | no |
| `` |  | ` ` | no |
| `` |  | ` ` | no |
| `` |  | ` ` | no |
| `` |  | ` ` | no |
| `` |  | ` ` | no |
| `` |  | ` ` | no |
| `` |  | ` ` | no |

### WriteBalanceOutSerializer

| Field | Type | Pattern | Required |
| ----- | ---- | ------- | -------- |

### WriteOrderSerializer

| Field | Type | Pattern | Required |
| ----- | ---- | ------- | -------- |

### WriteBalanceInSerializer

| Field | Type | Pattern | Required |
| ----- | ---- | ------- | -------- |
| `channel` | string | ` ` | yes |

### WriteWalletSerializer

| Field | Type | Pattern | Required |
| ----- | ---- | ------- | -------- |
| `alipay` | string | ` ` | no |
| `balance` | string | ` ` | yes |
| `full_name` | string | ` ` | no |

### /api/balance/in/

```
GET /api/balance/in/
```

QueryString Parameters

| Attribute | Type | Required | Description | Example |
| --------- | ---- | -------- | ----------- | ------- |
| `page` | integer | no |  | 
| `page_size` | integer | no |  | 

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/balance/in/{pk}/

```
GET /api/balance/in/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/balance/out/

```
POST /api/balance/out/
```

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/balance/out/

```
GET /api/balance/out/
```

QueryString Parameters

| Attribute | Type | Required | Description | Example |
| --------- | ---- | -------- | ----------- | ------- |
| `page` | integer | no |  | 
| `page_size` | integer | no |  | 
| `created_at_from` | string | no |  | 
| `created_at_to` | string | no |  | 
| `order_by` | string | no |  | 

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/balance/out/{pk}/

```
PUT /api/balance/out/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/balance/out/{pk}/

```
GET /api/balance/out/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/balance/out/{pk}/

```
PATCH /api/balance/out/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/balance/out/{pk}/

```
DELETE /api/balance/out/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/balance/wallet/

```
GET /api/balance/wallet/
```

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/balance/wallet/{pk}/

```
GET /api/balance/wallet/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

