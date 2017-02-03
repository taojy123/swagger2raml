# statistics API documentation
http://heidianapi.com

---

## Models

### CustomerStatisticsSerializer

| Field | Type | Pattern | Required |
| ----- | ---- | ------- | -------- |
| `` |  | ` ` | no |
| `` |  | ` ` | no |
| `` |  | ` ` | no |
| `` |  | ` ` | no |
| `` |  | ` ` | no |
| `` |  | ` ` | no |

### WriteProductVariantSerializer

| Field | Type | Pattern | Required |
| ----- | ---- | ------- | -------- |
| `sku` | string | ` ` | yes |
| `price` | string | ` ` | no |
| `grams` | string | ` ` | no |
| `options` | array | ` ` | yes |

### NewestCustomerSerializer

| Field | Type | Pattern | Required |
| ----- | ---- | ------- | -------- |
| `` |  | ` ` | no |
| `` |  | ` ` | no |
| `` |  | ` ` | no |
| `` |  | ` ` | no |
| `` |  | ` ` | no |
| `` |  | ` ` | no |

### WriteNewestCustomerSerializer

| Field | Type | Pattern | Required |
| ----- | ---- | ------- | -------- |
| `mobile` | string | ` ` | yes |
| `gender` | string | ` ` | no |
| `full_name` | string | ` ` | no |

### WritePlaceSerializer

| Field | Type | Pattern | Required |
| ----- | ---- | ------- | -------- |
| `parent` | string | ` ` | no |
| `code` | string | ` ` | yes |
| `name` | string | ` ` | yes |
| `short_name` | string | ` ` | no |
| `area` | string | ` ` | no |
| `pinyin` | string | ` ` | no |

### ArticleStatisticsSerializer

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

### WriteOrderSerializer

| Field | Type | Pattern | Required |
| ----- | ---- | ------- | -------- |
| `is_test` | boolean | ` ` | no |
| `metafield` | string | ` ` | no |
| `buyer_accepts_marketing` | boolean | ` ` | no |
| `mobile` | string | ` ` | no |
| `note` | string | ` ` | no |
| `full_name` | string | ` ` | no |
| `shipping_address` | ShippingAddressSerializer | ` ` | yes |
| `email` | string | ` ` | no |

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

### ProductOptionValueSerializer

| Field | Type | Pattern | Required |
| ----- | ---- | ------- | -------- |
| `` |  | ` ` | no |
| `` |  | ` ` | no |

### WriteOrderLineSerializer

| Field | Type | Pattern | Required |
| ----- | ---- | ------- | -------- |
| `variant_title` | string | ` ` | no |
| `image` | string | ` ` | no |
| `product_title` | string | ` ` | no |
| `requires_shipping` | boolean | ` ` | no |
| `title` | string | ` ` | no |

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

### WriteArticleStatisticsSerializer

| Field | Type | Pattern | Required |
| ----- | ---- | ------- | -------- |
| `metafield` | string | ` ` | no |
| `views` | integer | ` ` | no |
| `shares` | integer | ` ` | no |
| `likes` | integer | ` ` | no |
| `date` | string | ` ` | yes |
| `article` | string | ` ` | yes |

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

### WriteProductSerializer

| Field | Type | Pattern | Required |
| ----- | ---- | ------- | -------- |
| `name` | string | ` ` | yes |
| `title` | string | ` ` | no |

### ProductStatisticsSerializer

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

### WriteOrderStatisticsSerializer

| Field | Type | Pattern | Required |
| ----- | ---- | ------- | -------- |
| `date` | string | ` ` | yes |
| `sum_price` | string | ` ` | no |
| `metafield` | string | ` ` | no |
| `successful_quantity` | integer | ` ` | no |
| `quantity` | integer | ` ` | no |

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

### WriteProductStatisticsSerializer

| Field | Type | Pattern | Required |
| ----- | ---- | ------- | -------- |
| `product` | string | ` ` | yes |
| `metafield` | string | ` ` | no |
| `views` | integer | ` ` | no |
| `sold_quantity` | integer | ` ` | no |
| `date` | string | ` ` | yes |
| `sum_price` | string | ` ` | no |

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

### OrderStatisticsSerializer

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

### WriteCustomerStatisticsSerializer

| Field | Type | Pattern | Required |
| ----- | ---- | ------- | -------- |
| `date` | string | ` ` | yes |
| `metafield` | string | ` ` | no |
| `quantity` | integer | ` ` | no |

### WriteFulfillmentSerializer

| Field | Type | Pattern | Required |
| ----- | ---- | ------- | -------- |
| `status` | string | ` ` | no |
| `tracking_number` | string | ` ` | no |
| `tracking_info` | string | ` ` | no |
| `tracking_url` | string | ` ` | no |
| `tracking_company` | string | ` ` | no |

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

### WriteOrderDiscountSerializer

| Field | Type | Pattern | Required |
| ----- | ---- | ------- | -------- |

### /api/statistics/order/

```
GET /api/statistics/order/
```

QueryString Parameters

| Attribute | Type | Required | Description | Example |
| --------- | ---- | -------- | ----------- | ------- |
| `page` | integer | no |  | 
| `page_size` | integer | no |  | 
| `date` | string | no |  | 
| `date__gte` | string | no |  | 
| `date__lte` | string | no |  | 

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/statistics/order/aggregate/

```
GET /api/statistics/order/aggregate/
```

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/statistics/order/manual_statistics/

```
GET /api/statistics/order/manual_statistics/
```

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/statistics/order/{pk}/

```
GET /api/statistics/order/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/statistics/customer/

```
GET /api/statistics/customer/
```

QueryString Parameters

| Attribute | Type | Required | Description | Example |
| --------- | ---- | -------- | ----------- | ------- |
| `page` | integer | no |  | 
| `page_size` | integer | no |  | 
| `date` | string | no |  | 
| `date__gte` | string | no |  | 
| `date__lte` | string | no |  | 

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/statistics/customer/{pk}/

```
GET /api/statistics/customer/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/statistics/product/

```
GET /api/statistics/product/
```

QueryString Parameters

| Attribute | Type | Required | Description | Example |
| --------- | ---- | -------- | ----------- | ------- |
| `page` | integer | no |  | 
| `page_size` | integer | no |  | 
| `product` | string | no |  | 
| `product__in` | string | no |  | 
| `date` | string | no |  | 
| `date__gte` | string | no |  | 
| `date__lte` | string | no |  | 

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/statistics/product/{pk}/

```
GET /api/statistics/product/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/statistics/article/

```
GET /api/statistics/article/
```

QueryString Parameters

| Attribute | Type | Required | Description | Example |
| --------- | ---- | -------- | ----------- | ------- |
| `page` | integer | no |  | 
| `page_size` | integer | no |  | 
| `article` | string | no |  | 
| `article__in` | string | no |  | 
| `date` | string | no |  | 
| `date__gte` | string | no |  | 
| `date__lte` | string | no |  | 

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/statistics/article/{pk}/

```
GET /api/statistics/article/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/statistics/newest_order/

```
GET /api/statistics/newest_order/
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

### /api/statistics/newest_order/{pk}/

```
GET /api/statistics/newest_order/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/statistics/newest_customer/

```
GET /api/statistics/newest_customer/
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

### /api/statistics/newest_customer/{pk}/

```
GET /api/statistics/newest_customer/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

