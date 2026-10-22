total = int(input())
silver_count = 96
gold_count = silver_count // 16
silver_price = 48
silver_total = silver_price * silver_count
gold_price = (total - silver_total) // gold_count
print(gold_price)