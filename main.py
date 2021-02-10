#   Oyetunde Oyewo
#   1881782


lemon_juice = float(input("Enter amount of lemon juice (in cups):\n"))
water = float(input("Enter amount of water (in cups):\n"))
agave_nectar = float(input("Enter amount of agave nectar (in cups):\n"))
servings = float(input("How many servings does this make?\n"))
print()
print("Lemonade ingredients - yields {:.2f}".format(servings), "servings")
print("{:.2f}".format(lemon_juice), "cup(s) lemon juice")
print("{:.2f}".format(water), "cup(s) water")
print("{:.2f}".format(agave_nectar), "cup(s) agave nectar")
print()

lemon_juice_per_serving = lemon_juice / servings
water_per_serving = water / servings
agave_nectar_per_serving = agave_nectar / servings

servings_wanted = float(input("How many servings would you like to make?\n"))
print()
print("Lemonade ingredients - yields {:.2f}".format(servings_wanted), "servings")
print("{:.2f}".format(lemon_juice_per_serving * servings_wanted), "cup(s) lemon juice")
print("{:.2f}".format(water_per_serving * servings_wanted), "cup(s) water")
print("{:.2f}".format(agave_nectar_per_serving * servings_wanted), "cup(s) agave nectar")

lemon_juice_gallon = (lemon_juice_per_serving * servings_wanted) / 16
water_gallon = (water_per_serving * servings_wanted) / 16
agave_nectar_gallon = (agave_nectar_per_serving * servings_wanted) / 16
print()
print("Lemonade ingredients - yields {:.2f}".format(servings_wanted), "servings")
print("{:.2f}".format(lemon_juice_gallon), "gallon(s) lemon juice")
print("{:.2f}".format(water_gallon), "gallon(s) water")
print("{:.2f}".format(agave_nectar_gallon), "gallon(s) agave nectar")
