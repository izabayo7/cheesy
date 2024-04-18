# menu.py

class Menu:
    def __init__(self):
        self.menu_items = {
           "Cold Starters": [
                {"name": "Chief Classic Salad", "description": "Composition of Lettuce, onion, tomato, carrots, cucumber, Ham, croutons, avocado, egg, black olive, cheese, dressed with vinaigrette", "price": "7000 Fr"},
                {"name": "Classic Ceasar Salad", "description": "An eye appeal Crips bacon, croutons, Lettuce, tomato, onion, parmessa cheese, Egg, Green pepper, Dressed with thousand hills dressing", "price": "7000 Fr"},
                {"name": "Avocado Salad", "description": "A large portion of fanned avocado, tomato, bedded on crispy lettuce and splashed with French dressing sauce", "price": "5000 Fr"},
                {"name": "Californian Salad", "description": "Assorted timbale of fresh lettuce, carrots, onion, tomato avocado, egg, feta cheese, peanuts, tuna fish, dressed with Americano sauce", "price": "6500 Fr"},
                {"name": "Nicoise Salad", "description": "Nice for Rwandan potato, tomato, lettuce, egg, green beans, tuna fish, anchovy, mayonnaise", "price": "6500 Fr"},
                {"name": "Chicken Noodles Salad", "description": "Composed with noodles, chicken, peanuts, egg, tomato, finished with dressing sauce", "price": "8500 Fr"},
                {"name": "Greek Salad", "description": "Mixed with tomato, green pepper, onion, black olives, feta cheese, lettuce, cucumber, dressed with French vinaigrette", "price": "7500 Fr"},
                {"name": "Fresh Italiano Salad", "description": "Composed with penne pasta, sliced tomato, onion, sausage, fresh basil, finished with balsamic dressing sauce", "price": "7500 Fr"},
                {"name": "Beef’s Lettuce Avocado And Tomato Salad", "description": "Composed with Beef, lettuce, Parsley, Fresh basil, Olive oil, red onion, garlic, Balsamic vinegar", "price": "8500 Fr"},
                {"name": "Stuffed Avocado", "description": "A large avocado put on tomato, shrimps, egg, lemon juice, mayonnaise", "price": "7500 Fr"}
            ],
            "Hot Starters": [
                {"name": "Creamed Of Mushroom Soup", "description": "Puree of mushrooms, onion, Olive oil", "price": "6500 Fr"},
                {"name": "Fresh Vegetable Soup", "description": "Made from Rwandan vegetables purred and seasoned with cream", "price": "4500 Fr"},
                {"name": "Vegans Soup", "description": "An eye appeal of vegetarian soup contain without meat and any other animal products", "price": "8000 Fr"},
                {"name": "Chicken Soup", "description": "Thickened cream of chicken soup selected onion, chicken, green pepper, carrots, celery", "price": "8000 Fr"},
                {"name": "Chicken Noodle Soup", "description": "Properly selected fresh onion, celery, leeks, carrots, cream", "price": "8000 Fr"},
                {"name": "Fish Soup", "description": "Dices of fish, carrot, celery, onion, leek added with cream", "price": "8500 Fr"},
                {"name": "Cream Of Tomato Soup", "description": "Properly selected tomato, potato, leeks, onion blended and seasoned to taste garnished with bread croutons", "price": "4500 Fr"},
                {"name": "Chicken Consomme Celestin", "description": "Clear chicken consommé strained minced chicken, carrots, egg, leeks, onion, celery, bay leaf Flavored and garnished with chapatti", "price": "8000 Fr"},
                {"name": "Oxtail Beef Consomme Soup", "description": "Clear oxtail beef, egg, leeks, onion, bay leaf, thyme, carrots flavored and garnished with beef brunoises", "price": "8000 Fr"},
                {"name": "Tom Yunggoong Soup", "description": "An eye appeal of Asian soup selected clear leeks, carrots, zucchini, onion, shrimps", "price": "8000 Fr"},
                {"name": "Coconut Roasted Eggplant Soup", "description": "Dices of finely grated and squeezed coconuts added with roasted eggplant, Irish potato strained seasoned with salt and pepper", "price": "8000 Fr"}
            ],
            "Snacks": [
                {"name": "Cheesy Mushroom Style", "description": "Baked spinach, mushrooms, Garlic, cheese", "price": "5000 Fr"},
                {"name": "Cheesy Club Sandwich", "description": "A selection of chicken, fresh lettuce, cheese, fried egg, tomato, served with Toasted bread, portion of chips and salad", "price": "10000 Fr"},
                {"name": "Beef Samosas", "description": "3 Pairs of meat served with chips and salad", "price": "8500 Fr"},
                {"name": "Vegetable Samosas", "description": "3 Pairs of vegetable samosas served with chips and salad", "price": "4000 Fr"},
                {"name": "Chicken Mayonnaise Sandwich", "description": "Served with chips and salad", "price": "10000 Fr"},
                {"name": "Plate of cheese and sausage", "description": "Assortment of cheese and sausage", "price": "8500 Fr"},
                {"name": "Plate Of Cheese", "description": "Assortment of cheese", "price": "7000 Fr"},
                {"name": "Cheese Beef Burger", "description": "Beef burger with cheese, served with chips and salad", "price": "9000 Fr"},
                {"name": "Chicken Burger", "description": "Chicken burger, served with chips and salad", "price": "9000 Fr"},
                {"name": "Beef Burger", "description": "Beef burger, served with chips and salad", "price": "8000 Fr"},
                {"name": "Chicken Pie", "description": "Chicken pie with salad and chips", "price": "12000 Fr"},
                {"name": "Fish Finger", "description": "Marinated and coated finger of fish deep fried, served with tartar sauce, salad and chips", "price": "12000 Fr"},
                {"name": "Meat Balls", "description": "Trio of meat balls sautéed in red sauce served with chips and salad", "price": "6000 Fr"},
                {"name": "Chicken Wings", "description": "Chicken wings marinated and deep-fried, served with chips and salad", "price": "6500 Fr"},
                {"name": "Special Omelet", "description": "Omelet with onion, beef or ham, tomato, chips, eggs", "price": "8000 Fr"},
                {"name": "Spanish Omelet", "description": "Omelet with eggs, onion, green pepper, mushroom, tomato", "price": "6000 Fr"},
                {"name": "Toasted Ham, Cheese Sandwich", "description": "Ham and cheese sandwich served with chips and salad", "price": "6500 Fr"},
                {"name": "Toasted Cheese Sandwich", "description": "Cheese sandwich served with chips and salad", "price": "9000 Fr"},
                {"name": "Plate Of Sausage", "description": "Assortment of sausages", "price": "10000 Fr"}
            ],
              "Beefs": [
                {"name": "Beef Steak", "description": "Pan-seared beef fillet with green pepper, red wine, cream sauce, served with vegetables, rice or chips", "price": "15500 Fr"},
                {"name": "Beef Mignon", "description": "Grilled beef fillet with onion, white wine served with chateau potatoes and vegetables", "price": "15500 Fr"},
                {"name": "T-Bone Steak", "description": "Char-grilled perfectly aged 250 grams prime T-bone steak, served with red wine dry pepper sauce, croquette potato and vegetables", "price": "16500 Fr"},
                {"name": "Five To Five Beef", "description": "Char-grilled beef tenderloin made to order, served with spiced butter sauce, straw potatoes, vegetables", "price": "15500 Fr"},
                {"name": "Beef Curry Sauce", "description": "Fried beef fillet with original Indian curry sauce, served with steamed rice, chapatti and vegetables", "price": "15500 Fr"},
                {"name": "Beef Stew", "description": "Cooked sliced beef in red sauce, served with rice, French fries and vegetables", "price": "15500 Fr"},
                {"name": "Tarragon Beef", "description": "Pan-seared beef fillet set on wilted spinach, shavings Zucchini, carrots, served with potato, rice and finished with a white wine tarragon sauce", "price": "15500 Fr"},
                {"name": "Sauté De Veau MARENGO", "description": "Sautéed veau of beef with carrots, leeks, tomato, salsa, white wine, brown roux served with rice and vegetables", "price": "15500 Fr"},
                {"name": "Swiss Steak", "description": "Pan-fried beef with garlic, celery, onion, mustard, tomato, salsa, paprika, oregano, mushroom, brown roux, pepper; served with broccoli vegetable and rice", "price": "15500 Fr"},
                {"name": "Beef Stroganoff", "description": "Cooked juliennes of beef sautéed with mushrooms, green pepper, onion finished with cream served with vegetables, rice", "price": "15500 Fr"},
                {"name": "Beef Escalope Cordon Blue", "description": "Roasted fillet with ham, cheese, bread crumbs, egg served with sauce of your choice, chips, vegetables", "price": "15500 Fr"},
                {"name": "Chang’s Mongolian Beef", "description": "Cooked panned sliced beef with garlic, ginger, cayenne pepper, julienne of carrots, leeks, onion, soy sauce, brown roux, white wine, served with rice and vegetables", "price": "15500 Fr"}
            ],
             "Chickens": [
                {"name": "Indian Princess Special Chicken", "description": "Spicy chicken kebabs, fresh chili, fish kernels served with rice, poppadum. A beautiful essence of the famous Kumar tandoori", "price": "16500 Fr"},
                {"name": "Bronze Chicken Breast", "description": "Supreme of chicken breast spiced cubes and sautéed with Paprika potato, rice, vegetables", "price": "14500 Fr"},
                {"name": "Five To Five Chicken", "description": "Char-grilled half chicken coupon marinated in fresh herbs and seasoning, served with fresh red sauce, maize posho, garlic, spinach", "price": "14500 Fr"},
                {"name": "Chicken Stroganoff", "description": "Pan-seared Juliennes of chicken sautéed with mushrooms, green pepper, onions, finished with cream; served with vegetables, rice or mashed potatoes", "price": "14500 Fr"},
                {"name": "KIEV Chicken", "description": "Roasted marinated chicken breast in garlic, soy sauce, egg, coated with bread crumbs; served with sauce of choice, vegetables, potato, rice", "price": "16500 Fr"},
                {"name": "Chicken Curry Sauce", "description": "Stewed chicken in oriental curry sauce served with rice, chips and vegetables", "price": "16500 Fr"},
                {"name": "Chicken Yassa Sauce", "description": "Slow-cooked chicken in onion, lemon juice, mustard, tomato paste, served with vegetables, steamed rice, parsley potatoes", "price": "16500 Fr"},
                {"name": "Chicken Tikka Masala", "description": "Cooked marinated cubes of chicken in chicken masala, ginger essence, onion, tomato paste; served with puréed carrots, steamed rice, chapatti. A beautiful taste of Indian", "price": "14500 Fr"}
            ],
               "Fish": [
                {"name": "Fish Fillet Meuniere Sauce", "description": "Pan-fried fillet of fish in lemon butter sauce, served with seasonal vegetables and parsley potatoes", "price": "16500 Fr"},
                {"name": "Chief’s Special Fish Fillet", "description": "Roasted fish fillet in mushroom sauce, topped with Tarragon, spinach accompanied by pita bread and Spanish potatoes", "price": "16000 Fr"},
                {"name": "Roasted Fish Curry", "description": "Roasted fish fillet in curry sauce served with chips, rice and vegetables", "price": "17000 Fr"},
                {"name": "Baked Captain Fish Fillet", "description": "Captain fish fillet in béchamel sauce set on wilted spinach, cheese accompanied with sautéed banana and vegetables", "price": "16000 Fr"},
                {"name": "Tilapia Papiotte Au Vin Blanc", "description": "Cooked captain with white wine served with parsley potatoes and vegetables", "price": "17000 Fr"},
                {"name": "Fish Fillet With Mushroom Sauce", "description": "Grilled fish fillet served with mushroom sauce, vegetables, Chinese rice or posho maize", "price": "16500 Fr"}
            ],
              "Pork": [
                {"name": "Boneless Pork Medallions", "description": "Boneless medallions of pork with onion, tomato ragout served with parsley potato, rice, and vegetables", "price": "16500 Fr"},
                {"name": "Pork Medallion", "description": "Fried pork medallion with onion and flambéed with calvados sauce, served with Spanish potatoes and vegetables", "price": "14500 Fr"},
                {"name": "Grilled Pork", "description": "Pork chops served with merchant wine sauce, Lyonnaise potatoes, and vegetables", "price": "16500 Fr"},
                {"name": "Baked Pork Chops or Cutlets", "description": "Served with warm fruit salsa, pont-neuf potato, and vegetables", "price": "16500 Fr"}
            ],
            "Pastas": [
                {"name": "Amatricana Pasta", "description": "A delicious blend of smoked bacon, onion, fresh tomato, basil, served with Penne pasta or fusil pasta", "price": "11500 Fr"},
                {"name": "Spaghetti Bolognaise", "description": "Spaghetti tossed in minced beef, tomato, onion, cheese", "price": "11500 Fr"},
                {"name": "Carbonara Pasta", "description": "Cooked pasta topped with mushrooms, ham, garlic, cheese", "price": "12000 Fr"},
                {"name": "Ravioli Bolognaise", "description": "Cooked stuffed minced meat in flour dough", "price": "12000 Fr"},
                {"name": "Pasta Fusil Pesto", "description": "A brilliant summer dish with fresh basil, walnuts, cheese, garlic, olive oil, mixed with Pasta fusil", "price": "9500 Fr"},
                {"name": "Alabiata Spaghetti", "description": "Made of fresh tomato, onion, basil, fresh chili, mixed with spaghetti", "price": "9500 Fr"}
            ],
            "Vegetarians": [
                {"name": "Vegetables Curry Sauce", "description": "Diced seasonal vegetables blended in original Indian curry sauce, served with chapatti or rice", "price": "8000 Fr"},
                {"name": "Cooked Mixed Vegetables With Red Sauce", "description": "Served with parsley potato or boiled banana", "price": "9500 Fr"},
                {"name": "Stuffed Vegetables In Chapatti", "description": "Chapatti stuffed with vegetables", "price": "9500 Fr"}
            ],
            "Health Food": [
                {"name": "Boiled Only Chicken Leg or Breast", "description": "Boiled chicken with leeks, fresh chili without oil", "price": "9500 Fr"},
                {"name": "Boiled Only Beef", "description": "Boiled beef with leeks, fresh chili without oil", "price": "9500 Fr"},
                {"name": "Boiled Chicken Leg", "description": "Boiled chicken leg with leeks, green banana, or potatoes without oil", "price": "11500 Fr"},
                {"name": "Boiled Whole Chicken", "description": "Boiled whole chicken with leeks, green banana without oil", "price": "22500 Fr"},
                {"name": "Boiled Half Chicken", "description": "Boiled half chicken with green banana, leeks, tomato without oil", "price": "15000 Fr"},
                {"name": "Boiled Goat Leg", "description": "Boiled goat leg with leeks, banana, tomato fresh without oil", "price": "15500 Fr"}
            ],
            "Pizza": [
                {"name": "Five To Five Special Pizza", "description": "Dough with sausage, garlic, onion, tomato, green pepper, ham, black olive, oregano, cheese, tomato sauce", "price": "11500 Fr"},
                {"name": "Chicken Pizza", "description": "Dough with chicken, onion, green pepper, garlic, tomato sauce, cheese", "price": "11500 Fr"},
                {"name": "Vegetarian Pizza", "description": "Original Napolitano with tomatoes, carrot, basil, green pepper, cheese, tomato sauce", "price": "9500 Fr"},
                {"name": "Altano Pizza", "description": "Dough with onion, black olives, tuna fish, cheese, tomato sauce", "price": "9500 Fr"},
                {"name": "Mexican Pizza", "description": "Dough with Bolognaise, sweet corn, fresh chili, cheese, tomato sauce", "price": "11500 Fr"},
                {"name": "Pizza Supreme Jaffle", "description": "Dough with garlic, red onion, capsicum, mushrooms, salami, basil, cheese, sesame", "price": "10500 Fr"}
            ],
            "Grilled": [
                {"name": "Simple Goat Brochette", "description": "Simple goat brochette", "price": "2000 Fr"},
                {"name": "Goat Brochette", "description": "Goat brochette with chips and salad", "price": "4500 Fr"},
                {"name": "Goat Zingalo Brochette", "description": "Goat zingalo brochette with chips and salad", "price": "5000 Fr"},
                {"name": "Simple Goat Zingalo Brochette", "description": "Simple goat zingalo brochette", "price": "2500 Fr"},
                {"name": "Goat Liver Brochette", "description": "Goat liver brochette with chips and salad", "price": "4500 Fr"},
                {"name": "Simple Goat Liver Brochette", "description": "Simple goat liver brochette", "price": "2000 Fr"},
                {"name": "Beef Brochette", "description": "Beef brochette with chips or banana and salad", "price": "6000 Fr"},
                {"name": "Chicken Brochette", "description": "Chicken brochette with accompaniment", "price": "5500 Fr"},
                {"name": "Simple Chicken Brochette", "description": "Simple chicken brochette", "price": "3000 Fr"},
                {"name": "Fish Brochette", "description": "Fish brochette with accompaniment", "price": "Not Available"},
                {"name": "Grilled Whole Chicken", "description": "Grilled whole chicken with accompaniment", "price": "15000 Fr"},
                {"name": "Half Chicken", "description": "Half chicken with accompaniment", "price": "10000 Fr"},
                {"name": "Grilled Only Chicken", "description": "Grilled only chicken without garnish", "price": "15000 Fr"},
                {"name": "Grilled Only Half Chicken", "description": "Grilled only half chicken", "price": "7500 Fr"},
                {"name": "Goat Leg Nyamachoma", "description": "Goat leg nyamachoma with accompaniment", "price": "20000 Fr"}
            ],
            "Desserts": [
                {"name": "Fresh Fruits Salad", "description": "Assortment of fresh fruits", "price": "6500 Fr"},
                {"name": "Assortment Fruits", "description": "Variety of assorted fruits", "price": "8500 Fr"},
                {"name": "Plain Pancakes", "description": "Plain pancakes", "price": "4000 Fr"},
                {"name": "Pancakes With Strawberry Jam", "description": "Pancakes with strawberry jam", "price": "5000 Fr"},
            ]

            
        }

    def get_menu_items(self):
        return self.menu_items
