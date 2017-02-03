# oauth API documentation
http://heidianapi.com

---

## Models

### WriteNewUserSerializer

| Field | Type | Pattern | Required |
| ----- | ---- | ------- | -------- |
| `theme_install_intent` | string | ` ` | no |
| `code` | string | ` ` | no |
| `password` | string | ` ` | yes |
| `email` | string | ` ` | yes |
| `shopname` | string | ` ` | yes |

### NewUserSerializer

| Field | Type | Pattern | Required |
| ----- | ---- | ------- | -------- |
| `domain` | string | ` ` | no |

### /api/oauth/dashboard/token/

```
POST /api/oauth/dashboard/token/
```

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/oauth/dashboard/password/forgot/

```
POST /api/oauth/dashboard/password/forgot/
```

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/oauth/dashboard/password/reset/

```
POST /api/oauth/dashboard/password/reset/
```

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/oauth/homepage/shop-create/

```
POST /api/oauth/homepage/shop-create/
```

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/oauth/homepage/shop-name/forgot/

```
POST /api/oauth/homepage/shop-name/forgot/
```

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

