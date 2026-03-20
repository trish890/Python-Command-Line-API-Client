import sys
import requests
import json

URL = "http://127.0.0.1:8000"

def view():
    print("\n--- List of all orders ---")
    response = requests.get(f"{URL}/orders/")
    
    if response.status_code == 200:
        orders = response.json()
        for order in orders:
            print(f"ID: {order['id']} | Name: {order['customer_name']} | Type: {order['paper_type']} | Pages: {order['pages']} | Status: {order['status']}")
    else:
        print(f"Fetch Error: {response.status_code}")

def search(args):
    if len(args) < 2:
        print("Usage: python client.py search <order_id>")
        return

    try:
        order_id = int(args[1])
    except ValueError:
        print("Invalid ID: Must be a number")
        return 
    
    response = requests.get(f"{URL}/orders/{order_id}")

    if response.status_code == 200:
        order = response.json()
        print(f"\nOrder Found:")
        print(f"Name: {order['customer_name']} | Type: {order['paper_type']} | Pages: {order['pages']} | Cost: ${order['total_cost']}")
    else:
        print("Order not found")

def order(args):
    if len(args) < 5:
        print("Usage: python client.py order <name> <email> <pages> <paper_type>")
        print("Paper types: black_white, colored, photo")
        return

    data = {
        "customer_name": args[1],
        "customer_email": args[2],
        "pages": int(args[3]),
        "paper_type": args[4],
        "notes": "Ordered via CLI"
    }

    print(f"Sending data: {data}")
    response = requests.post(f"{URL}/orders/", json=data)

    if response.status_code == 200:
        result = response.json()
        print(f"✅ Order placed! ID: {result['id']} | Total Cost: ${result['total_cost']}")
    else:
        print(f"❌ Error: {response.json().get('detail', 'Unknown error')}")

def stats():
    """Added this so you can show your Admin stats in the demo too!"""
    response = requests.get(f"{URL}/admin/stats")
    if response.status_code == 200:
        print("\n--- Shop Statistics ---")
        print(json.dumps(response.json(), indent=2))

def main():
    if len(sys.argv) < 2:
        print("Commands: view, search, order, stats")
        return

    cmnd = sys.argv[1]
    
    if cmnd == "order":
        order(sys.argv[1:])
    elif cmnd == "search":
        search(sys.argv[1:])
    elif cmnd == "view":
        view()
    elif cmnd == "stats":
        stats()
    else:
        print(f"Unknown command: {cmnd}")

if __name__ == "__main__":
    main()