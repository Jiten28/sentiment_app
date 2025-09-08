from django.shortcuts import render
from textblob import TextBlob

def index(request):
    return render(request, 'sentiment/index.html')

def analyze(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        blob = TextBlob(text)
        polarity = round(blob.sentiment.polarity, 2)
        subjectivity = round(blob.sentiment.subjectivity, 2)

        if polarity > 0:
            sentiment = "Positive 😀"
        elif polarity < 0:
            sentiment = "Negative 😞"
        else:
            sentiment = "Neutral 😐"

        context = {
            'text': text,
            'polarity': polarity,
            'subjectivity': subjectivity,
            'sentiment': sentiment
        }
        return render(request, 'sentiment/result.html', context)
    return render(request, 'sentiment/index.html')
