import json

def load_inventory():
    try:
        with open("inventory.json", "r", encoding="utf-8") as file:
            items = json.load(file)
            print("--- รายการสินค้าในคลัง ---")
            for item in items:
                print(f"รหัส: {item['id']} | ชื่อสินค้า: {item['name']} | จำนวน: {item['quantity']} ชิ้น")
    except FileNotFoundError:
        print("ไม่พบไฟล์ inventory.json")

if __name__ == "__main__":
    load_inventory()