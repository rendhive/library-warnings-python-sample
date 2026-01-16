import warnings

def function_with_warning():
    warnings.warn("Ini hanya peringatan.", UserWarning)

warnings.filterwarnings("ignore")  # Menyembunyikan semua peringatan
function_with_warning()
# Fungsi: Menyembunyikan peringatan yang muncul.
# Kondisi: Ketika Anda ingin mengabaikan peringatan tertentu dalam kode.