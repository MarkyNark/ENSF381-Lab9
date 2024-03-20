import requests
import json

def fetch_product_data ( url ) :
    try :
        response = requests . get ( url )
         # Raises an error for bad responses
        response . raise_for_status ()
        # The JSON structure includes a ' products ' key
        return response . json () [ ' products ']
    except requests . exceptions . RequestException as e :
        print ( f " Error fetching data : { e }")
        return None
    
def list_all_products ( products ) :
    for product in products :
        print ( f " { product [ ' name ' ]} ( { product [ ' price ' ]} )")
        
def search_product(product, name):
    for p in product:
        if p['name'] == name:
            return p
    return None

def main():
    products_url = "https://dummyjson.com/products"
    products = fetch_product_data(products_url)
    
    if products:
        while True:
            choice = input("Choose an option: \n1. List all products\n2. Search for a product\n3. Exit\n")
            if choice == "1":
                list_all_products(products)
            elif choice == "2":
                product_name = input("Enter the product name: ")
                product = search_product(products, product_name)
                if product:
                    print(f"Product found: {product['name']} ({product['price']})")
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