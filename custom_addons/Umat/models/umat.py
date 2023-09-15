from odoo import fields, models
class DataUmat(models.Model):
    _name = "simu_umat"
    _description = "Data Umat"

    # FORM AWAL UMAT

    kode = fields.Integer(string='Kode')
    nama = fields.Char(string='Nama', required=True)
    nik = fields.Integer(string='Nik')
    jenisKelamin = fields.Selection([('lakiLaki', 'Laki-Laki'), ('perempuan', 'Perempuan')], string='Jenis Kelamin')
    tanggalLahir = fields.Date('Tanggal Lahir')
    daerahLahir = fields.Char(string='Daerah Lahir')
    kotaLahir = fields.Char(string='Kota Lahir')
    agama = fields.Char(string='Agama')

    keuskupan = fields.Char(string='Keuskupan')
    paroki = fields.Char(string='Paroki')
    lingkungan = fields.Char(string='Lingkungan')
    tanggalBaptis = fields.Date(string='Tanggal Baptis')
    tanggalKomuniPertama = fields.Date(string='Tanggal Komuni Pertama')
    tanggalPenguatan = fields.Date(string='Tanggal Penguatan')

    golonganDarah = fields.Selection([('a', 'A'), ('b', 'B'), ('ab', 'AB'), ('o', 'O')], string='Golongan Darah')
    ras = fields.Char(string= 'Ras / Suku')
    kewarganegaraan = fields.Selection([('indonesia', 'Indonesia'), ('asing', 'Asing')], string='Kewarganegaraan')
    bahasaUtama = fields.Selection([('bahasa indonesia', 'Bahasa Indonesia'), ('bahasa inggris', 'Bahasa Inggris'), ('bahasa mandarin', 'Bahasa Mandarin'), ('bahasa sunda', 'Bahasa Sunda'), ('bahasa jawa', 'Bahasa Jawa'), ('bahasa batak', 'Bahasa Batak')], string='Bahasa Utama')
    tipeProtestan = fields.Selection([('baptis', 'Baptis'), ('angklikan', 'Angklikan'), ('protestan', 'Protestan'), ('lutheran', 'Lutheran')], string='Tipe Protestan')
    agamaSebelumnya = fields.Selection([('katolik', 'Katolik'), ('kristen', 'Kristen'), ('buddha', 'Buddha'), ('islam', 'Islam'), ('hindhu', 'Hindhu'), ('konghucu', 'Konghucu'), ('lainnya', 'Lainnya')], string='Agama Sebelumnya')

    # Kontak

    alamat = fields.Char(string='Alamat')
    kabupaten = fields.Char(string='Kabupaten')
    kota = fields.Char(string='Kota')
    kecamatan = fields.Char(string='Kecamatan')
    kelurahan = fields.Char(string='Kelurahan')
    rt = fields.Integer(string='RT')
    rw = fields.Integer(string='RW')
    bulanTinggal = fields.Integer(string='Bulan Tinggal')
    tahunTinggal = fields.Integer(string='Tahun Tinggal')
    noTelepon = fields.Integer(string='No Telepon')
    noHP = fields.Integer(string='No HP')
    email = fields.Char(string='Email')

    # Data Pribadi

    hobi = fields.Char(string='Hobi')
    anggotaAsuransi = fields.Char(string='Anggota Asuransi')
    statusKesehatan = fields.Char(string='Status Kesehatan')
    deskripsiKesehatan = fields.Char(string='Deskripsi Kesehatan')
    cacatTubuh= fields.Char(string='Catat Tubuh')
    deskripsiCacat = fields.Char(string='Deskripsi Cacat Tubuh')

    # Keluarga

    statusPerkawinan = fields.Char(string='Status Perkawinan')
    statusHubKeluarga = fields.Char(string='Status Hubungan Keluarga')
    namaIbuKandung = fields.Char(string='Nama Ibu Kandung')
    namaAyahKandung = fields.Char(string='Nama Ayah Kandung')
    anakKe = fields.Char(string='Anak Ke')
    namaAnggotaKeluarga = fields.Char(string='Nama Anggota Keluarga 1')
    namaAnggotaKeluarga2 = fields.Char(string='Nama Anggota Keluarga 2')
    namaAnggotaKeluarga3 = fields.Char(string='Nama Anggota Keluarga 3')
    namaAnggotaKeluarga4 = fields.Char(string='Nama Anggota Keluarga 4')
    namaAnggotaKeluarga5 = fields.Char(string='Nama Anggota Keluarga 5')

    # Sakramen Baptis  = fields.Char(string='')

    noSuratBaptis = fields.Integer(string='No Surat Baptis')
    namaBaptis = fields.Char(string='Nama Baptis')
    jenisBaptis = fields.Char(string='Jenis Baptis')
    agamaSebelumnya2 = fields.Selection(
        [('katolik', 'Katolik'), ('kristen', 'Kristen'), ('buddha', 'Buddha'), ('islam', 'Islam'), ('hindhu', 'Hindhu'),
         ('konghucu', 'Konghucu'), ('lainnya', 'Lainnya')], string='Agama Sebelumnya')
    gerejaBaptis = fields.Char(string='Gereja Baptis')
    tanggalBaptis2 = fields.Date(string='Tanggal Baptis')
    parokiBaptis = fields.Char(string='Paroki Baptis')
    kotaBaptis = fields.Char(string='Kota Baptis')

    # Komuni Pertama

    nomorSuratKomuni = fields.Integer(string='No Surat Komuni')
    tanggalKomuni = fields.Date(string='Tanggal Komuni')
    gerejaKomuni = fields.Char(string='di Gereja')
    namaParoki = fields.Char(string='Nama Paroki')
    kotaParoki = fields.Char(string='Kota')

    # Penguatan

    nomorSuratPenguatan = fields.Integer(string='No Surat Penguatan')
    tanggalPenguatan2 = fields.Date(string='Tanggal Penguatan')
    namaPenguatan = fields.Char(string='Nama Penguatan')
    gerejaPenguatan = fields.Char(string='di Gereja')
    namaParokiPenguatan = fields.Char(string='Nama Paroki')
    kotaPenguatan = fields.Char(string='Kota')

    # Perkawinan

    nomorSuratPerkawinan = fields.Integer(string='No Surat Perkawinan')
    tanggalPerkawinan = fields.Date(string='Tanggal Perkawinan')
    gerejaPerkawinan = fields.Char(string='di Gereja')
    namaParokiPerkawinan = fields.Char(string='Nama Paroki')
    kotaPerkawinan = fields.Char(string='Kota')
    namaSuami = fields.Char(string='Suami')
    namaIstri = fields.Char(string='Istri')
    kategoriPerkawinan = fields.Char(string='Kategori Perkawinan')

    pekerjaan = fields.Char(string='Pekerjaan')
    alamatPekerjaan = fields.Char(string='Alamat Pekerjaan')
    profesi = fields.Char(string='Profesi')
    profesiLain = fields.Char(string='Profesi Lain')
    pendapatanPerbulan = fields.Char(string='Pendapatan Perbulan')
    keahlian = fields.Char(string='Keahlian / Keterampilan')
    kursusGerejaPastoral = fields.Char(string='Kursus Gereja / Pastoral')
    jenisKursus = fields.Char(string='Jenis Kursus')
    pendidikanSaatIni = fields.Char(string='Pendidikan Saat Ini')
    pendidikanTerakhir = fields.Char(string='Pendidikan Terakhir')
    jurusan = fields.Char(string='Jurusan / Prodi')
    namaSekolah = fields.Char(string='Nama Sekolah / Universitas')
    kotaSekolah = fields.Char(string='di Kota')
    alamatSekolah = fields.Char(string='Alamat')
    kategoriSekolah = fields.Char(string='Kategori Sekolah / Universitas')

    # Aktivitas

    jenisRohaniwan = fields.Char(string='Jenis Rohaniwan')
    misaHarian = fields.Char(string='Misa Harian')
    misaMingguan = fields.Char(string='Misa Mingguan')
    misaHariRaya = fields.Char(string='Misa Hari Raya')
    aktifMasyarakat = fields.Char(string='Aktif di Masyarakat')
    posisiMasyarakat = fields.Char(string='Posisi Masyarakat')
    aktifKeuskupan = fields.Char(string='Aktif Keuskupan')
    aktifParoki = fields.Char(string='Aktif Paroki / Stasi')
    aktifLingkungan = fields.Char(string='Aktif di Lingkungan')
    aktifWilayah = fields.Char(string='Aktif di Wilayah')
    petugasLiturgi = fields.Char(string='Petugas Liturgi')
    aktifKategorial = fields.Char(string='Aktif di Kategorial')
    namaKategorial = fields.Char(string='Nama Kategorial')

    # APK

    anggotaAPK = fields.Char(string='Anggota APK')
    nomorAPK = fields.Integer(string='Nomor APK')
    tanggalAPK = fields.Date(string='Tanggal APK')
    status = fields.Char(string='Status')
    tanggalKematian = fields.Date(string='Tanggal Kematian')
    pastorPengurus = fields.Char(string='Pastor Pengurus Kematian')