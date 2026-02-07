// script.js
let cart = [];


function addToCart(id, name, price) {
    const existingItem = cart.find(item => item.id === id);
    if (existingItem) {
        existingItem.qty++;
    } else {
        cart.push({ id, name, price, qty: 1 });
    }
    updateCart();
}

function updateCart() {
    const cartList = document.getElementById('cart');
    const totalSpan = document.getElementById('total');
    const orderData = document.getElementById('order_data');

    cartList.innerHTML = '';
    let total = 0;

    cart.forEach(item => {
        const li = document.createElement('li');
        li.textContent = `${item.name} x ${item.qty} - $${item.price * item.qty}`;
        cartList.appendChild(li);
        total += item.price * item.qty;
    });

    totalSpan.textContent = total.toFixed(2);
    orderData.value = JSON.stringify(cart);
}

