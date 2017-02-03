# payments API documentation
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

### TransactionSerializer

| Field | Type | Pattern | Required |
| ----- | ---- | ------- | -------- |
| `` |  | ` ` | no |
| `` |  | ` ` | no |
| `` |  | ` ` | no |
| `` |  | ` ` | no |
| `` |  | ` ` | no |
| `` |  | ` ` | no |

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
| `subtotal_price` | string | ` ` | no |
| `buyer_accepts_marketing` | boolean | ` ` | no |
| `cart_token` | string | ` ` | no |
| `requires_shipping` | string | ` ` | no |
| `updated_at` | string | ` ` | no |
| `is_test` | boolean | ` ` | no |
| `total_weight` | string | ` ` | no |
| `full_name` | string | ` ` | no |
| `shipping_cost` | string | ` ` | no |
| `closed_at` | string | ` ` | no |
| `id` | integer | ` ` | no |
| `metafield` | string | ` ` | no |
| `fulfillments` | array | ` ` | no |
| `transaction_number` | string | ` ` | no |
| `financial_status` | string | ` ` | no |
| `note` | string | ` ` | no |
| `discounts` | array | ` ` | no |
| `total_line_items_price` | string | ` ` | no |
| `cancelled_at` | string | ` ` | no |
| `order_status` | string | ` ` | no |
| `email` | string | ` ` | no |
| `cancel_reason` | string | ` ` | no |
| `total_discounts` | string | ` ` | no |
| `referring_platform` | string | ` ` | no |
| `total_price` | string | ` ` | no |
| `mobile` | string | ` ` | no |
| `created_at` | string | ` ` | no |
| `lines` | array | ` ` | no |
| `fulfillment_status` | string | ` ` | no |
| `token` | string | ` ` | no |
| `shipping_address` | object | ` ` | yes |
| `order_number` | string | ` ` | no |
| `paid_at` | string | ` ` | no |

### WriteTransactionSerializer

| Field | Type | Pattern | Required |
| ----- | ---- | ------- | -------- |
| `status` | string | ` ` | no |
| `transaction_number` | string | ` ` | yes |
| `transaction_type` | string | ` ` | no |

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
| `shipping_address` | ShippingAddressSerializer | ` ` | yes |
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

### /api/payments/transaction/

```
GET /api/payments/transaction/
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

### /api/payments/transaction/{pk}/

```
GET /api/payments/transaction/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

