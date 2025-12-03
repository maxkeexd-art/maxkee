price_apple = 1000
price_banana = 2000

print("--- ຮ້ານຂາຍໝາກໄມ້ BorHu ---")
print("1. apple = 1000")
print("2. banana = 2000")

choice = input("ກະລຸນາເລືອກສິນຄ້າ (ກົດເລກ 1 ຫຼື 2): ")
price_to_pay = 0
if choice == "1":
    price_to_pay = price_apple
    print("ທ່ານເລືອກຊື້ Apple ລາຄາ 1000")
elif choice == "2":
    price_to_pay = price_banana
    print("ທ່ານເລືອກຊື້ Banana ລາຄາ 2000")
else:
    print("ທ່ານເລືອກບໍ່ຖືກຕ້ອງ")
    exit()
money_input = input("ກະລຸນາໃສ່ຈຳນວນເງິນທີ່ມີ: ")
money = int(money_input) 

if money < price_to_pay:
    need_more = price_to_pay - money
    print(f"ເງິນບໍ່ພໍ, ຕ້ອງເພີ່ມເງິນອີກ: {need_more}")

elif money > price_to_pay:
    change = money - price_to_pay
    print(f"ຊຳລະເງິນສຳເລັດ, ເງິນທອນຂອງທ່ານແມ່ນ:{change}")
else:
    print("ຊຳລະເງິນສຳເລັດ, ບໍ່ມີເງິນທອນ")
print("ຂອບໃຈ")