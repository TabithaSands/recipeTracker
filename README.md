## Recipies Tracker App
![recipesTrackerApp.png](assets%2FrecipesTrackerApp.png)
#### These libraries were used for creating a web-app to search for recipes based on keywords, retrieve list of matching recipes and select through recipes to display recipe details like recipe image, ingredient list, and step by step instructions.
- python-allrecipes - retrieve recipe details from allrecipe API
- urllib3 - for requests
- uvicorn - for serving the webapp
- beautifulsoup4 - for webscraping
- fastapi - for creating API endpoint/routes for the application
- Jinja2 - for customizing the page layout

## Dash App
#### These libraries were used to create different plots provided by plotly and dash using world population data over time. 
![dash.png](assets%2Fdash.png)
- dash - set up dash callbacks for displaying dash components and graphs
- pandas - to create a dataframe from a CSV file (population data) and pull continent, country, population, and year data to feed to the plotly graphs
- plotly - to create line, bar, and sunburst graphs and display via dash components
