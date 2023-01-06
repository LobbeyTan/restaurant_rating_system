import skfuzzy as fuzz

from src import Variable, Term, sentiment, service, food_quality, price, environmnet, rating

MF = {
    # Sentiment (likert-scale)
    Variable.SENTIMENT: {
        Term.BAD: fuzz.trapmf(sentiment, [-1, 0, 3, 5]),
        Term.NORMAL: fuzz.trapmf(sentiment, [3, 4, 6, 7]),
        Term.GOOD: fuzz.trapmf(sentiment, [5, 7, 10, 11]),
    },
    # Service (likert-scale)
    Variable.SERVICE: {
        Term.BAD: fuzz.trapmf(service, [-1, 0, 3, 5]),
        Term.NORMAL: fuzz.trapmf(service, [3, 4, 6, 7]),
        Term.GOOD: fuzz.trapmf(service, [5, 7, 10, 11]),
    },
    # Food Quality (likert-scale)
    Variable.FOOD_QUALITY: {
        Term.BAD: fuzz.trimf(food_quality, [-1, 0, 5]),
        Term.NORMAL: fuzz.trapmf(food_quality, [3, 4, 6, 7]),
        Term.GOOD: fuzz.trimf(food_quality, [5, 10, 11]),
    },
    # Price in Ringgit Malaysia (RM)
    Variable.PRICE: {
        Term.LOW: fuzz.gaussmf(price, 5, 10),
        Term.NORMAL: fuzz.gaussmf(price, 32.5, 10),
        Term.HIGH: fuzz.gaussmf(price, 60, 10),
    },
    # Environment (likert-scale)
    Variable.ENVIRONMENT: {
        Term.BAD: fuzz.zmf(environmnet, 10, 40),
        Term.NORMAL: fuzz.gaussmf(environmnet, 50, 20),
        Term.GOOD: fuzz.smf(environmnet, 70, 100),
    },
    # Restaurant Rating (likert-scale)
    Variable.RATING: {
        Term.BAD: fuzz.trapmf(rating, [-10, 0, 30, 50]),
        Term.NORMAL: fuzz.trapmf(rating, [30, 40, 60, 70]),
        Term.GOOD: fuzz.trapmf(rating, [50, 70, 100, 110]),
    },
}
