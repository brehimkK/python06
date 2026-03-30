def validate_ingredients(ingredients: str) -> str:
    valid_keywords = ["fire", "water", "earth",  "air"]

    for i in valid_keywords:
        if i in ingredients:
            return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"