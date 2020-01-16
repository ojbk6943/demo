class SellView:
    def show_sale_menu(self):
        print('*销售出库*')
        barcode = input('条码:')
        goodsserial = input('货号:')
        goodsname = input('品名：')
        unitprice = input('单价：')
        discountratio = input('折扣：')
        discountprice = input('折后单价：')
        buyquantity = input('购买数量：')
        subtotal =discountprice*int(buyquantity)
        # goodstype
        # goodssize
        # customerid
        # sellid
        # sellsumid
        # createtime

if __name__ == '__main__':
    pass