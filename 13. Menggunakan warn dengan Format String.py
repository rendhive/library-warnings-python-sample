import warnings

def check_numeric(value):
    if not isinstance(value, (int, float)):
        warnings.warn(f"Nilai '{value}' tidak numerik!", UserWarning)

check_numeric("tes")
# Fungsi: Memeriksa apakah nilai adalah numerik dan memberi peringatan jika tidak.
# Kondisi: Ketika Anda ingin memperingatkan pengguna tentang nilai yang tidak sesuai.