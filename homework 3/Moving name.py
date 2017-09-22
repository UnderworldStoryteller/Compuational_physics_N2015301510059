i=0

while i<7:                                                                             #主体循环结构
    k=0
    while k<=i:                                                                        #循环内部实现循环以求文字移动
        print('    ', end = " ");                                                      #在文字前输出空格
        k=k+1
    print("    #####   ###   ###   ###    #   ######         ")


    m=0
    while m<=i:
        print('    ', end = " ");
        m=m+1
    print("       #     #    #     # ##   #   #              ")

    n=0
    while n<=i:
        print('    ', end = " ");
        n=n+1
    print("       #     #    #     #  ##  #   ######         ")

    q=0
    while q<=i:
        print('    ', end = " ");
        q=q+1
    print("       #     #    #     #   ## #   #              ")

    p=0
    while p<=i:
        print('    ', end = " ");
        p=p+1
    print("     ###     ######     #    ###   ######         ")
    i=i+1
    import time                                                                       #引入时间函数
    time.sleep(1)                                                                     
    import os                                                                         #清屏
    os.system('cls')
    time.sleep(1)                                                                     #暂停一秒实现闪动
