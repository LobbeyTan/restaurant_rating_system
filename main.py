from src.inference_system import RestaurantRatingSystem

model = RestaurantRatingSystem()

score = model.predict(
    sentiment=5,
    service=5,
    food_quality=5,
    price=35,
    environment=50,
)

print(score)

model.visualize()
