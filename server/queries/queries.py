# Define the SQL insert statements for each table

INSERT_QUERIES = {
    "sellers": """
        INSERT INTO sellers (wallet_address, name, shop_address, shop_name)
        VALUES (%s, %s, %s, %s)
    """,

    "users": """
        INSERT INTO users (wallet_address, name, reward_points)
        VALUES (%s, %s, %s)
    """,

    "products": """
        INSERT INTO products (name, image_location, price, seller_wallet_address, description)
        VALUES (%s, %s, %s, %s, %s)
    """,

    "purchases": """
        INSERT INTO purchases (product_id, user_wallet_address, unique_code)
        VALUES (%s, %s, %s)
    """,

    "referral_codes": """
        INSERT INTO referral_codes (referral_code, user_wallet_address)
        VALUES (%s, %s)
    """,

    "virtual_tryon": """
        INSERT INTO virtual_tryon (product_id, user_wallet_address, processed_image_location)
        VALUES (%s, %s, %s)
    """
}

