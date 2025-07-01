from app.database.categories_database import CategoriesDatabase

class CategoriesService:
    def get_aggregated_categories(self) -> dict:
        """
        Get aggregated categories and subcategories.
        :return: Dictionary of categories with their subcategories.
        """
        try:
            return CategoriesDatabase().get_categories()
        except Exception as e:
            print(f"Error fetching aggregated categories: {e}")
            return {} 