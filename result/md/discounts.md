# discounts API documentation
http://heidianapi.com

---

## Models

### CustomerWithCouponCodeSerializer

| Field | Type | Pattern | Required |
| ----- | ---- | ------- | -------- |
| `` |  | ` ` | no |
| `` |  | ` ` | no |
| `` |  | ` ` | no |
| `` |  | ` ` | no |

### WriteCustomerSerializer

| Field | Type | Pattern | Required |
| ----- | ---- | ------- | -------- |
| `mobile` | string | ` ` | no |
| `gender` | string | ` ` | no |
| `note` | string | ` ` | no |
| `birthday` | string | ` ` | no |
| `full_name` | string | ` ` | no |
| `accepts_marketing` | boolean | ` ` | no |
| `email` | string | ` ` | no |

### WritePromotionCodeSerializer

| Field | Type | Pattern | Required |
| ----- | ---- | ------- | -------- |
| `description` | string | ` ` | no |
| `discount_type` | string | ` ` | no |
| `minimum_amount` | string | ` ` | no |
| `value` | string | ` ` | no |
| `title` | string | ` ` | no |
| `ends_at` | string | ` ` | no |
| `is_limit_once` | boolean | ` ` | no |
| `starts_at` | string | ` ` | no |
| `code` | string | ` ` | yes |
| `quantity` | integer | ` ` | no |
| `is_forever` | boolean | ` ` | no |

### WriteCustomerWithCouponCodeSerializer

| Field | Type | Pattern | Required |
| ----- | ---- | ------- | -------- |
| `mobile` | string | ` ` | yes |
| `full_name` | string | ` ` | no |

### CouponSerializer

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

### CustomerSerializer

| Field | Type | Pattern | Required |
| ----- | ---- | ------- | -------- |
| `email` | string | ` ` | no |
| `birthday` | string | ` ` | no |
| `note` | string | ` ` | no |
| `accepts_marketing` | boolean | ` ` | no |
| `id` | integer | ` ` | no |
| `gender` | string | ` ` | no |
| `full_name` | string | ` ` | no |
| `mobile` | string | ` ` | no |
| `created_at` | string | ` ` | no |

### PromotionCodeSerializer

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

### CouponCodeSerializer

| Field | Type | Pattern | Required |
| ----- | ---- | ------- | -------- |
| `` |  | ` ` | no |
| `` |  | ` ` | no |
| `` |  | ` ` | no |
| `` |  | ` ` | no |
| `` |  | ` ` | no |
| `` |  | ` ` | no |

### WriteCouponCodeSerializer

| Field | Type | Pattern | Required |
| ----- | ---- | ------- | -------- |
| `status` | string | ` ` | no |
| `code` | string | ` ` | yes |
| `used_at` | string | ` ` | no |
| `coupon_id` | integer | ` ` | yes |

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

### /api/discounts/promotion_code/

```
POST /api/discounts/promotion_code/
```

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/discounts/promotion_code/

```
GET /api/discounts/promotion_code/
```

QueryString Parameters

| Attribute | Type | Required | Description | Example |
| --------- | ---- | -------- | ----------- | ------- |
| `page` | integer | no |  | 
| `page_size` | integer | no |  | 
| `code` | string | no |  | 
| `code__in` | string | no |  | 
| `id` | string | no |  | 
| `id__in` | string | no |  | 
| `available` | string | no |  | 
| `unstart` | string | no |  | 
| `expired` | string | no |  | 
| `order_by` | string | no |  | 

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/discounts/promotion_code/{pk}/

```
PUT /api/discounts/promotion_code/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/discounts/promotion_code/{pk}/

```
GET /api/discounts/promotion_code/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/discounts/promotion_code/{pk}/

```
PATCH /api/discounts/promotion_code/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/discounts/promotion_code/{pk}/

```
DELETE /api/discounts/promotion_code/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/discounts/customer/

```
GET /api/discounts/customer/
```

QueryString Parameters

| Attribute | Type | Required | Description | Example |
| --------- | ---- | -------- | ----------- | ------- |
| `page` | integer | no |  | 
| `page_size` | integer | no |  | 
| `id` | string | no |  | 
| `id__in` | string | no |  | 
| `order_by` | string | no |  | 

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/discounts/customer/{pk}/

```
GET /api/discounts/customer/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/discounts/customer/{parent_lookup_customer}/coupon_code/

```
POST /api/discounts/customer/{parent_lookup_customer}/coupon_code/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `parent_lookup_customer` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/discounts/customer/{parent_lookup_customer}/coupon_code/

```
GET /api/discounts/customer/{parent_lookup_customer}/coupon_code/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `parent_lookup_customer` | string | yes |  |

QueryString Parameters

| Attribute | Type | Required | Description | Example |
| --------- | ---- | -------- | ----------- | ------- |
| `page` | integer | no |  | 
| `page_size` | integer | no |  | 
| `status` | string | no |  | 
| `status__in` | string | no |  | 
| `customer` | string | no |  | 
| `customer__in` | string | no |  | 
| `id` | string | no |  | 
| `id__in` | string | no |  | 
| `is_issued` | string | no |  | 
| `order_by` | string | no |  | 

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/discounts/customer/{parent_lookup_customer}/coupon_code/{pk}/

```
PUT /api/discounts/customer/{parent_lookup_customer}/coupon_code/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `parent_lookup_customer` | string | yes |  |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/discounts/customer/{parent_lookup_customer}/coupon_code/{pk}/

```
GET /api/discounts/customer/{parent_lookup_customer}/coupon_code/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `parent_lookup_customer` | string | yes |  |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/discounts/customer/{parent_lookup_customer}/coupon_code/{pk}/

```
PATCH /api/discounts/customer/{parent_lookup_customer}/coupon_code/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `parent_lookup_customer` | string | yes |  |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/discounts/customer/{parent_lookup_customer}/coupon_code/{pk}/

```
DELETE /api/discounts/customer/{parent_lookup_customer}/coupon_code/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `parent_lookup_customer` | string | yes |  |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/discounts/coupon/{pk}/customers/

```
GET /api/discounts/coupon/{pk}/customers/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/discounts/coupon/

```
POST /api/discounts/coupon/
```

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/discounts/coupon/

```
GET /api/discounts/coupon/
```

QueryString Parameters

| Attribute | Type | Required | Description | Example |
| --------- | ---- | -------- | ----------- | ------- |
| `page` | integer | no |  | 
| `page_size` | integer | no |  | 
| `id` | string | no |  | 
| `id__in` | string | no |  | 
| `available` | string | no |  | 
| `unstart` | string | no |  | 
| `expired` | string | no |  | 
| `order_by` | string | no |  | 

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/discounts/coupon/{pk}/

```
PUT /api/discounts/coupon/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/discounts/coupon/{pk}/

```
GET /api/discounts/coupon/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/discounts/coupon/{pk}/

```
PATCH /api/discounts/coupon/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/discounts/coupon/{pk}/

```
DELETE /api/discounts/coupon/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/discounts/coupon/{parent_lookup_coupon}/coupon_code/

```
POST /api/discounts/coupon/{parent_lookup_coupon}/coupon_code/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `parent_lookup_coupon` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/discounts/coupon/{parent_lookup_coupon}/coupon_code/

```
GET /api/discounts/coupon/{parent_lookup_coupon}/coupon_code/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `parent_lookup_coupon` | string | yes |  |

QueryString Parameters

| Attribute | Type | Required | Description | Example |
| --------- | ---- | -------- | ----------- | ------- |
| `page` | integer | no |  | 
| `page_size` | integer | no |  | 
| `status` | string | no |  | 
| `status__in` | string | no |  | 
| `customer` | string | no |  | 
| `customer__in` | string | no |  | 
| `id` | string | no |  | 
| `id__in` | string | no |  | 
| `is_issued` | string | no |  | 
| `order_by` | string | no |  | 

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/discounts/coupon/{parent_lookup_coupon}/coupon_code/{pk}/

```
PUT /api/discounts/coupon/{parent_lookup_coupon}/coupon_code/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `parent_lookup_coupon` | string | yes |  |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/discounts/coupon/{parent_lookup_coupon}/coupon_code/{pk}/

```
GET /api/discounts/coupon/{parent_lookup_coupon}/coupon_code/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `parent_lookup_coupon` | string | yes |  |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/discounts/coupon/{parent_lookup_coupon}/coupon_code/{pk}/

```
PATCH /api/discounts/coupon/{parent_lookup_coupon}/coupon_code/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `parent_lookup_coupon` | string | yes |  |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/discounts/coupon/{parent_lookup_coupon}/coupon_code/{pk}/

```
DELETE /api/discounts/coupon/{parent_lookup_coupon}/coupon_code/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `parent_lookup_coupon` | string | yes |  |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/discounts/get_all_items/

```
GET /api/discounts/get_all_items/
```

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/discounts/delete_items/

```
PATCH /api/discounts/delete_items/
```

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

