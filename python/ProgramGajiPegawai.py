# data akan d tampilkan setiap perulangan berakhir

# set gaji pokok
gajis = 2500
gajij = 1800

# melakukan perulangan 3kali
for i in range(0, 3):
	#deklarasi
	totalgaji = 0
	gajiistri = 0
	jabatan = "string kosong"
	
	#inputan
	print("======================")
	name = input("Nama: ")
	jkl = input("Jenis kelamin: ")
	umur = int(input("Umur(Angka): "))
	lastedu = input("Pendidikan terakhir: ")
	ttl = input("Tempat,tanggal lahir: ")
	alamat = input("Alamat: ")
	anak = int(input("Jumlah anak(Angka): "))
	istri = input("Memiliki istri?(y/n): ")
	
	#if statment
	if istri == "y":
		istrijumlah = int(input("Jumlah istri?(Angka): "))
	lembur = int(input("Total lembur(Angka): "))
	if umur < 25:
		jabatan = "Senior office"
		totalgaji = gajij
	else:
		jabatan = "Junior office"
		totalgaji = gajis
	if istri == "y":
		gajiistri = 500 * istrijumlah
	else:
		gajiistri = 0
	if anak > 5:
		anak = 5
	tunjangan = gajiistri + (anak * 200)
	if lembur > 50:
		lembur = 50
		
	# mengset hasil akhir
	bonuslembur = 50 * lembur 
	totalgajilast = totalgaji + tunjangan + lembur
	
	# tampilan
	print("======================")
	print(f"Nama: {name}")
	print(f"Jenis kelamin: {jkl}")
	print(f"Pendidikan terakhir: {lastedu}")
	print(f"alamat: {alamat}")
	print(f"Jabatan: {jabatan}")
	print(f"Gaji pokok: Rp.{totalgaji}.000")
	print(f"Tunjangan Rp.{tunjangan}.000")
	print(f"Bonus lembur: Rp.{bonuslembur}.000")
	print(f"Total gaji 1bulan: Rp.{totalgajilast}.000")
	print(f"Total gaji 1tahun: Rp.{totalgajilast * 12}.000")
