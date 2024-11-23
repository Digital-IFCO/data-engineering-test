import unittest
from pyspark.sql import SparkSession
from pyspark.sql import Row
from pyspark.sql.functions import lit
from challenge.challenge_4 import calculate_commissions

class TestCalculateCommissions(unittest.TestCase):
    def setUp(self):
        # Create SparkSession
        self.spark = SparkSession.builder.master("local").appName("TestCalculateCommissions").getOrCreate()

        # Sample orders data
        self.orders_data = self.spark.createDataFrame(
            [
                Row(order_id="order_1", salesowners="Leonard Cohen, Luke Skywalker, David Goliat"),
                Row(order_id="order_2", salesowners="Chris Pratt, David Goliat, Leonard Cohen"),
                Row(order_id="order_3", salesowners="Luke Skywalker"),
            ]
        )

        # Sample invoices data
        self.invoices_data = self.spark.createDataFrame(
            [
                Row(order_id="order_1", gross_value="324222", vat="0"),
                Row(order_id="order_2", gross_value="193498", vat="19"),
                Row(order_id="order_3", gross_value="500000", vat="21"),
            ]
        )

    def tearDown(self):
        self.spark.stop()

    def test_calculate_commissions(self):
        # Run the calculate_commissions function
        result = calculate_commissions(self.orders_data, self.invoices_data)

        # Expected output
        expected_data = self.spark.createDataFrame(
            [
                Row(sales_owner="Leonard Cohen", total_commission=209.42),
                Row(sales_owner="Chris Pratt", total_commission=94.04),
                Row(sales_owner="Luke Skywalker", total_commission=318.06),
                Row(sales_owner="David Goliat", total_commission=69.98),
            ]
        )

        # Sort and compare results
        result_sorted = result.orderBy("sales_owner").collect()
        expected_sorted = expected_data.orderBy("sales_owner").collect()
        self.assertEqual(result_sorted, expected_sorted)

if __name__ == "__main__":
    unittest.main()