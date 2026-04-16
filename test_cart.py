from cart import ShoppingCart

def test_add_item_and_total():
    # Yeni sınıf yapısını kullanarak bir sepet oluşturuyoruz
    cart = ShoppingCart()
    cart.add_item("Laptop", 1000.0, 1)
    # Toplam tutarın doğruluğunu kontrol ediyoruz
    assert cart.get_total() == 1000.0

def test_discount_apply():
    cart = ShoppingCart()
    cart.add_item("Phone", 100.0, 1)
    # SAVE10 kodunu uyguluyoruz (%10 indirim)
    cart.apply_discount("SAVE10")
    # 100 - 10 = 90 olmalı
    assert cart.get_total() == 90.0

def test_item_count():
    cart = ShoppingCart()
    cart.add_item("Apple", 1.0, 5)
    cart.add_item("Banana", 2.0, 3)
    # Toplam ürün adedi 8 olmalı
    assert cart.get_item_count() == 8
