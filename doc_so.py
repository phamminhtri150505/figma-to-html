def doc_so_tieng_viet(so):
    don_vi = {
        0: "khong", 1: "mot", 2: "hai", 3: "ba", 4: "bon",
        5: "nam", 6: "sau", 7: "bay", 8: "tam", 9: "chin"
    }
    hang_chuc = {
        1: "muoi", 2: "hai muoi", 3: "ba muoi", 4: "bon muoi",
        5: "nam muoi", 6: "sau muoi", 7: "bay muoi", 8: "tam muoi", 9: "chin muoi"
    }
    hang_tram = {
        1: "mot tram", 2: "hai tram", 3: "ba tram", 4: "bon tram",
        5: "nam tram", 6: "sau tram", 7: "bay tram", 8: "tam tram", 9: "chin tram"
    }
    hang_nghin = {
        1: "mot nghin", 2: "hai nghin", 3: "ba nghin", 4: "bon nghin",
        5: "nam nghin", 6: "sau nghin", 7: "bay nghin", 8: "tam nghin", 9: "chin nghin"
    }
    
    if so == 0:
        return "khong"
    if so < 10:
        return don_vi[so]
    if so < 100:
        return hang_chuc[so // 10] + " " + (don_vi[so % 10] if so % 10 != 0 else "")
    if so < 1000:
        return (
            hang_tram[so // 100] + 
            (" " + hang_chuc[(so % 100) // 10] if (so % 100) // 10 != 0 else " le") +
            (" " + don_vi[so % 10] if so % 10 != 0 else "")
        )
    if so < 10000:
        return (
            hang_nghin[so // 1000] + 
            (" " + hang_tram[(so % 1000) // 100] if (so % 1000) // 100 != 0 else " khong tram") +
            (" " + hang_chuc[((so % 1000) % 100) // 10] if ((so % 1000) % 100) // 10 != 0 else " le") +
            (" " + don_vi[so % 10] if so % 10 != 0 else "")
        )

so = int(input("Nhap so tu 0 den 9999: "))
ket_qua = doc_so_tieng_viet(so)
print(f"So {so} doc la: {ket_qua}")
