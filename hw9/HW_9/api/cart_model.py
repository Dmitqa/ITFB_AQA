from pydantic import BaseModel


class ProductProperties(BaseModel):
    cart_id: str | int
    model: str
    name: str
    option: list | None
    price: str
    product_id: str | int
    quantity: str
    reward: str | int | None
    shipping: str
    stock: bool
    total: str


class TotalsProperties(BaseModel):
    text: str
    title: str


class VoucherProperties(BaseModel):
    code: int | str
    description: str
    from_name: str
    from_email: str
    to_name: str
    to_email: str
    voucher_theme_id: str
    message: str
    price: str
    amount: int | float | str


class CartModel(BaseModel):
    products: list[ProductProperties]
    totals: list[TotalsProperties]
    vouchers: list[VoucherProperties] | list
