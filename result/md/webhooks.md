# webhooks API documentation
http://heidianapi.com

---

## Models

### WriteWebhookSerializer

| Field | Type | Pattern | Required |
| ----- | ---- | ------- | -------- |
| `url` | string | ` ` | yes |
| `metafield` | string | ` ` | no |
| `event` | string | ` ` | yes |

### WebhookSerializer

| Field | Type | Pattern | Required |
| ----- | ---- | ------- | -------- |
| `` |  | ` ` | no |
| `` |  | ` ` | no |
| `` |  | ` ` | no |
| `` |  | ` ` | no |
| `` |  | ` ` | no |
| `` |  | ` ` | no |

### /api/webhooks/webhook/

```
POST /api/webhooks/webhook/
```

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/webhooks/webhook/

```
GET /api/webhooks/webhook/
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

### /api/webhooks/webhook/{pk}/

```
PUT /api/webhooks/webhook/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/webhooks/webhook/{pk}/

```
GET /api/webhooks/webhook/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/webhooks/webhook/{pk}/

```
PATCH /api/webhooks/webhook/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/webhooks/webhook/{pk}/

```
DELETE /api/webhooks/webhook/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

