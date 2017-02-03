# orders API documentation
http://heidianapi.com

---

## Models

### OrderLineSerializer

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

### ShippingAddressSerializer

| Field | Type | Pattern | Required |
| ----- | ---- | ------- | -------- |
| `province` | string | ` ` | no |
| `city` | string | ` ` | no |
| `metafield` | string | ` ` | no |
| `district` | string | ` ` | no |
| `mobile` | string | ` ` | no |
| `address1` | string | ` ` | no |
| `address2` | string | ` ` | no |
| `updated_at` | string | ` ` | no |
| `id` | integer | ` ` | no |
| `customer_address_id` | integer | ` ` | no |
| `place` | object | ` ` | yes |
| `full_name` | string | ` ` | no |
| `country` | string | ` ` | no |
| `created_at` | string | ` ` | no |

### WriteProductVariantSerializer

| Field | Type | Pattern | Required |
| ----- | ---- | ------- | -------- |
| `sku` | string | ` ` | yes |
| `price` | string | ` ` | no |
| `grams` | string | ` ` | no |
| `options` | array | ` ` | yes |

### WriteProductOptionValueSerializer

| Field | Type | Pattern | Required |
| ----- | ---- | ------- | -------- |
| `value` | string | ` ` | no |
| `title` | string | ` ` | yes |

### ProductSerializer

| Field | Type | Pattern | Required |
| ----- | ---- | ------- | -------- |
| `title` | string | ` ` | no |
| `id` | integer | ` ` | no |
| `name` | string | ` ` | yes |

### OrderDiscountSerializer

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
| `sku` | string | ` ` | yes |
| `grams` | string | ` ` | no |
| `title` | string | ` ` | no |
| `image` | string | ` ` | no |
| `id` | integer | ` ` | no |
| `options` | array | ` ` | yes |
| `price` | string | ` ` | no |

### WriteShippingAddressSerializer

| Field | Type | Pattern | Required |
| ----- | ---- | ------- | -------- |
| `city` | string | ` ` | no |
| `place_code` | string | ` ` | no |
| `metafield` | string | ` ` | no |
| `address1` | string | ` ` | no |
| `address2` | string | ` ` | no |
| `customer_address_id` | integer | ` ` | no |
| `full_name` | string | ` ` | no |
| `mobile` | string | ` ` | no |
| `province` | string | ` ` | no |
| `country` | string | ` ` | no |
| `district` | string | ` ` | no |

### ProductOptionValueSerializer

| Field | Type | Pattern | Required |
| ----- | ---- | ------- | -------- |
| `` |  | ` ` | no |
| `` |  | ` ` | no |

### PlaceSerializer

| Field | Type | Pattern | Required |
| ----- | ---- | ------- | -------- |
| `code` | string | ` ` | yes |
| `parent` | string | ` ` | no |
| `short_name` | string | ` ` | no |
| `area` | string | ` ` | no |
| `pinyin` | string | ` ` | no |
| `id` | integer | ` ` | no |
| `name` | string | ` ` | yes |

### OrderSerializer

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
| `` |  | ` ` | no |
| `` |  | ` ` | no |
| `` |  | ` ` | no |
| `` |  | ` ` | no |
| `` |  | ` ` | no |
| `` |  | ` ` | no |

### WriteFulfillmentSerializer

| Field | Type | Pattern | Required |
| ----- | ---- | ------- | -------- |
| `status` | string | ` ` | no |
| `tracking_number` | string | ` ` | no |
| `tracking_info` | string | ` ` | no |
| `tracking_url` | string | ` ` | no |
| `tracking_company` | string | ` ` | no |

### WriteProductSerializer

| Field | Type | Pattern | Required |
| ----- | ---- | ------- | -------- |
| `name` | string | ` ` | yes |
| `title` | string | ` ` | no |

### WritePlaceSerializer

| Field | Type | Pattern | Required |
| ----- | ---- | ------- | -------- |
| `parent` | string | ` ` | no |
| `code` | string | ` ` | yes |
| `name` | string | ` ` | yes |
| `short_name` | string | ` ` | no |
| `area` | string | ` ` | no |
| `pinyin` | string | ` ` | no |

### WriteOrderSerializer

| Field | Type | Pattern | Required |
| ----- | ---- | ------- | -------- |
| `is_test` | boolean | ` ` | no |
| `metafield` | string | ` ` | no |
| `buyer_accepts_marketing` | boolean | ` ` | no |
| `mobile` | string | ` ` | no |
| `note` | string | ` ` | no |
| `full_name` | string | ` ` | no |
| `shipping_address` | object | ` ` | yes |
| `email` | string | ` ` | no |

### WriteOrderLineSerializer

| Field | Type | Pattern | Required |
| ----- | ---- | ------- | -------- |
| `variant_title` | string | ` ` | no |
| `image` | string | ` ` | no |
| `product_title` | string | ` ` | no |
| `requires_shipping` | boolean | ` ` | no |
| `title` | string | ` ` | no |

### WriteOrderDiscountSerializer

| Field | Type | Pattern | Required |
| ----- | ---- | ------- | -------- |

### FulfillmentSerializer

| Field | Type | Pattern | Required |
| ----- | ---- | ------- | -------- |
| `` |  | ` ` | no |
| `` |  | ` ` | no |
| `` |  | ` ` | no |
| `` |  | ` ` | no |
| `` |  | ` ` | no |
| `` |  | ` ` | no |
| `` |  | ` ` | no |

### /api/orders/order/output/

```
GET /api/orders/order/output/
```

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/orders/order/{pk}/check_paid/

```
GET /api/orders/order/{pk}/check_paid/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/orders/order/

```
POST /api/orders/order/
```

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/orders/order/

```
GET /api/orders/order/
```

QueryString Parameters

| Attribute | Type | Required | Description | Example |
| --------- | ---- | -------- | ----------- | ------- |
| `page` | integer | no |  | 
| `page_size` | integer | no |  | 
| `fulfillment_status` | string | no |  | 
| `fulfillment_status__in` | string | no |  | 
| `order_status` | string | no |  | 
| `order_status__in` | string | no |  | 
| `order_number` | string | no |  | 
| `order_number__in` | string | no |  | 
| `id` | string | no |  | 
| `id__in` | string | no |  | 
| `financial_status` | string | no |  | 
| `financial_status__in` | string | no |  | 
| `created_at_from` | string | no |  | 
| `created_at_to` | string | no |  | 
| `referring_platform` | string | no |  | 
| `order_by` | string | no |  | 

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/orders/order/{pk}/

```
PUT /api/orders/order/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/orders/order/{pk}/

```
GET /api/orders/order/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/orders/order/{pk}/

```
PATCH /api/orders/order/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/orders/order/{pk}/

```
DELETE /api/orders/order/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/orders/order/{parent_lookup_order}/fulfillment/

```
POST /api/orders/order/{parent_lookup_order}/fulfillment/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `parent_lookup_order` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/orders/order/{parent_lookup_order}/fulfillment/

```
GET /api/orders/order/{parent_lookup_order}/fulfillment/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `parent_lookup_order` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/orders/order/{parent_lookup_order}/fulfillment/{pk}/

```
PUT /api/orders/order/{parent_lookup_order}/fulfillment/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `parent_lookup_order` | string | yes |  |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/orders/order/{parent_lookup_order}/fulfillment/{pk}/

```
GET /api/orders/order/{parent_lookup_order}/fulfillment/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `parent_lookup_order` | string | yes |  |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/orders/order/{parent_lookup_order}/fulfillment/{pk}/

```
PATCH /api/orders/order/{parent_lookup_order}/fulfillment/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `parent_lookup_order` | string | yes |  |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/orders/order/{parent_lookup_order}/fulfillment/{pk}/

```
DELETE /api/orders/order/{parent_lookup_order}/fulfillment/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `parent_lookup_order` | string | yes |  |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/orders/kd100webhooks/

```
POST /api/orders/kd100webhooks/
```

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

