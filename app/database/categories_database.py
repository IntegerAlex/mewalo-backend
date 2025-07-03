from app.config import db

class CategoriesDatabase:
    def get_categories(self) -> dict:
        """
        Get aggregated data of categories and their subcategories.
        :return: Dictionary of categories with their subcategories and images.
        """
        pipeline = [
            {
                "$group": {
                    "_id": "$category",
                    "subcategories": { "$addToSet": "$subcategory" },
                    "category_image": { "$first": "$category_image" }
                }
            },
            {
                "$project": {
                    "_id": 0,
                    "category": "$_id",
                    "subcategories": 1,
                    "category_image": 1
                }
            }
        ]
        
        result = db.products.aggregate(pipeline)
        
        aggregated_data = {}
        for item in result:
            category_name = item["category"]
            subcategories_list = item["subcategories"]
            category_image = item.get("category_image", None)
            aggregated_data[category_name] = {
                "subcategories": subcategories_list,
                "category_image": category_image
            }
            
        return aggregated_data
    
    def add_category(self, category_name: str, category_image: str) -> dict:
        """
        Add a new category.
        :param category_name: Name of the category to add.
        :return: Dictionary of the added category.
        """
        try:
            return db.products.insert_one({"category": category_name, "category_image": category_image})
        except Exception as e:
            print(f"Error adding category: {e}")