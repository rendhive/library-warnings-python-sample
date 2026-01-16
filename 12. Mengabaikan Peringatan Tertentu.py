import warnings

def no_warning():
    warnings.warn("Peringatan ini akan diabaikan.", UserWarning)

warnings.filterwarnings("ignore", category=UserWarning)

no_warning()  # Peringatan ini akan diabaikan
# Fungsi: Mengabaikan peringatan tertentu berdasarkan kategori.
# Kondisi: Ketika Anda tahu ada peringatan yang tidak relevan dan ingin mengabaikannya.