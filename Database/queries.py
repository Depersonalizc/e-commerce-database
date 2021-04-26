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
        self._cursor = self._cnx.cursor(dictionary=True)  # Hopefully this will make cursor return a dict
        self._seller_id = seller_id

    @property
    def seller_id(self):
        return self._seller_id

    def login(self, seller_id):
        self._seller_id = seller_id

    def my_selling_items(self, order_by='itemID', asc=False):
        """
        Get all items sold by this seller,
        ordered by some attributes in {'itemID', 'type', 'stock', 'SUM(quantity)', AVG(rating)}
        :param order_by: one of {'itemID', 'type', 'stock', 'status', 'SUM(quantity), AVG(rating)'}
        :param asc: Whether order is ascending
        :return: [{itemID, type, description, stock, SUM(quantity), AVG(rating)}]
        """
        options = {'itemID', 'type', 'stock', 'SUM(quantity)', 'AVG(rating)'}
        assert order_by in options, f"can only order by one of {options}!"

        self._cursor.execute(
            "SELECT items.itemID, type, description, stock, SUM(quantity), AVG(rating) "
            "   FROM (SELECT itemID, quantity, rating "
            f"       FROM (SELECT orderID FROM orders WHERE sellerID = {self.seller_id}) oid "
            "           NATURAL JOIN order_item"
            "         ) odit "
            "       RIGHT OUTER JOIN items USING (itemID)"
            f"WHERE sellerID = {self.seller_id} "
            "GROUP BY items.itemID "
            f"ORDER BY {order_by} {'ASC' if asc else 'DESC'};"
        )
        return self._cursor.fetchall()

    # def my_selling_items_analytics(self):

    def item_info(self, item, order_by='itemID', asc=False):
        """
        Get related info about an item specified by item ID or description.
        :param item: ID or description of the item.
        :param order_by: one of {'itemID', 'type', 'description', 'stock'}.
        :param asc: Whether order is ascending
        :return : [{itemID, type, description, stock}]
        """
        options = {'itemID', 'type', 'description', 'stock'}
        assert order_by in options, f"can only order by one of {options}!"

        if isinstance(item, int):
            self._cursor.execute(
                "SELECT itemID, type, description, stock FROM items "
                f"WHERE itemID = {item} "
                f"ORDER BY {order_by} {'ASC' if asc else 'DESC'};"
            )
        elif isinstance(item, str):
            self._cursor.execute(
                "SELECT itemID, type, description, stock FROM items "
                f"WHERE description like '%{item}%' "
                f"ORDER BY {order_by} {'ASC' if asc else 'DESC'};"
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
                   {
                   orderID, itemID, description, quantity,
                   custID, time, address, status
                   }
                ]
        """

        options = {'orderID', 'custID', 'time', 'status'}
        assert order_by in options, f"can only order by one of {options}!"

        self._cursor.execute(
            "SELECT orders.orderID, custID, itemID, quantity, time, address, status "
            "FROM orders JOIN order_item USING (orderID) "
            f"WHERE orders.sellerID = {self.seller_id} "
            "GROUP BY orders.orderID "
            f"ORDER BY {order_by} {'ASC' if asc else 'DESC'};"
        )
        return self._cursor.fetchall()

    def my_customers(self, order_by='custID', asc=False):
        """
        Get info of all customers of the seller.
                                                                    number of orders
        :param order_by: one of {'custID', 'cust_name', 'cust_age', 'COUNT(custID)'}
        :param asc: Whether order is ascending.
        :return: [{'custID', 'cust_name', 'cust_age', 'COUNT(custID)'}]
        """

        options = {'custID', 'cust_name', 'cust_age', 'COUNT(custID)'}
        assert order_by in options, f"can only order by one of {options}!"

        self._cursor.execute(
            "SELECT c.custID, c.cust_name, c.cust_gender, c.cust_age, COUNT(custID) "
            "FROM customers as c NATURAL JOIN orders WHERE sellerID = 1 "
            "GROUP BY custID "
            f"ORDER BY {order_by} {'ASC' if asc else 'DESC'};"
        )
        return self._cursor.fetchall()

    def rating_counts(self, asc=False):
        """
        Get counts of rating received.
        :param asc: If set True, return counts for rating 0, 1, ..., 10,
                           else, return counts for rating 10, 9, ..., 0.
        """

        self._cursor.execute(
            "SELECT COUNT(rating) "
            "FROM orders NATURAL JOIN order_item "
            "WHERE sellerID = 1 "
            "GROUP BY rating "
            f"ORDER BY rating {'ASC' if asc else 'DESC'};"
        )
        return self._cursor.fetchall()

    def sales_trend(self, timespan='monthly'):
        """
        Get trend of either daily, weekly, monthly, or yearly sales.
        :param timespan: one of {'daily', 'weekly', 'monthly', or 'yearly'}.
        """
        options = {'daily', 'weekly', 'monthly', 'yearly'}
        assert timespan in options, f"timespan can only be one of {options}!"

        seconds = {'daily': 86400,
                   'weekly': 604800,
                   'monthly': 2678400,
                   'yearly': 31556952}

        self._cursor.execute(
            "SELECT time, COUNT(orderID) "
            "FROM orders WHERE sellerID = 1 "
            f"GROUP BY UNIX_TIMESTAMP(time) DIV {seconds[timespan]} "
            "ORDER BY time;"
        )
        return self._cursor.fetchall()







if __name__ == '__main__':

    cfg = {
        'user': 'root',
        'password': '2333',
        'database': 'csc3170'
    }

    ana = SellerAnalytics(cfg, seller_id=1)

    def disp(result):
        print('\n'.join(str(tup) for tup in result))
        print()

    print("My selling items, ordered by stock, ascending:")
    disp(ana.my_selling_items(order_by='stock', asc=True))

    print("My selling items, ordered by SUM(quantity), descending    (sales):")
    disp(ana.my_selling_items(order_by='SUM(quantity)', asc=False))

    print("My selling items, ordered by AVG(rating), ascending:")
    disp(ana.my_selling_items(order_by='AVG(rating)', asc=True))

    print("Item whose description contains '3935':")
    disp(ana.item_info(item="3935"))

    print("My orders, ordered by time:")
    disp(ana.my_orders(order_by='time'))

    print("My customers, ordered by COUNT(custID) descending:")
    disp(ana.my_customers(order_by='COUNT(custID)', asc=False))

    print("Rating counts, descending from 10 to 0:")
    disp(ana.rating_counts(asc=False))

    print("Yearly sales trend:")
    disp(ana.sales_trend(timespan='yearly'))

