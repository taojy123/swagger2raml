# users API documentation
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

### WriteUserSerializer

| Field | Type | Pattern | Required |
| ----- | ---- | ------- | -------- |
| `username` | string | ` ` | yes |
| `password` | string | ` ` | yes |
| `last_login` | string | ` ` | no |
| `email` | string | ` ` | yes |
| `date_joined` | string | ` ` | no |

### WritePlanBillingSerializer

| Field | Type | Pattern | Required |
| ----- | ---- | ------- | -------- |
| `plan_period` | string | ` ` | yes |
| `plan_name` | string | ` ` | yes |

### PageConfigPresetSerializer

| Field | Type | Pattern | Required |
| ----- | ---- | ------- | -------- |
| `` |  | ` ` | no |
| `` |  | ` ` | no |
| `` |  | ` ` | no |
| `` |  | ` ` | no |

### UserSerializer

| Field | Type | Pattern | Required |
| ----- | ---- | ------- | -------- |
| `` |  | ` ` | no |
| `` |  | ` ` | no |
| `` |  | ` ` | no |
| `` |  | ` ` | no |
| `` |  | ` ` | no |
| `` |  | ` ` | no |
| `` |  | ` ` | no |

### WriteScriptTagSerializer

| Field | Type | Pattern | Required |
| ----- | ---- | ------- | -------- |
| `content` | string | ` ` | no |
| `src` | string | ` ` | no |
| `metafield` | string | ` ` | no |
| `display_scope` | string | ` ` | no |

### ShopSerializer

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

### ShopNotificationConfigSerializer

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

### PlanBillingSerializer

| Field | Type | Pattern | Required |
| ----- | ---- | ------- | -------- |
| `order_token` | string | ` ` | no |
| `billing_type` | string | ` ` | no |
| `plan_period` | string | ` ` | yes |
| `title` | string | ` ` | no |
| `ends_at` | string | ` ` | no |
| `status` | string | ` ` | no |
| `starts_at` | string | ` ` | no |
| `id` | integer | ` ` | no |
| `plan_name` | string | ` ` | yes |
| `order_number` | string | ` ` | no |

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

### ThemeSerializer

| Field | Type | Pattern | Required |
| ----- | ---- | ------- | -------- |
| `screenshot_mobile` | string | ` ` | no |
| `current_preset` | string | ` ` | no |
| `presets` | array | ` ` | no |
| `settings_schema` | string | ` ` | no |
| `name` | string | ` ` | no |
| `screenshot` | string | ` ` | no |
| `title` | string | ` ` | no |
| `private_settings_data` | string | ` ` | no |
| `version` | string | ` ` | no |
| `is_current` | boolean | ` ` | no |
| `metafield` | string | ` ` | no |
| `assets` | string | ` ` | no |
| `id` | integer | ` ` | no |
| `settings_data` | string | ` ` | no |

### WriteThemePresetSerializer

| Field | Type | Pattern | Required |
| ----- | ---- | ------- | -------- |
| `metafield` | string | ` ` | no |
| `description` | string | ` ` | no |
| `title` | string | ` ` | no |

### WriteShopSettingsSerializer

| Field | Type | Pattern | Required |
| ----- | ---- | ------- | -------- |
| `description` | string | ` ` | no |
| `address` | string | ` ` | no |
| `email` | string | ` ` | no |
| `slogan` | string | ` ` | no |
| `logo` | string | ` ` | no |
| `favicon` | string | ` ` | no |
| `customer_email` | string | ` ` | no |
| `customer_phone` | string | ` ` | no |
| `metafield` | string | ` ` | no |
| `title` | string | ` ` | no |
| `website` | string | ` ` | no |
| `mobile` | string | ` ` | no |
| `company` | string | ` ` | no |

### WriteShopNotificationConfigSerializer

| Field | Type | Pattern | Required |
| ----- | ---- | ------- | -------- |
| `sms_enabled` | boolean | ` ` | no |
| `dashboard_enabled` | boolean | ` ` | no |
| `email_enabled` | boolean | ` ` | no |

### ScriptTagSerializer

| Field | Type | Pattern | Required |
| ----- | ---- | ------- | -------- |
| `` |  | ` ` | no |
| `` |  | ` ` | no |
| `` |  | ` ` | no |
| `` |  | ` ` | no |
| `` |  | ` ` | no |
| `` |  | ` ` | no |
| `` |  | ` ` | no |

### WriteShopSerializer

| Field | Type | Pattern | Required |
| ----- | ---- | ------- | -------- |
| `description` | string | ` ` | no |
| `address` | string | ` ` | no |
| `email` | string | ` ` | no |
| `slogan` | string | ` ` | no |
| `logo` | string | ` ` | no |
| `favicon` | string | ` ` | no |
| `customer_email` | string | ` ` | no |
| `customer_phone` | string | ` ` | no |
| `metafield` | string | ` ` | no |
| `title` | string | ` ` | no |
| `website` | string | ` ` | no |
| `mobile` | string | ` ` | no |
| `company` | string | ` ` | no |

### WritePlanSerializer

| Field | Type | Pattern | Required |
| ----- | ---- | ------- | -------- |
| `next_billing` | object | ` ` | yes |
| `active_billing` | object | ` ` | yes |

### ShopAdminUserSerializer

| Field | Type | Pattern | Required |
| ----- | ---- | ------- | -------- |
| `` |  | ` ` | no |
| `` |  | ` ` | no |
| `` |  | ` ` | no |
| `` |  | ` ` | no |
| `` |  | ` ` | no |
| `` |  | ` ` | no |

### ShopSettingsSerializer

| Field | Type | Pattern | Required |
| ----- | ---- | ------- | -------- |
| `domain` | string | ` ` | no |
| `identification_type` | string | ` ` | no |
| `updated_at` | string | ` ` | no |
| `favicon` | string | ` ` | no |
| `logo` | string | ` ` | no |
| `id` | integer | ` ` | no |
| `metafield` | string | ` ` | no |
| `title` | string | ` ` | no |
| `payment_channels` | string | ` ` | no |
| `theme` | object | ` ` | yes |
| `email` | string | ` ` | no |
| `website` | string | ` ` | no |
| `customer_email` | string | ` ` | no |
| `description` | string | ` ` | no |
| `company` | string | ` ` | no |
| `customer_phone` | string | ` ` | no |
| `notifications` | array | ` ` | no |
| `plan` | object | ` ` | yes |
| `address` | string | ` ` | no |
| `has_pending_identification` | string | ` ` | no |
| `slogan` | string | ` ` | no |
| `name` | string | ` ` | no |
| `mobile` | string | ` ` | no |
| `created_at` | string | ` ` | no |
| `script_tags` | array | ` ` | no |

### WriteShopAdminUserSerializer

| Field | Type | Pattern | Required |
| ----- | ---- | ------- | -------- |
| `mobile` | string | ` ` | no |
| `email` | string | ` ` | yes |
| `full_name` | string | ` ` | no |

### PlanSerializer

| Field | Type | Pattern | Required |
| ----- | ---- | ------- | -------- |
| `is_expired` | string | ` ` | no |
| `name` | string | ` ` | no |
| `title` | string | ` ` | no |
| `ends_at` | string | ` ` | no |
| `active_billing` | object | ` ` | yes |
| `starts_at` | string | ` ` | no |
| `can_publish_products` | string | ` ` | no |
| `id` | integer | ` ` | no |
| `days_left` | string | ` ` | no |
| `next_billing` | object | ` ` | yes |
| `period` | string | ` ` | no |

### /api/users/user/

```
GET /api/users/user/
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

### /api/users/user/change_password/

```
PUT /api/users/user/change_password/
```

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/users/user/{pk}/

```
GET /api/users/user/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/users/shopadmin/

```
GET /api/users/shopadmin/
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

### /api/users/shopadmin/auth/

```
POST /api/users/shopadmin/auth/
```

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/users/shopadmin/change_password/

```
PUT /api/users/shopadmin/change_password/
```

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/users/shopadmin/create_shop/

```
POST /api/users/shopadmin/create_shop/
```

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/users/shopadmin/{pk}/

```
GET /api/users/shopadmin/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/users/shop/

```
POST /api/users/shop/
```

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/users/shop/

```
GET /api/users/shop/
```

QueryString Parameters

| Attribute | Type | Required | Description | Example |
| --------- | ---- | -------- | ----------- | ------- |
| `id` | string | no |  | 
| `id__in` | string | no |  | 
| `name` | string | no |  | 
| `name__in` | string | no |  | 
| `q` | string | no |  | 
| `order_by` | string | no |  | 

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/users/shop/{pk}/

```
PUT /api/users/shop/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/users/shop/{pk}/

```
GET /api/users/shop/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/users/shop/{pk}/

```
PATCH /api/users/shop/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/users/shop/{pk}/

```
DELETE /api/users/shop/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

