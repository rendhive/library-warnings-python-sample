import warnings

def check_value(value):
    if value < 0:
        warnings.warn("Negatif tidak diperbolehkan!", UserWarning)

check_value(-5)
# Fungsi: Emit warning berdasarkan nilai parameter.
# Kondisi: Ketika Anda ingin memperingatkan pengguna tentang nilai-nilai di luar batas yang diharapkan.