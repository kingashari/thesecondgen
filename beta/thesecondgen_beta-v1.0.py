import requests
from bs4 import BeautifulSoup

# URL halaman yang ingin di-scrape
url = "https://w34.angkanet.fit/prediksi-hongkong/"

# Lakukan permintaan ke halaman tersebut
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# Temukan elemen textarea yang mengandung data angka
textareas = soup.find_all('textarea')

# Gabungkan konten dari setiap textarea
combined_data = ""
for textarea in textareas:
    combined_data += textarea.text.strip() + " "

# Cetak hasil gabungan dari semua textarea
print(combined_data.strip())
