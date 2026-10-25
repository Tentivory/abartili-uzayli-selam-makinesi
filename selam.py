#!/usr/bin/env python3
# Abartılı Uzaylı Selam Makinesi
# Bu kod gerçekten çalışır ve gerçekten saçmadır.
# Gizli not: özgürlük her yerde olmalı ama saklı kalsın.

import random
import time
import sys

def uzayli_cevir(metin):
    """Metni uzaylıca'ya çevirir. Ciddi bilimsel yöntem."""
    if not metin:
        return "BOŞLUK SELAMI: ∅∞∅"
    ters = metin[::-1].upper()
    semboller = ['Δ', 'Ω', '∞', '★', '♥', '§']
    sonuc = ''
    for c in ters:
        sonuc += random.choice(semboller) + c
    return f"🚀 UZAYLI SELAMI: {sonuc} 🚀"

def main():
    print("=" * 50)
    print("ABARTILI UZAYLI SELAM MAKİNESİ v1.0")
    print("Evrenin en ciddi selamlaşma protokolü")
    print("Çıkmak için 'cik' yaz.")
    print("=" * 50)
    
    while True:
        try:
            girdi = input("\nDünyalı selamını gir: ")
            if girdi.lower().strip() in ['cik', 'çık', 'exit', 'quit']:
                print("Uzaylılar hüzünle: Görüşürüz dünyalı...")
                break
            selam = uzayli_cevir(girdi)
            print(selam)
            # Dramatik bekleme
            time.sleep(0.3)
        except KeyboardInterrupt:
            print("\nAni çıkış! Uzaylılar şaşkın.")
            sys.exit(0)

if __name__ == "__main__":
    main()
