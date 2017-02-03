# clients API documentation
http://heidianapi.com

---

## Models

### WriteTrialApplicationSerializer

| Field | Type | Pattern | Required |
| ----- | ---- | ------- | -------- |
| `description` | string | ` ` | no |
| `email` | string | ` ` | yes |
| `weidian` | string | ` ` | no |
| `homepage` | string | ` ` | no |
| `weibo` | string | ` ` | no |
| `telephone` | string | ` ` | yes |
| `industry` | string | ` ` | no |
| `name` | string | ` ` | yes |
| `misc_channel` | string | ` ` | no |
| `brand` | string | ` ` | yes |
| `wechat` | string | ` ` | no |
| `taobao` | string | ` ` | no |

### SubscriptionSerializer

| Field | Type | Pattern | Required |
| ----- | ---- | ------- | -------- |
| `id` | integer | ` ` | no |
| `email` | string | ` ` | yes |

### WriteSubscriptionSerializer

| Field | Type | Pattern | Required |
| ----- | ---- | ------- | -------- |
| `email` | string | ` ` | yes |

### WriteReleaseRSVPSerializer

| Field | Type | Pattern | Required |
| ----- | ---- | ------- | -------- |
| `mobile` | string | ` ` | no |
| `gender` | string | ` ` | no |
| `company` | string | ` ` | no |
| `email` | string | ` ` | no |
| `full_name` | string | ` ` | no |

### ReleaseRSVPSerializer

| Field | Type | Pattern | Required |
| ----- | ---- | ------- | -------- |
| `mobile` | string | ` ` | no |
| `gender` | string | ` ` | no |
| `company` | string | ` ` | no |
| `email` | string | ` ` | no |
| `full_name` | string | ` ` | no |
| `id` | integer | ` ` | no |

### TrialApplicationSerializer

| Field | Type | Pattern | Required |
| ----- | ---- | ------- | -------- |
| `description` | string | ` ` | no |
| `email` | string | ` ` | yes |
| `weidian` | string | ` ` | no |
| `homepage` | string | ` ` | no |
| `weibo` | string | ` ` | no |
| `telephone` | string | ` ` | yes |
| `industry` | string | ` ` | no |
| `name` | string | ` ` | yes |
| `misc_channel` | string | ` ` | no |
| `brand` | string | ` ` | yes |
| `wechat` | string | ` ` | no |
| `id` | integer | ` ` | no |
| `taobao` | string | ` ` | no |

### /api/clients/subscription/

```
POST /api/clients/subscription/
```

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/clients/trialapplication/

```
POST /api/clients/trialapplication/
```

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/clients/release_rsvp/

```
POST /api/clients/release_rsvp/
```

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/clients/translation/output_json/

```
GET /api/clients/translation/output_json/
```

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/clients/qiniu-uptoken/{bucket}

```
GET /api/clients/qiniu-uptoken/{bucket}
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `bucket` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/clients/wechat-jsapi-ticket/

```
GET /api/clients/wechat-jsapi-ticket/
```

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/clients/wechat-auth/

```
GET /api/clients/wechat-auth/
```

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

