import warnings

def special_warning():
    warnings.warn("Peringatan khusus untuk pengembangan!", UserWarning)

warnings.filterwarnings("always", category=UserWarning)
special_warning()
# Fungsi: Memastikan peringatan khusus ditangkap setiap kali fungsi dipanggil.
# Kondisi: Ketika Anda ingin memperingatkan pengguna tentang keadaan khusus yang penting.