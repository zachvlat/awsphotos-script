print("this is my aws-photo-app-lazy-invalidation-builder");

print("    .")
print("   ...")
print("  .....")
print(" .......")
print("......... MERRY CHRISTMAS")
print("    Π")
print("      ")

photoCode = input("What is the photo code?: ")
print("      ")

chooseSizes = input("What size do you want?: ")
if chooseSizes == "4" :
    print("/verybig/"+photoCode+"@"+chooseSizes+".JPG")
    print("/verybig/"+photoCode+"@"+chooseSizes+".jpg")
    print("/small/"+photoCode+"@"+chooseSizes+".JPG")
    print("/small/"+photoCode+"@"+chooseSizes+".jpg")
elif chooseSizes == "6":
    print("/verybig/"+photoCode+"@6.JPG")
    print("/verybig/"+photoCode+"@6.jpg")
    print("/small/"+photoCode+"@6.JPG")
    print("/small/"+photoCode+"@6.jpg")
elif chooseSizes == "5":
    print("/verybig/"+photoCode+"@5.JPG")
    print("/verybig/"+photoCode+"@5.jpg")
    print("/small/"+photoCode+"@5.JPG")
    print("/small/"+photoCode+"@5.jpg")
elif chooseSizes == "1F":
    print("/verybig/"+photoCode+"@1F.JPG")
    print("/verybig/"+photoCode+"@1F.jpg")
    print("/small/"+photoCode+"@1F.JPG")
    print("/small/"+photoCode+"@1F.jpg")
elif chooseSizes == "2F":
    print("/verybig/"+photoCode+"@2F.JPG")
    print("/verybig/"+photoCode+"@2F.jpg")
    print("/small/"+photoCode+"@2F.JPG")
    print("/small/"+photoCode+"@2F.jpg")
else:
    print("choose the right size please!")