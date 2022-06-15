class _rambut():
    def _init_(self, nama, tmpt_lahir, tgl_lahir, gender, panjang_rambut,):
        self.nama = nama
        self.tmpt_lahir = tmpt_lahir
        self.tgl_lahir = tgl_lahir
        self.gender = gender
        self.panjang_rambut = panjang_rambut
        
    def _set (self, nama, tmpt_lahir, tgl_lahir, gender, panjang_rambut,):
        self.nama = nama
        self.tmpt_lahir = tmpt_lahir
        self.tgl_lahir = tgl_lahir
        self.gender = gender
        self.panjang_rambut = panjang_rambut

    def _get (self):
        print('Nama lengkap   : ' + self.nama)
        print('TTL      : ' + self.tmpt_lahir + ', ' +  self.tgl_lahir)
        if self.gender in ['L', 'l']:
            gender = 'Laki-Laki'
        else:
            gender = 'Perempuan'
        print('Gender      :' + gender)

        if self.panjang_rambut >30:
            print('Cocok di Blow')
        else:
            if self.panjang_rambut >30:
                print('Cocok di Blow')
            else:
                if self.panjang_rambut <30:
                    print('Tidak cocok di Blow')

print('=====================================')
print('     PROGRAM CEK PANJANG RAMBUT      ')
print('=====================================')

nama      = input('Nama lengkap        :')
tmpt_lahir = input('Tempat lahir        :')
tgl_lahir  = input('Tanggal lahir       :')
gender     = input('Gender L/P          :')
panjang_rambut = float(input('Masukkan panjang rambut :'))

print('======================================')

proses = _rambut(nama,tmpt_lahir,tgl_lahir,gender,panjang_rambut)
print (proses._get())