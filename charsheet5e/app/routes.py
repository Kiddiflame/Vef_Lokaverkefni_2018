from flask import render_template, flash, redirect, url_for, request
from app import app

@app.route('/')
@app.route('/index')
def index():
    movie = {
        'name': 'Spiderman Homecoming',
        'body': ("Spider-Man: Homecoming is a 2017 American superhero film "
                "based on the Marvel Comics character Spider-Man, co-produced "
                "by Columbia Pictures and Marvel Studios, and distributed by "
                "Sony Pictures Releasing. It is the second Spider-Man film "
                "reboot and the sixteenth film in the Marvel Cinematic Universe "
                "(MCU). The film is directed by Jon Watts, from a screenplay by "
                "the writing teams of Jonathan Goldstein and John Francis Daley, "
                "Watts and Christopher Ford, and Chris McKenna and Erik Sommers. "
                "Tom Holland stars as Peter Parker / Spider-Man, alongside Michael "
                "Keaton, Jon Favreau, Zendaya, Donald Glover, Tyne Daly, "
                "Marisa Tomei, and Robert Downey Jr. In Spider-Man: Homecoming, "
                "Peter Parker tries to balance high school life with being Spider-Man, "
                "while facing the Vulture."),
        'pic': 'http://www.joblo.com/timthumb.php?src=/posters/images/full/Spiderman-poster-7-large.jpg&h=600&q=100'
    }
    return render_template("index.html", title='Forsíða', movie=movie)


@app.route('/leikarar')
def leikarar():
    actors = [
        {
            'name': 'Tom Holland',
            'body':("Born in England in 1996, Tom Holland joined "
                    "the London production of Billy Elliot the "
                    "Musical in 2008. He soon found success in film, "
                    "drawing strong reviews for his performance in "
                    "The Impossible (2012). Tapped to take over the "
                    "iconic role of Peter Parker/Spider-Man for the "
                    "big screen, Holland made his debut as the superhero "
                    "in Captain America: Civil War (2016), before "
                    "earning the chance to carry his own feature "
                    "with Spider-Man: Homecoming (2017)."),
            'pic': 'https://ia.media-imdb.com/images/M/MV5BNTAzMzA3NjQwOF5BMl5BanBnXkFtZTgwMDUzODQ5MTI@._V1_UY317_CR23,0,214,317_AL_.jpg'
        },
        {
            'name': 'Robert Downey Jr.',
            'body':("Born in New York City on April 4, 1965, Robert "
                    "Downey Jr. began acting as a young child. He made "
                    "his first film appearances and was a cast member on "
                    "Saturday Night Live in the 1980s, but his growing "
                    "success was marred by years of struggles with drug "
                    "abuse. Eventually turning his life around, he earned "
                    "a resurgence of critical and popular acclaim, and is "
                    "considered one of Hollywood's A-list actors."),
            'pic': 'https://ia.media-imdb.com/images/M/MV5BNzg1MTUyNDYxOF5BMl5BanBnXkFtZTgwNTQ4MTE2MjE@._V1_UX214_CR0,0,214,317_AL_.jpg'
        },
        {
            'name': 'Michael Keaton',
            'body':("Michael Keaton was born on September 5, "
                    "1951 in McKees Rocks, Penn. He attended "
                    "Kent State, but dropped out to pursue acting. "
                    "After some false starts in television, Keaton "
                    "had his first hit with Mr. Mom. He later worked "
                    "with directors Tim Burton (Beetlejuice, Batman), "
                    "Kenneth Branagh and Quentin Tarantino, and in the "
                    "new millennium won great acclaim for his "
                    "Oscar-nominated lead role in the drama Birdman, "
                    "for which he also won a Golden Globe."),
            'pic': 'https://ia.media-imdb.com/images/M/MV5BMTk4NTE2MzczOF5BMl5BanBnXkFtZTYwNTM4MjYz._V1_UY317_CR21,0,214,317_AL_.jpg'
        },
        {
            'name': 'Marissa Tomei',
            'body': ("Born in Brooklyn in 1964, Marisa Tomei got her "
                    "start acting on TV in shows like As the World Turns "
                    "and A Different World. She went on to become a "
                    "highly successful film actress, starring in projects "
                    "like My Cousin Vinny, for which she earned an Academy "
                    "Award, In the Bedroom and The Wrestler."),
            'pic': 'https://ia.media-imdb.com/images/M/MV5BMTUwMjA3OTc3N15BMl5BanBnXkFtZTcwNTA1MzY1Mw@@._V1_UY317_CR12,0,214,317_AL_.jpg'
        }
    ]
    return render_template("actors.html", title='Leikarar', actors=actors)

@app.route('/contact')
def contact():
    return render_template("contact.html", title='Hafa samband')