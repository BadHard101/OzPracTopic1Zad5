# task_A542
# Создать список (супермаркет), состоящий из словарей (товары). Словари должны содержать как минимум 5 полей
# (например, номер, наименование, отдел продажи, ...). В список добавить хотя бы 10 словарей.
# Конструкция вида:
# market = [{"id":123456, "product":"coca-cola 0.5", "department": "drinks", ...} , {...}, {...}, ...].
# Реализовать функции:
# – вывода информации о всех товарах;
# – вывода информации о товаре по введенному с клавиатуры номеру;
# – вывода количества товаров, продающихся в определенном отделе;
# – обновлении всей информации о товаре по введенному номеру;
# – удалении товара по номеру.
# Провести тестирование функций.

def print_prod_info(elem):
    print(
        "id:", "%-4d" % (elem.get("id")),
        "product:", "%-14s" % (elem.get("product")),
        "department:","%-10s" % (elem.get("department")),
        "sale(%):","%-6d" % (elem.get("sale%")),
        "license:", elem.get("license"),
        )

def print_all_prods_info(market):
    print("All found products:")
    for elem in market:
        print_prod_info(elem)
    print()

def update_info_by_id(market):
    print("Enter the ID of the product you want to update information about: ", end='')
    whats_id = int(input())
    for elem in market:
        if elem.get("id") == whats_id:
            print("Enter new name of product (was ", elem.get("product"), "): ", sep='', end='')
            elem["product"] = str(input())
            print("Enter new department of the product (was ", elem.get("department"), "): ", sep='', end='')
            elem["department"] = str(input())
            print("Enter new sale of the product (was ", elem.get("sale%"), "%): ", sep='', end='')
            elem["sale%"] = int(input())
            print("Is there a license for this product? (was ", elem.get("license"), "): ", sep='', end='')
            gotten_license = input()
            if gotten_license == "True":
                elem["license"] = True
            if gotten_license == "False":
                elem["license"] = False
            print()
            return
    print("There's no product with this id.\n")

def find_by_id(market):
    print("Enter the ID of the product you want to get information about: ", end='')
    whats_id = int(input())
    for elem in market:
        if elem.get("id")==whats_id:
            print_prod_info(elem)
            return
    print("There's no product with this id.\n")

def num_of_prods_by_department(market):
    print("Enter the DEPARTMENT, whose number of products you want to get: ", end='')
    whats_depart = str(input())
    num_of_prods=0
    for elem in market:
        if elem.get("department")==whats_depart:
            num_of_prods+=1
    print("Number of",whats_depart,"products is",num_of_prods,"\n")

def delete_product_by_id(market):
    print("Enter the ID of the product you want to delete from database: ", end='')
    whats_id = int(input())
    for elem in market:
        if elem.get("id") == whats_id:
            market.remove(elem)
            return
    print("There's no product with this id.\n")

market=[
    {"id":0, "product":"coca-cola", "department": "drinks", "sale%":0, "license": True},
    {"id":1, "product":"pepsi", "department": "drinks", "sale%":10, "license": True},
    {"id":2, "product":"merinda", "department": "drinks", "sale%":20, "license": True},
    {"id":3, "product":"croissants", "department": "bakery", "sale%":0, "license": False},
    {"id":4, "product":"bread", "department": "bakery", "sale%":0, "license": False}
    ]

menu=0
while menu!=1:
    print("Select what you want to do:\n"
          "1 - Get information about all products in the database\n"
          "2 - Get information about product by it's ID\n"
          "3 - Get the number of products in a specific department\n"
          "4 - Update information about specific product\n"
          "5 - Delete all information about product\n"
          "Enter your option: ",
          sep='', end='')
    flag=str(input())
    print()
    match flag:
        case "1":
            print_all_prods_info(market)
        case "2":
            find_by_id(market)
        case "3":
            num_of_prods_by_department(market)
        case "4":
            update_info_by_id(market)
        case "5":
            delete_product_by_id(market)