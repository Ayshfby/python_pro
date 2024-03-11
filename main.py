meme_dict = {
            "CRINGE": "Sesuatu yang sangat aneh atau memalukan",
            "LOL": "Tanggapan umum terhadap sesuatu yang lucu",
            "EPIC": "Sesuatu hal yang keren"
            }
            
word = input("Ketik kata yang tidak Kamu mengerti (gunakan huruf kapital semua!): ") 

if word in meme_dict.keys():
    # Apa yang harus kita lakukan jika kata itu ditemukan?
    print("kata yang kamu cari:" word)
    print("keterangannya adalah:", meme_dict.get(word))
else:
    # Apa yang harus kita lakukan jika kata itu tidak ditemukan?
    print("maaf, kata tidak ada")

