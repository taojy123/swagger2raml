# crm API documentation
http://heidianapi.com

---

## Models

### CustomerMessageSerializer

| Field | Type | Pattern | Required |
| ----- | ---- | ------- | -------- |
| `customer` | string | ` ` | no |
| `id` | integer | ` ` | no |
| `context` | string | ` ` | no |

### WriteCustomerSerializer

| Field | Type | Pattern | Required |
| ----- | ---- | ------- | -------- |
| `mobile` | string | ` ` | no |
| `gender` | string | ` ` | no |
| `note` | string | ` ` | no |
| `birthday` | string | ` ` | no |
| `full_name` | string | ` ` | no |
| `accepts_marketing` | boolean | ` ` | no |
| `email` | string | ` ` | no |

### WriteCustomFormSerializer

| Field | Type | Pattern | Required |
| ----- | ---- | ------- | -------- |
| `fields` | string | ` ` | no |

### WriteCustomerMessageSerializer

| Field | Type | Pattern | Required |
| ----- | ---- | ------- | -------- |
| `customer` | string | ` ` | no |
| `context` | string | ` ` | no |

### CustomerSerializer

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

### CustomFormSerializer

| Field | Type | Pattern | Required |
| ----- | ---- | ------- | -------- |
| `` |  | ` ` | no |
| `` |  | ` ` | no |

### /api/crm/customer/

```
POST /api/crm/customer/
```

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/crm/customer/

```
GET /api/crm/customer/
```

QueryString Parameters

| Attribute | Type | Required | Description | Example |
| --------- | ---- | -------- | ----------- | ------- |
| `page` | integer | no |  | 
| `page_size` | integer | no |  | 
| `id` | string | no |  | 
| `id__in` | string | no |  | 
| `coupon` | string | no |  | 
| `coupon__exclude` | string | no |  | 

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/crm/customer/{pk}/

```
PUT /api/crm/customer/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/crm/customer/{pk}/

```
GET /api/crm/customer/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/crm/customer/{pk}/

```
PATCH /api/crm/customer/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/crm/customer/{pk}/

```
DELETE /api/crm/customer/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/crm/custom_form/

```
POST /api/crm/custom_form/
```

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/crm/custom_form/

```
GET /api/crm/custom_form/
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

### /api/crm/custom_form/{pk}/

```
PUT /api/crm/custom_form/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/crm/custom_form/{pk}/

```
GET /api/crm/custom_form/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/crm/custom_form/{pk}/

```
PATCH /api/crm/custom_form/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/crm/custom_form/{pk}/

```
DELETE /api/crm/custom_form/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/crm/customer_message/

```
POST /api/crm/customer_message/
```

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

