# shippings API documentation
http://heidianapi.com

---

## Models

### ShippingZoneSerializer

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

### WriteShippingMethodSerializer

| Field | Type | Pattern | Required |
| ----- | ---- | ------- | -------- |
| `metafield` | string | ` ` | no |
| `title` | string | ` ` | no |
| `normal_price` | string | ` ` | no |
| `rate_type` | string | ` ` | no |
| `over_price` | string | ` ` | no |
| `normal_unit` | string | ` ` | no |
| `over_unit` | string | ` ` | no |
| `is_used` | boolean | ` ` | no |
| `shipping_zones` | array | ` ` | no |
| `free_shipping_price` | string | ` ` | no |

### ShippingMethodSerializer

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

### PlaceSerializer

| Field | Type | Pattern | Required |
| ----- | ---- | ------- | -------- |
| `` |  | ` ` | no |
| `` |  | ` ` | no |
| `` |  | ` ` | no |
| `` |  | ` ` | no |
| `` |  | ` ` | no |
| `` |  | ` ` | no |
| `` |  | ` ` | no |

### WriteShippingZoneSerializer

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

### WritePlaceSerializer

| Field | Type | Pattern | Required |
| ----- | ---- | ------- | -------- |
| `parent` | string | ` ` | no |
| `code` | string | ` ` | yes |
| `name` | string | ` ` | yes |
| `short_name` | string | ` ` | no |
| `area` | string | ` ` | no |
| `pinyin` | string | ` ` | no |

### /api/shippings/shippingmethod/{pk}/choose/

```
PUT /api/shippings/shippingmethod/{pk}/choose/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/shippings/shippingmethod/

```
POST /api/shippings/shippingmethod/
```

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/shippings/shippingmethod/

```
GET /api/shippings/shippingmethod/
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

### /api/shippings/shippingmethod/{pk}/

```
PUT /api/shippings/shippingmethod/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/shippings/shippingmethod/{pk}/

```
GET /api/shippings/shippingmethod/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/shippings/shippingmethod/{pk}/

```
PATCH /api/shippings/shippingmethod/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/shippings/shippingmethod/{pk}/

```
DELETE /api/shippings/shippingmethod/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/shippings/shippingmethod/{parent_lookup_shipping_method}/shippingzone/

```
POST /api/shippings/shippingmethod/{parent_lookup_shipping_method}/shippingzone/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `parent_lookup_shipping_method` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/shippings/shippingmethod/{parent_lookup_shipping_method}/shippingzone/

```
GET /api/shippings/shippingmethod/{parent_lookup_shipping_method}/shippingzone/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `parent_lookup_shipping_method` | string | yes |  |

QueryString Parameters

| Attribute | Type | Required | Description | Example |
| --------- | ---- | -------- | ----------- | ------- |
| `page` | integer | no |  | 
| `page_size` | integer | no |  | 

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/shippings/shippingmethod/{parent_lookup_shipping_method}/shippingzone/{pk}/

```
PUT /api/shippings/shippingmethod/{parent_lookup_shipping_method}/shippingzone/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `parent_lookup_shipping_method` | string | yes |  |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/shippings/shippingmethod/{parent_lookup_shipping_method}/shippingzone/{pk}/

```
GET /api/shippings/shippingmethod/{parent_lookup_shipping_method}/shippingzone/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `parent_lookup_shipping_method` | string | yes |  |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/shippings/shippingmethod/{parent_lookup_shipping_method}/shippingzone/{pk}/

```
PATCH /api/shippings/shippingmethod/{parent_lookup_shipping_method}/shippingzone/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `parent_lookup_shipping_method` | string | yes |  |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/shippings/shippingmethod/{parent_lookup_shipping_method}/shippingzone/{pk}/

```
DELETE /api/shippings/shippingmethod/{parent_lookup_shipping_method}/shippingzone/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `parent_lookup_shipping_method` | string | yes |  |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/shippings/place/for_area/

```
GET /api/shippings/place/for_area/
```

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/shippings/place/

```
GET /api/shippings/place/
```

QueryString Parameters

| Attribute | Type | Required | Description | Example |
| --------- | ---- | -------- | ----------- | ------- |
| `parent_code` | string | no |  | 

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/shippings/place/{pk}/

```
GET /api/shippings/place/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

