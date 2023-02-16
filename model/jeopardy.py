
from flask import Flask,jsonify,request
from __main__ import app
from flask import request

questions = [
    {
        'category': 'UFC',
        'question': 'Who won the Welterweight title from Tyron Woodley',
        'answer': 'Kamaru Usman',
        'points' : '100'
    },
    {
        'category': 'UFC',
        'question': 'Who has most title defenses of all time?',
        'answer': 'Demetrius Johnson',
        'points' : '200'
    },
    {    
        'category': 'UFC',
        'question': 'Who was the first UFC Champ from England',
        'answer': 'Michael Bisping',
        'points' : '300'
    },
    {
        'category': 'UFC',
        'question': 'Who beat Connor Mcgregor at UFC 229?',
        'answer': 'Khabib',
        'points' : '400'
    },
    
    {
        'category': 'UFC',
        'question': 'Who has most wins in the UFC all time before a champsionship fight?',
        'answer': 'Jorge Masvidal',
        'points' : '500'
    },
    {
        'category': 'NFL',
        'question': 'Which round was Tom Brady Drafted in?',
        'answer': '6th',
        'points' : '100'
    },
    {
        'category': 'NFL',
        'question': 'Which NFL player has most rings?',
        'answer': 'Tom Brady',
        'points' : '200'
    },
    {    
        'category': 'NFL',
        'question': 'Which team won the first superbowl',
        'answer': 'Packers',
        'points' : '300'
    },
    {
        'category': 'NFL',
        'question': 'Which player retired during halftime',
        'answer': 'Vontae Davis',
        'points' : '400'
    },
    
    {
        'category': 'NFL',
        'question': 'Which overall pick was traded for AJ Brown',
        'answer': '18th',
        'points' : '500'
    },
    {
        'category': 'NBA',
        'question': 'Which team did Kareem Abdul Jabar play for as a rookie',
        'answer': 'Bucks',
        'points' : '100'
    },
    {
        'category': 'NBA',
        'question': 'Who leads in all time assits',
        'answer': 'John Stockton',
        'points' : '200'
    },
    {    
        'category': 'NBA',
        'question': 'When did Lebron leave Cleveland the first time',
        'answer': '2010',
        'points' : '300'
    },
    {
        'category': 'NBA',
        'question': 'Who was the most recent back to back MVP winner',
        'answer': 'Nikola Jokic',
        'points' : '400'
    },
    
    {
        'category': 'NBA',
        'question': 'How many career 3pts has Steph Curry made',
        'answer': '3302',
        'points' : '500'
    },
    {
        'category': 'MLB',
        'question': 'Who has the most home runs in MLB history',
        'answer': 'Barry Bonds',
        'points' : '100'
    },
    {
        'category': 'MLB',
        'question': 'Who has the most strikeouts in MLB history',
        'answer': 'Nolan Ryan',
        'points' : '200'
    },
    {    
        'category': 'MLB',
        'question': 'Who is the oldest Major Leaguer ever to hit a home run?',
        'answer': 'Julio Franco',
        'points' : '300'
    },
    {
        'category': 'MLB',
        'question': 'How many home runs did Aaron Judge have when he broke the record',
        'answer': '22',
        'points' : '400'
    },
    
    {
        'category': 'MLB',
        'question': 'How many intentional walks did Roger Maris get in his 61 home run season?',
        'answer': '0',
        'points' : '500'
    },
    {
        'category': 'Soccer',
        'question': 'Which team has the most LaLiga titles?',
        'answer': 'Real Madrid',
        'points' : '100'
    },
    {
        'category': 'Soccer',
        'question': 'How many world cups has Ronaldo Won',
        'answer': '0',
        'points' : '200'
    },
    {    
        'category': 'Soccer',
        'question': 'What year did Vinicius Jr. Transfer to Real Madrid',
        'answer': '2017',
        'points' : '300'
    },
    {
        'category': 'Soccer',
        'question': 'Which club is known as the "Red Devils" ?',
        'answer': 'Machester United',
        'points' : '400'
    },
    
    {
        'category': 'Soccer',
        'question': 'Who won the first Ballon dOR?',
        'answer': 'Stanley Matthews',
        'points' : '500'
    },
]

@app.route("/questions", methods=["GET"])
def get_questions():
    return jsonify(questions)

@app.route("/check_answer", methods=["POST"])
def check_answer():
    answer = request.get_json()["answer"]
    for question in questions:
        if answer == question["answer"]:
            return jsonify({"result": "Correct"})
    return jsonify({"result": "Incorrect"})

@app.route('/api/jeopardy')
def data():
    category = request.args.get('category')
    points = request.args.get('points')
    print(category,points)
    for question in questions:
        if category == question["category"] and points == question["points"]:
            return question["question"]
    return 'Not Found'


if __name__ == '__main__':
    app.run()
