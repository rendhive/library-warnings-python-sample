import warnings

def compute():
    warnings.warn("Peringatan: Perhitungan mungkin tidak akurat!", RuntimeWarning)

warnings.filterwarnings("default", category=RuntimeWarning)
compute()
# Fungsi: Mengeluarkan peringatan dengan kategori spesifik.
# Kondisi: Ketika Anda ingin lebih spesifik dalam tipe peringatan yang ditampilkan.