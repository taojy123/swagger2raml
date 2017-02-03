# notifications API documentation
http://heidianapi.com

---

## Models

### ShopNotificationSerializer

| Field | Type | Pattern | Required |
| ----- | ---- | ------- | -------- |
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
| `description` | string | ` ` | no |
| `name` | string | ` ` | no |
| `allow_email_enable` | string | ` ` | no |
| `email_enabled` | boolean | ` ` | no |
| `title` | string | ` ` | no |
| `sms_enabled` | boolean | ` ` | no |
| `id` | integer | ` ` | no |
| `kind` | string | ` ` | no |
| `allow_sms_enable` | string | ` ` | no |
| `dashboard_enabled` | boolean | ` ` | no |

### WriteShopNotificationConfigSerializer

| Field | Type | Pattern | Required |
| ----- | ---- | ------- | -------- |
| `sms_enabled` | boolean | ` ` | no |
| `dashboard_enabled` | boolean | ` ` | no |
| `email_enabled` | boolean | ` ` | no |

### WriteShopNotificationSerializer

| Field | Type | Pattern | Required |
| ----- | ---- | ------- | -------- |
| `category` | string | ` ` | yes |
| `content` | string | ` ` | no |
| `is_read` | boolean | ` ` | no |
| `detail` | string | ` ` | no |

### /api/notifications/category/

获取所有的通知类型的数据和配置

```
GET /api/notifications/category/
```

QueryString Parameters

| Attribute | Type | Required | Description | Example |
| --------- | ---- | -------- | ----------- | ------- |
| `page` | integer | no |  | 
| `page_size` | integer | no |  | 
| `kind` | string | no | 筛选大类 | 

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/notifications/category/{category__id}/dashboard_disable/

关闭站内信通知提醒

```
POST /api/notifications/category/{category__id}/dashboard_disable/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `category__id` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/notifications/category/{category__id}/dashboard_enable/

开启站内信通知提醒

```
POST /api/notifications/category/{category__id}/dashboard_enable/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `category__id` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/notifications/category/{category__id}/email_disable/

关闭 email 通知提醒

```
POST /api/notifications/category/{category__id}/email_disable/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `category__id` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/notifications/category/{category__id}/email_enable/

开启 email 通知提醒

```
POST /api/notifications/category/{category__id}/email_enable/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `category__id` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/notifications/category/{category__id}/sms_disable/

关闭短信通知提醒

```
POST /api/notifications/category/{category__id}/sms_disable/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `category__id` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/notifications/category/{category__id}/sms_enable/

开启短信通知提醒

```
POST /api/notifications/category/{category__id}/sms_enable/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `category__id` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/notifications/shop_notification/

```
GET /api/notifications/shop_notification/
```

QueryString Parameters

| Attribute | Type | Required | Description | Example |
| --------- | ---- | -------- | ----------- | ------- |
| `page` | integer | no |  | 
| `page_size` | integer | no |  | 
| `is_read` | string | no |  | 

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/notifications/shop_notification/delete_all/

批量删除通知 (url 中的 shop_notification 改成 customer_notification 即为买家接口)

```
POST /api/notifications/shop_notification/delete_all/
```

QueryString Parameters

| Attribute | Type | Required | Description | Example |
| --------- | ---- | -------- | ----------- | ------- |
| `id__in` | string | no |  | 1,3,19

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/notifications/shop_notification/read_all/

通知批量标记已读 (url 中的 shop_notification 改成 customer_notification 即为买家接口)

```
POST /api/notifications/shop_notification/read_all/
```

QueryString Parameters

| Attribute | Type | Required | Description | Example |
| --------- | ---- | -------- | ----------- | ------- |
| `id__in` | string | no |  | 1,3,19

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/notifications/shop_notification/{pk}/

```
GET /api/notifications/shop_notification/{pk}/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/notifications/shop_notification/{pk}/delete/

删除通知 (url 中的 shop_notification 改成 customer_notification 即为买家接口)

```
POST /api/notifications/shop_notification/{pk}/delete/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/notifications/shop_notification/{pk}/read/

通知标记已读 (url 中的 shop_notification 改成 customer_notification 即为买家接口)

```
POST /api/notifications/shop_notification/{pk}/read/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `pk` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

