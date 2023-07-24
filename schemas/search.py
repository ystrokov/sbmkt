SOUR_CREAM = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "suggests": {
            "type": "array",
            "items": [
                {
                    "type": "object",
                    "properties": {
                        "type": {
                            "type": "string"
                        },
                        "text": {
                            "type": "object",
                            "properties": {
                                "completion": {
                                    "type": "array",
                                    "items": [
                                        {
                                            "type": "object",
                                            "properties": {
                                                "text": {
                                                    "type": "string",
                                                    "pattern": "(^сметана$)"
                                                }
                                            },
                                            "required": [
                                                "text"
                                            ]
                                        },
                                        {
                                            "type": "object",
                                            "properties": {
                                                "text": {
                                                    "type": "string",
                                                    "pattern": "(^сметана 20%$)"
                                                }
                                            },
                                            "required": [
                                                "text"
                                            ]
                                        },
                                        {
                                            "type": "object",
                                            "properties": {
                                                "text": {
                                                    "type": "string",
                                                    "pattern": "(^сметана 15%$)"
                                                }
                                            },
                                            "required": [
                                                "text"
                                            ]
                                        },
                                        {
                                            "type": "object",
                                            "properties": {
                                                "text": {
                                                    "type": "string",
                                                    "pattern": "(^сметана 10$)"
                                                }
                                            },
                                            "required": [
                                                "text"
                                            ]
                                        },
                                        {
                                            "type": "object",
                                            "properties": {
                                                "text": {
                                                    "type": "string",
                                                    "pattern": "(^сметана простоквашино$)"
                                                }
                                            },
                                            "required": [
                                                "text"
                                            ]
                                        }
                                    ]
                                }
                            },
                            "required": [
                                "completion"
                            ]
                        }
                    },
                    "required": [
                        "type",
                        "text"
                    ]
                },
                {
                    "type": "object",
                    "properties": {
                        "type": {
                            "type": "string"
                        },
                        "category": {
                            "type": "object",
                            "properties": {
                                "completion": {
                                    "type": "array",
                                    "items": [
                                        {
                                            "type": "object",
                                            "properties": {
                                                "id": {
                                                    "type": "string",
                                                    "pattern": "(^77192$)"
                                                },
                                                "name": {
                                                    "type": "string",
                                                    "pattern": "(^Сметана$)"
                                                },
                                                "images": {
                                                    "type": "array",
                                                    "items": [
                                                        {
                                                            "type": "object",
                                                            "properties": {
                                                                "mini_url": {
                                                                    "type": "string"
                                                                },
                                                                "small_url": {
                                                                    "type": "string"
                                                                },
                                                                "product_url": {
                                                                    "type": "string"
                                                                },
                                                                "preview_url": {
                                                                    "type": "string"
                                                                },
                                                                "original_url": {
                                                                    "type": "string"
                                                                }
                                                            },
                                                            "required": [
                                                                "mini_url",
                                                                "small_url",
                                                                "product_url",
                                                                "preview_url",
                                                                "original_url"
                                                            ]
                                                        }
                                                    ]
                                                },
                                                "requirements": {
                                                    "type": "array",
                                                    "items": {}
                                                },
                                                "slug": {
                                                    "type": "string"
                                                }
                                            },
                                            "required": [
                                                "id",
                                                "name",
                                                "images",
                                                "requirements",
                                                "slug"
                                            ]
                                        },
                                        {
                                            "type": "object",
                                            "properties": {
                                                "id": {
                                                    "type": "string"
                                                },
                                                "name": {
                                                    "type": "string"
                                                },
                                                "images": {
                                                    "type": "array",
                                                    "items": [
                                                        {
                                                            "type": "object",
                                                            "properties": {
                                                                "mini_url": {
                                                                    "type": "string"
                                                                },
                                                                "small_url": {
                                                                    "type": "string"
                                                                },
                                                                "product_url": {
                                                                    "type": "string"
                                                                },
                                                                "preview_url": {
                                                                    "type": "string"
                                                                },
                                                                "original_url": {
                                                                    "type": "string"
                                                                }
                                                            },
                                                            "required": [
                                                                "mini_url",
                                                                "small_url",
                                                                "product_url",
                                                                "preview_url",
                                                                "original_url"
                                                            ]
                                                        }
                                                    ]
                                                },
                                                "requirements": {
                                                    "type": "array",
                                                    "items": {}
                                                },
                                                "slug": {
                                                    "type": "string"
                                                }
                                            },
                                            "required": [
                                                "id",
                                                "name",
                                                "images",
                                                "requirements",
                                                "slug"
                                            ]
                                        }
                                    ]
                                }
                            },
                            "required": [
                                "completion"
                            ]
                        }
                    },
                    "required": [
                        "type",
                        "category"
                    ]
                },
                {
                    "type": "object",
                    "properties": {
                        "type": {
                            "type": "string"
                        },
                        "product": {
                            "type": "object",
                            "properties": {
                                "completion": {
                                    "type": "array",
                                    "items": [
                                        {
                                            "type": "object",
                                            "properties": {
                                                "id": {
                                                    "type": "string"
                                                },
                                                "sku": {
                                                    "type": "string"
                                                },
                                                "retailer_sku": {
                                                    "type": "string"
                                                },
                                                "available": {
                                                    "type": "boolean"
                                                },
                                                "legacy_offer_id": {
                                                    "type": "integer"
                                                },
                                                "name": {
                                                    "type": "string"
                                                },
                                                "price": {
                                                    "type": "number"
                                                },
                                                "original_price": {
                                                    "type": "number"
                                                },
                                                "discount": {
                                                    "type": "number"
                                                },
                                                "human_volume": {
                                                    "type": "string"
                                                },
                                                "volume": {
                                                    "type": "integer"
                                                },
                                                "volume_type": {
                                                    "type": "string"
                                                },
                                                "items_per_pack": {
                                                    "type": "integer"
                                                },
                                                "discount_ends_at": {
                                                    "type": "string"
                                                },
                                                "price_type": {
                                                    "type": "string"
                                                },
                                                "grams_per_unit": {
                                                    "type": "integer"
                                                },
                                                "unit_price": {
                                                    "type": "number"
                                                },
                                                "original_unit_price": {
                                                    "type": "number"
                                                },
                                                "promo_badge_ids": {
                                                    "type": "array",
                                                    "items": {}
                                                },
                                                "score": {
                                                    "type": "integer"
                                                },
                                                "labels": {
                                                    "type": "array",
                                                    "items": {}
                                                },
                                                "image_urls": {
                                                    "type": "array",
                                                    "items": [
                                                        {
                                                            "type": "string"
                                                        },
                                                        {
                                                            "type": "string"
                                                        },
                                                        {
                                                            "type": "string"
                                                        }
                                                    ]
                                                },
                                                "requirements": {
                                                    "type": "array",
                                                    "items": {}
                                                },
                                                "slug": {
                                                    "type": "string"
                                                },
                                                "max_select_quantity": {
                                                    "type": "integer"
                                                },
                                                "canonical_url": {
                                                    "type": "string"
                                                },
                                                "vat_info": {
                                                    "type": "null"
                                                },
                                                "bmpl_info": {
                                                    "type": "object"
                                                },
                                                "max_per_order": {
                                                    "type": "null"
                                                },
                                                "ads_meta": {
                                                    "type": "null"
                                                },
                                                "with_options": {
                                                    "type": "boolean"
                                                }
                                            },
                                            "required": [
                                                "id",
                                                "sku",
                                                "retailer_sku",
                                                "available",
                                                "legacy_offer_id",
                                                "name",
                                                "price",
                                                "original_price",
                                                "discount",
                                                "human_volume",
                                                "volume",
                                                "volume_type",
                                                "items_per_pack",
                                                "discount_ends_at",
                                                "price_type",
                                                "grams_per_unit",
                                                "unit_price",
                                                "original_unit_price",
                                                "promo_badge_ids",
                                                "score",
                                                "labels",
                                                "image_urls",
                                                "requirements",
                                                "slug",
                                                "max_select_quantity",
                                                "canonical_url",
                                                "vat_info",
                                                "bmpl_info",
                                                "max_per_order",
                                                "ads_meta",
                                                "with_options"
                                            ]
                                        },
                                        {
                                            "type": "object",
                                            "properties": {
                                                "id": {
                                                    "type": "string"
                                                },
                                                "sku": {
                                                    "type": "string"
                                                },
                                                "retailer_sku": {
                                                    "type": "string"
                                                },
                                                "available": {
                                                    "type": "boolean"
                                                },
                                                "legacy_offer_id": {
                                                    "type": "integer"
                                                },
                                                "name": {
                                                    "type": "string"
                                                },
                                                "price": {
                                                    "type": "number"
                                                },
                                                "original_price": {
                                                    "type": "number"
                                                },
                                                "discount": {
                                                    "type": "number"
                                                },
                                                "human_volume": {
                                                    "type": "string"
                                                },
                                                "volume": {
                                                    "type": "integer"
                                                },
                                                "volume_type": {
                                                    "type": "string"
                                                },
                                                "items_per_pack": {
                                                    "type": "integer"
                                                },
                                                "discount_ends_at": {
                                                    "type": "string"
                                                },
                                                "price_type": {
                                                    "type": "string"
                                                },
                                                "grams_per_unit": {
                                                    "type": "integer"
                                                },
                                                "unit_price": {
                                                    "type": "number"
                                                },
                                                "original_unit_price": {
                                                    "type": "number"
                                                },
                                                "promo_badge_ids": {
                                                    "type": "array",
                                                    "items": {}
                                                },
                                                "score": {
                                                    "type": "number"
                                                },
                                                "labels": {
                                                    "type": "array",
                                                    "items": {}
                                                },
                                                "image_urls": {
                                                    "type": "array",
                                                    "items": [
                                                        {
                                                            "type": "string"
                                                        }
                                                    ]
                                                },
                                                "requirements": {
                                                    "type": "array",
                                                    "items": {}
                                                },
                                                "slug": {
                                                    "type": "string"
                                                },
                                                "max_select_quantity": {
                                                    "type": "integer"
                                                },
                                                "canonical_url": {
                                                    "type": "string"
                                                },
                                                "vat_info": {
                                                    "type": "null"
                                                },
                                                "bmpl_info": {
                                                    "type": "object"
                                                },
                                                "max_per_order": {
                                                    "type": "null"
                                                },
                                                "ads_meta": {
                                                    "type": "null"
                                                },
                                                "with_options": {
                                                    "type": "boolean"
                                                }
                                            },
                                            "required": [
                                                "id",
                                                "sku",
                                                "retailer_sku",
                                                "available",
                                                "legacy_offer_id",
                                                "name",
                                                "price",
                                                "original_price",
                                                "discount",
                                                "human_volume",
                                                "volume",
                                                "volume_type",
                                                "items_per_pack",
                                                "discount_ends_at",
                                                "price_type",
                                                "grams_per_unit",
                                                "unit_price",
                                                "original_unit_price",
                                                "promo_badge_ids",
                                                "score",
                                                "labels",
                                                "image_urls",
                                                "requirements",
                                                "slug",
                                                "max_select_quantity",
                                                "canonical_url",
                                                "vat_info",
                                                "bmpl_info",
                                                "max_per_order",
                                                "ads_meta",
                                                "with_options"
                                            ]
                                        },
                                        {
                                            "type": "object",
                                            "properties": {
                                                "id": {
                                                    "type": "string"
                                                },
                                                "sku": {
                                                    "type": "string"
                                                },
                                                "retailer_sku": {
                                                    "type": "string"
                                                },
                                                "available": {
                                                    "type": "boolean"
                                                },
                                                "legacy_offer_id": {
                                                    "type": "integer"
                                                },
                                                "name": {
                                                    "type": "string"
                                                },
                                                "price": {
                                                    "type": "number"
                                                },
                                                "original_price": {
                                                    "type": "number"
                                                },
                                                "discount": {
                                                    "type": "integer"
                                                },
                                                "human_volume": {
                                                    "type": "string"
                                                },
                                                "volume": {
                                                    "type": "integer"
                                                },
                                                "volume_type": {
                                                    "type": "string"
                                                },
                                                "items_per_pack": {
                                                    "type": "integer"
                                                },
                                                "discount_ends_at": {
                                                    "type": "string"
                                                },
                                                "price_type": {
                                                    "type": "string"
                                                },
                                                "grams_per_unit": {
                                                    "type": "integer"
                                                },
                                                "unit_price": {
                                                    "type": "number"
                                                },
                                                "original_unit_price": {
                                                    "type": "number"
                                                },
                                                "promo_badge_ids": {
                                                    "type": "array",
                                                    "items": {}
                                                },
                                                "score": {
                                                    "type": "integer"
                                                },
                                                "labels": {
                                                    "type": "array",
                                                    "items": {}
                                                },
                                                "image_urls": {
                                                    "type": "array",
                                                    "items": [
                                                        {
                                                            "type": "string"
                                                        }
                                                    ]
                                                },
                                                "requirements": {
                                                    "type": "array",
                                                    "items": {}
                                                },
                                                "slug": {
                                                    "type": "string"
                                                },
                                                "max_select_quantity": {
                                                    "type": "integer"
                                                },
                                                "canonical_url": {
                                                    "type": "string"
                                                },
                                                "vat_info": {
                                                    "type": "null"
                                                },
                                                "bmpl_info": {
                                                    "type": "object"
                                                },
                                                "max_per_order": {
                                                    "type": "null"
                                                },
                                                "ads_meta": {
                                                    "type": "null"
                                                },
                                                "with_options": {
                                                    "type": "boolean"
                                                }
                                            },
                                            "required": [
                                                "id",
                                                "sku",
                                                "retailer_sku",
                                                "available",
                                                "legacy_offer_id",
                                                "name",
                                                "price",
                                                "original_price",
                                                "discount",
                                                "human_volume",
                                                "volume",
                                                "volume_type",
                                                "items_per_pack",
                                                "discount_ends_at",
                                                "price_type",
                                                "grams_per_unit",
                                                "unit_price",
                                                "original_unit_price",
                                                "promo_badge_ids",
                                                "score",
                                                "labels",
                                                "image_urls",
                                                "requirements",
                                                "slug",
                                                "max_select_quantity",
                                                "canonical_url",
                                                "vat_info",
                                                "bmpl_info",
                                                "max_per_order",
                                                "ads_meta",
                                                "with_options"
                                            ]
                                        }
                                    ]
                                }
                            },
                            "required": [
                                "completion"
                            ]
                        }
                    },
                    "required": [
                        "type",
                        "product"
                    ]
                }
            ]
        }
    },
    "required": [
        "suggests"
    ]
}

BREAD = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "suggests": {
            "type": "array",
            "items": [
                {
                    "type": "object",
                    "properties": {
                        "type": {
                            "type": "string"
                        },
                        "text": {
                            "type": "object",
                            "properties": {
                                "completion": {
                                    "type": "array",
                                    "items": [
                                        {
                                            "type": "object",
                                            "properties": {
                                                "text": {
                                                    "type": "string",
                                                    "pattern": "(^хлеб$)"
                                                }
                                            },
                                            "required": [
                                                "text"
                                            ]
                                        },
                                        {
                                            "type": "object",
                                            "properties": {
                                                "text": {
                                                    "type": "string",
                                                    "pattern": "(^хлебцы$)"
                                                }
                                            },
                                            "required": [
                                                "text"
                                            ]
                                        },
                                        {
                                            "type": "object",
                                            "properties": {
                                                "text": {
                                                    "type": "string",
                                                    "pattern": "(^хлеб тостовый$)"
                                                }
                                            },
                                            "required": [
                                                "text"
                                            ]
                                        },
                                        {
                                            "type": "object",
                                            "properties": {
                                                "text": {
                                                    "type": "string",
                                                    "pattern": "(^хлеб черный$)"

                                                }
                                            },
                                            "required": [
                                                "text"
                                            ]
                                        },
                                        {
                                            "type": "object",
                                            "properties": {
                                                "text": {
                                                    "type": "string",
                                                    "pattern": "(^хлеб белый$)"
                                                }
                                            },
                                            "required": [
                                                "text"
                                            ]
                                        }
                                    ]
                                }
                            },
                            "required": [
                                "completion"
                            ]
                        }
                    },
                    "required": [
                        "type",
                        "text"
                    ]
                },
                {
                    "type": "object",
                    "properties": {
                        "type": {
                            "type": "string"
                        },
                        "category": {
                            "type": "object",
                            "properties": {
                                "completion": {
                                    "type": "array",
                                    "items": [
                                        {
                                            "type": "object",
                                            "properties": {
                                                "id": {
                                                    "type": "string",
                                                    "pattern": "(^43509$)"
                                                },
                                                "name": {
                                                    "type": "string",
                                                    "pattern": "(^Хлеб, лаваш, лепешки$)"
                                                },
                                                "images": {
                                                    "type": "array",
                                                    "items": [
                                                        {
                                                            "type": "object",
                                                            "properties": {
                                                                "mini_url": {
                                                                    "type": "string"
                                                                },
                                                                "small_url": {
                                                                    "type": "string"
                                                                },
                                                                "product_url": {
                                                                    "type": "string"
                                                                },
                                                                "preview_url": {
                                                                    "type": "string"
                                                                },
                                                                "original_url": {
                                                                    "type": "string"
                                                                }
                                                            },
                                                            "required": [
                                                                "mini_url",
                                                                "small_url",
                                                                "product_url",
                                                                "preview_url",
                                                                "original_url"
                                                            ]
                                                        }
                                                    ]
                                                },
                                                "requirements": {
                                                    "type": "array",
                                                    "items": {}
                                                },
                                                "slug": {
                                                    "type": "string"
                                                }
                                            },
                                            "required": [
                                                "id",
                                                "name",
                                                "images",
                                                "requirements",
                                                "slug"
                                            ]
                                        },
                                        {
                                            "type": "object",
                                            "properties": {
                                                "id": {
                                                    "type": "string",
                                                    "pattern": "(^72094$)"
                                                },
                                                "name": {
                                                    "type": "string",
                                                    "pattern": "(^Мед, варенье, сиропы$)"
                                                },
                                                "images": {
                                                    "type": "array",
                                                    "items": [
                                                        {
                                                            "type": "object",
                                                            "properties": {
                                                                "mini_url": {
                                                                    "type": "string"
                                                                },
                                                                "small_url": {
                                                                    "type": "string"
                                                                },
                                                                "product_url": {
                                                                    "type": "string"
                                                                },
                                                                "preview_url": {
                                                                    "type": "string"
                                                                },
                                                                "original_url": {
                                                                    "type": "string"
                                                                }
                                                            },
                                                            "required": [
                                                                "mini_url",
                                                                "small_url",
                                                                "product_url",
                                                                "preview_url",
                                                                "original_url"
                                                            ]
                                                        }
                                                    ]
                                                },
                                                "requirements": {
                                                    "type": "array",
                                                    "items": {}
                                                },
                                                "slug": {
                                                    "type": "string"
                                                }
                                            },
                                            "required": [
                                                "id",
                                                "name",
                                                "images",
                                                "requirements",
                                                "slug"
                                            ]
                                        }
                                    ]
                                }
                            },
                            "required": [
                                "completion"
                            ]
                        }
                    },
                    "required": [
                        "type",
                        "category"
                    ]
                },
                {
                    "type": "object",
                    "properties": {
                        "type": {
                            "type": "string"
                        },
                        "product": {
                            "type": "object",
                            "properties": {
                                "completion": {
                                    "type": "array",
                                    "items": [
                                        {
                                            "type": "object",
                                            "properties": {
                                                "id": {
                                                    "type": "string"
                                                },
                                                "sku": {
                                                    "type": "string"
                                                },
                                                "retailer_sku": {
                                                    "type": "string"
                                                },
                                                "available": {
                                                    "type": "boolean"
                                                },
                                                "legacy_offer_id": {
                                                    "type": "integer"
                                                },
                                                "name": {
                                                    "type": "string"
                                                },
                                                "price": {
                                                    "type": "number"
                                                },
                                                "original_price": {
                                                    "type": "number"
                                                },
                                                "discount": {
                                                    "type": "integer"
                                                },
                                                "human_volume": {
                                                    "type": "string"
                                                },
                                                "volume": {
                                                    "type": "integer"
                                                },
                                                "volume_type": {
                                                    "type": "string"
                                                },
                                                "items_per_pack": {
                                                    "type": "integer"
                                                },
                                                "discount_ends_at": {
                                                    "type": "string"
                                                },
                                                "price_type": {
                                                    "type": "string"
                                                },
                                                "grams_per_unit": {
                                                    "type": "integer"
                                                },
                                                "unit_price": {
                                                    "type": "number"
                                                },
                                                "original_unit_price": {
                                                    "type": "number"
                                                },
                                                "promo_badge_ids": {
                                                    "type": "array",
                                                    "items": {}
                                                },
                                                "score": {
                                                    "type": "integer"
                                                },
                                                "labels": {
                                                    "type": "array",
                                                    "items": {}
                                                },
                                                "image_urls": {
                                                    "type": "array",
                                                    "items": [
                                                        {
                                                            "type": "string"
                                                        }
                                                    ]
                                                },
                                                "requirements": {
                                                    "type": "array",
                                                    "items": {}
                                                },
                                                "slug": {
                                                    "type": "string"
                                                },
                                                "max_select_quantity": {
                                                    "type": "integer"
                                                },
                                                "canonical_url": {
                                                    "type": "string"
                                                },
                                                "vat_info": {
                                                    "type": "null"
                                                },
                                                "bmpl_info": {
                                                    "type": "object"
                                                },
                                                "max_per_order": {
                                                    "type": "null"
                                                },
                                                "ads_meta": {
                                                    "type": "null"
                                                },
                                                "with_options": {
                                                    "type": "boolean"
                                                }
                                            },
                                            "required": [
                                                "id",
                                                "sku",
                                                "retailer_sku",
                                                "available",
                                                "legacy_offer_id",
                                                "name",
                                                "price",
                                                "original_price",
                                                "discount",
                                                "human_volume",
                                                "volume",
                                                "volume_type",
                                                "items_per_pack",
                                                "discount_ends_at",
                                                "price_type",
                                                "grams_per_unit",
                                                "unit_price",
                                                "original_unit_price",
                                                "promo_badge_ids",
                                                "score",
                                                "labels",
                                                "image_urls",
                                                "requirements",
                                                "slug",
                                                "max_select_quantity",
                                                "canonical_url",
                                                "vat_info",
                                                "bmpl_info",
                                                "max_per_order",
                                                "ads_meta",
                                                "with_options"
                                            ]
                                        },
                                        {
                                            "type": "object",
                                            "properties": {
                                                "id": {
                                                    "type": "string"
                                                },
                                                "sku": {
                                                    "type": "string"
                                                },
                                                "retailer_sku": {
                                                    "type": "string"
                                                },
                                                "available": {
                                                    "type": "boolean"
                                                },
                                                "legacy_offer_id": {
                                                    "type": "integer"
                                                },
                                                "name": {
                                                    "type": "string"
                                                },
                                                "price": {
                                                    "type": "number"
                                                },
                                                "original_price": {
                                                    "type": "number"
                                                },
                                                "discount": {
                                                    "type": "number"
                                                },
                                                "human_volume": {
                                                    "type": "string"
                                                },
                                                "volume": {
                                                    "type": "integer"
                                                },
                                                "volume_type": {
                                                    "type": "string"
                                                },
                                                "items_per_pack": {
                                                    "type": "integer"
                                                },
                                                "discount_ends_at": {
                                                    "type": "string"
                                                },
                                                "price_type": {
                                                    "type": "string"
                                                },
                                                "grams_per_unit": {
                                                    "type": "integer"
                                                },
                                                "unit_price": {
                                                    "type": "number"
                                                },
                                                "original_unit_price": {
                                                    "type": "number"
                                                },
                                                "promo_badge_ids": {
                                                    "type": "array",
                                                    "items": {}
                                                },
                                                "score": {
                                                    "type": "integer"
                                                },
                                                "labels": {
                                                    "type": "array",
                                                    "items": {}
                                                },
                                                "image_urls": {
                                                    "type": "array",
                                                    "items": [
                                                        {
                                                            "type": "string"
                                                        }
                                                    ]
                                                },
                                                "requirements": {
                                                    "type": "array",
                                                    "items": {}
                                                },
                                                "slug": {
                                                    "type": "string"
                                                },
                                                "max_select_quantity": {
                                                    "type": "integer"
                                                },
                                                "canonical_url": {
                                                    "type": "string"
                                                },
                                                "vat_info": {
                                                    "type": "null"
                                                },
                                                "bmpl_info": {
                                                    "type": "object"
                                                },
                                                "max_per_order": {
                                                    "type": "null"
                                                },
                                                "ads_meta": {
                                                    "type": "null"
                                                },
                                                "with_options": {
                                                    "type": "boolean"
                                                }
                                            },
                                            "required": [
                                                "id",
                                                "sku",
                                                "retailer_sku",
                                                "available",
                                                "legacy_offer_id",
                                                "name",
                                                "price",
                                                "original_price",
                                                "discount",
                                                "human_volume",
                                                "volume",
                                                "volume_type",
                                                "items_per_pack",
                                                "discount_ends_at",
                                                "price_type",
                                                "grams_per_unit",
                                                "unit_price",
                                                "original_unit_price",
                                                "promo_badge_ids",
                                                "score",
                                                "labels",
                                                "image_urls",
                                                "requirements",
                                                "slug",
                                                "max_select_quantity",
                                                "canonical_url",
                                                "vat_info",
                                                "bmpl_info",
                                                "max_per_order",
                                                "ads_meta",
                                                "with_options"
                                            ]
                                        },
                                        {
                                            "type": "object",
                                            "properties": {
                                                "id": {
                                                    "type": "string"
                                                },
                                                "sku": {
                                                    "type": "string"
                                                },
                                                "retailer_sku": {
                                                    "type": "string"
                                                },
                                                "available": {
                                                    "type": "boolean"
                                                },
                                                "legacy_offer_id": {
                                                    "type": "integer"
                                                },
                                                "name": {
                                                    "type": "string"
                                                },
                                                "price": {
                                                    "type": "number"
                                                },
                                                "original_price": {
                                                    "type": "number"
                                                },
                                                "discount": {
                                                    "type": "integer"
                                                },
                                                "human_volume": {
                                                    "type": "string"
                                                },
                                                "volume": {
                                                    "type": "integer"
                                                },
                                                "volume_type": {
                                                    "type": "string"
                                                },
                                                "items_per_pack": {
                                                    "type": "integer"
                                                },
                                                "discount_ends_at": {
                                                    "type": "string"
                                                },
                                                "price_type": {
                                                    "type": "string"
                                                },
                                                "grams_per_unit": {
                                                    "type": "integer"
                                                },
                                                "unit_price": {
                                                    "type": "number"
                                                },
                                                "original_unit_price": {
                                                    "type": "number"
                                                },
                                                "promo_badge_ids": {
                                                    "type": "array",
                                                    "items": {}
                                                },
                                                "score": {
                                                    "type": "integer"
                                                },
                                                "labels": {
                                                    "type": "array",
                                                    "items": {}
                                                },
                                                "image_urls": {
                                                    "type": "array",
                                                    "items": [
                                                        {
                                                            "type": "string"
                                                        }
                                                    ]
                                                },
                                                "requirements": {
                                                    "type": "array",
                                                    "items": {}
                                                },
                                                "slug": {
                                                    "type": "string"
                                                },
                                                "max_select_quantity": {
                                                    "type": "integer"
                                                },
                                                "canonical_url": {
                                                    "type": "string"
                                                },
                                                "vat_info": {
                                                    "type": "null"
                                                },
                                                "bmpl_info": {
                                                    "type": "object"
                                                },
                                                "max_per_order": {
                                                    "type": "null"
                                                },
                                                "ads_meta": {
                                                    "type": "null"
                                                },
                                                "with_options": {
                                                    "type": "boolean"
                                                }
                                            },
                                            "required": [
                                                "id",
                                                "sku",
                                                "retailer_sku",
                                                "available",
                                                "legacy_offer_id",
                                                "name",
                                                "price",
                                                "original_price",
                                                "discount",
                                                "human_volume",
                                                "volume",
                                                "volume_type",
                                                "items_per_pack",
                                                "discount_ends_at",
                                                "price_type",
                                                "grams_per_unit",
                                                "unit_price",
                                                "original_unit_price",
                                                "promo_badge_ids",
                                                "score",
                                                "labels",
                                                "image_urls",
                                                "requirements",
                                                "slug",
                                                "max_select_quantity",
                                                "canonical_url",
                                                "vat_info",
                                                "bmpl_info",
                                                "max_per_order",
                                                "ads_meta",
                                                "with_options"
                                            ]
                                        }
                                    ]
                                }
                            },
                            "required": [
                                "completion"
                            ]
                        }
                    },
                    "required": [
                        "type",
                        "product"
                    ]
                }
            ]
        }
    },
    "required": [
        "suggests"
    ]
}


MILK = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "suggests": {
            "type": "array",
            "items": [
                {
                    "type": "object",
                    "properties": {
                        "type": {
                            "type": "string"
                        },
                        "text": {
                            "type": "object",
                            "properties": {
                                "completion": {
                                    "type": "array",
                                    "items": [
                                        {
                                            "type": "object",
                                            "properties": {
                                                "text": {
                                                    "type": "string",
                                                    "pattern": "(^молоко$)"
                                                }
                                            },
                                            "required": [
                                                "text"
                                            ]
                                        },
                                        {
                                            "type": "object",
                                            "properties": {
                                                "text": {
                                                    "type": "string",
                                                    "pattern": "(^молоко безлактозное$)"
                                                }
                                            },
                                            "required": [
                                                "text"
                                            ]
                                        },
                                        {
                                            "type": "object",
                                            "properties": {
                                                "text": {
                                                    "type": "string",
                                                    "pattern": "(^молоко ультрапастеризованное$)"
                                                }
                                            },
                                            "required": [
                                                "text"
                                            ]
                                        },
                                        {
                                            "type": "object",
                                            "properties": {
                                                "text": {
                                                    "type": "string",
                                                    "pattern": "(^молоко 3.2$)"

                                                }
                                            },
                                            "required": [
                                                "text"
                                            ]
                                        },
                                        {
                                            "type": "object",
                                            "properties": {
                                                "text": {
                                                    "type": "string",
                                                    "pattern": "(^молоко топленое$)"
                                                }
                                            },
                                            "required": [
                                                "text"
                                            ]
                                        }
                                    ]
                                }
                            },
                            "required": [
                                "completion"
                            ]
                        }
                    },
                    "required": [
                        "type",
                        "text"
                    ]
                },
                {
                    "type": "object",
                    "properties": {
                        "type": {
                            "type": "string"
                        },
                        "category": {
                            "type": "object",
                            "properties": {
                                "completion": {
                                    "type": "array",
                                    "items": [
                                        {
                                            "type": "object",
                                            "properties": {
                                                "id": {
                                                    "type": "string",
                                                    "pattern": "(^76153$)"
                                                },
                                                "name": {
                                                    "type": "string",
                                                    "pattern": "(^Молоко, сливки$)"
                                                },
                                                "images": {
                                                    "type": "array",
                                                    "items": [
                                                        {
                                                            "type": "object",
                                                            "properties": {
                                                                "mini_url": {
                                                                    "type": "string"
                                                                },
                                                                "small_url": {
                                                                    "type": "string"
                                                                },
                                                                "product_url": {
                                                                    "type": "string"
                                                                },
                                                                "preview_url": {
                                                                    "type": "string"
                                                                },
                                                                "original_url": {
                                                                    "type": "string"
                                                                }
                                                            },
                                                            "required": [
                                                                "mini_url",
                                                                "small_url",
                                                                "product_url",
                                                                "preview_url",
                                                                "original_url"
                                                            ]
                                                        }
                                                    ]
                                                },
                                                "requirements": {
                                                    "type": "array",
                                                    "items": {}
                                                },
                                                "slug": {
                                                    "type": "string"
                                                }
                                            },
                                            "required": [
                                                "id",
                                                "name",
                                                "images",
                                                "requirements",
                                                "slug"
                                            ]
                                        },
                                        {
                                            "type": "object",
                                            "properties": {
                                                "id": {
                                                    "type": "string",
                                                    "pattern": "(^77201$)"
                                                },
                                                "name": {
                                                    "type": "string",
                                                    "pattern": "(^Йогурты, творожок$)"
                                                },
                                                "images": {
                                                    "type": "array",
                                                    "items": [
                                                        {
                                                            "type": "object",
                                                            "properties": {
                                                                "mini_url": {
                                                                    "type": "string"
                                                                },
                                                                "small_url": {
                                                                    "type": "string"
                                                                },
                                                                "product_url": {
                                                                    "type": "string"
                                                                },
                                                                "preview_url": {
                                                                    "type": "string"
                                                                },
                                                                "original_url": {
                                                                    "type": "string"
                                                                }
                                                            },
                                                            "required": [
                                                                "mini_url",
                                                                "small_url",
                                                                "product_url",
                                                                "preview_url",
                                                                "original_url"
                                                            ]
                                                        }
                                                    ]
                                                },
                                                "requirements": {
                                                    "type": "array",
                                                    "items": {}
                                                },
                                                "slug": {
                                                    "type": "string"
                                                }
                                            },
                                            "required": [
                                                "id",
                                                "name",
                                                "images",
                                                "requirements",
                                                "slug"
                                            ]
                                        }
                                    ]
                                }
                            },
                            "required": [
                                "completion"
                            ]
                        }
                    },
                    "required": [
                        "type",
                        "category"
                    ]
                },
                {
                    "type": "object",
                    "properties": {
                        "type": {
                            "type": "string"
                        },
                        "product": {
                            "type": "object",
                            "properties": {
                                "completion": {
                                    "type": "array",
                                    "items": [
                                        {
                                            "type": "object",
                                            "properties": {
                                                "id": {
                                                    "type": "string"
                                                },
                                                "sku": {
                                                    "type": "string"
                                                },
                                                "retailer_sku": {
                                                    "type": "string"
                                                },
                                                "available": {
                                                    "type": "boolean"
                                                },
                                                "legacy_offer_id": {
                                                    "type": "integer"
                                                },
                                                "name": {
                                                    "type": "string"
                                                },
                                                "price": {
                                                    "type": "number"
                                                },
                                                "original_price": {
                                                    "type": "number"
                                                },
                                                "discount": {
                                                    "type": "number"
                                                },
                                                "human_volume": {
                                                    "type": "string"
                                                },
                                                "volume": {
                                                    "type": "integer"
                                                },
                                                "volume_type": {
                                                    "type": "string"
                                                },
                                                "items_per_pack": {
                                                    "type": "integer"
                                                },
                                                "discount_ends_at": {
                                                    "type": "string"
                                                },
                                                "price_type": {
                                                    "type": "string"
                                                },
                                                "grams_per_unit": {
                                                    "type": "integer"
                                                },
                                                "unit_price": {
                                                    "type": "number"
                                                },
                                                "original_unit_price": {
                                                    "type": "number"
                                                },
                                                "promo_badge_ids": {
                                                    "type": "array",
                                                    "items": {}
                                                },
                                                "score": {
                                                    "type": "number"
                                                },
                                                "labels": {
                                                    "type": "array",
                                                    "items": {}
                                                },
                                                "image_urls": {
                                                    "type": "array",
                                                    "items": [
                                                        {
                                                            "type": "string"
                                                        },
                                                        {
                                                            "type": "string"
                                                        }
                                                    ]
                                                },
                                                "requirements": {
                                                    "type": "array",
                                                    "items": {}
                                                },
                                                "slug": {
                                                    "type": "string"
                                                },
                                                "max_select_quantity": {
                                                    "type": "integer"
                                                },
                                                "canonical_url": {
                                                    "type": "string"
                                                },
                                                "vat_info": {
                                                    "type": "null"
                                                },
                                                "bmpl_info": {
                                                    "type": "object"
                                                },
                                                "max_per_order": {
                                                    "type": "null"
                                                },
                                                "ads_meta": {
                                                    "type": "null"
                                                },
                                                "with_options": {
                                                    "type": "boolean"
                                                }
                                            },
                                            "required": [
                                                "id",
                                                "sku",
                                                "retailer_sku",
                                                "available",
                                                "legacy_offer_id",
                                                "name",
                                                "price",
                                                "original_price",
                                                "discount",
                                                "human_volume",
                                                "volume",
                                                "volume_type",
                                                "items_per_pack",
                                                "discount_ends_at",
                                                "price_type",
                                                "grams_per_unit",
                                                "unit_price",
                                                "original_unit_price",
                                                "promo_badge_ids",
                                                "score",
                                                "labels",
                                                "image_urls",
                                                "requirements",
                                                "slug",
                                                "max_select_quantity",
                                                "canonical_url",
                                                "vat_info",
                                                "bmpl_info",
                                                "max_per_order",
                                                "ads_meta",
                                                "with_options"
                                            ]
                                        },
                                        {
                                            "type": "object",
                                            "properties": {
                                                "id": {
                                                    "type": "string"
                                                },
                                                "sku": {
                                                    "type": "string"
                                                },
                                                "retailer_sku": {
                                                    "type": "string"
                                                },
                                                "available": {
                                                    "type": "boolean"
                                                },
                                                "legacy_offer_id": {
                                                    "type": "integer"
                                                },
                                                "name": {
                                                    "type": "string"
                                                },
                                                "price": {
                                                    "type": "number"
                                                },
                                                "original_price": {
                                                    "type": "number"
                                                },
                                                "discount": {
                                                    "type": "integer"
                                                },
                                                "human_volume": {
                                                    "type": "string"
                                                },
                                                "volume": {
                                                    "type": "integer"
                                                },
                                                "volume_type": {
                                                    "type": "string"
                                                },
                                                "items_per_pack": {
                                                    "type": "integer"
                                                },
                                                "discount_ends_at": {
                                                    "type": "string"
                                                },
                                                "price_type": {
                                                    "type": "string"
                                                },
                                                "grams_per_unit": {
                                                    "type": "integer"
                                                },
                                                "unit_price": {
                                                    "type": "number"
                                                },
                                                "original_unit_price": {
                                                    "type": "number"
                                                },
                                                "promo_badge_ids": {
                                                    "type": "array",
                                                    "items": {}
                                                },
                                                "score": {
                                                    "type": "integer"
                                                },
                                                "labels": {
                                                    "type": "array",
                                                    "items": {}
                                                },
                                                "image_urls": {
                                                    "type": "array",
                                                    "items": [
                                                        {
                                                            "type": "string"
                                                        }
                                                    ]
                                                },
                                                "requirements": {
                                                    "type": "array",
                                                    "items": {}
                                                },
                                                "slug": {
                                                    "type": "string"
                                                },
                                                "max_select_quantity": {
                                                    "type": "integer"
                                                },
                                                "canonical_url": {
                                                    "type": "string"
                                                },
                                                "vat_info": {
                                                    "type": "null"
                                                },
                                                "bmpl_info": {
                                                    "type": "object"
                                                },
                                                "max_per_order": {
                                                    "type": "null"
                                                },
                                                "ads_meta": {
                                                    "type": "null"
                                                },
                                                "with_options": {
                                                    "type": "boolean"
                                                }
                                            },
                                            "required": [
                                                "id",
                                                "sku",
                                                "retailer_sku",
                                                "available",
                                                "legacy_offer_id",
                                                "name",
                                                "price",
                                                "original_price",
                                                "discount",
                                                "human_volume",
                                                "volume",
                                                "volume_type",
                                                "items_per_pack",
                                                "discount_ends_at",
                                                "price_type",
                                                "grams_per_unit",
                                                "unit_price",
                                                "original_unit_price",
                                                "promo_badge_ids",
                                                "score",
                                                "labels",
                                                "image_urls",
                                                "requirements",
                                                "slug",
                                                "max_select_quantity",
                                                "canonical_url",
                                                "vat_info",
                                                "bmpl_info",
                                                "max_per_order",
                                                "ads_meta",
                                                "with_options"
                                            ]
                                        },
                                        {
                                            "type": "object",
                                            "properties": {
                                                "id": {
                                                    "type": "string"
                                                },
                                                "sku": {
                                                    "type": "string"
                                                },
                                                "retailer_sku": {
                                                    "type": "string"
                                                },
                                                "available": {
                                                    "type": "boolean"
                                                },
                                                "legacy_offer_id": {
                                                    "type": "integer"
                                                },
                                                "name": {
                                                    "type": "string"
                                                },
                                                "price": {
                                                    "type": "number"
                                                },
                                                "original_price": {
                                                    "type": "number"
                                                },
                                                "discount": {
                                                    "type": "integer"
                                                },
                                                "human_volume": {
                                                    "type": "string"
                                                },
                                                "volume": {
                                                    "type": "integer"
                                                },
                                                "volume_type": {
                                                    "type": "string"
                                                },
                                                "items_per_pack": {
                                                    "type": "integer"
                                                },
                                                "discount_ends_at": {
                                                    "type": "string"
                                                },
                                                "price_type": {
                                                    "type": "string"
                                                },
                                                "grams_per_unit": {
                                                    "type": "integer"
                                                },
                                                "unit_price": {
                                                    "type": "number"
                                                },
                                                "original_unit_price": {
                                                    "type": "number"
                                                },
                                                "promo_badge_ids": {
                                                    "type": "array",
                                                    "items": {}
                                                },
                                                "score": {
                                                    "type": "null"
                                                },
                                                "labels": {
                                                    "type": "array",
                                                    "items": {}
                                                },
                                                "image_urls": {
                                                    "type": "array",
                                                    "items": [
                                                        {
                                                            "type": "string"
                                                        },
                                                        {
                                                            "type": "string"
                                                        }
                                                    ]
                                                },
                                                "requirements": {
                                                    "type": "array",
                                                    "items": {}
                                                },
                                                "slug": {
                                                    "type": "string"
                                                },
                                                "max_select_quantity": {
                                                    "type": "integer"
                                                },
                                                "canonical_url": {
                                                    "type": "string"
                                                },
                                                "vat_info": {
                                                    "type": "null"
                                                },
                                                "bmpl_info": {
                                                    "type": "object"
                                                },
                                                "max_per_order": {
                                                    "type": "null"
                                                },
                                                "ads_meta": {
                                                    "type": "null"
                                                },
                                                "with_options": {
                                                    "type": "boolean"
                                                }
                                            },
                                            "required": [
                                                "id",
                                                "sku",
                                                "retailer_sku",
                                                "available",
                                                "legacy_offer_id",
                                                "name",
                                                "price",
                                                "original_price",
                                                "discount",
                                                "human_volume",
                                                "volume",
                                                "volume_type",
                                                "items_per_pack",
                                                "discount_ends_at",
                                                "price_type",
                                                "grams_per_unit",
                                                "unit_price",
                                                "original_unit_price",
                                                "promo_badge_ids",
                                                "score",
                                                "labels",
                                                "image_urls",
                                                "requirements",
                                                "slug",
                                                "max_select_quantity",
                                                "canonical_url",
                                                "vat_info",
                                                "bmpl_info",
                                                "max_per_order",
                                                "ads_meta",
                                                "with_options"
                                            ]
                                        }
                                    ]
                                }
                            },
                            "required": [
                                "completion"
                            ]
                        }
                    },
                    "required": [
                        "type",
                        "product"
                    ]
                }
            ]
        }
    },
    "required": [
        "suggests"
    ]
}
