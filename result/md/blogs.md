# blogs API documentation
http://heidianapi.com

---

## Models

### WriteArticleTagSerializer

| Field | Type | Pattern | Required |
| ----- | ---- | ------- | -------- |
| `title` | string | ` ` | no |

### ArticleSerializer

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

### ArticleTagSerializer

| Field | Type | Pattern | Required |
| ----- | ---- | ------- | -------- |
| `` |  | ` ` | no |
| `` |  | ` ` | no |

### WriteArticleSerializer

| Field | Type | Pattern | Required |
| ----- | ---- | ------- | -------- |
| `description` | string | ` ` | no |
| `tags` | array | ` ` | yes |
| `name` | string | ` ` | yes |
| `metafield` | string | ` ` | no |
| `title` | string | ` ` | no |
| `published_at` | string | ` ` | no |
| `author` | string | ` ` | no |
| `body_html` | string | ` ` | no |
| `image` | string | ` ` | no |
| `published` | boolean | ` ` | no |

### /api/blogs/article/

```
POST /api/blogs/article/
```

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/blogs/article/

```
GET /api/blogs/article/
```

QueryString Parameters

| Attribute | Type | Required | Description | Example |
| --------- | ---- | -------- | ----------- | ------- |
| `page` | integer | no |  | 
| `page_size` | integer | no |  | 
| `id` | string | no |  | 
| `id__in` | string | no |  | 
| `name` | string | no |  | 
| `name__in` | string | no |  | 
| `published_at_from` | string | no |  | 
| `published_at_to` | string | no |  | 
| `published` | string | no |  | 
| `title` | string | no |  | 
| `tag` | string | no |  | 
| `order_by` | string | no |  | 

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/blogs/article/{pk}/

```
PUT /api/blogs/article/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/blogs/article/{pk}/

```
GET /api/blogs/article/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/blogs/article/{pk}/

```
PATCH /api/blogs/article/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/blogs/article/{pk}/

```
DELETE /api/blogs/article/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/blogs/tag/

```
POST /api/blogs/tag/
```

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/blogs/tag/

```
GET /api/blogs/tag/
```

QueryString Parameters

| Attribute | Type | Required | Description | Example |
| --------- | ---- | -------- | ----------- | ------- |
| `title` | string | no |  | 

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/blogs/tag/{pk}/

```
PUT /api/blogs/tag/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/blogs/tag/{pk}/

```
GET /api/blogs/tag/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/blogs/tag/{pk}/

```
PATCH /api/blogs/tag/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/blogs/tag/{pk}/

```
DELETE /api/blogs/tag/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

