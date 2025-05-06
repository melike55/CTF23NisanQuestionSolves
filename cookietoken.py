import hashlib

# Hedef hash
target_hash = "946ef8d5679d62756d5d89a9a747cf74"

# Tahmini kelime listesi (23 Nisan temalı)
kelimeler = [
    "23nisan", "23_nisan", "23nisan2024", "23nisanulusal", "ulusalegemenlik",
    "egemenlik", "cocukbayrami", "23nisancocuk", "egemenlikvecocuk", "ulusal23nisan",
    "bayram", "23nisanbayrami", "tbmm", "mustafakemal", "atatürk", "atatürkçülük" , "23nisanulusalegemenlikvecocukbayrami"
]

for kelime in kelimeler:
    md5 = hashlib.md5(kelime.encode()).hexdigest()
    if md5 == target_hash:
        print(f"✅ Eşleşme bulundu!\nKelime: {kelime}\nHash: {md5}")
        break
else:
    print("❌ Hiçbir eşleşme bulunamadı.")
