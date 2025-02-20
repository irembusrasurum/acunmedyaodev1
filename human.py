class Human:
    # isim = "James"
    def _init_(self, isim):  # Yapıcı (constructor) metot
        self.isim = isim
        print("Bir Human örneği oluşturuldu")

    # return f"İnsan(isim={self.isim})"

    def _str_(self):  # Nesnenin string temsili
        return f"STR foknsiyonunda dönen değer: {self.isim})"

    def talk(self, sentence):
        print(f"{self.isim}: {sentence}")
        # self.walk()

    def walk(self):
        print(f"{self.isim} yürüyor")