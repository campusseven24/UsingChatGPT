```mermaid
sequenceDiagram
    participant User
    participant ProductPage
    participant Cart
    participant Checkout
    participant OrderSystem

    User->>ProductPage: 상품 목록 조회
    ProductPage-->>User: 상품 목록 반환

    User->>ProductPage: 상품 선택
    ProductPage->>Cart: 장바구니에 상품 추가
    Cart-->>User: 장바구니에 추가 완료

    User->>Cart: 장바구니 보기
    Cart-->>User: 담긴 상품 목록 반환

    User->>Checkout: 구매하기 클릭
    Checkout->>OrderSystem: 주문 생성 요청
    OrderSystem-->>Checkout: 주문 번호 반환
    Checkout-->>User: 주문 완료 및 주문 번호 표시
```