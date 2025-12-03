students = ["ເພັດສະຫວັນ", "ແມັກ", "ບີ", "ຫວິດ", "ຫລາ"]

print("ເລີ່ມການກວດສອບລາຍຊື່")

for std in students:
    if std == "ແມັກ":
        continue 
    if std == "Somchai":
        print(f">> ພົບເປົ້າໝາຍແລ້ວ ຢຸດການເຮັດວຽກ (Break): {std}")
        break 
    print("ຊື່: " + std)