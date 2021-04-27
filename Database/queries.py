import mysql.connector
from mysql.connector import errorcode
from typing import Union


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
    Seller-end Analytics of the e-commerce database
    containing useful querying methods.
    """
    def __init__(self, cnx, seller_id=None):
        """
        :param cnx: MySQLConnection object returned by get_cnx()
        :param seller_id: ID of seller
        """
        self._cnx = cnx
        self._cursor = self._cnx.cursor(dictionary=True)  # Hopefully this will make cursor return a dict
        self._seller_id = seller_id

    @property
    def seller_id(self):
        return self._seller_id

    def login(self, seller_id):
        self._seller_id = seller_id

    def my_selling_items(self, description='', order_by='itemID', asc=False):
        """
        Get all items currently sold by this seller,
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
            f"WHERE sellerID = {self.seller_id} AND description LIKE '%{description}%'"
            "GROUP BY items.itemID "
            f"ORDER BY {order_by} {'ASC' if asc else 'DESC'};"
        )
        return self._cursor.fetchall()

    def item_info(self, item: Union[int, str], order_by='itemID', asc=False):
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
                                                                 [number of orders made]
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
            f"FROM orders WHERE sellerID = {self.seller_id} "
            f"GROUP BY UNIX_TIMESTAMP(time) DIV {seconds[timespan]} "
            "ORDER BY time;"
        )
        return self._cursor.fetchall()

    def competing_sellers(self, type='Food', k=2, order_by='COUNT(DISTINCT orderID)'):
        """
        Get info about top k competing sellers ordered by sales or rating.
        :param order_by: one of {'COUNT(DISTINCT orderID)', 'AVG(rating)'}.
        """
        options = {'COUNT(DISTINCT orderID)', 'AVG(rating)'}
        assert order_by in options, f"can only order by one of {options}!"

        self._cursor.execute(
            f"SELECT sellerID, seller_name, {order_by} "
            "FROM(SELECT orderID, sellerID FROM orders) o "
            "NATURAL JOIN sellers "
            "NATURAL JOIN(SELECT orderID, itemID, rating FROM order_item) oi "
            f"NATURAL JOIN(SELECT itemID, type FROM items WHERE type = '{type}') it "
            f"WHERE sellerID != {self.seller_id} "
            "GROUP BY sellerID "
            f"ORDER BY {order_by} DESC LIMIT {k};"
        )
        return self._cursor.fetchall()

    def customer_distribution(self, group_by='cust_gender'):
        options = {'cust_gender', 'address'}
        assert group_by in options, f"can only order by one of {options}!"

        self._cursor.execute(
            f"""
            SELECT
            {group_by}, COUNT(DISTINCT custID) FROM
            customers as c
            NATURAL
            JOIN
            orders
            WHERE
            sellerID = {self.seller_id}
            GROUP
            BY
            {group_by}
            """
        )

        return self._cursor.fetchall()



class CustomerAnalytics:
    """
    Buyer-end Analytics of the e-commerce database
    containing useful querying methods.
    """
    def __init__(self, cnx, cust_id=None):
        """
        :param cnx: MySQLConnection object returned by get_cnx()
        :param cust_id: ID of customer
        """
        self._cnx = cnx
        self._cursor = self._cnx.cursor(dictionary=True)  # Hopefully this will make cursor return a dict
        self._cust_id = cust_id

    @property
    def cust_id(self):
        return self._cust_id

    def login(self, cust_id):
        self._cust_id = cust_id

    def my_orders(self, order_by='orderID', asc=False):
        """
        Get info of all orders of the buyer.
        :param order_by: one of {'orderID', 'sellerID', 'time', 'status'}
        :param asc: Whether order is ascending
        :return: [
                   {
                   orderID, itemID, description, quantity,
                   sellerID, time, address, status
                   }
                ]
        """

        options = {'orderID', 'sellerID', 'time', 'status'}
        assert order_by in options, f"can only order by one of {options}!"

        self._cursor.execute(
            "SELECT orders.orderID, sellerID, itemID, quantity, time, address, status "
            "FROM orders JOIN order_item USING (orderID) "
            f"WHERE orders.custID = {self.cust_id} "
            "GROUP BY orders.orderID "
            f"ORDER BY {order_by} {'ASC' if asc else 'DESC'};"
        )
        return self._cursor.fetchall()

    def search_item(self, description: str, order_by='SUM(quantity)', asc=False):
        """
        Returns all items who description string is contained in `description`
        :param description: description of the item to search
        :param order_by: one of {'itemID', 'type', 'description', 'sellerID', 'SUM(quantity)' [sales], 'AVG(rating)'}.
        :param asc: Whether order is ascending
        :return : [{itemID, type, description, sellerID, SUM(quantity), AVG(rating)}]
        """
        options = {'itemID', 'type', 'description', 'sellerID', 'SUM(quantity)', 'AVG(rating)'}
        assert order_by in options, f"can only order by one of {options}!"

        self._cursor.execute(
            "SELECT items.itemID, type, description, sellerID, SUM(quantity), AVG(rating) "
            "   FROM (SELECT itemID, quantity, rating "
            f"       FROM (SELECT orderID FROM orders) oid "
            "           NATURAL JOIN order_item"
            "         ) odit "
            "       RIGHT OUTER JOIN items USING (itemID)"
            f"WHERE description like '%{description}%' "
            "GROUP BY items.itemID "
            f"ORDER BY {order_by} {'ASC' if asc else 'DESC'};"
        )
        return self._cursor.fetchall()

    def search_seller(self, seller: Union[int, str], order_by='SUM(quantity)', asc=False):
        """
        Returns all sellers whose name string is contained in `seller`, or directly by sellerID.
        :param seller: either seller's ID or name
        :param order_by: one of {'sellerID', 'seller_name', 'description', 'sellerID',
                                 'COUNT(DISTINCT orderID)' [number of orders], 'AVG(rating)'}.
        TODO: order by major types?
        :param asc: Whether order is ascending
        :return : [{sellerID, seller_name, COUNT(DISTINCT orderID), AVG(rating)}]
        """
        options = {'itemID', 'type', 'description', 'sellerID',
                   'COUNT(DISTINCT orderID)', 'AVG(rating)'}
        assert order_by in options, f"can only order by one of {options}!"

        if isinstance(seller, int):
            self._cursor.execute(
                "SELECT sellerID, seller_name, COUNT(DISTINCT orderID), AVG(rating) "
                "FROM (SELECT * FROM sellers WHERE sellerID = 1) s "
                "LEFT OUTER JOIN (SELECT orderID, sellerID FROM orders) o "
                "NATURAL JOIN order_item "
                "USING (sellerID);"
            )

        elif isinstance(seller, str):
            self._cursor.execute(
                "SELECT sellerID, seller_name, COUNT(DISTINCT orderID), AVG(rating) "
                f"FROM (SELECT * FROM sellers WHERE seller_name like '%{seller}%') s "
                "LEFT OUTER JOIN (SELECT orderID, sellerID FROM orders) o "
                "USING (sellerID) "
                "NATURAL JOIN order_item oi "
                "GROUP BY sellerID "
                f"ORDER BY {order_by} {'ASC' if asc else 'DESC'};"
            )

        return self._cursor.fetchall()




if __name__ == '__main__':

    def disp(result):
        print('\n'.join(str(tup) for tup in result))
        print()

    cfg = {
        'user': 'root',
        'password': '1234',
        'database': 'csc3170'
    }
    cnx = get_cnx(cfg)
    seller = SellerAnalytics(cnx, seller_id=7)
    customer = CustomerAnalytics(cnx, cust_id=1)

    # SELLER-END ANALYTICS
    print('------------SELLER-END ANALYTICS------------')

    # print("My selling items containing letter 'th', ordered by stock, ascending:")
    # disp(seller.my_selling_items(description='th', order_by='stock', asc=True))
    #
    # print("My selling items, ordered by SUM(quantity), descending    (sales):")
    # disp(seller.my_selling_items(order_by='SUM(quantity)', asc=False))
    #
    # print("My selling items, ordered by AVG(rating), ascending:")
    # disp(seller.my_selling_items(order_by='AVG(rating)', asc=True))
    #
    # print("Item whose description contains '3935':")
    # disp(seller.item_info(item="3935"))
    #
    # print("My orders, ordered by time:")
    # disp(seller.my_orders(order_by='time'))
    #
    # print("My customers, ordered by COUNT(custID) descending:")
    # disp(seller.my_customers(order_by='COUNT(custID)', asc=False))
    #
    # print("Rating counts, descending from 10 to 0:")
    # disp(seller.rating_counts(asc=False))
    #
    # print("Top 2 competing sellers of type 'Food' with highest number of orders:")
    # disp(seller.competing_sellers(type='Food', k=2, order_by='COUNT(DISTINCT orderID)'))
    #
    # print("Monthly sales trend:")
    # disp(seller.sales_trend(timespan='monthly'))
    disp(seller.customer_distribution(group_by='address'))
    #
    # # CUSTOMER-END ANALYTICS
    # print('------------CUSTOMER-END ANALYTICS------------')
    #
    # print("My orders, ordered by time:")
    # disp(customer.my_orders(order_by='time', asc=True))
    #
    # print("All items whose description contain 'a', ordered by sales:")
    # disp(customer.search_item(description='ab', order_by='SUM(quantity)', asc=False))
    #
    # print("All sellers whose name contains 'Bab', ordered by average rating:")
    # disp(customer.search_seller(seller='Bab', order_by='AVG(rating)', asc=False))

