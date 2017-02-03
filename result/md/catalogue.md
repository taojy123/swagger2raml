# catalogue API documentation
http://heidianapi.com

---

## Models

### WriteCollectionSerializer

| Field | Type | Pattern | Required |
| ----- | ---- | ------- | -------- |
| `description` | string | ` ` | no |
| `title` | string | ` ` | no |
| `image` | string | ` ` | no |
| `body_html` | string | ` ` | no |
| `published_at` | string | ` ` | no |
| `published` | boolean | ` ` | no |
| `name` | string | ` ` | yes |

### WriteCollectSerializer

| Field | Type | Pattern | Required |
| ----- | ---- | ------- | -------- |
| `collection_id` | integer | ` ` | yes |
| `featured` | boolean | ` ` | no |
| `product_id` | integer | ` ` | yes |
| `position` | integer | ` ` | no |

### WriteProductVariantSerializer

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

### WriteProductTagSerializer

| Field | Type | Pattern | Required |
| ----- | ---- | ------- | -------- |
| `title` | string | ` ` | no |

### WriteProductCategorySerializer

| Field | Type | Pattern | Required |
| ----- | ---- | ------- | -------- |
| `position` | integer | ` ` | no |
| `title` | string | ` ` | no |

### ProductOptionSerializer

| Field | Type | Pattern | Required |
| ----- | ---- | ------- | -------- |
| `` |  | ` ` | no |
| `` |  | ` ` | no |
| `` |  | ` ` | no |

### WriteProductCategoryNodeSerializer

| Field | Type | Pattern | Required |
| ----- | ---- | ------- | -------- |
| `position` | integer | ` ` | no |
| `title` | string | ` ` | no |

### WriteProductOptionSerializer

| Field | Type | Pattern | Required |
| ----- | ---- | ------- | -------- |
| `` |  | ` ` | no |
| `` |  | ` ` | no |

### WriteProductOptionValueSerializer

| Field | Type | Pattern | Required |
| ----- | ---- | ------- | -------- |
| `` |  | ` ` | no |
| `` |  | ` ` | no |

### ProductSerializer

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
| `` |  | ` ` | no |
| `` |  | ` ` | no |
| `` |  | ` ` | no |
| `` |  | ` ` | no |
| `` |  | ` ` | no |
| `` |  | ` ` | no |
| `` |  | ` ` | no |
| `` |  | ` ` | no |
| `` |  | ` ` | no |

### ProductOptionValueSerializer

| Field | Type | Pattern | Required |
| ----- | ---- | ------- | -------- |
| `` |  | ` ` | no |
| `` |  | ` ` | no |

### ProductCategoryNodeSerializer

| Field | Type | Pattern | Required |
| ----- | ---- | ------- | -------- |
| `` |  | ` ` | no |
| `` |  | ` ` | no |
| `` |  | ` ` | no |

### ProductTypeSerializer

| Field | Type | Pattern | Required |
| ----- | ---- | ------- | -------- |
| `` |  | ` ` | no |
| `` |  | ` ` | no |
| `` |  | ` ` | no |

### ProductCategorySerializer

| Field | Type | Pattern | Required |
| ----- | ---- | ------- | -------- |
| `position` | integer | ` ` | no |
| `children` | array | ` ` | no |
| `id` | integer | ` ` | no |
| `title` | string | ` ` | no |

### ProductTagSerializer

| Field | Type | Pattern | Required |
| ----- | ---- | ------- | -------- |
| `` |  | ` ` | no |
| `` |  | ` ` | no |

### WriteProductSerializer

| Field | Type | Pattern | Required |
| ----- | ---- | ------- | -------- |
| `vendor` | string | ` ` | no |
| `description` | string | ` ` | no |
| `title` | string | ` ` | no |
| `inventory_policy` | string | ` ` | no |
| `tags` | array | ` ` | yes |
| `requires_shipping` | boolean | ` ` | no |
| `body_html` | string | ` ` | no |
| `category_ids` | array | ` ` | no |
| `published_at` | string | ` ` | no |
| `published` | boolean | ` ` | no |
| `images` | array | ` ` | no |
| `metafield` | string | ` ` | no |
| `variants` | array | ` ` | yes |
| `product_type_id` | string | ` ` | yes |
| `options` | array | ` ` | no |
| `name` | string | ` ` | yes |

### CollectionSerializer

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

### ProductVariantSerializer

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

### CollectSerializer

| Field | Type | Pattern | Required |
| ----- | ---- | ------- | -------- |
| `` |  | ` ` | no |
| `` |  | ` ` | no |
| `` |  | ` ` | no |
| `` |  | ` ` | no |
| `` |  | ` ` | no |
| `` |  | ` ` | no |

### WriteProductTypeSerializer

| Field | Type | Pattern | Required |
| ----- | ---- | ------- | -------- |
| `name` | string | ` ` | yes |
| `title` | string | ` ` | yes |

### WriteProductImageSerializer

| Field | Type | Pattern | Required |
| ----- | ---- | ------- | -------- |
| `` |  | ` ` | no |
| `` |  | ` ` | no |
| `` |  | ` ` | no |
| `` |  | ` ` | no |

### ProductImageSerializer

| Field | Type | Pattern | Required |
| ----- | ---- | ------- | -------- |
| `` |  | ` ` | no |
| `` |  | ` ` | no |
| `` |  | ` ` | no |
| `` |  | ` ` | no |

### /api/catalogue/productoption/

```
POST /api/catalogue/productoption/
```

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/catalogue/productoption/

```
GET /api/catalogue/productoption/
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

### /api/catalogue/productoption/{pk}/

```
PUT /api/catalogue/productoption/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/catalogue/productoption/{pk}/

```
GET /api/catalogue/productoption/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/catalogue/productoption/{pk}/

```
PATCH /api/catalogue/productoption/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/catalogue/productoption/{pk}/

```
DELETE /api/catalogue/productoption/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/catalogue/product/count/

```
GET /api/catalogue/product/count/
```

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/catalogue/product/{pk}/copy_product/

```
POST /api/catalogue/product/{pk}/copy_product/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/catalogue/product/

```
POST /api/catalogue/product/
```

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/catalogue/product/

```
GET /api/catalogue/product/
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
| `price_from` | string | no |  | 
| `price_to` | string | no |  | 
| `collection` | string | no |  | 
| `collection__exclude` | string | no |  | 
| `category` | string | no |  | 
| `category__in` | string | no |  | 
| `q` | string | no |  | 
| `order_by` | string | no |  | 

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/catalogue/product/{pk}/

```
PUT /api/catalogue/product/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/catalogue/product/{pk}/

```
GET /api/catalogue/product/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/catalogue/product/{pk}/

```
PATCH /api/catalogue/product/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/catalogue/product/{pk}/

```
DELETE /api/catalogue/product/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/catalogue/variant/

```
POST /api/catalogue/variant/
```

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/catalogue/variant/

```
GET /api/catalogue/variant/
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

### /api/catalogue/variant/{pk}/

```
PUT /api/catalogue/variant/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/catalogue/variant/{pk}/

```
GET /api/catalogue/variant/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/catalogue/variant/{pk}/

```
PATCH /api/catalogue/variant/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/catalogue/variant/{pk}/

```
DELETE /api/catalogue/variant/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/catalogue/producttype/

```
GET /api/catalogue/producttype/
```

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/catalogue/producttype/{pk}/

```
GET /api/catalogue/producttype/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/catalogue/tag/

```
POST /api/catalogue/tag/
```

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/catalogue/tag/

```
GET /api/catalogue/tag/
```

QueryString Parameters

| Attribute | Type | Required | Description | Example |
| --------- | ---- | -------- | ----------- | ------- |
| `title` | string | no |  | 

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/catalogue/tag/{pk}/

```
PUT /api/catalogue/tag/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/catalogue/tag/{pk}/

```
GET /api/catalogue/tag/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/catalogue/tag/{pk}/

```
PATCH /api/catalogue/tag/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/catalogue/tag/{pk}/

```
DELETE /api/catalogue/tag/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/catalogue/collection/

```
POST /api/catalogue/collection/
```

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/catalogue/collection/

```
GET /api/catalogue/collection/
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
| `published` | string | no |  | 
| `title` | string | no |  | 
| `published_at_from` | string | no |  | 
| `published_at_to` | string | no |  | 
| `order_by` | string | no |  | 

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/catalogue/collection/{pk}/

```
PUT /api/catalogue/collection/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/catalogue/collection/{pk}/

```
GET /api/catalogue/collection/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/catalogue/collection/{pk}/

```
PATCH /api/catalogue/collection/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/catalogue/collection/{pk}/

```
DELETE /api/catalogue/collection/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/catalogue/collection/{parent_lookup_collection}/collect/

```
POST /api/catalogue/collection/{parent_lookup_collection}/collect/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `parent_lookup_collection` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/catalogue/collection/{parent_lookup_collection}/collect/

```
GET /api/catalogue/collection/{parent_lookup_collection}/collect/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `parent_lookup_collection` | string | yes |  |

QueryString Parameters

| Attribute | Type | Required | Description | Example |
| --------- | ---- | -------- | ----------- | ------- |
| `page` | integer | no |  | 
| `page_size` | integer | no |  | 
| `product` | string | no |  | 
| `product__in` | string | no |  | 

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/catalogue/collection/{parent_lookup_collection}/collect/{pk}/

```
PUT /api/catalogue/collection/{parent_lookup_collection}/collect/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `parent_lookup_collection` | string | yes |  |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/catalogue/collection/{parent_lookup_collection}/collect/{pk}/

```
GET /api/catalogue/collection/{parent_lookup_collection}/collect/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `parent_lookup_collection` | string | yes |  |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/catalogue/collection/{parent_lookup_collection}/collect/{pk}/

```
PATCH /api/catalogue/collection/{parent_lookup_collection}/collect/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `parent_lookup_collection` | string | yes |  |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/catalogue/collection/{parent_lookup_collection}/collect/{pk}/

```
DELETE /api/catalogue/collection/{parent_lookup_collection}/collect/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `parent_lookup_collection` | string | yes |  |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/catalogue/category/

```
GET /api/catalogue/category/
```

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/catalogue/category/

```
PUT /api/catalogue/category/
```

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

