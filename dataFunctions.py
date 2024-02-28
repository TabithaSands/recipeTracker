from allrecipes import AllRecipes

# Search:
# search_string = "pork curry"  # Query
search_list = ["japanese curry", "minestrone", "paneer"]


def find_recipe(search_item):
    print(f"========== Searching for {search_item} ==========")
    query_result = AllRecipes.search(search_item)

    # Get:
    main_recipe_url = query_result[0]['url']
    detailed_recipe = AllRecipes.get(main_recipe_url)

    # Display result:
    print(f"{detailed_recipe['name']}")

    if detailed_recipe['nb_servings']:
        print(f"For {detailed_recipe['nb_servings']} servings")

    for ingredient in detailed_recipe['ingredients']:  # List of ingredients
        print(f"- {ingredient}")

    for step in detailed_recipe['steps']:  # List of cooking steps
        print(f"{step}")


for item in search_list:
    find_recipe(item)