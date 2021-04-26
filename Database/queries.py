import mysql.connector
from mysql.connector import errorcode


def get_cnx(config):
    """
    Create connection to the MySQL server, return a MySQLConnection object.
    """
    try:
        cnx = mysql.connector.connect(**config)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        print(f"Successfully connected to database '{config['database']}'!")
        return cnx


class SellerAnalytics:
    """
    Analytics class of the e-commerce database
    containing useful querying methods.
    """
    def __init__(self, db_cfg, seller_id):
        """
        :param db_cfg: config dict of the database
        """
        self._cnx = get_cnx(db_cfg)
        self._cursor = self._cnx.cursor()
        self._seller_id = seller_id

    def login(self, seller_id):
        self._seller_id = seller_id

    @property
    def seller_id(self):
        return self._seller_id

    def my_selling_items(self, order_by='itemID', asc=False):
        """
        Get all items sold by this seller,
        ordered by some attributes in {'itemID', 'type', 'stock', 'quantity' (sales)}

        :param order_by: one of {'itemID', 'type', 'stock', 'status', 'quantity'}
        :param asc: Whether order is ascending
        :return: [(itemID, type, description, stock, quantity)]
        """
        assert order_by in ('itemID', 'type', 'stock', 'quantity'), \
            "can only order by one of {'itemID', 'type', 'stock', 'quantity'}!"

        self._cursor.execute(
            "SELECT items.itemID, type, description, stock, SUM(quantity) "
            "   FROM (SELECT itemID, quantity "
            f"       FROM (SELECT orderID FROM orders WHERE sellerID = {self.seller_id}) oid "
            "           NATURAL JOIN order_item"
            "         ) odit "
            "       RIGHT OUTER JOIN items USING (itemID)"
            f"WHERE sellerID = {self.seller_id} "
            "GROUP BY items.itemID "
            f"ORDER BY {order_by};"
        )
        return self._cursor.fetchall()

    # def my_selling_items_analytics(self):

    def item_info(self, item, order_by='itemID', asc=False):
        """
        Get related info about an item specified by item ID or description.

        :param item: ID or description of the item.
        :param order_by: one of {'itemID', 'type', 'description', 'stock'}.
        :param asc: Whether order is ascending
        """
        assert order_by in ('itemID', 'type', 'description', 'stock'), \
            "can only order by one of {'itemID', 'type', 'description', 'stock'}!"

        if isinstance(item, int):
            self._cursor.execute(
                "SELECT itemID, type, description, stock FROM items "
                f"WHERE itemID = {item} "
                f"ORDER BY {order_by} {'ASC' if asc else 'DESC'}"
            )
        elif isinstance(item, str):
            self._cursor.execute(
                "SELECT itemID, type, description, stock FROM items "
                f"WHERE description like '%{item}%' "
                f"ORDER BY {order_by} {'ASC' if asc else 'DESC'}"
            )
        else:
            raise NotImplementedError

        return self._cursor.fetchall()

    def my_orders(self, order_by='orderID', asc=False):
        """
        Get info of all orders of the seller.

        :param order_by: one of {'orderID', 'custID', 'time', 'status'}
        :param asc: Whether order is ascending
        :return: [
                   (
                   orderID, itemID, description, quantity,
                   custID, time, address, status
                   )
                ]
        """

        assert order_by in ('orderID', 'custID', 'time', 'status'), \
            "can only order by one of {'orderID', 'custID', 'time', 'status'}!"

        self._cursor.execute(
            "SELECT orders.orderID, custID, itemID, quantity, time, address, status "
            "FROM orders JOIN order_item USING (orderID) "
            f"WHERE orders.sellerID = {self.seller_id} "
            "GROUP BY orders.orderID "
            f"ORDER BY {order_by} "
        )
        return self._cursor.fetchall()


    # def



if __name__ == '__main__':
    cfg = {
        'user': 'root',
        'password': '1234',
        'database': 'csc3170'
    }

    ana = SellerAnalytics(cfg, seller_id=1)

    def disp(result):
        print('\n'.join(str(tup) for tup in result))

    print("My selling items, ordered by stock, ascending:")
    disp(ana.my_selling_items(order_by='stock', asc=True))

    print("My selling items, ordered by sales (quantity):")
    disp(ana.my_selling_items(order_by='quantity', asc=False))

    print("Item whose description contains '3935':")
    disp(ana.item_info(item="3935"))

    print("My orders:")
    disp(ana.my_orders())


