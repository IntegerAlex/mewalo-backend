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
        
    def add_category(self, category_name: str, category_image: str) -> dict:
        """
        Add a new category.
        :param category_name: Name of the category to add.
        :return: Dictionary of the added category.
        """
        try:
            return CategoriesDatabase().add_category(category_name, category_image)
        except Exception as e:
            print(f"Error adding category: {e}")