# 1. taskınız ilk olaraq bir text faylı yaradıb içərisinə istədiyiniz bir cümlə yazırsınız 

# with open("oldfile.txt", mode="x" ,encoding="utf-8") as new:
#     new.write("Yeni text yaradib, icine cumle yazmaq...")
 

# 2. daha sonra həmin textin ilk sətrindəki  sözlərin bütün hərflərini böyük hərflərə çeviririk    
# with open("oldfile.txt", mode="r", encoding="utf-8") as up:
#     up_text = up.readline().upper()
#     print(up_text)


# 3. Ən sonda bu sözləri başqa  bir text faylı yaradıb onun içərisində yazırıq.
# with open("newfile.txt", mode="w", encoding="utf-8") as old:
#     old.write(up_text)