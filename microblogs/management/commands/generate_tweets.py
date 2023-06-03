import random
from django.core.management.base import BaseCommand, CommandError
from faker import Faker
from microblogs.models import User, Post

def generateTweets():
    templates = [
        "Just {verb} {object} and it feels amazing!",
        "{subject} is the {superlative} {noun} I've ever seen! #Impressed",
        "Feeling {adjective} after a {time_period} {activity}. #SelfCare",
        "Game day vibes! Let's go {team}! #Sports",
        "Spending the day {activity} with {number} {noun}. #FunTimes",
        "Congratulations to {subject} for an incredible {achievement}! #Celebration",
        "Practiced {activity} for {duration}. Hard work pays off! #Dedication",
        "{subject} inspires me to {verb} every day. #Motivation",
        "Enjoying a {weather} day while {activity}. #OutdoorFun",
        "Attending a {event} today. Excited to be a part of it! #Networking",
    ]

    football_templates = [
        "I'm in awe of {footballer}! What a player! ⚽️🔥",
        "{footballer} is a true legend of the game. 🙌⚽️",
        "Watching {footballer} play is a treat for football fans. ⚽️🎉",
        "{footballer} has incredible skills on the field. Truly mesmerizing! ⚽️😮",
        "No one can match the talent and finesse of {footballer}. A class apart! ⚽️💫",
        "I wish I could play like {footballer} someday. Truly inspiring! ⚽️🔝",
        "{footballer} is a game-changer. Always makes a difference on the field! ⚽️👏",
        "Every team dreams of having a player like {footballer}. What a gem! ⚽️💎",
        "{footballer} is the embodiment of excellence in football. ⚽️✨",
        "I can't get enough of {footballer}'s amazing skills. A joy to watch! ⚽️😍"
        "{footballer} is the GOAT 🐐"
    ]

    footballers = [
        "Messi",
        "Ronaldo",
        "Lewandowski",
        "Neymar",
        "Kylian Mbappé",
        "Kevin De Bruyne",
        "Karim Benzema",
        "Salah",
        "Harry Kane",
        "Erling Haaland",
        "Sadio Mané",
        "Bruno Fernandes",
        "Kimmich",
        "Manuel Neuer",
        "Van Dijk",
        "Modrić",
        "Ramos",
        "Sterling",
        "Oblak",
        "Kanté",
        "Saka",
        "Martinelli"
    ]

    verbs = [
        "completed",
        "achieved",
        "mastered",
        "conquered",
        "experienced",
        "enjoyed",
        "celebrated",
        "embraced",
        "unleashed",
        "discovered"
    ]

    objects = [
        "a challenging puzzle",
        "a new recipe",
        "a creative project",
        "an exciting adventure",
        "a thrilling roller coaster ride",
        "a captivating book",
        "a mesmerizing sunset",
        "a breathtaking view",
        "a hidden gem",
        "a magical moment"
    ]

    subject_adjectives = [
        "my friend",
        "my pet",
        "a random stranger",
        "a famous celebrity",
        "an adorable puppy",
        "an inspiring artist",
        "a talented musician",
        "a wise old man",
        "a curious child",
        "a brilliant scientist",
        "an alien from area 51"
    ]

    superlatives = [
        "most incredible",
        "amazing",
        "remarkable",
        "unbelievable",
        "jaw-dropping",
        "awe-inspiring",
        "extraordinary",
        "mind-blowing",
        "phenomenal",
        "unforgettable"
    ]

    nouns = [
        "singer",
        "dancer",
        "athlete",
        "chef",
        "writer",
        "actor",
        "explorer",
        "inventor",
        "dreamer",
        "inspiration"
    ]

    adjectives = [
        "amazing",
        "spectacular",
        "unbelievable",
        "mind-blowing",
        "phenomenal",
        "inspiring",
        "extraordinary",
        "incredible",
        "impressive",
        "unforgettable"
    ]

    time_periods = [
        "weekend",
        "vacation",
        "day off",
        "sabbatical",
        "summer break",
        "long weekend",
        "retreat",
        "staycation",
        "adventure-filled week",
        "relaxing stay"
    ]

    activities = [
        "exploring a new city",
        "learning a new language",
        "trying out a new hobby",
        "practicing mindfulness",
        "volunteering for a cause",
        "immersing myself in nature",
        "indulging in self-care",
        "embarking on a road trip",
        "discovering local cuisine",
        "capturing beautiful moments"
    ]

    teams = [
        "my favorite team",
        "the underdogs",
        "the champions",
        "the dream team",
        "the fearless warriors",
        "the mighty contenders",
        "the extraordinary athletes",
        "the unbeatable squad",
        "the passionate players",
        "the relentless competitors"
    ]

    numbers = [
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
        "ten",
        "a dozen"
    ]

    weathers = [
        "sunny",
        "breezy",
        "rainy",
        "snowy",
        "cloudy",
        "stormy",
        "windy",
        "clear",
        "foggy",
        "serene"
    ]

    events = [
        "fashion show",
        "art exhibition",
        "music concert",
        "film festival",
        "technology expo",
        "culinary competition",
        "science fair",
        "charity gala",
        "business summit",
        "cultural carnival"
    ]

    durations = [
        "hours",
        "the entire day",
        "a week",
        "months",
        "years",
        "a lifetime",
        "countless hours",
        "endless days",
        "eternity",
        "forever"
    ]

    achievements = [
        "achievement",
        "milestone",
        "victory",
        "breakthrough",
        "triumph",
        "feat",
        "success",
        "conquest",
        "glory",
        "accomplishment"
    ]

    def footballerTweet():
        footballer = random.choice(footballers)
        template = random.choice(football_templates)
        tweet = template.format(footballer=footballer)
        obj = User.objects.order_by('?').first()
        Post.objects.create(author=obj, text=tweet)

    def normalTweet():
        template = random.choice(templates)
        tweet = template.format(
            verb=random.choice(verbs),
            object=random.choice(objects),
            subject=random.choice(subject_adjectives),
            superlative=random.choice(superlatives),
            noun=random.choice(nouns),
            adjective=random.choice(adjectives),
            time_period=random.choice(time_periods),
            activity=random.choice(activities),
            team=random.choice(teams),
            number=random.choice(numbers),
            weather=random.choice(weathers),
            event=random.choice(events),
            duration=random.choice(durations),
            achievement=random.choice(achievements),
            footballer=random.choice(footballers)
        )
        obj = User.objects.order_by('?').first()
        Post.objects.create(author=obj, text=tweet)

    


    for _ in range(100):
        rand_choice = random.randint(1,4)
        if (rand_choice == 1):
            footballerTweet()
        else: 
            normalTweet()
                    
