from flask import Flask, render_template, request, redirect, url_for
from Goods_algorithm import knapsack
from Shortest_path_algorithm import Graph

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/solutions', methods=['POST'])
def solutions():
    truck_capacity_str = request.form.get('truck_capacity', '')
    truck_capacity = int(truck_capacity_str) if truck_capacity_str.isdigit() else 0

    num_goods_str = request.form.get('num_goods', '')
    num_goods = int(num_goods_str) if num_goods_str.isdigit() else 0

    values = [int(request.form[f'value_{i+1}']) if request.form[f'value_{i+1}'].isdigit() else 0 for i in range(num_goods)]
    weights = [int(request.form[f'weight_{i+1}']) if request.form[f'weight_{i+1}'].strip() else 0 for i in range(num_goods)]

    max_value, total_weight, selected_items = knapsack(values, weights, truck_capacity)
    
    num_addresses_str = request.form.get('num_addresses', '')
    num_addresses = int(num_addresses_str) if num_addresses_str.isdigit() else 0

    travel_times = []
    for i in range(num_addresses):
        row = list(map(int, request.form.get(f'travel_time_{i+1}', '').split()))
        travel_times.append(row)

    graph = Graph(num_addresses)
    for i in range(num_addresses):
        for j in range(num_addresses):
            if i != j and i < len(travel_times) and j < len(travel_times[i]):
                graph.add_edge(i, j, travel_times[i][j])

    total_time, path = graph.tsp_greedy(0)

    return render_template('solutions.html', max_value=max_value, total_weight=total_weight,
                           selected_items=selected_items, total_time=total_time, path=path)

if __name__ == '__main__':
    app.run(debug=True)
