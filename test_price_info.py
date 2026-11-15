import price_info

def test_total_cost():
    cost=price_info.total_cost_shopping()
    assert(cost==46.75)
    
def test_cost_fruit():
    cost=price_info.cost_of_fruits("orange",10)
    correct_cost=14
    assert(cost==correct_cost)