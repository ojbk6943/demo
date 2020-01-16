
userinfo = (('admin', 'admin'), ('admin', ''), ('admin', 'ww123'), ('', 'admin'), ('', ''))
for idx, one in enumerate(userinfo):
        if idx==3:
           print(one)
           continue
        if idx == 4:
            print(one)
            continue
        print(idx)

