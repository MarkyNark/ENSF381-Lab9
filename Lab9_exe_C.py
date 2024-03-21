import requests
import json

def fetch_product_data (url):
    try :
        response = requests.get (url)
         # Raises an error for bad responses
        response.raise_for_status()
        # The JSON structure includes a ' products ' key
        return response.json() ['products']
    except requests.exceptions.RequestException as e:
        print (f"Error fetching data: {e}")
        return None
    
def list_all_products (products):
    
    """The list_all_products function takes a list of products and prints the title of each product."""

    for product in products:
        print (product['title'])
        
def search_product(product, name):
    
    """The search_product function takes a list of products and a name. 
    It iterates over the list of products and checks if the product title matches the given name. 
    If a match is found, it prints the product details in JSON format and returns the product. If no match is found, it returns None."""

    for p in product:
        if p['title'] == name:
            print(json.dumps(p, indent=4))
            return p
    return None

def main():
    
    """The main function sets the products URL, fetches the product data, 
    and provides a menu for the user to list all products or search for a specific product."""
    
    products_url = "https://dummyjson.com/products"
    products = fetch_product_data(products_url)
    
    if products:
        while True:
            choice = input("Choose an option: \n1. List all products\n2. Search for a product\n3. Exit\n> ")
            if choice == "1":
                list_all_products(products)
            elif choice == "2":
                product_name = input("Enter the product name: ")
                product = search_product(products, product_name)
                if product:
                    print(f"Product found: {product['title']}")
                else:
                    print("Product not found")
            elif choice == "3":
                break
            else:
                print("Invalid choice. Please try again.")
    else:
        print("Failed to fetch product data.")
        
if __name__ == "__main__":
    main()
