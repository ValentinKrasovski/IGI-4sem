// Базовый класс Product
function Product(name, price) {
    this.name = name;
    this.price = price;
}

// Функция для получения цены продукта
Product.prototype.getPrice = function () {
    return this.price;
};

// Функция для установки цены продукта
Product.prototype.setPrice = function (newPrice) {
    this.price = newPrice;
};

// Класс-наследник DeliverableProduct
function DeliverableProduct(name, price, deliveryTime) {
    Product.call(this, name, price);
    this.deliveryTime = deliveryTime;
}

// Наследование прототипа
DeliverableProduct.prototype = Object.create(Product.prototype);
DeliverableProduct.prototype.constructor = DeliverableProduct;


// Создание экземпляра DeliverableProduct
const product = new DeliverableProduct("Pancake", 100, "6 days");

console.log(`Product: ${product.name}`);
console.log(`Price: $${product.getPrice()}`);
console.log(`Delivery Time: ${product.deliveryTime}`);

///////////////////////////////////

// Базовый класс Product1
class Product1 {
    constructor(name, price) {
        this.name = name;
        this.price = price;
    }

    // Геттер для цены продукта
    get getPrice() {
        return this.price;
    }

    // Сеттер для цены продукта
    set setPrice(newPrice) {
        this.price = newPrice;
    }
}

// Класс-наследник DeliverableProduct1
class DeliverableProduct1 extends Product1 {
    constructor(name, price, deliveryTime) {
        super(name, price);
        this.deliveryTime = deliveryTime;
    }

    // Применяем декоратор к геттеру getPrice
//    @withPriceMultiplier
//    get getPrice() {
//        return this.price;
//    }
}

// Декоратор для умножения цены на коэффициент
function withPriceMultiplier(target, key, descriptor) {
    const originalMethod = descriptor.get;

    descriptor.get = function () {
        const originalPrice = originalMethod.call(this);
        const multiplier = 1.2; // Например, умножим на 1.2
        const modifiedPrice = originalPrice * multiplier;
        console.log(`Applying price multiplier. Original price: $${originalPrice}, Modified price: $${modifiedPrice}`);
        return modifiedPrice;
    };

    return descriptor;
}

// Создание экземпляра DeliverableProduct1
const product1 = new DeliverableProduct1("Pancake", 100, "6 days");

console.log(`Product: ${product1.name}`);
console.log(`Price: $${product1.getPrice}`);
console.log(`Delivery Time: ${product1.deliveryTime}`);
