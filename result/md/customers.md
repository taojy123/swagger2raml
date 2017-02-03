# customers API documentation
http://heidianapi.com

---

## Models

### WriteProductVariantSerializer

| Field | Type | Pattern | Required |
| ----- | ---- | ------- | -------- |
| `sku` | string | ` ` | yes |
| `price` | string | ` ` | no |
| `grams` | string | ` ` | no |
| `options` | array | ` ` | yes |

### CouponSerializer

| Field | Type | Pattern | Required |
| ----- | ---- | ------- | -------- |
| `description` | string | ` ` | no |
| `discount_type` | string | ` ` | no |
| `minimum_amount` | string | ` ` | no |
| `value` | string | ` ` | no |
| `verbose_title` | string | ` ` | no |
| `title` | string | ` ` | no |
| `ends_at` | string | ` ` | no |
| `is_limit_once` | boolean | ` ` | no |
| `code_prefix` | string | ` ` | yes |
| `starts_at` | string | ` ` | no |
| `id` | integer | ` ` | no |
| `quantity` | integer | ` ` | no |
| `is_forever` | boolean | ` ` | no |
| `created_at` | string | ` ` | no |

### CouponCodeSerializer

| Field | Type | Pattern | Required |
| ----- | ---- | ------- | -------- |
| `` |  | ` ` | no |
| `` |  | ` ` | no |
| `` |  | ` ` | no |
| `` |  | ` ` | no |
| `` |  | ` ` | no |

### WriteAuthTokenSerializer

| Field | Type | Pattern | Required |
| ----- | ---- | ------- | -------- |
| `mobile` | string | ` ` | yes |
| `password` | string | ` ` | no |
| `code` | string | ` ` | no |

### PasswordCustomerSerializer

| Field | Type | Pattern | Required |
| ----- | ---- | ------- | -------- |
| `mobile` | string | ` ` | no |
| `gender` | string | ` ` | no |
| `cart_token` | string | ` ` | no |
| `email` | string | ` ` | no |
| `token` | string | ` ` | no |
| `birthday` | string | ` ` | no |
| `full_name` | string | ` ` | no |
| `id` | integer | ` ` | no |

### WritePlaceSerializer

| Field | Type | Pattern | Required |
| ----- | ---- | ------- | -------- |
| `parent` | string | ` ` | no |
| `code` | string | ` ` | yes |
| `name` | string | ` ` | yes |
| `short_name` | string | ` ` | no |
| `area` | string | ` ` | no |
| `pinyin` | string | ` ` | no |

### CartSerializer

| Field | Type | Pattern | Required |
| ----- | ---- | ------- | -------- |
| `total_price` | string | ` ` | no |
| `items` | array | ` ` | no |
| `created_at` | string | ` ` | no |
| `updated_at` | string | ` ` | no |
| `note` | string | ` ` | no |
| `token` | string | ` ` | no |
| `id` | integer | ` ` | no |

### WritePasswordCustomerSerializer

| Field | Type | Pattern | Required |
| ----- | ---- | ------- | -------- |
| `mobile` | string | ` ` | no |
| `gender` | string | ` ` | no |
| `birthday` | string | ` ` | no |
| `full_name` | string | ` ` | no |
| `password` | string | ` ` | yes |
| `email` | string | ` ` | no |

### CustomerAddressSerializer

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

### WriteCustomerAddressSerializer

| Field | Type | Pattern | Required |
| ----- | ---- | ------- | -------- |
| `is_default` | boolean | ` ` | no |
| `city` | string | ` ` | no |
| `place_code` | string | ` ` | no |
| `address1` | string | ` ` | no |
| `address2` | string | ` ` | no |
| `full_name` | string | ` ` | no |
| `mobile` | string | ` ` | no |
| `province` | string | ` ` | no |
| `country` | string | ` ` | no |
| `district` | string | ` ` | no |

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

### CartItemSerializer

| Field | Type | Pattern | Required |
| ----- | ---- | ------- | -------- |
| `` |  | ` ` | no |
| `` |  | ` ` | no |
| `` |  | ` ` | no |
| `` |  | ` ` | no |
| `` |  | ` ` | no |
| `` |  | ` ` | no |

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

### WriteCouponCodeSerializer

| Field | Type | Pattern | Required |
| ----- | ---- | ------- | -------- |
| `status` | string | ` ` | no |
| `code` | string | ` ` | yes |
| `used_at` | string | ` ` | no |

### WriteProductSerializer

| Field | Type | Pattern | Required |
| ----- | ---- | ------- | -------- |
| `name` | string | ` ` | yes |
| `title` | string | ` ` | no |

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

### WriteCouponSerializer

| Field | Type | Pattern | Required |
| ----- | ---- | ------- | -------- |
| `description` | string | ` ` | no |
| `discount_type` | string | ` ` | no |
| `minimum_amount` | string | ` ` | no |
| `value` | string | ` ` | no |
| `title` | string | ` ` | no |
| `ends_at` | string | ` ` | no |
| `is_limit_once` | boolean | ` ` | no |
| `code_prefix` | string | ` ` | yes |
| `starts_at` | string | ` ` | no |
| `quantity` | integer | ` ` | no |
| `is_forever` | boolean | ` ` | no |

### WriteProductOptionValueSerializer

| Field | Type | Pattern | Required |
| ----- | ---- | ------- | -------- |
| `value` | string | ` ` | no |
| `title` | string | ` ` | yes |

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

### AuthTokenSerializer

| Field | Type | Pattern | Required |
| ----- | ---- | ------- | -------- |
| `mobile` | string | ` ` | yes |
| `password` | string | ` ` | no |
| `code` | string | ` ` | no |

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

### WriteCartSerializer

| Field | Type | Pattern | Required |
| ----- | ---- | ------- | -------- |
| `note` | string | ` ` | no |

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

### WriteCartItemSerializer

| Field | Type | Pattern | Required |
| ----- | ---- | ------- | -------- |
| `quantity` | integer | ` ` | no |
| `checked` | boolean | ` ` | no |
| `variant_id` | string | ` ` | yes |

### /api/customers/order/

```
POST /api/customers/order/
```

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/customers/order/

```
GET /api/customers/order/
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
| `order_by` | string | no |  | 

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/customers/order/{pk}/

```
PUT /api/customers/order/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/customers/order/{pk}/

```
GET /api/customers/order/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/customers/order/{pk}/

```
PATCH /api/customers/order/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/customers/order/{pk}/

```
DELETE /api/customers/order/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/customers/order/{pk}/buy_again/

```
POST /api/customers/order/{pk}/buy_again/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/customers/coupon_code/

```
GET /api/customers/coupon_code/
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

### /api/customers/coupon_code/{pk}/

```
GET /api/customers/coupon_code/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/customers/address/

```
POST /api/customers/address/
```

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/customers/address/

```
GET /api/customers/address/
```

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/customers/address/{pk}/

```
PUT /api/customers/address/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/customers/address/{pk}/

```
GET /api/customers/address/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/customers/address/{pk}/

```
PATCH /api/customers/address/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/customers/address/{pk}/

```
DELETE /api/customers/address/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/customers/ordertoken/{token}/

```
PUT /api/customers/ordertoken/{token}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `token` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/customers/ordertoken/{token}/

```
GET /api/customers/ordertoken/{token}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `token` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/customers/ordertoken/{token}/

```
PATCH /api/customers/ordertoken/{token}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `token` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/customers/ordertoken/{token}/

```
DELETE /api/customers/ordertoken/{token}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `token` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/customers/ordertoken/{token}/bind_discount/

```
POST /api/customers/ordertoken/{token}/bind_discount/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `token` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/customers/ordertoken/{token}/remove_discount/

```
POST /api/customers/ordertoken/{token}/remove_discount/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `token` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/customers/ordertoken/{token}/usable_coupon_codes/

```
GET /api/customers/ordertoken/{token}/usable_coupon_codes/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `token` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/customers/cart/quick_buy/

快速下单购买

```
POST /api/customers/cart/quick_buy/
```

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/customers/cart/{token}/checkout/

```
POST /api/customers/cart/{token}/checkout/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `token` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/customers/cart/

```
POST /api/customers/cart/
```

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/customers/cart/{token}/

```
GET /api/customers/cart/{token}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `token` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/customers/cart/{parent_lookup_cart__token}/item/{pk}/check/

```
POST /api/customers/cart/{parent_lookup_cart__token}/item/{pk}/check/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `parent_lookup_cart__token` | string | yes |  |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/customers/cart/{parent_lookup_cart__token}/item/{pk}/uncheck/

```
POST /api/customers/cart/{parent_lookup_cart__token}/item/{pk}/uncheck/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `parent_lookup_cart__token` | string | yes |  |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/customers/cart/{parent_lookup_cart__token}/item/

```
POST /api/customers/cart/{parent_lookup_cart__token}/item/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `parent_lookup_cart__token` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/customers/cart/{parent_lookup_cart__token}/item/

```
GET /api/customers/cart/{parent_lookup_cart__token}/item/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `parent_lookup_cart__token` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/customers/cart/{parent_lookup_cart__token}/item/{pk}/

```
PUT /api/customers/cart/{parent_lookup_cart__token}/item/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `parent_lookup_cart__token` | string | yes |  |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/customers/cart/{parent_lookup_cart__token}/item/{pk}/

```
GET /api/customers/cart/{parent_lookup_cart__token}/item/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `parent_lookup_cart__token` | string | yes |  |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/customers/cart/{parent_lookup_cart__token}/item/{pk}/

```
PATCH /api/customers/cart/{parent_lookup_cart__token}/item/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `parent_lookup_cart__token` | string | yes |  |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/customers/cart/{parent_lookup_cart__token}/item/{pk}/

```
DELETE /api/customers/cart/{parent_lookup_cart__token}/item/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `parent_lookup_cart__token` | string | yes |  |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/customers/customer/

```
GET /api/customers/customer/
```

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/customers/customer/

```
POST /api/customers/customer/
```

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/customers/customer/

```
PUT /api/customers/customer/
```

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/customers/customer/

```
PATCH /api/customers/customer/
```

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/customers/login/quick/

```
POST /api/customers/login/quick/
```

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/customers/login/

```
POST /api/customers/login/
```

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/customers/password/forgot/

```
POST /api/customers/password/forgot/
```

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/customers/password/reset/

```
POST /api/customers/password/reset/
```

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

