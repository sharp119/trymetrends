CREATE TABLE sellers (
    wallet_address VARCHAR(255) PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    shop_address TEXT NOT NULL,
    shop_name VARCHAR(255) NOT NULL
);


CREATE TABLE users (
    wallet_address VARCHAR(255) PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    reward_points INT DEFAULT 0
);


CREATE TABLE products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    image_location VARCHAR(255) NOT NULL,
    price DECIMAL(19, 9) NOT NULL,
    seller_wallet_address VARCHAR(255),
    description TEXT,
    FOREIGN KEY (seller_wallet_address) REFERENCES sellers(wallet_address)
);


CREATE TABLE purchases (
    purchase_id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT,
    user_wallet_address VARCHAR(255),
    unique_code VARCHAR(255) NOT NULL,
    FOREIGN KEY (product_id) REFERENCES products(product_id),
    FOREIGN KEY (user_wallet_address) REFERENCES users(wallet_address)
);

CREATE TABLE referral_codes (
    code_id INT AUTO_INCREMENT PRIMARY KEY,
    referral_code VARCHAR(255) NOT NULL UNIQUE,
    user_wallet_address VARCHAR(255),
    FOREIGN KEY (user_wallet_address) REFERENCES users(wallet_address)
);


CREATE TABLE virtual_tryon (
    tryon_id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT,
    user_wallet_address VARCHAR(255),
    processed_image_location VARCHAR(255) NOT NULL,
    FOREIGN KEY (product_id) REFERENCES products(product_id),
    FOREIGN KEY (user_wallet_address) REFERENCES users(wallet_address)
);
