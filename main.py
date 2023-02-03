print("PhotoCode Invalidation Builder")
print("      ")
print("    .")
print("   ...")
print("  .....")
print(" .......")
print("......... MERRY CHRISTMAS")
print("    Π")
print("      ")

photoCode = input("What is the photo code?: ")
print("      ")

chooseSizes = input("What size do you want? Choose between 2,3,4,5,6,7,1F,2F or all! ")
sizes = ["2", "3", "4", "5", "6", "7", "1F", "2F"]

if chooseSizes == "all":
  sizes = sizes
else:
  sizes = [chooseSizes]

for size in sizes:
  print("/verybig/" + photoCode + "@" + size + ".JPG")
  print("/verybig/" + photoCode + "@" + size + ".jpg")
  print("/small/" + photoCode + "@" + size + ".JPG")
  print("/small/" + photoCode + "@" + size + ".jpg")