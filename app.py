from pyscript import document

def calculate_bmi(event):
    # Mengambil elemen input dari DOM
    age_input = document.querySelector("#input-usia").value
    weight_input = document.querySelector("#input-berat-badan").value
    height_input = document.querySelector("#input-tinggi-badan").value
    
    # Mengambil elemen output hasil dari DOM
    result_bmi = document.querySelector("#result-bmi")
    result_status = document.querySelector("#result-status")
    result_desc = document.querySelector("#result-desc")
    result_card = document.querySelector("#result-card")
    
    # 1. Validasi jika ada data yang belum diisi
    if not age_input or not weight_input or not height_input:
        result_bmi.innerText = "-"
        result_status.innerText = "Data Belum Lengkap"
        result_status.style.color = "#ffc107"
        result_card.style.borderLeft = "5px solid #ffc107"
        result_desc.innerText = "Mohon pastikan seluruh kolom Usia, Berat Badan, dan Tinggi Badan telah terisi sebelum melakukan perhitungan."
        return

    try:
        age = int(age_input)
        weight = float(weight_input)
        height_cm = float(height_input)

        # 2. Rumus Hitung Nilai BMI (Tinggi badan dikonversi dari cm ke meter)
        height_m = height_cm / 100
        bmi = weight / (height_m * height_m)
        bmi_rounded = round(bmi, 1)
        
        # Tampilkan angka skor BMI
        result_bmi.innerText = str(bmi_rounded)
        
        # 3. Pengkondisian Kategori Kesehatan, Warna Teks, dan Border Samping Kotak
        if bmi_rounded < 18.5:
            result_status.innerText = "Kurang Berat Badan (Underweight)"
            result_status.style.color = "#ffc107"  # Warna Kuning Emas
            result_card.style.borderLeft = "5px solid #ffc107"
            result_desc.innerText = "Kadar indeks tubuh Anda berada di bawah rentang normal. Pertimbangkan untuk meningkatkan asupan nutrisi seimbang dan perbanyak konsumsi makanan kaya protein."
            
        elif 18.5 <= bmi_rounded < 25.0:
            result_status.innerText = "Berat Badan Ideal (Normal)"
            result_status.style.color = "#28a745"  # Warna Hijau Sukses
            result_card.style.borderLeft = "5px solid #28a745"
            result_desc.innerText = "Luar biasa! Berat badan Anda berada di rentang yang sangat ideal dan sehat menurut standar kesehatan. Pertahankan pola makan aktif dan gaya hidup saat ini."
            
        elif 25.0 <= bmi_rounded < 30.0:
            result_status.innerText = "Kelebihan Berat Badan (Overweight)"
            result_status.style.color = "#fd7e14"  # Warna Oranye Rentan
            result_card.style.borderLeft = "5px solid #fd7e14"
            result_desc.innerText = "Anda berada pada kategori ambang batas berlebih. Cobalah untuk mengatur kembali porsi kalori harian dan tingkatkan intensitas aktivitas fisik atau olahraga ringan."
            
        else:
            result_status.innerText = "Obesitas (Obese)"
            result_status.style.color = "#dc3545"  # Warna Merah Peringatan
            result_card.style.borderLeft = "5px solid #dc3545"
            result_desc.innerText = "Tubuh Anda mengindikasikan akumulasi lemak berlebih yang masuk kategori obesitas. Disarankan mulai membatasi makanan tinggi gula/lemak jenuh dan berkonsultasi dengan profesional kesehatan."
            
    except Exception as e:
        result_bmi.innerText = "Error"
        result_status.innerText = "Gagal Memproses Data"
        result_status.style.color = "#dc3545"
        result_card.style.borderLeft = "5px solid #dc3545"
        result_desc.innerText = "Terjadi kesalahan sistem saat membaca format angka. Pastikan Anda memasukkan karakter angka yang valid."

def reset_form(event):
    # Mengosongkan kembali seluruh value input field form
    document.querySelector("#input-usia").value = ""
    document.querySelector("#input-berat-badan").value = ""
    document.querySelector("#input-tinggi-badan").value = ""
    
    # Mengembalikan default check radio selector ke pilihan 'Pria'
    document.querySelector("#gender-pria").checked = True
    
    # Mengembalikan tampilan visual komponen kotak hasil ke kondisi awal
    document.querySelector("#result-bmi").innerText = "-"
    document.querySelector("#result-status").innerText = "Silakan masukkan data Anda."
    document.querySelector("#result-status").style.color = "rgba(255, 255, 255, 0.9)"
    document.querySelector("#result-desc").innerText = "Gunakan kalkulator di samping untuk mengetahui indeks massa tubuh ideal Anda berdasarkan standar WHO."
    document.querySelector("#result-card").style.borderLeft = "5px solid rgba(255, 255, 255, 0.3)"
