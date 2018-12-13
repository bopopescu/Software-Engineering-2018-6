from recommend_app.models import Recommend
from product_mgr_app.models import Product
from account_app.models import Account

class interface:
    def __init__(self, username, maxProducts=5):
        self._noProducts = maxProducts
        self._username = username
        self._accountPK = None
        self._table_recommended = None
        self._product_list = list()

    def _set_accountPK(self):
        self._accountPK = Account.objects.get(user__username=self._username).id

    def _set_table(self):
        self._set_accountPK()
        table_recommended = Recommend.objects.filter(account_id=self._accountPK)
        sorted_table_recommended = table_recommended.order_by('-date')
        self._table_recommended = sorted_table_recommended[:self._noProducts]

    def _set_product_list(self):
        db_mgr = Product.objects
        for record in self._table_recommended:
            product = db_mgr.get(recommend=record)
            self._product_list.append(product)

    def get_recommend_list(self):
        self._set_accountPK()
        self._set_table()
        self._set_product_list()
        return self._product_list


    def test(self):
        # 추천리스트 불러오기
        #self._set_memberPK()
        #table = recommend.objects.filter(U_SN_id=self._memberPK)
        #table = table.order_by('-date')
        #return table

        # 추천리스트 불러와서 product_db 에서 내용 뽑아오기
        #self._set_memberPK()
        #self._set_table()
        #self._set_product_list()
        #return self._product_list
        pass
