import warnings

with open('warning_log.txt', 'w') as f:
    def custom_warning_handler(message, category, filename, lineno, file=None):
        f.write(f"{message}\n")

    warnings.showwarning = custom_warning_handler
    
    warnings.warn("Peringatan ini ditulis ke file!", UserWarning)
# Fungsi: Mengalihkan output peringatan ke file.
# Kondisi: Ketika Anda perlu merekam peringatan untuk analisis di kemudian hari.