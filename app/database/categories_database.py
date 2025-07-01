from app.config import db

class CategoriesDatabase:
    def get_categories(self) -> dict:
        """
        Get aggregated data of categories and their subcategories.
        :return: Dictionary of categories with their subcategories.
        """
        pipeline = [
            {
                "$group": {
                    "_id": "$category",
                    "subcategories": { "$addToSet": "$subcategory" }
                }
            },
            {
                "$project": {
                    "_id": 0,
                    "category": "$_id",
                    "subcategories": 1
                }
            }
        ]
        
        result = db.products.aggregate(pipeline)
        
        aggregated_data = {}
        for item in result:
            category_name = item["category"]
            subcategories_list = item["subcategories"]
            aggregated_data[category_name] = subcategories_list
            
        return aggregated_data