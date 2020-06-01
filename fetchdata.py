from flask import Flask, jsonify, request
@app.route('/covid19', methods=['GET'])
def covid19():
    covid19_url = "https://api.covid19india.org/data.json"
    data = requests.get(covid19_url,verify=False)
    data = data.json()
    data = data["statewise"][0]

    data1 = {
            "confirmed" : data["confirmed"],
            "deltaconfirmed" : data["deltaconfirmed"],
            "active": int(data["active"]),
            "deltadeaths": data["deltadeaths"],
            "deaths": data["deaths"],
            "deltarecovered": data["deltarecovered"],
            "recovered": data["recovered"]
            }

    return jsonify(data1)
    
if __name__ == '__main__':
    app.run()
