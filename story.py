text = ['Once upon a time, there was a ', ' named ', ' who lived on a ', '. They lived in a ', ' ', ' on the ',
        ' and worked at a ', ' on the base of the ', ' to provide for their ', '. Every morning, ', ' would ',
        ' up at ',
        ' and ', ' for their ', ' with the ', ' their ', ' ', ' and ', ' from their ', '. Then, every ',
        ' they would ',
        ' down the ', ' to ', ' to their ', ' and go to the ', '. ', ' was ', '. They ', ' their ', ', their ',
        ', and most importantly—their ', '. They would do anything to make sure that their ',
        ' was safe and healthy. Then, one night, there was a ', ' ', '. The ',
        ' sky filled with light briefly as a massive ', ' ', ' over the ', '. The ', ' hammered the roof of ',
        '’s little cottage. An intense ', ' woke ', ' from their sleep. It wasn’t ',
        ' before I went to bed, they thought. Just as they woke, they could hear a ', ' ', ' come from their ',
        ' pen. ',
        ' rushed out of bed and got on their ', ' and their ', ' and went to check on their ',
        's. “There, there” they told the ',
        's as they entered the coop “It’s only a little rain! There’s nothing to worry about.” ',
        ' stayed with their ', 's for a while and made sure that they were safe. They checked the ',
        ' of the coop to make sure it was secure. ', ' poured the ',
        's some more feed and went back to bed. Oh my, they thought, It’s ',
        '! I have to get to bed now so I can get up at ', ' to make ', '. As the ', ' slowed and the sun rose, ',
        ' slept, and they slept, and they slept. Finally, ',
        ' opened their eyes and rolled over to look at their clock. The clock read ', '! ',
        ' was going to be late for work! They ',
        ' out of bed and began to get dressed. They kissed their spouse as they slept and began to ', ' a ',
        '. They left it ', ' the ', ' ', ' where their spouse slept. They placed the ', ' on the ',
        ' and ran out of the ', ' and down the side of the ', '. ',
        ' knew their path like the back of their hand. They traveled the same way down the ', ' every ', ', every ',
        ' and ', ' catalogued in their brain. What ',
        ' didn’t know was that a big divot in the ground formed overnight when a ', ' fell in the ',
        ' and rolled down the hill. The divot was covered by some ', ' and some ',
        ', so it looked as if nothing was there. Suddenly, they tripped and fell into the hole in the ground. Pain '
        'shot through ',
        '’s ', ' and they let out a resounding ',
        '. They tried to get up to continue down the path, but to no avail. ', ' had injured their ',
        ' and they watched it lay there ', '. Luckily, a woman traveling back up the ', ' saw ',
        ' lying on the ground and stopped her ', '. The ', ' to her ', ' flew open and she rushed out toward ',
        '’s side. “Oh no! Are you okay?” she asked. “I wish! I just fell and I can no longer walk. I need to get '
        'down to my ',
        ' to make so I can ', ' some ', ', can you help me?” ',
        ' pleaded. “I may have something for you.” the woman said as she reached into her ', ' and pulled out a ',
        ' bottle filled with a ', ' ',
        '. “I carry this healing potion with me just in case I begin to feel faint, but I am willing to give it to '
        'you if you answer one question: what is the most important thing in your life?” “That’s easy! It’s my ',
        ', they’re the whole reason I’m in this mess in the first place.” ',
        ' explains to the woman that they had been rushing to ', ' ', ' so their ', ' could afford to ', ' for the ',
        '. “Perfect! I was worried when you spoke about work that you were only motivated by money, my potion only '
        'works on those who hold their loved ones closest to their heart. I will give you my potion so you can go to '
        'the ',
        '.” The woman uncorked the glass vial and handed it to ',
        '. Slowly, they drank the potion and began to feel a whizzing sensation through their body. Their ',
        ' began to move, and they regained their strength. The woman helped ', ' to get up and dust themselves off. ',
        ' thanked the woman and they began on their way down the ', ' as the woman smiled and returned to her ',
        '. In the end, ', ' got to their ', ' just on time to ', ' ', ' to buy some food for their ',
        '. That night, they made their ', ' a special dinner, filled with love and a little bit of magic. ']

full_replace = ['(living being1)', '(name1) ', '(land type1)', '(relative size1)', '(residence1)', '(land type1)',
                '(place to work1)', '(land type1)', '(group of people1)', '(name1) ', '(verb 1)', '(time of day 1)',
                '(routine item)', '(group of people1)', '(plural noun)', '(animal 1)', '(action verb 1)', '(noun 1)',
                '(animal 2)', '(time of day)', '(verb 2)', '(land type1)', '(verb 3)', '(product)', '(place 1)',
                '(name1)', '(emotion)', '(past tense objective verb 1)', '(thing to do- noun)',
                '(plural category of beings)', '(group of people1)', '(group of people1)', '(adjective)',
                '(weather event 1)', '(amount of light)', '(weather event) ', '(past tense verb)', '(land type1)',
                '(weather event)', '(name1) ', '(onomatopoeia)', '(name1) ', '(gerund of a weather event)',
                '(emotive adjective)', '(onomatopoeia)', '(animal 1)', '(name1)', '(article of clothing 1) ',
                '(article of clothing 2)', '(animal 1)', '(animal 1)', '(name1)', '(animal 1)', '(building piece)',
                '(name1)', '(animal 1)', '(time of day)', '(later time of day)', '(meal)', '(weather event 1)',
                '(name1)', '(name1)', '(even later time)', '(name1)', '(past tense verb)', '(verb 4)',
                '(object of verb 2)', '(preposition)', '(bedroom item 1)', '(directional phrase)', '(object of verb 2)',
                '(bedroom item 1)', '(residence 1)', '(land type1)', '(name1)', '(land type1)', '(time of day 1)',
                '(noun 2)', '(noun 3)', '(name1)', '(noun 4)', '(weather event 1)', '(outdoor noun)',
                '(outdoor plural noun) ', '(name1)', '(body part 1)', '(noise)', '(name1)', '(body part 2)', '(adverb)',
                '(land type1)', '(name1)', '(vehicle 1)', '(vehicle 1 part)', '(vehicle 1)', '(name1) ',
                '(place to work1)', '(verb 5)', '(product)', '(name1)', '(article of clothing 3)', '(relative size 2) ',
                '(color)', '(state of matter)', '(group of people1) ', '(name1) ', '(verb 5) ', '(product) ',
                '(group of people1)', '(verb 6)', '(time period) ', '(place 1) ', '(name1)', '(body part 2)', '(name1)',
                '(name1)', '(land type1)', '(vehicle)', '(name1)', '(place to work1)', '(verb 5) ', '(product)',
                '(group of people1)', '(group of people1)']


def main():
    # story_parts = to_replace.split("\n")
    # print(story_parts)
    print(len(text))
    print(len(full_replace))


if __name__ == '__main__':
    main()
