# other API documentation
http://heidianapi.com

---

## Models

### /api/customers/voucher/available_for_order/

获取该用户针对某订单可使用哪些代金券

```
GET /api/customers/voucher/available_for_order/
```

QueryString Parameters

| Attribute | Type | Required | Description | Example |
| --------- | ---- | -------- | ----------- | ------- |
| `order_id` | integer | no |  | 

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /api/customers/voucher/{voucher_id}/pay_for_order/

使用代金券支付订单

```
POST /api/customers/voucher/{voucher_id}/pay_for_order/
```

URI Parameters

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `voucher_id` | string | yes |  |

Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

