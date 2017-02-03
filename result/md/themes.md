# themes API documentation
http://heidianapi.com

---

## Models

### WriteThemeSerializer

| Field | Type | Pattern | Required |
| ----- | ---- | ------- | -------- |
| `metafield` | string | ` ` | no |
| `description` | string | ` ` | no |
| `author` | string | ` ` | no |
| `price` | string | ` ` | no |
| `title` | string | ` ` | no |
| `name` | string | ` ` | yes |

### ThemeUploadSerializer

| Field | Type | Pattern | Required |
| ----- | ---- | ------- | -------- |
| `settings_schema` | string | ` ` | no |
| `description` | string | ` ` | no |
| `author` | string | ` ` | no |
| `title` | string | ` ` | no |
| `version` | string | ` ` | no |
| `metafield` | string | ` ` | no |
| `id` | integer | ` ` | no |
| `name` | string | ` ` | yes |

### ThemePresetSerializer

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
| `` |  | ` ` | no |
| `` |  | ` ` | no |

### ThemeSerializer

| Field | Type | Pattern | Required |
| ----- | ---- | ------- | -------- |
| `` |  | ` ` | no |
| `` |  | ` ` | no |
| `` |  | ` ` | no |
| `` |  | ` ` | no |
| `` |  | ` ` | no |
| `` |  | ` ` | no |
| `` |  | ` ` | no |

### WriteThemePresetSerializer

| Field | Type | Pattern | Required |
| ----- | ---- | ------- | -------- |
| `description` | string | ` ` | no |
| `settings_data` | string | ` ` | no |
| `color` | string | ` ` | no |
| `assets` | string | ` ` | no |
| `name` | string | ` ` | yes |
| `screenshot_mobile` | string | ` ` | no |
| `metafield` | string | ` ` | no |
| `title` | string | ` ` | no |
| `theme` | string | ` ` | yes |
| `demo` | string | ` ` | no |
| `screenshot` | string | ` ` | no |

### WriteThemeUploadSerializer

| Field | Type | Pattern | Required |
| ----- | ---- | ------- | -------- |
| `settings_schema` | string | ` ` | no |
| `description` | string | ` ` | no |
| `author` | string | ` ` | no |
| `title` | string | ` ` | no |
| `version` | string | ` ` | no |
| `metafield` | string | ` ` | no |
| `name` | string | ` ` | yes |

### /api/themes/uploadtheme/{pk}/file/

```
POST /api/themes/uploadtheme/{pk}/file/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/themes/uploadtheme/{pk}/preset/

```
POST /api/themes/uploadtheme/{pk}/preset/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/themes/uploadtheme/{pk}/reset/

```
POST /api/themes/uploadtheme/{pk}/reset/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/themes/uploadtheme/{pk}/

```
PUT /api/themes/uploadtheme/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/themes/uploadtheme/{pk}/

```
PATCH /api/themes/uploadtheme/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/themes/theme/

```
POST /api/themes/theme/
```

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/themes/theme/

```
GET /api/themes/theme/
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

### /api/themes/theme/{pk}/

```
PUT /api/themes/theme/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/themes/theme/{pk}/

```
GET /api/themes/theme/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/themes/theme/{pk}/

```
PATCH /api/themes/theme/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/themes/theme/{pk}/

```
DELETE /api/themes/theme/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/themes/preset/

```
POST /api/themes/preset/
```

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/themes/preset/

```
GET /api/themes/preset/
```

QueryString Parameters

| Attribute | Type | Required | Description | Example |
| --------- | ---- | -------- | ----------- | ------- |
| `page` | integer | no |  | 
| `page_size` | integer | no |  | 
| `theme` | string | no |  | 
| `id` | string | no |  | 
| `id__in` | string | no |  | 
| `name` | string | no |  | 
| `name__in` | string | no |  | 
| `tag` | string | no |  | 
| `title` | string | no |  | 

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/themes/preset/{pk}/

```
PUT /api/themes/preset/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/themes/preset/{pk}/

```
GET /api/themes/preset/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/themes/preset/{pk}/

```
PATCH /api/themes/preset/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/themes/preset/{pk}/

```
DELETE /api/themes/preset/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

