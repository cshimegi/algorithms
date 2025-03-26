# Questions to ask:
# 1. What is the time complexity? O(R + I), R = number of recipes, I = number of ingredients
# 2. What is the space complexity? O(R + I)
class Solution:
    def findAllRecipes(self, recipes: list[str], ingredients: list[list[str]], supplies: list[str]) -> list[str]:
        from collections import deque

        recipe_ingredients = {recipe: ingredients[i] for i, recipe in enumerate(recipes)}
        supply_set = set(supplies)
        recipe_degrees = {recipe: 0 for recipe in recipes}
        recipe_graph = {recipe: [] for recipe in recipes}

        # Build graph and calculate in-degrees
        for recipe, ingredients_list in recipe_ingredients.items():
            for ingredient in ingredients_list:
                if ingredient in recipe_ingredients:
                    recipe_graph[ingredient].append(recipe)
                    recipe_degrees[recipe] += 1

        queue = deque([recipe for recipe, degree in recipe_degrees.items() if degree == 0])
        ans = []
        while queue:
            recipe = queue.popleft()
            if all(ingredient in supply_set or ingredient in ans for ingredient in recipe_ingredients[recipe]):
                ans.append(recipe)
                for neighbor in recipe_graph[recipe]:
                    recipe_degrees[neighbor] -= 1
                    if recipe_degrees[neighbor] == 0:
                        queue.append(neighbor)
        return ans


# Problem 2115
# Link: https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/description/
if __name__ == '__main__':
    s = Solution()
    cases = [
        (
            ["bread"],
            [["yeast", "flour"]],
            ["yeast", "flour", "corn"],
            ["bread"],
        ),
        (
            ["bread", "sandwich"],
            [["yeast", "flour"], ["bread", "meat"]],
            ["yeast", "flour", "meat"],
            ["bread", "sandwich"],
        ),
        (
            ["bread", "sandwich", "burger"],
            [["yeast", "flour"], ["bread", "meat"], ["sandwich", "meat", "bread"]],
            ["yeast", "flour", "meat"],
            ["bread", "sandwich", "burger"],
        )
    ]
    for recipes, ingredients, supplies, expected in cases:
        assert s.findAllRecipes(recipes, ingredients, supplies) == expected
