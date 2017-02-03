# pricing API documentation
http://heidianapi.com

---

## Models

### PlanSerializer

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
| `` |  | ` ` | no |

### WritePlanBillingSerializer

| Field | Type | Pattern | Required |
| ----- | ---- | ------- | -------- |
| `plan_period` | string | ` ` | yes |
| `plan_name` | string | ` ` | yes |

### WritePlanSerializer

| Field | Type | Pattern | Required |
| ----- | ---- | ------- | -------- |
| `next_billing` | object | ` ` | yes |
| `active_billing` | object | ` ` | yes |

### PlanBillingSerializer

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

### /api/pricing/plan/

```
GET /api/pricing/plan/
```

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/pricing/plan/renew/

```
POST /api/pricing/plan/renew/
```

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/pricing/plan/upgrade/

```
POST /api/pricing/plan/upgrade/
```

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/pricing/plan/{pk}/

```
GET /api/pricing/plan/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/pricing/plan_billing/

```
GET /api/pricing/plan_billing/
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

### /api/pricing/plan_billing/{pk}/

```
GET /api/pricing/plan_billing/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

