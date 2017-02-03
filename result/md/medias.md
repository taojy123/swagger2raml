# medias API documentation
http://heidianapi.com

---

## Models

### FileSerializer

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
| `` |  | ` ` | no |
| `` |  | ` ` | no |
| `` |  | ` ` | no |
| `` |  | ` ` | no |
| `` |  | ` ` | no |

### WriteFileSerializer

| Field | Type | Pattern | Required |
| ----- | ---- | ------- | -------- |
| `description` | string | ` ` | no |
| `path` | string | ` ` | no |
| `parent` | string | ` ` | no |
| `file_type` | string | ` ` | no |
| `width` | integer | ` ` | no |
| `orientation` | string | ` ` | no |
| `src` | string | ` ` | no |
| `image_ave` | string | ` ` | no |
| `file_size` | integer | ` ` | no |
| `metafield` | string | ` ` | no |
| `title` | string | ` ` | yes |
| `title_pinyin` | string | ` ` | no |
| `origin_file_type` | string | ` ` | no |
| `children_id` | string | ` ` | no |
| `height` | integer | ` ` | no |

### /api/medias/all_folders/

```
GET /api/medias/all_folders/
```

QueryString Parameters

| Attribute | Type | Required | Description | Example |
| --------- | ---- | -------- | ----------- | ------- |
| `id` | string | no |  | 
| `id__in` | string | no |  | 
| `parent` | string | no |  | 
| `order_by` | string | no |  | 

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/medias/all_material_folders/

```
GET /api/medias/all_material_folders/
```

QueryString Parameters

| Attribute | Type | Required | Description | Example |
| --------- | ---- | -------- | ----------- | ------- |
| `id` | string | no |  | 
| `id__in` | string | no |  | 
| `parent` | string | no |  | 
| `order_by` | string | no |  | 

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/medias/file/

```
POST /api/medias/file/
```

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/medias/file/

```
GET /api/medias/file/
```

QueryString Parameters

| Attribute | Type | Required | Description | Example |
| --------- | ---- | -------- | ----------- | ------- |
| `page` | integer | no |  | 
| `page_size` | integer | no |  | 
| `file_type` | string | no |  | 
| `file_type__in` | string | no |  | 
| `id` | string | no |  | 
| `id__in` | string | no |  | 
| `parent` | string | no |  | 
| `order_by` | string | no |  | 

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/medias/file/{pk}/

```
PUT /api/medias/file/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/medias/file/{pk}/

```
GET /api/medias/file/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/medias/file/{pk}/

```
PATCH /api/medias/file/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/medias/file/{pk}/

```
DELETE /api/medias/file/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/medias/material/

```
POST /api/medias/material/
```

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/medias/material/

```
GET /api/medias/material/
```

QueryString Parameters

| Attribute | Type | Required | Description | Example |
| --------- | ---- | -------- | ----------- | ------- |
| `page` | integer | no |  | 
| `page_size` | integer | no |  | 
| `file_type` | string | no |  | 
| `file_type__in` | string | no |  | 
| `id` | string | no |  | 
| `id__in` | string | no |  | 
| `parent` | string | no |  | 
| `order_by` | string | no |  | 

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/medias/material/{pk}/

```
PUT /api/medias/material/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/medias/material/{pk}/

```
GET /api/medias/material/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/medias/material/{pk}/

```
PATCH /api/medias/material/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/medias/material/{pk}/

```
DELETE /api/medias/material/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

