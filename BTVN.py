def doc_so_tieng_viet_khong_dau(so):
    don_vi = {
        0: "", 1: "mot", 2: "hai", 3: "ba", 4: "bon",
        5: "nam", 6: "sau", 7: "bay", 8: "tam", 9: "chin"
    }
    hang_chuc = {
        0: "", 1: "muoi", 2: "hai muoi", 3: "ba muoi", 4: "bon muoi",
        5: "nam muoi", 6: "sau muoi", 7: "bay muoi", 8: "tam muoi", 9: "chin muoi"
    }
    def doc_hang_chuc_va_don_vi(n):
        if n == 0:
            return "khong"
        elif n < 10:
            return don_vi[n]
        elif n < 20:
            return "muoi " + ( don_vi[n % 10] if n % 10 != 0 else "" )
        else:
            return hang_chuc[n // 10] + ( don_vi[n % 10] if n % 10 != 0 else "" )
        
    def doc_hang_tram(n):
        tram = n // 100
        chuc_don_vi = n % 100
        ket_qua = ""
        
        
        