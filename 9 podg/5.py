def dd():
    if d1.get("фрукт") != "яблоко":
        d1["фрукт"] = "яблоко"
    print("Измененный словарь:", d1)

d1 = {"овощ": "морковь", "напиток": "вода"}
dd()
