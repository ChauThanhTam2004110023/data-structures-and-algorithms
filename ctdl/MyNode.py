from Node import *

class MyNode:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def in_ds(self):
        stt = 0
        hien_tai = self.head
        kq = 'DS['
        while hien_tai != None:
            stt = stt + 1
            if stt == 1:
                kq = kq + ' ' + str(hien_tai.gia_tri)
            else:
                kq = kq + ' -> ' + str(hien_tai.gia_tri)
            hien_tai = hien_tai.nut_ke_tiep
        kq = kq + ' ]'
        print(kq)

    def them(self, gia_tri):
        nut = Node(gia_tri)
        if self.head == None:
            self.head = nut
            self.tail = nut
        else:
            self.tail.nut_ke_tiep = nut
            self.tail = nut

    def chen(self, chi_muc, gia_tri):
        nut = Node(gia_tri)
        truoc = None
        hien_tai = self.head
        i = 0
        while i < chi_muc and hien_tai != None:
            i = i + 1
            truoc = hien_tai
            hien_tai = hien_tai.nut_ke_tiep
        if truoc == None:
            # them dau ds
            nut.nut_ke_tiep = self.head
            self.head = nut
            if self.tail == None:
                self.tail = nut
        else:
            if hien_tai == None:
                # them cuoi ds
                self.tail.nut_ke_tiep = nut
                self.tail = nut
            else:
                # them giua ds
                truoc.nut_ke_tiep = nut
                nut.nut_ke_tiep = hien_tai


    def tim(self, gia_tri):
        pass

    def xoa(self, gia_tri):
        pass

    def cap_nhat(self, vi_tri, gia_tri):
        pass



        