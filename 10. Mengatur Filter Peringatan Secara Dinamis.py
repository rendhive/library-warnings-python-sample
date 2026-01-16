import warnings

def dynamic_warning_control():
    warnings.warn("Ini adalah peringatan awal.", UserWarning)
    warnings.filterwarnings("ignore")
    warnings.warn("Ini tidak akan terlihat.", UserWarning)

dynamic_warning_control()
# Fungsi: Mengatur filter peringatan secara dinamis selama eksekusi.
# Kondisi: Ketika Anda perlu mengubah kebijakan peringatan di tengah proses.