erDiagram

  users ||--o{ carts : has
  users ||--o{ orders : places

  categories ||--o{ products : contains
  products ||--|| product_details : has
  products ||--o{ cart_items : includes
  products ||--o{ order_items : includes

  carts ||--o{ cart_items : holds
  orders ||--o{ order_items : contains

  users {
    int id PK
    varchar username
    text address
  }

  categories {
    int id PK
    varchar name
  }

  products {
    int id PK
    varchar name
    numeric price
    text image_url
    int category_id FK
  }

  product_details {
    int product_id PK, FK
    text description
  }

  carts {
    int id PK
    int user_id FK
  }

  cart_items {
    int id PK
    int cart_id FK
    int product_id FK
    int quantity
  }

  orders {
    int id PK
    int user_id FK
    numeric total_price
    text shipping_address
    timestamp created_at
  }

  order_items {
    int id PK
    int order_id FK
    int product_id FK
    int quantity
    numeric price
  }
