from MyNode import *

class TestDrive:
    def main():
        ds = MyNode()
        ds.in_ds()

        # them
        print('a: them-----')
        so = 12
        print(f'Them {so}')
        ds.them(so)
        ds.in_ds()

        
        so = 10
        print(f'Them {so}')
        ds.them(so)
        ds.in_ds()

        # chen
        print('b: chen--------')
        so = 8
        vt = 0
        print(f'chen {so} vao vi tri {vt}')
        ds.chen(vt, so)
        ds.in_ds()

        # tim

        # xoa

        # cap nhat

        # xoa het


    if __name__ == '__main__':
        main()