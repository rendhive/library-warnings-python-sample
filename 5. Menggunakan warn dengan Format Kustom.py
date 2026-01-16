import warnings

def risky_operation(value):
    if value < 0:
        warnings.warn(f"Nilai negativa: {value}", UserWarning)
    return value

risky_operation(-10)
# Fungsi: Mengeluarkan peringatan yang berkaitan dengan nilai spesifik.
# Kondisi: Ketika Anda ingin memberi lebih banyak konteks dalam peringatan.