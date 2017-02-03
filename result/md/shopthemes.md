# shopthemes API documentation
http://heidianapi.com

---

## Models

### WriteThemeSerializer

| Field | Type | Pattern | Required |
| ----- | ---- | ------- | -------- |
| `current_preset` | string | ` ` | no |
| `private_settings_data` | string | ` ` | no |
| `metafield` | string | ` ` | no |
| `assets` | string | ` ` | no |
| `settings_data` | string | ` ` | no |

### WritePageConfigPresetSerializer

| Field | Type | Pattern | Required |
| ----- | ---- | ------- | -------- |

### WriteActivateThemeSerializer

| Field | Type | Pattern | Required |
| ----- | ---- | ------- | -------- |
| `name` | string | ` ` | yes |

### ActivateThemeSerializer

| Field | Type | Pattern | Required |
| ----- | ---- | ------- | -------- |

### ContainerSerializer

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

### TemplateSerializer

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

### PageConfigPresetSerializer

| Field | Type | Pattern | Required |
| ----- | ---- | ------- | -------- |
| `` |  | ` ` | no |
| `` |  | ` ` | no |
| `` |  | ` ` | no |
| `` |  | ` ` | no |

### PageSerializer

| Field | Type | Pattern | Required |
| ----- | ---- | ------- | -------- |
| `permanent` | boolean | ` ` | no |
| `id` | integer | ` ` | no |
| `name` | string | ` ` | no |
| `page_type` | string | ` ` | no |

### WriteInstallThemeSerializer

| Field | Type | Pattern | Required |
| ----- | ---- | ------- | -------- |
| `preset` | string | ` ` | yes |
| `name` | string | ` ` | yes |

### PageConfigSerializer

| Field | Type | Pattern | Required |
| ----- | ---- | ------- | -------- |
| `` |  | ` ` | no |
| `` |  | ` ` | no |
| `` |  | ` ` | no |
| `` |  | ` ` | no |
| `` |  | ` ` | no |
| `` |  | ` ` | no |
| `` |  | ` ` | no |

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

### WritePageSerializer

| Field | Type | Pattern | Required |
| ----- | ---- | ------- | -------- |
| `permanent` | boolean | ` ` | no |
| `page_type` | string | ` ` | no |
| `name` | string | ` ` | no |

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
| `` |  | ` ` | no |
| `` |  | ` ` | no |
| `` |  | ` ` | no |
| `` |  | ` ` | no |
| `` |  | ` ` | no |
| `` |  | ` ` | no |
| `` |  | ` ` | no |

### WriteSnippetSerializer

| Field | Type | Pattern | Required |
| ----- | ---- | ------- | -------- |
| `settings_schema` | string | ` ` | no |
| `description` | string | ` ` | no |
| `title` | string | ` ` | no |
| `content` | string | ` ` | no |
| `metafield` | string | ` ` | no |
| `icon` | string | ` ` | no |
| `settings_data` | string | ` ` | no |
| `name` | string | ` ` | yes |

### SnippetSerializer

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

### WriteThemePresetSerializer

| Field | Type | Pattern | Required |
| ----- | ---- | ------- | -------- |
| `metafield` | string | ` ` | no |
| `description` | string | ` ` | no |
| `title` | string | ` ` | no |

### WriteFileSerializer

| Field | Type | Pattern | Required |
| ----- | ---- | ------- | -------- |
| `description` | string | ` ` | no |
| `settings_data` | string | ` ` | no |
| `content` | string | ` ` | no |
| `src` | string | ` ` | no |
| `icon` | string | ` ` | no |
| `metafield` | string | ` ` | no |
| `title` | string | ` ` | no |
| `permanent` | boolean | ` ` | no |
| `settings_schema` | string | ` ` | no |

### WriteContainerSerializer

| Field | Type | Pattern | Required |
| ----- | ---- | ------- | -------- |
| `settings_schema` | string | ` ` | no |
| `description` | string | ` ` | no |
| `title` | string | ` ` | no |
| `content` | string | ` ` | no |
| `metafield` | string | ` ` | no |
| `icon` | string | ` ` | no |
| `settings_data` | string | ` ` | no |
| `name` | string | ` ` | yes |

### WriteTemplateSerializer

| Field | Type | Pattern | Required |
| ----- | ---- | ------- | -------- |
| `description` | string | ` ` | no |
| `settings_data` | string | ` ` | no |
| `file_type` | string | ` ` | yes |
| `content` | string | ` ` | no |
| `name` | string | ` ` | yes |
| `icon` | string | ` ` | no |
| `metafield` | string | ` ` | no |
| `title` | string | ` ` | no |
| `settings_schema` | string | ` ` | no |

### InstallThemeSerializer

| Field | Type | Pattern | Required |
| ----- | ---- | ------- | -------- |

### WritePageConfigSerializer

| Field | Type | Pattern | Required |
| ----- | ---- | ------- | -------- |
| `metafield` | string | ` ` | no |
| `settings_data` | string | ` ` | no |

### /api/shopthemes/file/

```
POST /api/shopthemes/file/
```

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/shopthemes/file/

```
GET /api/shopthemes/file/
```

QueryString Parameters

| Attribute | Type | Required | Description | Example |
| --------- | ---- | -------- | ----------- | ------- |
| `file_type` | string | no |  | 
| `file_type__in` | string | no |  | 
| `id` | string | no |  | 
| `id__in` | string | no |  | 
| `name` | string | no |  | 
| `name__in` | string | no |  | 
| `permanent` | string | no |  | 
| `order_by` | string | no |  | 

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/shopthemes/file/{pk}/

```
PUT /api/shopthemes/file/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/shopthemes/file/{pk}/

```
GET /api/shopthemes/file/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/shopthemes/file/{pk}/

```
PATCH /api/shopthemes/file/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/shopthemes/file/{pk}/

```
DELETE /api/shopthemes/file/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/shopthemes/template/

```
GET /api/shopthemes/template/
```

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/shopthemes/template/{pk}/

```
GET /api/shopthemes/template/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/shopthemes/block/

```
GET /api/shopthemes/block/
```

QueryString Parameters

| Attribute | Type | Required | Description | Example |
| --------- | ---- | -------- | ----------- | ------- |
| `file_type` | string | no |  | 
| `file_type__in` | string | no |  | 
| `id` | string | no |  | 
| `id__in` | string | no |  | 
| `name` | string | no |  | 
| `name__in` | string | no |  | 
| `permanent` | string | no |  | 
| `order_by` | string | no |  | 

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/shopthemes/block/{pk}/

```
GET /api/shopthemes/block/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/shopthemes/pageconfig/

```
GET /api/shopthemes/pageconfig/
```

QueryString Parameters

| Attribute | Type | Required | Description | Example |
| --------- | ---- | -------- | ----------- | ------- |
| `page_type` | string | no |  | 
| `name` | string | no |  | 

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/shopthemes/pageconfig/{pk}/

```
PUT /api/shopthemes/pageconfig/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/shopthemes/pageconfig/{pk}/

```
PATCH /api/shopthemes/pageconfig/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/shopthemes/pageconfig/{pk}/

```
GET /api/shopthemes/pageconfig/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/shopthemes/snippet/

```
GET /api/shopthemes/snippet/
```

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/shopthemes/snippet/{pk}/

```
GET /api/shopthemes/snippet/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/shopthemes/container/

```
GET /api/shopthemes/container/
```

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/shopthemes/container/{pk}/

```
GET /api/shopthemes/container/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/shopthemes/theme/apply_preset/

```
POST /api/shopthemes/theme/apply_preset/
```

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/shopthemes/theme/save_as_preset/

```
POST /api/shopthemes/theme/save_as_preset/
```

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/shopthemes/theme/

```
POST /api/shopthemes/theme/
```

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/shopthemes/theme/

```
GET /api/shopthemes/theme/
```

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/shopthemes/theme/{pk}/

```
PUT /api/shopthemes/theme/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/shopthemes/theme/{pk}/

```
GET /api/shopthemes/theme/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/shopthemes/theme/{pk}/

```
PATCH /api/shopthemes/theme/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/shopthemes/theme/{pk}/

```
DELETE /api/shopthemes/theme/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/shopthemes/theme/{parent_lookup_theme}/file/

```
POST /api/shopthemes/theme/{parent_lookup_theme}/file/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `parent_lookup_theme` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/shopthemes/theme/{parent_lookup_theme}/file/

```
GET /api/shopthemes/theme/{parent_lookup_theme}/file/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `parent_lookup_theme` | string | yes |  |

QueryString Parameters

| Attribute | Type | Required | Description | Example |
| --------- | ---- | -------- | ----------- | ------- |
| `file_type` | string | no |  | 
| `file_type__in` | string | no |  | 

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/shopthemes/theme/{parent_lookup_theme}/file/{pk}/

```
PUT /api/shopthemes/theme/{parent_lookup_theme}/file/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `parent_lookup_theme` | string | yes |  |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/shopthemes/theme/{parent_lookup_theme}/file/{pk}/

```
GET /api/shopthemes/theme/{parent_lookup_theme}/file/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `parent_lookup_theme` | string | yes |  |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/shopthemes/theme/{parent_lookup_theme}/file/{pk}/

```
PATCH /api/shopthemes/theme/{parent_lookup_theme}/file/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `parent_lookup_theme` | string | yes |  |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/shopthemes/theme/{parent_lookup_theme}/file/{pk}/

```
DELETE /api/shopthemes/theme/{parent_lookup_theme}/file/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `parent_lookup_theme` | string | yes |  |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/shopthemes/theme/{parent_lookup_theme}/pageconfig/{pk}/lock/

```
PUT /api/shopthemes/theme/{parent_lookup_theme}/pageconfig/{pk}/lock/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `parent_lookup_theme` | string | yes |  |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/shopthemes/theme/{parent_lookup_theme}/pageconfig/{pk}/unlock/

```
PUT /api/shopthemes/theme/{parent_lookup_theme}/pageconfig/{pk}/unlock/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `parent_lookup_theme` | string | yes |  |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/shopthemes/theme/{parent_lookup_theme}/pageconfig/

```
GET /api/shopthemes/theme/{parent_lookup_theme}/pageconfig/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `parent_lookup_theme` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/shopthemes/theme/{parent_lookup_theme}/pageconfig/{pk}/

```
PUT /api/shopthemes/theme/{parent_lookup_theme}/pageconfig/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `parent_lookup_theme` | string | yes |  |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/shopthemes/theme/{parent_lookup_theme}/pageconfig/{pk}/

```
PATCH /api/shopthemes/theme/{parent_lookup_theme}/pageconfig/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `parent_lookup_theme` | string | yes |  |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/shopthemes/theme/{parent_lookup_theme}/pageconfig/{pk}/

```
GET /api/shopthemes/theme/{parent_lookup_theme}/pageconfig/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `parent_lookup_theme` | string | yes |  |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/shopthemes/activate_theme/

```
PUT /api/shopthemes/activate_theme/
```

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/shopthemes/install_theme/

```
POST /api/shopthemes/install_theme/
```

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

