from fastapi import FastAPI, Form, Request
from allrecipes import AllRecipes
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory='templates/')
g_search_string = ""
g_recipe_details = {}


def find_recipe(search_item, recipe_url):
    query_result = AllRecipes.search(search_item)
    if recipe_url:
        single_result = AllRecipes.get(recipe_url)
        return query_result, single_result
    else:
        return query_result


@app.get("/form")
def form_post(request: Request):
    if request.query_params:
        search_item = g_search_string
        result, recipe_details = find_recipe(search_item, request.query_params["url"])
        r_url = recipe_details["url"]
        try:
            if r_url.rsplit('/')[-1] != '':
                recipe_name = r_url.rsplit('/')[-1]
                recipe_name = recipe_name.capitalize().split('-')
            else:
                recipe_name = r_url.rsplit('/')[-2]
                recipe_name = recipe_name.capitalize().split('-')
        except Exception as e:
            recipe_name = ''
        recipe_name = ' '.join(recipe_name)
        print(f"Recipe name: {recipe_name}")
        recipe_details["name"] = recipe_name
        return templates.TemplateResponse('form.html', context={'request': request, 'result': result, 'recipe_details': recipe_details})
    else:
        return templates.TemplateResponse('form.html', context={'request': request, 'result': "Search a recipe", 'recipe_details': g_recipe_details})


@app.post("/form")
def form_post(request: Request, search_item: str = Form(...)):
    recipe_url = ''
    global g_search_string
    g_search_string = search_item
    result = find_recipe(g_search_string, recipe_url)
    return templates.TemplateResponse('form.html', context={'request': request, 'result': result, 'recipe_details': g_recipe_details})