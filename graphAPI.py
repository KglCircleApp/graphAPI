import facebook
from flask import Flask, jsonify

app = Flask(__name__)

access = "EAACEdEose0cBAIx46XmLVtW2eJizsB8KicXCddSk5hc8YZBOFDZB4gZASr40ZCuIQqomWNGfM4WvLImXZB25YtaLQops5Xw9K4TJS1O7Ou69aSdzZATSecUERynOkr1xFOJFlmuxZCzJg1DQ7mm4IRRia86EqA4O7U7mlSQO48BheyEdUYH7XkXfykQOqStOdxhyyLQ0ZB1WYwZDZD"
graph = facebook.GraphAPI(access_token=access, version="2.7")
group_id='118326262060941'



@app.route('/members')
def groupMembers(groupId=group_id):
        members = graph.get_object(id=group_id, fields='members')
        return jsonify({'members':members})


@app.route('/founder')
def groupFounder(groupId=group_id):
        founder = graph.get_object(id=group_id, fields='owner')
        return jsonify({'founder':founder})

@app.route('/description')
def groupDescription():
	des = graph.get_object(id=group_id, fields='description')
	return jsonify({'description':des})

@app.route('/name')
def groupName():
	name = graph.get_object(id=group_id, fields='name')
	return jsonify({'name':name})

@app.route('/feed')
def groupFeed():
        feed = graph.get_object(id=group_id, fields='feed')
        return jsonify({'feed':feed})

@app.route('/events')
def groupEvents():
        events = graph.get_object(id=group_id, fields='events')
        return jsonify({'events':events})




if __name__ == '__main__':
     app.run(debug=True)
