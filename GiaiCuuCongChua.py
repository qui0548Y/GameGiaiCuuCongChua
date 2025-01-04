import pygame
import random
pygame.init()
# Cửa sổ game
manhinh = pygame.display.set_mode((1530, 780))
# Thay đổi tiêu đề và icon
pygame.display.set_caption("Giải cứu công chúa")

icon= pygame.image.load(r"TaiNguyen\anh\logo.jpg")
pygame.display.set_icon(icon)

a1=pygame.image.load(r"TaiNguyen\anh\dragon-a.png").convert_alpha()
a2=pygame.image.load(r"TaiNguyen\anh\dragon-b.png").convert_alpha()
a3=pygame.image.load(r"TaiNguyen\anh\dragon-c.png").convert_alpha()
a4=pygame.image.load(r"TaiNguyen\anh\dragon-d.png").convert_alpha()
dsnv=[a1,a2 ,a3 ,a4 ]

b1= pygame.image.load(r"TaiNguyen\anh\lua1.png").convert_alpha()
b2= pygame.image.load(r"TaiNguyen\anh\lua2.png").convert_alpha()
b3= pygame.image.load(r"TaiNguyen\anh\lua3.png").convert_alpha()
b4= pygame.image.load(r"TaiNguyen\anh\lua4.png").convert_alpha()
b5= pygame.image.load(r"TaiNguyen\anh\lua5.png").convert_alpha()
dsLua=[b1,b2,b3,b4,b5]

tN1=pygame.image.load(r"TaiNguyen\anh\da.png").convert_alpha()
tN2=pygame.image.load(r"TaiNguyen\anh\da1.png").convert_alpha()


thienT=pygame.image.load(r"TaiNguyen\anh\thienThach.png").convert_alpha()


nV9a=pygame.image.load(r"TaiNguyen\anh\hoangTu1.png").convert_alpha()
nV9b=pygame.image.load(r"TaiNguyen\anh\hoangTu2.png").convert_alpha()
nV9c=pygame.image.load(r"TaiNguyen\anh\hoangTu3.png").convert_alpha()
nV9d=pygame.image.load(r"TaiNguyen\anh\hoangTu4.png").convert_alpha()
dsNV9=[nV9a,nV9b, nV9c,nV9d]


nenToaLua=pygame.image.load(r"TaiNguyen\anh\toaLua.png")

vP1=pygame.image.load(r"TaiNguyen\anh\vang.png").convert_alpha()
vP2=pygame.image.load(r"TaiNguyen\anh\mau.png").convert_alpha()
vP3=pygame.image.load(r"TaiNguyen\anh\ngoc.png").convert_alpha()
dsVatPham= [vP1,vP2,vP3]

anhDan=pygame.image.load(r"TaiNguyen\anh\danThuCuoi.png").convert_alpha()

anhVuNo=pygame.image.load(r"TaiNguyen\anh\vuNo.png").convert_alpha()

thoat=pygame.image.load(r"TaiNguyen\anh\dichChuyen.png").convert_alpha()

mauDo=pygame.image.load(r"TaiNguyen\anh\thanhMau2.png").convert_alpha()
mauXanh=pygame.image.load(r"TaiNguyen\anh\thanhMau1.png").convert_alpha()


class hoangTuVaCongChua():
    def __init__(self, toaDoX, toaDoY, tanCong):
        self.X=toaDoX
        self.Y=toaDoY
        self.trangPhuc=0
        self.tanCog=tanCong
        self.goiDan=False
        self.dsDan = []
        self.mau=100
        self.thanhMauHT=thanhHP(self.X, self.Y-100,self.mau)
        
        
    def nhanVat(self): 
        if(self.tanCog==False):
            self.goiDan=False
            if(self.trangPhuc==2):
                self.trangPhuc=0
        if(self.tanCog==True):
            if (self.trangPhuc < 2): 
                self.trangPhuc = 2 
            if(self.trangPhuc==3):
                self.tanCog=False
                self.goiDan=True
                self.trangPhuc=-1
        self.nv= dsNV9[self.trangPhuc]
        self.trangPhuc+=1
        return self.nv

    def nhanVat_hcn(self):
        self.nv_hcn=self.nv.get_rect(center=(self.X, self.Y))
        return self.nv_hcn
    def tanCong(self, event):
        if event.type==pygame.KEYDOWN:
            if event.key== pygame.K_SPACE:
                self.tanCog=True
        
    def goiLuaDanCong(self):
        if self.goiDan:
            Dan=danDaiBan(self.X+60, self.Y-30, self.goiDan, 50)
            self.dsDan.append(Dan)
            self.goiDan=False
            
    def toanBoDan(self):
        tam = []
        for dan in self.dsDan:
            if dan.capNhatDan():
                manhinh.blit(dan.nhanVat(),dan.nhanVat_hcn())
                dan.capNhatY()
            if(dan.X>-300):
                tam.append(dan)
        self.dsDan = tam

    def xoaCacVienDan(self):
        tam = []
        for dan in self.dsDan:
            if dan.X >-300:
                tam.append(dan)
        self.dsDan = tam
            
    def HTVaCChuaDiChuyen(self, event):
        if event.type==pygame.KEYDOWN:
            if event.key== pygame.K_UP:
                if self.Y>100:
                    self.Y-=60
        
    def HTvaCChuaRoi(self):
        if self.Y<700:
            self.Y+=30

    def getDSDan(self):
        return self.dsDan

    

    def getX(self):
        return self.X
    def getY(self):
        return self.Y

    def xoaDan(self, a):
        self.dsDan.remove(a)

    def thanhMau(self):
        manhinh.blit(mauDo,(self.X+1,self.Y-100))
        if self.mau<=0:
            self.mau=0
        self.thanhMauHT=thanhHP(self.X,self.Y-100, self.mau)
        manhinh.blit(self.thanhMauHT.nhanVat(), self.thanhMauHT.nhanVat_hcn())

    def setMau(self, mau):
        self.mau+=mau
        if self.mau>100:
            self.mau=100
    
    def getMau(self):
        return self.mau

    def traVeTrangThai(self):
        self.mau=100
        self.X=900
        self.Y=390
        self.dsDan.clear()

    

class danDaiBan():
    def __init__(self, toaDoX, toaDoY, goiDan, R):
        self.X=toaDoX
        self.Y=toaDoY
        self.goiLua=goiDan
        self.R=R
        self.xI=toaDoX
        dsRamDom=[1, 2]
        self.huong=random.choice(dsRamDom)
        if self.huong==1:
            self.yI=toaDoY-R
            self.gioiHan=toaDoY-2*R
        if self.huong==2:
            self.yI=toaDoY+R
            self.gioiHan=toaDoY+2*R
        self.luongTang=toaDoY/50
        
        
    def nhanVat(self): 
        self.nv= anhDan
        return self.nv
 
    def nhanVat_hcn(self):
        self.nv_hcn=self.nv.get_rect(center=(self.X, self.Y))
        return self.nv_hcn  

    def capNhatDan(self):
        if self.huong==1:
            if self.Y>self.gioiHan:
                self.X=self.xI+((self.R)**2-(self.Y-self.yI)**2)**0.5
            else:
                self.X-=8
        if self.huong==2:
            if self.Y<self.gioiHan:
                self.X=self.xI+((self.R)**2-(self.Y-self.yI)**2)**0.5
            else:
                self.X-=8
        return self.X>-300

    def capNhatY(self):
        if self.huong==1:
            if self.Y>self.gioiHan:
                self.Y-=self.luongTang
        if self.huong==2:
            if self.Y<self.gioiHan:
                self.Y+=self.luongTang  

    def getX(self):
        return self.X
    def getY(self):
        return self.Y

  

class khungLong():
    def __init__(self, toaDoX, toaDoY, tanCong):
        self.X=toaDoX
        self.Y=toaDoY
        self.trangPhuc=0
        self.tanCog=tanCong
        self.goiLua=False
        self.dsLua = []
        self.duoi=ngonLua(self.X-120,self.Y+10,False)
        self.KLToaLua=toaLua(0,0)
        self.mau=100
        self.thanhMauHT=thanhHP(self.X+30,self.Y-120, self.mau)
   
        
    def nhanVat(self): 
        if(self.tanCog==False):
            self.goiLua=False
            if(self.trangPhuc==2):
                self.trangPhuc=0
        if(self.tanCog==True):
            if (self.trangPhuc < 2): 
                self.trangPhuc = 2 
            if(self.trangPhuc==3):
                self.tanCog=False
                self.goiLua=True
                self.trangPhuc=-1
        self.nv= dsnv[self.trangPhuc]
        self.trangPhuc+=1
        return self.nv
    def nhanVat_hcn(self):
        self.nv_hcn=self.nv.get_rect(center=(self.X, self.Y))
        return self.nv_hcn

    def duoiCuaRong(self):
        duoiRong=self.duoi.nhanVat()
        duoiRong_hcn=self.duoi.nhanVat_hcn()    
        manhinh.blit(duoiRong,duoiRong_hcn)

    def tanCong(self):
        dsRamDom=[True, False]
        tiLe=[0.15,0.85]
        ngauNhien=random.choices(dsRamDom,weights=tiLe,k=1)[0]
        if ngauNhien:
            self.tanCog=True
            
    def goiLuaTanCong(self):
        if self.goiLua:
            lua=ngonLua(self.X+100, self.Y-80, self.goiLua)
            self.dsLua.append(lua)
            self.goiLua=False
            
    def toanBoLua(self):
        tam = []
        for lua in self.dsLua:
            if lua.luaDiChuyen(3):
                manhinh.blit(lua.nhanVat(),lua.nhanVat_hcn())
            if(lua.X<1530):
                tam.append(lua)
        self.dsLua = tam
                

    def xoaCacNgonLua(self):
        tam = []
        for lua in self.dsLua:
            if lua.X < 1530:
                tam.append(lua)
        self.dsLua = tam

    def khungLongDiChuyen(self):
        dsRamDom=[-10,10]
        tiLe1=[0.45,0.55]
        tiLe2=[0.55,0.45]
        if (0<self.Y<390):
            self.Y=self.Y+random.choices(dsRamDom,weights=tiLe1,k=1)[0]
        elif(390<self.Y<700):
            self.Y=self.Y+random.choices(dsRamDom,weights=tiLe2,k=1)[0] 
            
        elif(self.Y==390):
            self.Y=self.Y+random.choices(dsRamDom,weights=tiLe2,k=1)[0] 
        else:
            if(self.Y<=0):
                self.Y+=10
            elif(self.Y>=700):
                self.Y-=10
        self.duoi.duoiRong(self.Y)
        
    def khungLongToaLua(self):
        self.KLToaLua.capNhatToaDo(self.X,self.Y)
        nenTL=self.KLToaLua.nhanVat()
        nenTL_hcn=self.KLToaLua.nhanVat_hcn()
        manhinh.blit(nenTL,nenTL_hcn)

    def getDSLua(self):
        return self.dsLua


    def xoaLua(self, a):
        self.dsLua.remove(a)

    def getX(self):
        return self.X
    def getY(self):
        return self.Y

    def thanhMau(self):
        manhinh.blit(mauDo,(self.X+31,self.Y-120))
        if self.mau<=0:
            self.mau=0
        self.thanhMauHT=thanhHP(self.X+30,self.Y-120, self.mau)
        manhinh.blit(self.thanhMauHT.nhanVat(), self.thanhMauHT.nhanVat_hcn())

    def setMau(self, mau):
        self.mau+=mau
    
    def getMau(self):
        return self.mau
    
    def traVeTrangThai(self):
        self.mau=100
        self.X=150
        self.Y=390
        self.dsLua.clear()


class ngonLua():
    def __init__(self, toaDoX, toaDoY, goiLua):
        self.X=toaDoX
        self.Y=toaDoY
        self.trangPhucLua=0
        self.goiLua=goiLua
        
    def nhanVat(self): 
        if(self.trangPhucLua==4):
            self.trangPhucLua=0
        self.nv= dsLua[self.trangPhucLua]
        if(demKhungHinh==2):
            self.trangPhucLua+=1
        return self.nv

    def duoiRong(self, Y):
        self.Y=Y
        
    def nhanVat_hcn(self):
        self.nv_hcn=self.nv.get_rect(center=(self.X, self.Y))
        return self.nv_hcn  
    def luaDiChuyen(self, a): 
        self.X+=a
        return self.X < 1530

    def getX(self):
        return self.X

    def getY(self):
        return self.Y

class toaLua():
    def __init__(self, toaDoX, toaDoY):
        self.X=toaDoX
        self.Y=toaDoY
        
        
    def nhanVat(self):
        self.nv= nenToaLua
        return self.nv

    def nhanVat_hcn(self):
        self.nv_hcn=self.nv.get_rect(center=(self.X, self.Y))
        return self.nv_hcn  

    def capNhatToaDo(self,a,b):
        self.X=a
        self.Y=b
    
class thachNhu():
    def __init__(self, toaDoX, toaDoY, viTri):
        self.X=toaDoX
        self.Y=toaDoY
        self.YbanDau=toaDoY
        self.viTri=viTri
        self.roiXuong=random.randint(0,1700)   #(700,1500)
        self.goc=0
        
    def nhanVat(self):
        if(self.viTri==1):
            
            self.nv= tN1
            self.nv = pygame.transform.rotate(self.nv, self.goc)
        elif(self.viTri==2):
            self.nv=tN2

        return self.nv

    def nhanVat_hcn(self):
        self.nv_hcn=self.nv.get_rect(center=(self.X, self.Y))
        return self.nv_hcn  
    def thachNhuDiChuyen(self,a):
        self.X-=a 
        if(800<self.roiXuong<1600):
            if(self.X<self.roiXuong and self.viTri==1):
                self.Y+=5
        return self.X>0
    def getViTri(self):
        return self.viTri

    def getX(self):
        return self.X

    def getY(self):
        return self.Y

    def setGoc(self):
        if(self.Y!=self.YbanDau):
            if(self.goc<180):
                self.goc+=2
                self.X-=2

dsThachNhu=[]
def viTri():
    viTri=random.randint(1,2)
    return viTri

def goiTNTanCong(tam):
    vT=viTri()
    if 5<tam<50:
        if(vT==1):
            y=random.randint(-20,50)
        elif(vT==2):
            y=random.randint(750,800)
        tNhu=thachNhu(1800,y,vT)
        dsThachNhu.append(tNhu)
            
def toanThachNhu():
    global dsThachNhu
    tam = []
    for thachNhu in dsThachNhu:
        if thachNhu.thachNhuDiChuyen(3):
            manhinh.blit(thachNhu.nhanVat(),thachNhu.nhanVat_hcn())
        if (thachNhu.X>-300):
            tam.append(thachNhu)
    dsThachNhu = tam

class thienThach():
    def __init__(self, toaDoX, toaDoY):
        self.X=toaDoX
        self.Y=toaDoY
        
    def nhanVat(self):
        self.nv= thienT
        return self.nv

    def nhanVat_hcn(self):
        self.nv_hcn=self.nv.get_rect(center=(self.X, self.Y))
        return self.nv_hcn  

    def thienThachDiChuyen(self,a,b):
        self.X-=a 
        self.Y+=b
        return True

dsThienThach=[]

def goiTTTanCong(tam):
    if 5<tam<20:
        x=random.randint(1180,2310)
        y=random.randint(-20,-10)
        tThach=thienThach(x,y)
        dsThienThach.append(tThach)
            
def toanThienThach():
    global dsThienThach
    tam = []
    for thienThach in dsThienThach:
        if thienThach.thienThachDiChuyen(3*(2**0.5),3):
            manhinh.blit(thienThach.nhanVat(),thienThach.nhanVat_hcn())
        if (thienThach.Y<1000):
            tam.append(thienThach)
    dsThienThach = tam


class vatPham():
    def __init__(self, toaDoX, toaDoY):
        self.X=toaDoX
        self.Y=toaDoY
        dsRamDom=[0,1,2,3] #vang, mau, ngoc
        tiLe=[0.3, 0.2, 0.2, 0.3]
        ngauNhien=random.choices(dsRamDom,weights=tiLe,k=1)[0]
        self.loaiVP=ngauNhien
        self.trangPhuc=0
        
        # Lấy kích thước ảnh gốc
        if ngauNhien<3:
            self.rong, self.cao = dsVatPham[self.loaiVP].get_size()
            self.tile=1 
           
    def nhanVat(self):
        if(demKhungHinh==3):
            self.tile=random.uniform(1,2)
        # Tính kích thước mới 
        new_size = (self.rong // self.tile, self.cao // self.tile)
        # Thay đổi kích thước ảnh
        trangPhuc = pygame.transform.scale(dsVatPham[self.loaiVP], new_size)
        self.nv= trangPhuc
            
        return self.nv

    def nhanVat_hcn(self):
        self.nv_hcn=self.nv.get_rect(center=(self.X, self.Y))
        return self.nv_hcn  

    def vatPhamDiChuyen(self,a):
        self.X-=a 
        return True

    def getLoaiVP(self):
        if self.loaiVP>2:
            return False
    
    def getLoaiVP1(self):
        return self.loaiVP

    def goiNhac(self, a):
        a.play()

dsVatP=[]

def goiVatPham(tam):
    if 5<tam<20:
        x=1540
        y=random.randint(10,770)
        vP=vatPham(x,y)
        if vP.getLoaiVP()!=False:
            dsVatP.append(vP)
            
def toanVatPham():
    global dsVatP
    tam = []
    for vP in dsVatP:
        if vP.vatPhamDiChuyen(3):
            manhinh.blit(vP.nhanVat(),vP.nhanVat_hcn())
        if (vP.X>-300):
            tam.append(vP)
    dsVatP = tam

def xoaVatPham(vatPham):
    dsVatP.remove(vatPham)

class thanhHP():
    def __init__(self, toaDoX, toaDoY, rong):
        self.doi=50-rong/2
        self.X=toaDoX+50-self.doi
        self.Y=toaDoY+5
        self.rong=rong
          
    def nhanVat(self):
        # Tính kích thước mới 
        new_size = (self.rong, 10)
        # Thay đổi kích thước ảnh
        trangPhuc = pygame.transform.scale(mauXanh, new_size)
        self.nv= trangPhuc
        return self.nv

    def nhanVat_hcn(self):
        self.nv_hcn=self.nv.get_rect(center=(self.X, self.Y))
        return self.nv_hcn  

class canhCuaThoat():
    def __init__(self):
        self.X=1700
        self.Y=random.randint(100,600)
        self.rong, self.cao = thoat.get_size()
        self.tile=1 
        
    def nhanVat(self):
        if(demKhungHinh==3):
            self.tile=random.uniform(1,1.5)
        # Tính kích thước mới 
        new_size = (self.rong // self.tile, self.cao // self.tile)
        # Thay đổi kích thước ảnh
        self.nv = pygame.transform.scale(thoat, new_size)
        return self.nv

    def nhanVat_hcn(self):
        self.nv_hcn=self.nv.get_rect(center=(self.X, self.Y))
        return self.nv_hcn  

    def canhCuaDiChuyen(self):
        self.X-=3

    def getX(self):
        return self.X>-300

    def traVeX(self):
        return self.X

    def traVeY(self):
        return self.Y
    
    

class vaCham():
    def __init__(self, toaDoX, toaDoY):
        self.X=toaDoX
        self.Y=toaDoY
        self.thoiGian=0
        # Lấy kích thước ảnh gốc
        self.rong, self.cao = anhVuNo.get_size()
        self.tile=1
           
    def nhanVat(self):
        if(demKhungHinh==3):
            self.tile=random.uniform(1,2)
        # Tính kích thước mới 
        new_size = (self.rong // self.tile, self.cao // self.tile)
        # Thay đổi kích thước ảnh
        trangPhuc = pygame.transform.scale(anhVuNo, new_size)
        self.nv= trangPhuc
            
        return self.nv

    def nhanVat_hcn(self):
        self.nv_hcn=self.nv.get_rect(center=(self.X, self.Y))
        self.thoiGian+=1
        return self.nv_hcn  

    def getTG(self):
        return self.thoiGian


dsVuNo=[]

def goiVuNo(x,y):
    vuN= vaCham(x,y)
    dsVuNo.append(vuN)
    nhacVaCham.play()
            
def toanVuNo():
    global dsVuNo
    tam = []
    for vN in dsVuNo:
        manhinh.blit(vN.nhanVat(),vN.nhanVat_hcn())
        if vN.getTG()<40:
            tam.append(vN)
    dsVuNo = tam

def kiemTraVaCham(rect1, rect2):
    return rect1.colliderect(rect2)


def phatAmThanh(amThanh):
    amThanh.play()



demKhungHinh=0
# set bg TH1
truongHop1=False
bg= pygame.image.load(r"TaiNguyen\anh\bg.png").convert()
bg_x=0
bg_x1=1920

bg1 = pygame.transform.flip(bg, True, False)

bg2= pygame.image.load(r"TaiNguyen\anh\bgNgoaiTroi.png").convert()
bg3= pygame.transform.flip(bg2, True, False)

bg4= pygame.image.load(r"TaiNguyen\anh\bg.png").convert()
bg5= pygame.transform.flip(bg4, True, False)

# phongChu
font=pygame.font.Font(r"TaiNguyen\fontChu\04B_19.TTF",15)
font1=pygame.font.Font(r"TaiNguyen\fontChu\04B_19.TTF",40)
#HienThuthap
thuThap=pygame.image.load(r"TaiNguyen\anh\hienThiThuThap.png").convert_alpha()
    

# set nhan vat KhungLong
nv=khungLong(150, 390,False)
khungLog= nv.nhanVat()
khungLong_hcn= nv.nhanVat_hcn()

# set nhan vat chinh
nv9=hoangTuVaCongChua(900, 390,False)
hoangTu= nv9.nhanVat()
hoangTu_hcn= nv9.nhanVat_hcn()
# set thach Nhu
t=0

clock= pygame.time.Clock()
# Vòng lặp xử lý game
running = True

#chuyen man
chuyenMan=0

click=pygame.image.load(r"TaiNguyen\anh\click.png").convert()

trangChu=True
bgTrangChu=pygame.image.load(r"TaiNguyen\anh\BatDau.png").convert()

thoatKhoi=None
thoatKhoi1=None
goiCanhCua=False

Thang=False
bgThang=pygame.image.load(r"TaiNguyen\anh\Thang.png").convert()
Thua=False
bgThua=pygame.image.load(r"TaiNguyen\anh\Thua.png").convert()


dangChoi=False

xemHuongDan=False
bgHuongDan=pygame.image.load(r"TaiNguyen\anh\huongDan.png").convert()

nhacNen=pygame.mixer.Sound(r"TaiNguyen\amThanh\nhac.mp3")
nhacVaCham=pygame.mixer.Sound(r"TaiNguyen\amThanh\vaCham.mp3")
nhacThang=pygame.mixer.Sound(r"TaiNguyen\amThanh\thang.mp3")
nhacThua=pygame.mixer.Sound(r"TaiNguyen\amThanh\thua.mp3")


fi=open("diemHoangTu.txt","r")
si=fi.read()
vangNhieuI=si[4:]
phutI=si[:2]
giayI=si[2:4]

# ghi tệp
fo=open("diemHoangTu.txt", "w")



vang=0
thoigian=0
phut=0
giay=0
ngoc=0
dieuKien=0

anVang=pygame.mixer.Sound(r"TaiNguyen\amThanh\vang.wav")
anMau=pygame.mixer.Sound(r"TaiNguyen\amThanh\hoiMau.mp3")
anNgoc=pygame.mixer.Sound(r"TaiNguyen\amThanh\ngoc.mp3")


nhacNen.play(loops=-1) #nen
nhacNen.set_volume(0.5)
while running:
    clock.tick(60)
    

    if trangChu:
        
        manhinh.blit(bgTrangChu, (0,0))
        toaDoChuot=pygame.mouse.get_pos()
        text=font1.render(str(vangNhieuI),True, (255,255,255))
        manhinh.blit(text,(845,185))
        
        text1=font1.render("00:"+str(phutI)+":"+str(giayI),True, (255,255,255))
        manhinh.blit(text1,(845,140))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fo.write(f'{phutI}{giayI}{vangNhieuI}')
                fo.close()
                running = False
            if event.type==pygame.MOUSEBUTTONDOWN:
                if event.button==1:
                    if 555<=toaDoChuot[0]<=1010 and 345<=toaDoChuot[1]<=520:
                        manhinh.blit(click, toaDoChuot)
                        dangChoi=True
                        trangChu=False
                    if 555<=toaDoChuot[0]<=1010 and 560<=toaDoChuot[1]<=740:
                        manhinh.blit(click, toaDoChuot)
                        xemHuongDan=True
                        trangChu=False

    if xemHuongDan:
        manhinh.blit(bgHuongDan, (0,0))
        toaDoChuot=pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fo.write(f'{phutI}{giayI}{vangNhieuI}')
                fo.close()
                running = False
            if event.type==pygame.MOUSEBUTTONDOWN:
                if event.button==1:
                    if 1135<=toaDoChuot[0]<=1400 and 90<=toaDoChuot[1]<=190:
                        manhinh.blit(click, toaDoChuot)
                        xemHuongDan=False
                        trangChu=True
                    
            #even.buton =1trai; 3phai; 5cuon len; 4 cuon xuong
        
    if dangChoi:
        a=1
        thoigian+=1
        phut=int(thoigian/(60*60))
        giay=int(thoigian/60 -phut*60)
        if phut<10:
            phut="0"+str(phut)
        if giay<10:
            giay="0"+str(giay)
        demKhungHinh+=1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fo.write(f'{phutI}{giayI}{vangNhieuI}')
                running = False
            nv9.tanCong(event)
            nv9.HTVaCChuaDiChuyen(event)
            
        # ảnh nền   
        bg_x-=3
        bg_x1-=3
        manhinh.blit(bg, (bg_x, -290))
        manhinh.blit(bg1, (bg_x1,-290))


        if(bg_x==-1920):
            bg_x=1920
        if(bg_x1==-1920 ):
            bg_x1=1920
            
        if(truongHop1==False):
            dsThienThach.clear()
            if(demKhungHinh==20):
                t=random.randint(1,100)
                goiTNTanCong(t)
            toanThachNhu()
        
        
        if(truongHop1==True):
            dsThachNhu.clear()
            if(demKhungHinh==20):
                t=random.randint(1,80)
                goiTTTanCong(t)
            toanThienThach()

        if (ngoc%7==0 and ngoc>dieuKien):
            goiCanhCua=True
            dieuKien=ngoc
            thoatKhoi=canhCuaThoat()
            
        if goiCanhCua==True:
            if thoatKhoi!=None and thoatKhoi.getX()==False:
                thoatKhoi=None
                goiCanhCua==False
            elif thoatKhoi!=None and thoatKhoi.getX()==True:
                manhinh.blit(thoatKhoi.nhanVat(),thoatKhoi.nhanVat_hcn())
                thoatKhoi.canhCuaDiChuyen()

        chuyenMan+=1
        if(chuyenMan%1000==0):
            thoatKhoi1=canhCuaThoat()


        if thoatKhoi1!=None and thoatKhoi1.getX()==False:
            thoatKhoi1=None
        elif thoatKhoi1!=None and thoatKhoi1.getX()==True:
            manhinh.blit(thoatKhoi1.nhanVat(),thoatKhoi1.nhanVat_hcn())
            thoatKhoi1.canhCuaDiChuyen()

        if(truongHop1==False):
            if thoatKhoi1!=None:
                if(kiemTraVaCham(nv9.nhanVat_hcn(),thoatKhoi1.nhanVat_hcn())):
                    truongHop1=True
                    bg=bg2
                    bg1=bg3
                    thoatKhoi1=None
        else:
            if thoatKhoi1!=None:
                if(kiemTraVaCham(nv9.nhanVat_hcn(),thoatKhoi1.nhanVat_hcn())):
                    truongHop1=False
                    bg=bg4
                    bg1=bg5
                    thoatKhoi1=None
                
        
        if(demKhungHinh==20):
            t1=random.randint(1,100)
            goiVatPham(t1)
        toanVatPham()
        nv.khungLongToaLua()
        nv.goiLuaTanCong()

        nv9.goiLuaDanCong()
    
        
        nv.toanBoLua()
        nv9.toanBoDan()
        nv.duoiCuaRong()
        if (demKhungHinh==10):
            nv9.HTvaCChuaRoi()
        if(demKhungHinh==20):
            
            khungLog=nv.nhanVat()
            khungLong_hcn=nv.nhanVat_hcn()
            nv.khungLongDiChuyen()
            
            nv.tanCong()
            hoangTu=nv9.nhanVat()
            hoangTu_hcn=nv9.nhanVat_hcn()
            demKhungHinh=0
            
        manhinh.blit(khungLog,khungLong_hcn)
        manhinh.blit(hoangTu,hoangTu_hcn)
        nv.goiLuaTanCong()
        nv9.goiLuaDanCong()
        
        nv.toanBoLua()
        nv9.toanBoDan()


        #Hoang tu cham lua
        hoangTu_rect = nv9.nhanVat_hcn()
        for lua in nv.getDSLua():
            lua_rect = lua.nhanVat_hcn()
            if kiemTraVaCham(hoangTu_rect, lua_rect):
                # Nếu có va chạm, tạo một vụ nổ
                goiVuNo(nv9.getX(), nv9.getY())
                nv.xoaLua(lua)
                nv9.setMau(-0.6)
        # hoang tu cham thach nhu
        for tN in dsThachNhu:
            tN_rect = tN.nhanVat_hcn()
            if kiemTraVaCham(hoangTu_rect, tN_rect):
                # Nếu có va chạm, tạo một vụ nổ
                tN.setGoc()
                nv9.setMau(-0.05)

        
        for lua in nv.getDSLua():
            lua_rect = lua.nhanVat_hcn()
            for dan in nv9.getDSDan():
                dan_rect = dan.nhanVat_hcn()
                if kiemTraVaCham(lua_rect, dan_rect):
                    # Nếu có va chạm, tạo một vụ nổ
                    goiVuNo(lua.getX(), lua.getY())
                    nv.xoaLua(lua)
                    nv9.xoaDan(dan)

        for lua in nv.getDSLua():
            lua_rect = lua.nhanVat_hcn()
            for tn in dsThachNhu:
                tn_rect = tn.nhanVat_hcn()
                if kiemTraVaCham(lua_rect, tn_rect):
                    # Nếu có va chạm, tạo một vụ nổ
                    goiVuNo(lua.getX(), lua.getY())
                    if lua in nv.getDSLua():
                        nv.xoaLua(lua)
   

        for lua in nv.getDSLua():
            lua_rect = lua.nhanVat_hcn()
            for tt in dsThienThach:
                tt_rect = tt.nhanVat_hcn()
                if kiemTraVaCham(lua_rect, tt_rect):
                    # Nếu có va chạm, tạo một vụ nổ
                    goiVuNo(lua.getX(), lua.getY())
                    nv.xoaLua(lua)
                    dsThienThach.remove(tt)

        for dan in nv9.getDSDan():
            dan_rect = dan.nhanVat_hcn()
            for tn in dsThachNhu:
                tn_rect = tn.nhanVat_hcn()
                if kiemTraVaCham(dan_rect, tn_rect):
                    # Nếu có va chạm, tạo một vụ nổ
                    goiVuNo(dan.getX(), dan.getY())
                    if dan in nv9.getDSDan():
                        nv9.xoaDan(dan)
   

        for dan in nv9.getDSDan():
            dan_rect = dan.nhanVat_hcn()
            for tt in dsThienThach:
                tt_rect = tt.nhanVat_hcn( )
                if kiemTraVaCham(dan_rect, tt_rect):
                    # Nếu có va chạm, tạo một vụ nổ
                    goiVuNo(dan.getX(), dan.getY())
                    nv9.xoaDan(dan)
                    dsThienThach.remove(tt)

        for tt in dsThienThach:
            tt_rect = tt.nhanVat_hcn()
            if kiemTraVaCham(hoangTu_rect, tt_rect):
                # Nếu có va chạm, tạo một vụ nổ
                goiVuNo(nv9.getX(), nv9.getY())
                dsThienThach.remove(tt)
                nv9.setMau(-0.6)
                    

        rong_rect = nv.nhanVat_hcn()
        for dan in nv9.getDSDan():
            dan_rect = dan.nhanVat_hcn()
            if kiemTraVaCham(rong_rect, dan_rect):
                
                # Nếu có va chạm, tạo một vụ nổ
                 
                goiVuNo(nv.getX(), nv.getY()) 
                nv9.xoaDan(dan)
                nv.setMau(-3)

        for v in dsVatP:
            v_rect = v.nhanVat_hcn()
            if kiemTraVaCham(hoangTu_rect, v_rect):
                if v.getLoaiVP1()==0:#vang
                    vang+=random.randint(100,500)
                    v.goiNhac(anVang)
                elif v.getLoaiVP1()==1:#mau
                    nv9.setMau(random.randint(1,20))
                    v.goiNhac(anMau)
                elif v.getLoaiVP1()==2:#ngoc
                    ngoc+=1
                    v.goiNhac(anNgoc)
                xoaVatPham(v)
        # Cập nhật và vẽ vụ nổ
        toanVuNo()

        for vuNo in dsVuNo:
            vuNo.getTG()

        manhinh.blit(thuThap, (0,10))

        text=font.render(str(vang ),True, (255,255,255))
        manhinh.blit(text,(170,30))

        text1=font.render(str(ngoc) ,True, (255,255,255))
        manhinh.blit(text1,(170,53))

        text2=font.render("00:"+str(phut) +":" +str(giay) ,True, (255,255,255))
        manhinh.blit(text2,(140,76))
        

        nv9.thanhMau()
        nv.thanhMau()
        #Thua
        if(nv9.getMau()<=0):
            phatAmThanh(nhacThua)
            Thua=True
            dangChoi=False
        if thoatKhoi!=None:
            if(kiemTraVaCham(nv9.nhanVat_hcn(),thoatKhoi.nhanVat_hcn())):
                thoatKhoi1=None
                if(int(phut)<=int(phutI) and int(giay)<int(giayI)):
                    phutI=phut
                    giayI=giay
                if int(vang)>int(vangNhieuI):
                    vangNhieuI=vang
                phatAmThanh(nhacThang)
                Thang=True
                dangChoi=False

        if(nv.getMau()<=0):
            if(int(phut)<=int(phutI) and int(giay)<int(giayI)):
                phutI=phut
                giayI=giay
            if int(vang)>int(vangNhieuI):
                vangNhieuI=vang
            phatAmThanh(nhacThang)
            Thang=True
            dangChoi=False

    if Thua:
        manhinh.blit(bgThua, (0,0))
        toaDoChuot=pygame.mouse.get_pos()
        text=font1.render(str(vang ),True, (255,255,255))
        manhinh.blit(text,(830,405))

        text1=font1.render(str(ngoc) ,True, (255,255,255))
        manhinh.blit(text1,(830,450))

        text2=font1.render("00:"+str(phut) +":" +str(giay),True, (255,255,255))
        manhinh.blit(text2,(830,360))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fo.write(f'{phutI}{giayI}{vangNhieuI}')
                fo.close()
                running = False
            if event.type==pygame.MOUSEBUTTONDOWN:
                if event.button==1:
                    if 555<=toaDoChuot[0]<=1010 and 560<=toaDoChuot[1]<=740:
                        manhinh.blit(click, toaDoChuot)
                        vang=0
                        ngoc=0
                        thoigian=0
                        giay=0
                        phut=0
                        dieuKien=0
                        
                        dsThachNhu.clear()
                        dsThienThach.clear()
                        dsVatP.clear()
                        dsVuNo.clear()
                        nv.traVeTrangThai()
                        nv9.traVeTrangThai()
                        Thua=False
                        trangChu=True

    if Thang:
        
        manhinh.blit(bgThang, (0,0))
        toaDoChuot=pygame.mouse.get_pos()
        text=font1.render(str(vang ),True, (255,255,255))
        manhinh.blit(text,(830,405))

        text1=font1.render(str(ngoc) ,True, (255,255,255))
        manhinh.blit(text1,(830,450))

        text2=font1.render("00:"+str(phut) +":" +str(giay),True, (255,255,255))
        manhinh.blit(text2,(830,360))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fo.write(f'{phutI}{giayI}{vangNhieuI}')
                fo.close()
                running = False
            if event.type==pygame.MOUSEBUTTONDOWN:
                if event.button==1:
                    if 555<=toaDoChuot[0]<=1010 and 560<=toaDoChuot[1]<=740:
                        thoatKhoi1=thoatKhoi=None
                        manhinh.blit(click, toaDoChuot)
                        vang=0
                        ngoc=0
                        thoigian=0
                        giay=0
                        phut=0
                        dieuKien=0
                        dsThachNhu.clear()
                        dsThienThach.clear()
                        dsVatP.clear()
                        dsVuNo.clear()
                        nv.traVeTrangThai()
                        nv9.traVeTrangThai()
                        Thang=False
                        trangChu=True
    pygame.display.flip()
pygame.quit()



    

    
    



    

   
    
    