with open("deneme2.txt","a+") as fileObject:
    fileObject.write("Samet eve gel.\n")
    fileObject.seek(0) #a komutunu kullanınca işaretçiiz sonda olur ve ondan sonrasında hiçbir şey olmadığı iççin metni okumaz
    #ama seek komutunu kullanarak işaretçimizi başlangıca alır ve o başlangıçtan sonrasını yani tüm metni okumasını sağlarız
    text=fileObject.read()
    print(text)