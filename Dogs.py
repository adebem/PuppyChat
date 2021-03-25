# Dogs.py
# All of the information in this dictionary was gained from the American Kennel Club's website.

# A dictionary containing information about:
#     the top 60 most popular dog breeds according to the American Kennel Club in 2019
# Organized alphabetically into indexes.
# Each entry contains each breed's temperament, height, weight, lifespan, group membership, description (short and
# long), and nicknames (optional).

dogInfo = {
    'a': {
        'Airedale_Terrier': {
            'temperament': ['friendly', 'clever', 'courageous'],
            'height': 23,
            'weight': [50, 70],
            'lifespan': [11, 14],
            'group': 'terrier',
            'description_short':
                '   His size, strength, and unflagging spirit have earned the Airedale Terrier the nickname \'The\n'
                'King of Terriers.\' The Airedale stands among the world’s most versatile dog breeds and has\n'
                'distinguished himself as hunter, athlete, and companion.\n',
            'description_long':
                '   The Airedale Terrier is the largest of all terrier breeds. Males stand about 23 inches at the\n'
                'shoulder, females a little less. The dense, wiry coat is tan with black markings. Long, muscular\n'
                'legs give Airedales a regal lift in their bearing, and the long head—with its sporty beard and\n'
                'mustache, dark eyes, and neatly folded ears—conveys a keen intelligence. Airedales are the very\n'
                'picture of an alert and willing terrier—only bigger. And, like his smaller cousins in the terrier\n'
                'family, he can be bold, determined, and stubborn. Airedales are docile and patient with kids but\n'
                'won’t back down when protecting hearth and home. Thanks to their famous do-it-all attitude,\n'
                'Airedales excel in all kinds of sports and family activities.\n',
            'nicknames': {'Airedale'}
        },

        'Akita': {
            'temperament': ['courageous', 'dignified', 'profoundly loyal'],
            'height': {'male': [26, 28], 'female': [24, 26]},
            'weight': {'male': [100, 130], 'female': [70, 100]},
            'lifespan': [10, 13],
            'group': 'working',
            'description_short':
                '   Akitas are muscular, double-coated dogs of ancient Japanese lineage famous for their dignity,\n'
                'courage, and loyalty. In their native land, they are venerated as family protectors and symbols of\n'
                'good health, happiness, and long life.\n',
            'description_long':
                '   Akitas are burly, heavy-boned spitz-type dogs of imposing stature. Standing 24 to 28 inches at\n'
                'the shoulder, Akitas have a dense coat that comes in several colors, including white. The head is\n'
                'broad and massive, and is balanced in the rear by a full, curled-over tail. The erect ears and dark,\n'
                'shining eyes contribute to an expression of alertness, a hallmark of the breed.\n\n'
                '   Akitas are quiet, fastidious dogs. Wary of strangers and often intolerant of other animals,\n'
                'Akitas will gladly share their silly, affectionate side with family and friends. They thrive on\n'
                'companionship. The large, independent-thinking Akita is hardwired for protecting those they love.\n'
                'They must be well socialized from birth with people and other dogs.\n',
            'nicknames': {'Akita_Inu'}
        },

        'American_Bulldog': {
            'temperament': ['loyal', 'self-confident'],
            'height': {'male': [22, 25], 'female': [20, 23]},
            'weight': {'male': [75, 100], 'female': [60, 80]},
            'lifespan': [10, 12],
            'group': 'foundation stock service',
            'description_short':
                '   American Bulldogs are a well-balanced athletic dog that demonstrate great strength, endurance,\n'
                'agility, and a friendly attitude. Historically, they were bred to be a utility dog used for working\n'
                'the farm.\n',
            'description_long':
                '   The American Bulldog is a descendant of the English Bulldog. It is believed that the bulldog was\n'
                'in America as early as the 17th century. They came to the United States in the 1800s, with\n'
                'immigrants who brought their working bulldogs with them. Small farmers and ranchers used this\n'
                'all-around working dog for many tasks including farm guardians, stock dogs, and catch dogs. The\n'
                'breed largely survived, particularly in the southern states, due to its ability to bring down and\n'
                'catch feral pigs.\n\n'
                '   The breed we know as the American Bulldog was originally known by many different names before the\n'
                'name American Bulldog became the standard. In different parts of the South he was known as the White\n'
                'English Southern Bulldog, but most commonly just “bulldog.” The breed was not called a bulldog\n'
                'because of a certain look, but because they did real bulldog work.\n'
        },

        'Australian_Cattle_Dog': {
            'temperament': ['alert', 'curious', 'pleasant'],
            'height': {'male': [18, 20], 'female': [17, 19]},
            'weight': [35, 50],
            'lifespan': [12, 16],
            'group': 'herding',
            'description_short':
                '    The compact but muscular Australian Cattle Dog, also called Blue Heeler or Queensland Heeler,is\n'
                'related to Australia’s famous wild dog, the Dingo. These resilient herders are intelligent enough to\n'
                'routinely outsmart their owners.\n',
            'description_long':
                '   Standing between 17 to 20 inches at the shoulder, the Australian Cattle Dog is a sturdy, \n'
                'hard-muscled herder of strength and agility. The ACD is born with a white coat that turns blue-gray\n'
                ' or red. Both coat varieties feature distinctive mottling or specking patterns. ACDs have immense\n'
                'work drive and excel at hunting, chasing, and, of course, moving livestock. Their boundless energy\n'
                'and supple gait make them excellent running partners.\n\n'
                '   ACDs are true-blue loyal, famously smart, ever alert, and wary of strangers. If an ACD isn’t\n'
                'challenged, he easily becomes bored and gets into mischief. It is recommended that ACD owners\n'
                'participate with their dog in some work, sport, or regular exercise to keep him mentally and\n'
                'physically fit.\n',
            'nicknames': {'ACD', 'Heeler', 'Queensland', 'Queensland_Heeler', 'Blue_Heeler', 'Red_Heeler'}
        },

        'Australian_Shepherd': {
            'temperament': ['smart', 'word-oriented', 'exuberant'],
            'height': {'male': [20, 23], 'female': [18, 21]},
            'weight': {'male': [50, 65], 'female': [40, 55]},
            'lifespan': [12, 15],
            'group': 'herding',
            'description_short':
                '   The Australian Shepherd, a lean, tough ranch dog, is one of those “only in America” stories: a\n'
                'European breed perfected in California by way of Australia. Fixtures on the rodeo circuit, they are\n'
                'closely associated with the cowboy life.\n',
            'description_long':
                '   The Australian Shepherd, the cowboy’s herding dog of choice, is a medium-sized worker with a\n'
                'keen, penetrating gaze in the eye. Aussie coats offer different looks, including merle (a mottled\n'
                'pattern with contrasting shades of blue or red). In all ways, they’re the picture of rugged and\n'
                'agile movers of stock. Aussies exhibit an irresistible impulse to herd, anything: birds, dogs, kids.\n'
                'This strong work drive can make Aussies too much dog for a sedentary pet owner. Aussies are\n'
                'remarkably intelligent, quite capable of hoodwinking an unsuspecting novice owner. In short, this\n'
                'isn’t the pet for everyone. But if you’re looking for a brainy, tireless, and trainable partner for\n'
                'work or sport, your search might end here.\n'
        },
    },

    'b': {
        'Basset_Hound': {
            'temperament': ['charming', 'patient', 'low-key'],
            'height': (15, 'and under'),
            'weight': [40, 65],
            'lifespan': [12, 13],
            'group': 'hound',
            'description_short':
                '   Among the most appealing of the AKC breeds, the endearing and instantly recognizable Basset Hound\n'
                'is a perennial favorite of dog lovers all over the world. This low-slung and low-key hound can be\n'
                'sometimes stubborn, but is always charming.\n',
            'description_long':
                '   The Basset Hound stands no higher than 14 inches at the shoulder but, with his remarkably heavy\n'
                'bone, powerful little legs, and massive paws, he possesses big-dog strength and stamina. Bassets are\n'
                'famous for a large, domed head that features extremely long, velvety ears, mournful eyes, and a\n'
                'wrinkled brow, which give the breed the look of a sad clown. Built more for endurance than speed,\n'
                'the Basset moves in a deliberate but effortless manner. The breed’s scenting ability is uncanny;\n'
                'it’s said that among dogs only the Bloodhound’s nose is more accurate. Mild and agreeable at home,\n'
                'the Basset is stubborn on the trail and barks in a loud, ringing voice. Although they may not be\n'
                'wildly demonstrative in their affections, they are steadfastly loyal.\n',
        },

        'Beagle': {
            'temperament': ['friendly', 'curious', 'merry'],
            'height': [13, [13, 15]],
            'weight': [19, [20, 30]],
            'lifespan': [10, 15],
            'group': 'hound',
            'description_short':
                '   Not only is the Beagle an excellent hunting dog and loyal companion, it is also happy-go-lucky,\n'
                'funny, and—thanks to its pleading expression—cute. They were bred to hunt in packs, so they enjoy\n'
                'company and are generally easygoing.\n',
            'description_long':
                '   There are two Beagle varieties: those standing under 13 inches at the shoulder, and those between\n'
                '13 and 15 inches. Both varieties are sturdy, solid, and “big for their inches,” as dog folks say.\n'
                'They come in such pleasing colors as lemon, red and white, and tricolor. The Beagle’s fortune is in\n'
                'his adorable face, with its big brown or hazel eyes set off by long, houndy ears set low on a broad\n'
                'head.\n\n'
                '   A breed described as “merry” by its fanciers, Beagles are loving and lovable, happy, and\n'
                'companionable—all qualities that make them excellent family dogs. No wonder that for years the\n'
                'Beagle has been the most popular hound dog among American pet owners. These are curious, clever, and\n'
                'energetic hounds who require plenty of playtime.\n'
        },

        'Belgian_Malinois': {
            'temperament': ['confident', 'smart', 'hardworking'],
            'height': {'male': [24, 26], 'female': [22, 24]},
            'weight': {'male': [60, 80], 'female': [40, 60]},
            'lifespan': [14, 16],
            'group': 'herding',
            'description_short':
                '   The smart, confident, and versatile Belgian Malinois is a world-class worker who forges an\n'
                'unbreakable bond with his human partner. To deny a Mal activity and the pleasure of your company is\n'
                'to deprive him of his very reasons for being.\n',
            'description_long':
                '   Belgian Malinois are squarely built, proud, and alert herders standing 22 to 26 inches. Strong\n'
                'and well-muscled, but more elegant than bulky, there’s an honest, no-frills look about them, as\n'
                'befit dogs built to work hard for their feed. A breed hallmark is the proud carriage of the head.\n'
                'Coat colors range from a rich fawn to mahogany. The black ears and mask accentuate bright,\n'
                'questioning eyes the color of dark Belgian chocolate.\n\n'
                '   If you have ever seen a Mal perform an obedience routine, you know firsthand what a smart and\n'
                'eager breed this is. Problems set in, though, when this people-oriented dog is underemployed and\n'
                'neglected. Exercise, and plenty of it, preferably side by side with their adored owner, is key to\n'
                'Mal happiness.\n',
            'nicknames': {'Mal'}
        },

        'Bernese_Mountain_Dog': {
            'temperament': ['good-natured', 'calm', 'strong'],
            'height': {'male': [25, 27.5], 'female': [23, 26]},
            'weight': {'male': [80, 115], 'female': [70, 95]},
            'lifespan': [7, 10],
            'group': 'working',
            'description_short':
                '   Big, powerful, and built for hard work, the Bernese Mountain Dog is also strikingly beautiful and\n'
                'blessed with a sweet, affectionate nature. Berners are generally placid but are always up for a romp\n'
                'with the owner, whom they live to please.\n',
            'description_long':
                '   The Bernese Mountain Dog is a large, sturdy worker who can stand over 27 inches at the shoulder.\n'
                'The thick, silky, and moderately long coat is tricolored: jet black, clear white, and rust. The\n'
                'distinctive markings on the coat and face are breed hallmarks and, combined with the intelligent\n'
                'gleam in the dark eyes, add to the Berner’s aura of majestic nobility. A hardy dog who thrives in\n'
                'cold weather, the Berner’s brain and brawn helped him multitask on the farms and pastures of\n'
                'Switzerland.\n\n'
                '   Berners get along with the entire family and are particularly gentle with children, but they will\n'
                'often become more attached to one lucky human. Berners are imposing but not threatening, and they\n'
                'maintain an aloof dignity with strangers.\n',
            'nicknames': {'Bernese', 'Berner'}
        },

        'Bichon_Frise': {
            'temperament': ['playful', 'curious', 'peppy'],
            'height': [9.5, 11.5],
            'weight': [12, 18],
            'lifespan': [14, 15],
            'group': 'non-sporting',
            'description_short':
                '   The small but sturdy and resilient Bichon Frise stands among the world’s great \'personality\n'
                'dogs.\' Since antiquity, these irresistible canine comedians have relied on charm, beauty, and\n'
                'intelligence to weather history’s ups and downs.\n',
            'description_long':
                '   A good-size Bichon will stand a shade under a foot tall at the shoulder. The breed’s glory is a\n'
                'white hypoallergenic coat, plush and velvety to the touch, featuring rounded head hair that sets off\n'
                'the large, dark eyes and black leathers of the nose and lips.\n\n'
                '   Bichons are adaptable companions who get on well with other dogs and children. Alert and curious,\n'
                'Bichons make nice little watchdogs—but they are lovers, not fighters, and operate under the\n'
                'assumption that there are no strangers, just friends they haven’t met yet. Their confidence and size\n'
                'make them ideal city dogs. Bichons train nicely and enjoy performing for their loved ones. Finally,\n'
                'there’s the happy-go-lucky Bichon personality that draws smiles and hugs wherever they go.\n',
            'nicknames': {'Bichon'}
        },

        'Bloodhound': {
            'temperament': ['friendly', 'independent', 'inquisitive'],
            'height': {'male': [25, 27], 'female': [23, 25]},
            'weight': {'male': [90, 110], 'female': [80, 100]},
            'lifespan': [10, 12],
            'group': 'hound',
            'description_short':
                '   The world famous “Sleuth Hound” does one thing better than any creature on earth: find people who\n'
                'are lost or hiding. An off-duty Bloodhound is among the canine kingdom’s most docile citizens, but\n'
                'he’s relentless and stubborn on scent.\n',
            'description_long':
                '   Bloodhounds are large, substantial dogs standing 23 to 27 inches at the shoulder and weighing up\n'
                'to 110 pounds. Their most famous features are a long, wrinkled face with loose skin; huge, drooping\n'
                'ears; and warm, deep-set eyes that complete an expression of solemn dignity. Coat colors can be\n'
                'black and tan, liver and tan, or red. Powerful legs allow Bloodhounds to scent over miles of\n'
                'punishing terrain.\n\n'
                '   As pack dogs, Bloodhounds enjoy company, including other dogs and kids. They are easygoing, but\n'
                'their nose can sometimes lead them into trouble. A strong leash and long walks in places where they\n'
                'can enjoy sniffing around are recommended. Bloodhounds are droolers, and obedience training these\n'
                'sensitive sleuths can be a challenge.\n',
            'nicknames': {'Blood_Hound'}
        },

        'Border_Collie': {
            'temperament': ['affectionate', 'smart', 'energetic'],
            'height': {'male': [19, 22], 'female': [18, 21]},
            'weight': [30, 55],
            'lifespan': [12, 15],
            'group': 'herding',
            'description_short':
                '   A remarkably bright workaholic, the Border Collie is an amazing dog—maybe a bit too amazing for\n'
                'owners without the time, energy, or means to keep it occupied. These energetic dogs will settle down\n'
                'for cuddle time when the workday is done.\n',
            'description_long':
                '   Borders are athletic, medium-sized herders standing 18 to 22 inches at the shoulder. The overall\n'
                'look is that of a muscular but nimble worker unspoiled by passing fads. Both the rough coat and the\n'
                'smooth coat come in a variety of colors and patterns.\n\n'
                '   The almond eyes are the focus of an intelligent expression—an intense gaze, the Border’s famous\n'
                '\'herding eye\', is a breed hallmark. On the move, Borders are among the canine kingdom’s most\n'
                'agile, balanced, and durable citizens.\n\n'
                '   The intelligence, athleticism, and trainability of Borders have a perfect outlet in agility\n'
                'training. Having a job to perform, like agility—or herding or obedience work—is key to Border\n'
                'happiness. Amiable among friends, they may be reserved with strangers.\n'
        },

        'Boston_Terrier': {
            'temperament': ['friendly', 'bright', 'amusing'],
            'height': [15, 17],
            'weight': [12, 25],
            'lifespan': [11, 13],
            'group': 'non-sporting',
            'description_short':
                '   The Boston Terrier is a lively little companion recognized by his tight tuxedo jacket, sporty but\n'
                'compact body, and the friendly glow in his big, round eyes. His impeccable manners have earned him\n'
                'the nickname \'The American Gentleman.\'',
            'description_long':
                '   Boston Terriers are compact, short-tailed, well-balanced little dogs weighing no more than 25\n'
                'pounds. The stylish “tuxedo” coat can be white and either black, brindle, or seal (black with a red\n'
                'cast when viewed in sun or bright light). The head is square, the muzzle is short, and the large,\n'
                'round eyes can shine with kindness, curiosity, or mischief. Ever alert to their surroundings,\n'
                'Bostons move with a jaunty, rhythmic step.\n\n'
                '   It’s a safe bet that a breed named for a city—the Havanese or Brussels Griffon, for instance—will\n'
                'make an excellent urban pet. Bostons are no exception: they are sturdy but portable,\n'
                'people-oriented, and always up for a brisk walk to the park or outdoor cafe. A bright dog with a\n'
                'natural gift for comedy, the dapper Bostonian is a steady source of smiles.\n',
            'nicknames': {'Boston'}
        },

        'Boxer': {
            'temperament': ['bright', 'fun-loving', 'active'],
            'height': {'male': [23, 25], 'female': [21.5, 23.5]},
            'weight': {'male': [65, 80], 'female': [40, 65]},
            'lifespan': [10, 12],
            'group': 'working',
            'description_short':
                '   Loyalty, affection, intelligence, work ethic, and good looks: Boxers are the whole doggy package.\n'
                'Bright and alert, sometimes silly, but always courageous, the Boxer has been among America’s most\n'
                'popular dog breeds for a very long time.\n',
            'description_long':
                '   A well-made Boxer in peak condition is an awesome sight. A male can stand as high as 25 inches at\n'
                'the shoulder; females run smaller. Their muscles ripple beneath a short, tight-fitting coat. The\n'
                'dark brown eyes and wrinkled forehead give the face an alert, curious look. The coat can be fawn or\n'
                'brindle, with white markings. Boxers move like the athletes they are named for: smooth and graceful,\n'
                'with a powerful forward thrust.\n\n'
                '   Boxers are upbeat and playful. Their patience and protective nature have earned them a reputation\n'
                'as a great dog with children. They take the jobs of watchdog and family guardian seriously and will\n'
                'meet threats fearlessly. Boxers do best when exposed to a lot of people and other animals in early\n'
                'puppyhood.\n'
        },

        'Brittany': {
            'temperament': ['bright', 'fun-loving', 'upbeat'],
            'height': [17.5, 20.5],
            'weight': [30, 40],
            'lifespan': [12, 14],
            'group': 'sporting',
            'description_short':
                '   Sportsmen on both sides of the Atlantic cherish the agile, energetic Brittany as a stylish and\n'
                'versatile gundog. Bright and eager at home, and tireless afield, Brittanys require a lot of\n'
                'exercises, preferably with their favorite humans.\n',
            'description_long':
                '   Brittanys are smaller than setters but leggier than spaniels, standing about 20 inches at the\n'
                'shoulder. Their beautiful, boldly patterned coat comes in combinations of white and vivid orange and\n'
                'liver (reddish-brown). They are rugged and strong but smooth, clean, and quick afoot. The face has\n'
                'the \'softness\' prized by bird-dog lovers; high-set ears convey the breed’s essential eagerness.\n\n'
                '   The zeal and versatility that make Brittanys peerless hunters can be channeled into dog sports.\n'
                'Obedience, agility, flyball, dock diving—you name it, this trainable breed is up for it. The\n'
                'Brittany is a nice fit for those seeking an all-purpose hunting partner, a dog-sport teammate, or a\n'
                'companion in sync with an upbeat, outdoorsy family life.\n',
        },

        'Bulldog': {
            'temperament': ['friendly', 'courageous', 'calm'],
            'height': [14, 15],
            'weight': {'male': 50, 'female': 40},
            'lifespan': [8, 10],
            'group': 'non-sporting',
            'description_short':
                '   Kind but courageous, friendly but dignified, the Bulldog is a thick-set, low-slung, well-muscled\n'
                'bruiser whose “sourmug” face is the universal symbol of courage and tenacity. These docile, loyal\n'
                'companions adapt well to town or country.\n',
            'description_long':
                '   You can’t mistake a Bulldog for any other breed. The loose skin of the head, furrowed brow,\n'
                'pushed-in nose, small ears, undershot jaw with hanging chops on either side, and the distinctive\n'
                'rolling gait all practically scream “I’m a Bulldog!” The coat, seen in a variety of colors and\n'
                'patterns, is short, smooth, and glossy. Bulldogs can weigh up to 50 pounds, but that won’t stop them\n'
                'from curling up in your lap, or at least trying to. But don’t mistake their easygoing ways for\n'
                'laziness—Bulldogs enjoy brisk walks and need regular moderate exercise, along with a careful diet,\n'
                'to stay trim. Summer afternoons are best spent in an air-conditioned room as a Bulldog’s short snout\n'
                'can cause labored breathing in hot and humid weather.\n',
        },

        'Bullmastiff': {
            'temperament': ['affectionate', 'loyal', 'brave'],
            'height': {'male': [25, 27], 'female': [24, 26]},
            'weight': {'male': [110, 130], 'female': [100, 120]},
            'lifespan': [7, 9],
            'group': 'working',
            'description_short':
                '   Fearless at work, docile at home, the Bullmastiff is a large, muscular guarder who pursued and\n'
                'held poachers in Merry Old England—merry, we suppose, for everyone but poachers. Bullmastiffs are\n'
                'the result of Bulldog and Mastiff crosses.\n',
            'description_long':
                '   The Bullmastiff isn’t quite as large as his close cousin the Mastiff. Still, standing as high as\n'
                '27 inches at the shoulder and weighing between 100 and 130 pounds, this is still a whole lot of dog.\n'
                'After the first impression made by the Bullmastiff’s size, it is the large, broad head that conveys\n'
                'the breed’s essence: the dark eyes, high-set V-shaped ears, and broad, deep muzzle all combine to\n'
                'present the intelligence, alertness, and confidence that make the Bullmastiff a world-class\n'
                'protector and family companion. Coats come in fawn, red, or brindle.\n\n'
                '   These are biddable and reliable creatures, but as with any large guarding dog, owners must begin\n'
                'training and socialization early, while the puppy is still small enough to control.\n',
        },
    },

    'c': {
        'Cavalier_King_Charles_Spaniel': {
            'temperament': ['affectionate', 'gentle', 'graceful'],
            'height': [12, 13],
            'weight': [13, 18],
            'lifespan': [12, 15],
            'group': 'toy',
            'description_short':
                '   The Cavalier King Charles Spaniel wears his connection to British history in his breed’s name.\n'
                'Cavaliers are the best of two worlds, combining the gentle attentiveness of a toy breed with the\n'
                'verve and athleticism of a sporting spaniel.\n',
            'description_long':
                '   The Cavalier’s all-around beauty, regal grace, and even temper mark him as one of dogdom’s\n'
                'noblemen. A toy spaniel no more than 13 inches high, the Cavalier draws you in with his face: The\n'
                'sweet, gentle, melting expression emanating from large, round eyes is a breed hallmark. Another is\n'
                'the silky, richly-colored coat that can be one of four distinct varieties.\n\n'
                '   Cavaliers may be aristocrats, but they gladly descend from their royal high horse for a backyard\n'
                'frolic or a squirrel chase. They get along nicely with children and other dogs. Adaptable Cavaliers\n'
                'do equally well with active owners and homebodies—they can be upbeat athletes or shameless couch\n'
                'potatoes, depending on an owner’s lifestyle.\n',
            'nicknames': {'Cavalier'}
        },

        'Cane_Corso': {
            'temperament': ['affectionate', 'intelligent', 'majestic'],
            'height': {'male': [25, 27.5], 'female': [23.5, 26]},
            'weight': 'proportionate to height',
            'lifespan': [9, 12],
            'group': 'working',
            'description_short':
                '   Smart, trainable, and of noble bearing, the assertive and confident Cane Corso is a peerless\n'
                'protector. The Corso’s lineage goes back to ancient Roman times, and the breed’s name roughly\n'
                'translates from the Latin as \'bodyguard dog\'.\n',
            'description_long':
                '   At nearly 28 inches at the shoulder and often weighing more than 100 pounds, with a large head,\n'
                'alert expression, and muscles rippling beneath their short, stiff coat, Corsi are at a glance\n'
                'intimidating creatures. Their imposing appearance is their first line of defense against intruders.\n'
                'As one writer put it, \'An understated air of cool competence, the kind of demeanor you’d expect\n'
                'from a professional bodyguard, is the breed’s trademark.\'\n\n'
                '   Corsi are intelligent, loyal, eager to please, versatile, and intensely loyal to their humans,\n'
                'but are also assertive and willful, and can end up owning an unwitting owner. As with any other big\n'
                'guardian dog, responsible breeding and early socialization with people and other dogs is vital.\n',
            'nicknames': {'Corsi'}
        },

        'Chesapeake_Bay_Retriever': {
            'temperament': ['affectionate', 'bright', 'sensitive'],
            'height': {'male': [23, 26], 'female': [21, 24]},
            'weight': {'male': [65, 80], 'female': [55, 70]},
            'lifespan': [10, 13],
            'group': 'sporting',
            'description_short':
                '   The Chesapeake Bay Retriever, peerless duck dog of the Mid-Atlantic, is an American original who\n'
                'embodies the classic traits of a good retriever: loyal, upbeat, affectionate, and tireless. The\n'
                'Chessie is famous for his waterproof coat.\n',
            'description_long':
                '   Chessies are strong, powerfully built gundogs standing anywhere from 21 to 26 inches at the\n'
                'shoulder. A male can weigh up to 80 pounds. The distinctive breed trait is a wavy coat that is oily\n'
                'to the touch. Chessies are solid-colored, either chocolatey brown, sedge, or deadgrass, with keen\n'
                'yellow-amber eyes that nicely complement the coat.\n\n'
                '   Chessies are more emotionally complex than the usual gundog. Chessies take to training, but they\n'
                'have a mind of their own and can tenaciously pursue their own path. They are protective of their\n'
                'humans and polite, but not overtly friendly, to strangers. Chessies make excellent watchdogs and are\n'
                'versatile athletes. A well-socialized Chessie is a confident companion and world-class hunting\n'
                'buddy.\n',
            'nicknames': {'Chessy'}
        },

        'Chihuahua': {
            'temperament': ['charming', 'graceful', 'sassy'],
            'height': [5, 8],
            'weight': (6, 'and under'),
            'lifespan': [14, 16],
            'group': 'toy',
            'description_short':
                '   The Chihuahua is a tiny dog with a huge personality. A national symbol of Mexico, these alert and\n'
                'amusing purse dogs stand among the oldest breeds of the Americas, with a lineage going back to the\n'
                'ancient kingdoms of pre-Columbian times.\n',
            'description_long':
                '   The Chihuahua is a balanced, graceful dog of terrier-like demeanor, weighing no more than 6\n'
                'pounds. The rounded “apple” head is a breed hallmark. The erect ears and full, luminous eyes are\n'
                'acutely expressive. Coats come in many colors and patterns, and can be long or short. The varieties\n'
                'are identical except for coat.\n\n'
                '   Chihuahuas possess loyalty, charm, and big-dog attitude. Even tiny dogs require training, and\n'
                'without it this clever scamp will rule your household like a little Napoleon. Compact and confident,\n'
                'Chihuahuas are ideal city pets. They are too small for roughhousing with kids, and special care must\n'
                'be taken in cold weather, but Chihuahuas are adaptable—as long as they get lots of quality time in\n'
                'their preferred lap.\n'
        },

        'Cocker_Spaniel': {
            'temperament': ['Gentle', 'Smart', 'Happy'],
            'height': {'male': [14.5, 15.5], 'female': [13.5, 14.5]},
            'weight': {'male': [25, 30], 'female': [20, 30]},
            'lifespan': [10, 14],
            'group': 'sporting',
            'description_short':
                '   The merry and frolicsome Cocker Spaniel, with his big, dreamy eyes and impish personality, is one\n'
                'of the world’s best-loved breeds. They were developed as hunting dogs, but Cockers gained their wide\n'
                'popularity as all-around companions.\n',
            'description_long':
                '   Those big, dark eyes; that sweet expression; those long, lush ears that practically demand to be\n'
                'touched—no wonder the Cocker spent years as America’s most popular breed. The Cocker is the AKC’s\n'
                'smallest sporting spaniel, standing about 14 to 15 inches. The coat comes in enough colors and\n'
                'patterns to please any taste. The well-balanced body is sturdy and solid, and these quick, durable\n'
                'gundogs move with a smooth, easy gait.\n\n'
                '   Cockers are eager playmates for kids and are easily trained as companions and athletes. They are\n'
                'big enough to be sporty, but compact enough to be portable. A Cocker in full coat rewards extra\n'
                'grooming time by being the prettiest dog on the block. These energetic sporting dogs love playtime\n'
                'and brisk walks.\n',
        },

        'Collie': {
            'temperament': ['devoted', 'graceful', 'proud'],
            'height': {'male': [24, 26], 'female': [22, 24]},
            'weight': {'male': [60, 75], 'female': [50, 65]},
            'lifespan': [12, 14],
            'group': 'herding',
            'description_short':
                '   The majestic Collie, thanks to a hundred years as a pop-culture star, is among the world’s most\n'
                'recognizable and beloved dog breeds. The full-coated “rough” Collie is the more familiar variety,\n'
                'but there is also a sleek “smooth” Collie.\n',
            'description_long':
                '   The Collie is a large but lithe herder standing anywhere from 22 to 26 inches tall. The rough\n'
                'variety boasts one of the canine kingdom’s most impressively showy coats; the smooth coat’s charms\n'
                'are subtler but no less satisfying. Coat colors in both varieties are sable and white, tricolor,\n'
                'blue merle, or white. Collie fanciers take pride in their breed’s elegant wedge-shaped head, whose\n'
                'mobile ears and almond eyes convey a wide variety of expressions.\n\n'
                '   Collies are famously fond of children and make wonderful family pets. These swift, athletic dogs\n'
                'thrive on companionship and regular exercise. With gentle training, they learn happily and rapidly.\n'
                'The Collie’s loyalty, intelligence, and sterling character are the stuff of legend.\n',
        }
    },

    'd': {
        'Dachshund': {
            'temperament': ['Friendly', 'Curious', 'Spunky'],
            'height': {'standard': [8, 9], 'miniature': [5, 6]},
            'weight': {'standard': [16, 32], 'miniature': (11, 'and under')},
            'lifespan': [12, 16],
            'group': 'hound',
            'description_short':
                '   The famously long, low silhouette, ever-alert expression, and bold, vivacious personality of the\n'
                'Dachshund have made him a superstar of the canine kingdom. Dachshunds come in two sizes and in three\n'
                'coat types of various colors and patterns.\n',
            'description_long':
                '   The word “icon” is terribly overworked, but the Dachshund—with his unmistakable long-backed body,\n'
                'little legs, and big personality—is truly an icon of purebred dogdom. Dachshunds can be\n'
                'standard-sized (usually 16 to 32 pounds) or miniature (11 pounds or under), and come in one of three\n'
                'coat types: smooth, wirehaired, or longhaired.\n\n'
                '   Dachshunds aren’t built for distance running, leaping, or strenuous swimming, but otherwise these\n'
                'tireless hounds are game for anything. Smart and vigilant, with a big-dog bark, they make fine\n'
                'watchdogs. Bred to be an independent hunter of dangerous prey, they can be brave to the point of\n'
                'rashness, and a bit stubborn, but their endearing nature and unique look has won millions of hearts\n'
                'the world over.\n',
            'nicknames': {'Wiener_Dog'}
        },

        'Dalmatian': {
            'temperament': ['dignified', 'smart', 'outgoing'],
            'height': [19, 24],
            'weight': [45, 70],
            'lifespan': [11, 13],
            'group': 'non-sporting',
            'description_short':
                '   The dignified Dalmatian, dogdom\'s citizen of the world, is famed for his spotted coat and unique\n'
                'job description. During their long history, these \'coach dogs\' have accompanied the horse-drawn\n'
                'rigs of nobles, travelers, and firefighters.\n',
            'description_long':
                '   The Dalmatian’s delightful, eye-catching spots of black or liver adorn one of the most\n'
                'distinctive coats in the animal kingdom. Beneath the spots is a graceful, elegantly proportioned\n'
                'trotting dog standing between 19 and 23 inches at the shoulder. Dals are muscular, built to go the\n'
                'distance; the powerful hindquarters provide the drive behind the smooth, effortless gait.\n\n'
                '   The Dal was originally bred to guard horses and coaches, and some of the old protective instinct\n'
                'remains. Reserved and dignified, Dals can be aloof with strangers and are dependable watchdogs. With\n'
                'their preferred humans, Dals are bright, loyal, and loving house dogs. They are strong, active\n'
                'athletes with great stamina—a wonderful partner for runners and hikers.\n',
            'nicknames': {'Dal'}
        },

        'Doberman_Pinscher': {
            'temperament': ['Loyal', 'Fearless', 'Alert'],
            'height': {'male': [26, 28], 'female': [24, 26]},
            'weight': {'male': [75, 100], 'female': [60, 90]},
            'lifespan': [10, 12],
            'group': 'working',
            'description_short':
                '   Sleek and powerful, possessing both a magnificent physique and keen intelligence, the Doberman\n'
                'Pinscher is one of dogkind\'s noblemen. This incomparably fearless and vigilant breed stands proudly\n'
                'among the world\'s finest protection dogs.\n',
            'description_long':
                '   Dobermans are compactly-built dogs—muscular, fast, and powerful—standing between 24 to 28 inches\n'
                'at the shoulder. The body is sleek but substantial, and is covered with a glistening coat of black,\n'
                'blue, red, or fawn, with rust markings. These elegant qualities, combined with a noble, wedge-shaped\n'
                'head and an easy, athletic way of moving have earned Dobermans a reputation as royalty in the canine\n'
                'kingdom. A well-conditioned Doberman on patrol will deter all but the most foolish intruder.\n',
            'nicknames': {'Doberman'}
        },
    },

    'e': {
        'English_Cocker_Spaniel': {
            'temperament': ['energetic', 'merry', 'responsive'],
            'height': {'male': [16, 17], 'female': [15, 16]},
            'weight': {'male': [28, 34], 'female': [26, 34]},
            'lifespan': [12, 14],
            'group': 'sporting',
            'description_short':
                '   English Cocker Spaniel lovers often use the word \'merry\' to describe their breed. Upbeat in the\n'
                'field and mellow at home, this compact, silky-coated bird dog is widely admired for his delightful\n'
                'personality and irresistible good looks.\n',
            'description_long':
                '   The English Cocker Spaniel is a compactly built sporting dog standing between 15 to 17 inches at\n'
                'the shoulder. The softly contoured head, with its dark, melting eyes that convey an alert and\n'
                'dignified expression, is framed by lush, close-lying ears. The medium-length coat, seen in a variety\n'
                'of striking colors and patterns, is silky to the touch. \'Balance\' is a key word in understanding\n'
                'the breed: The EC is balanced in temperament, construction, and movement.\n\n'
                '   Beneath the EC’s physical beauty beats the heart of a tireless, eager-to-please hunter’s helper,\n'
                'famous the world over for his ability to flush and retrieve gamebirds. For those who prefer more\n'
                'domestic pursuits, there is no more charming and agreeable household companion.\n',
            'nicknames': {'Ec'}
        },

        'English_Springer_Spaniel': {
            'temperament': ['friendly', 'playful', 'obedient'],
            'height': {'male': 20, 'female': 19},
            'weight': {'male': 50, 'female': 40},
            'lifespan': [12, 14],
            'group': 'sporting',
            'description_short':
                '   The English Springer Spaniel is a sweet-faced, lovable bird dog of great energy, stamina, and\n'
                'brains. Sport hunters cherish the duality of working Springers: handsome, mannerly pets during the\n'
                'week, and trusty hunting buddies on weekends.\n',
            'description_long':
                '   Built for long days in the field, English Springer Spaniels are tough, muscular hunters standing\n'
                '19 to 20 inches at the shoulder and weighing between 40 and 50 pounds. The double coat comes in\n'
                'several colors and patterns, the ears are long and lush, and the kindly, trusting expression of the\n'
                'eyes is a cherished hallmark of the breed. Springers move with a smooth, ground-covering stride.\n\n'
                '   Bred to work closely with humans, Springers are highly trainable people-pleasers. They crave\n'
                'company and are miserable when neglected.\n\n'
                '   Polite dogs, Springers are good with kids and their fellow mammals. They are eager to join in any\n'
                'family activity. Long walks, games of chase and fetch, and swimming are favorite pastimes of these\n'
                'rugged spaniels.\n',
        }
    },

    'f': {
        'French_Bulldog': {
            'temperament': ['adaptable', 'playful', 'smart'],
            'height': [11, 13],
            'weight': (27, 'and under'),
            'lifespan': [10, 12],
            'group': 'non-sporting',
            'description_short':
                '   The one-of-a-kind French Bulldog, with his large bat ears and even disposition, is one of the\n'
                'world’s most popular small-dog breeds, especially among city dwellers. The Frenchie is playful,\n'
                'alert, adaptable, and completely irresistible.\n',
            'description_long':
                '   The French Bulldog resembles a Bulldog in miniature, except for the large, erect “bat ears” that\n'
                'are the breed’s trademark feature. The head is large and square, with heavy wrinkles rolled above\n'
                'the extremely short nose. The body beneath the smooth, brilliant coat is compact and muscular.\n\n'
                '   The bright, affectionate Frenchie is a charmer. Dogs of few words, Frenchies don’t bark\n'
                'much—but their alertness makes them excellent watchdogs. They happily adapt to life with singles,\n'
                'couples, or families, and do not require a lot of outdoor exercise. They get on well with other\n'
                'animals and enjoy making new friends of the human variety. It is no wonder that city folk from Paris\n'
                'to Peoria swear by this vastly amusing and companionable breed.\n',
        },
    },

    'g': {
        'German_Shepherd': {
            'temperament': ['confident', 'courageous', 'smart'],
            'height': {'male': [24, 26], 'female': [22, 24]},
            'weight': {'male': [65, 90], 'female': [50, 70]},
            'lifespan': [12, 14],
            'group': 'herding',
            'description_short':
                '   Generally considered dogkind’s finest all-purpose worker, the German Shepherd Dog is a large,\n'
                'muscular dog of noble character and high intelligence. Loyal, confident, courageous, and steady, the\n'
                'German Shepherd is truly a dog lover’s delight.',
            'description_long':
                '   German Shepherd Dogs can stand as high as 26 inches at the shoulder and, when viewed in outline,\n'
                'presents a picture of smooth, graceful curves rather than angles. The natural gait is a\n'
                'free-and-easy trot, but they can turn it up a notch or two and reach great speeds.\n\n'
                '   There are many reasons why German Shepherds stand in the front rank of canine royalty, but\n'
                'experts say their defining attribute is character: loyalty, courage, confidence, the ability to\n'
                'learn commands for many tasks, and the willingness to put their life on the line in defense of loved\n'
                'ones. German Shepherds will be gentle family pets and steadfast guardians, but, the breed standard\n'
                'says, there’s a “certain aloofness that does not lend itself to immediate and indiscriminate\n'
                'friendships.',
        },

        'German_Shorthaired_Pointer': {
            'temperament': ['friendly', 'smart', 'willing to please'],
            'height': {'male': [23, 25], 'female': [21, 23]},
            'weight': {'male': [55, 70], 'female': [45, 60]},
            'lifespan': [10, 12],
            'group': 'Sporting',
            'description_short':
                '   The versatile, medium-sized German Shorthaired Pointer is an enthusiastic gundog of all trades\n'
                'who thrives on vigorous exercise, positive training, and a lot of love. GSP people call their\n'
                'aristocratic companions the “perfect pointer.\n',
            'description_long':
                '   Male German Shorthaired Pointers stand between 23 and 25 inches at the shoulder and weigh\n'
                'anywhere from 55 to 70 pounds; females run smaller. The coat is solid liver (a reddish brown), or\n'
                'liver and white in distinctive patterns. The dark eyes shine with enthusiasm and friendliness. Built\n'
                'to work long days in the field or at the lake, GSPs are known for power, speed, agility, and\n'
                'endurance. “Noble” and “aristocratic” are words often used to describe the overall look.\n\n'
                '   GSPs make happy, trainable pets who bond firmly to their family. They are always up for physical\n'
                'activities like running, swimming, organized dog sports—in fact, anything that will burn some of\n'
                'their boundless energy while spending outdoors time with a human buddy.\n',
            'nicknames': {'Pointer'}
        },

        'Golden_Retriever': {
            'temperament': ['friendly', 'intelligent', 'devoted'],
            'height': {'male': [23, 24], 'female': [21.5, 22.5]},
            'weight': {'male': [65, 75], 'female': [55, 75]},
            'lifespan': [10, 12],
            'group': 'sporting',
            'description_short':
                '   The Golden Retriever, an exuberant Scottish gundog of great beauty, stands among America’s most\n'
                'popular dog breeds. They are serious workers at hunting and field work, as guides for the blind, and\n'
                'in search-and-rescue, enjoy obedience and other competitive events, and have an endearing love of\n'
                'life when not at work.\n',
            'description_long':
                '   The Golden Retriever is a sturdy, muscular dog of medium size, famous for the dense, lustrous\n'
                'coat of gold that gives the breed its name. The broad head, with its friendly and intelligent eyes,\n'
                'short ears, and straight muzzle, is a breed hallmark. In motion, Goldens move with a smooth,\n'
                'powerful gait, and the feathery tail is carried, as breed fanciers say, with a “merry action.\n\n'
                '   The most complete records of the development of the Golden Retriever are included in the record\n'
                'books that were kept from 1835 until about 1890 by the gamekeepers at the Guisachan (pronounced\n'
                'Gooeesicun) estate of Lord Tweedmouth at Inverness-Shire, Scotland. These records were released to\n'
                'public notice in Country Life in 1952, when Lord Tweedmouth’s great-nephew, the sixth Earl of\n'
                'Ilchester, historian and sportsman, published material that had been left by his ancestor. They\n'
                'provided factual confirmation to the stories that had been handed down through generations.\n\n'
                '   Goldens are outgoing, trustworthy, and eager-to-please family dogs, and relatively easy to train.\n'
                'They take a joyous and playful approach to life and maintain this puppyish behavior into adulthood.\n'
                'These energetic, powerful gundogs enjoy outdoor play. For a breed built to retrieve waterfowl for\n'
                'hours on end, swimming and fetching are natural pastimes.\n',
            'nicknames': {'Golden'}
        },

        'Great_Dane': {
            'temperament': ['friendly', 'patient', 'dependable'],
            'height': {'male': [30, 32], 'female': [28, 30]},
            'weight': {'male': [140, 175], 'female': [110, 140]},
            'lifespan': [7, 10],
            'group': 'working',
            'description_short':
                '   The easygoing Great Dane, the mighty “Apollo of Dogs,” is a total joy to live with—but owning a\n'
                'dog of such imposing size, weight, and strength is a commitment not to be entered into lightly. This\n'
                'breed is indeed great, but not a Dane.\n',
            'description_long':
                '   As tall as 32 inches at the shoulder, Danes tower over most other dogs—and when standing on their\n'
                'hind legs, they are taller than most people. These powerful giants are the picture of elegance and\n'
                'balance, with the smooth and easy stride of born noblemen. The coat comes in different colors and\n'
                'patterns, perhaps the best-known being the black-and-white patchwork pattern known as “harlequin.\n\n”'
                '   Despite their sweet nature, Danes are alert home guardians. Just the sight of these gentle giants\n'
                'is usually enough to make intruders think twice. But those foolish enough to mistake the breed’s\n'
                'friendliness for softness will meet a powerful foe of true courage and spirit. Patient with kids,\n'
                'Danes are people pleasers who make friends easily.\n',
        },
    },

    'h': {
        'Havanese': {
            'temperament': ['intelligent', 'outgoing', 'funny'],
            'height': [8.5, 11.5],
            'weight': [7, 13],
            'lifespan': [14, 16],
            'group': 'toy',
            'description_short':
                '   Havanese, the only dog breed native to Cuba, are cheerful little dogs with a spring in their step\n'
                'and a gleam in their big, brown eyes. These vivacious and sociable companions are becoming\n'
                'especially popular with American city dwellers.\n',
            'description_long':
                '   Distinctive features of the Havanese include a curled-over tail and a gorgeous silky coat, which\n'
                'comes in a variety of colors. Some owners enjoy cording the coat, in the manner of a Puli, and\n'
                'others clip it short to reduce grooming time. Happily, Havenese are just as cute no matter what\n'
                'hairdo you give them.\n\n'
                '   Their small but sturdy bodies, adaptable nature, and social skills make Havanese an ideal city\n'
                'dog, but they are content to be anywhere that they can command the attention of admirers young and\n'
                'old alike. Havanese, smart and trainable extroverts with the comic instincts of a born clown, are\n'
                'natural trick dogs. Havanese are also excellent watchdogs and take the job seriously, but will\n'
                'usually keep the barking to a minimum.\n',
        },
    },

    'l': {
        'Labrador': {
            'temperament': ['friendly', 'active', 'outgoing'],
            'height': {'male': [22.5, 24.5], 'female': [21.5, 23.5]},
            'weight': {'male': [60, 80], 'female': [55, 70]},
            'lifespan': [10, 12],
            'group': 'sporting',
            'description_short':
                '   The sweet-faced, lovable Labrador Retriever is America’s most popular dog breed. Labs are\n'
                'friendly, outgoing and high-spirited companions who have more than enough affection to go around for\n'
                'a family looking for a medium-to-large dog.\n',
            'description_long':
                '   The sturdy, well-balanced Labrador Retriever can, depending on the sex, stand from 21.5 to 24.5\n'
                'inches at the shoulder and weigh between 55 to 80 pounds. The dense, hard coat comes in yellow,\n'
                'black, and a luscious chocolate. The head is wide, the eyes glimmer with kindliness, and the thick,\n'
                'tapering “otter tail” seems to be forever signaling the breed’s innate eagerness.\n\n'
                '   Labs are famously friendly. They are companionable housemates who bond with the whole family, and\n'
                'they socialize well with neighbor dogs and humans alike. But don’t mistake his easygoing personality\n'
                'for low energy: The Lab is an enthusiastic athlete that requires lots of exercise, like swimming and\n'
                'marathon games of fetch, to keep physically and mentally fit.\n',
            'nicknames': {'Lab'}
        },
    },

    'm': {
        'Mastiff': {
            'temperament': ['courageous', 'dignified', 'good-natured'],
            'height': {'male': (30, 'and over'), 'female': (27.5, 'and over')},
            'weight': {'male': [160, 230], 'female': [120, 170]},
            'lifespan': [6, 10],
            'group': 'working',
            'description_short':
                '   The colossal Mastiff belongs to a canine clan as ancient as civilization itself. A massive,\n'
                'heavy-boned dog of courage and prodigious strength, the Mastiff is docile and dignified but also a\n'
                'formidable protector of those they hold dear.\n',
            'description_long':
                '   For the uninitiated, a face-to-face encounter with these black-masked giants can be startling. A\n'
                'male stands at least 30 inches at the shoulder and can outweigh many a full-grown man. The\n'
                'rectangular body is deep and thickly muscled, covered by a short double coat of fawn, apricot, or\n'
                'brindle stripes. The head is broad and massive, and a wrinkled forehead accentuates an alert,\n'
                'kindly expression. Mastiffs are patient, lovable companions and guardians who take best to gentle\n'
                'training.\n\n'
                '   Eternally loyal Mastiffs are protective of family, and a natural wariness of strangers makes\n'
                'early training and socialization essential. Mastiffs are magnificent pets, but acquiring a powerful\n'
                'giant-breed dog is commitment not to be taken lightly.\n'
        },

        'Maltese': {
            'temperament': ['gentle', 'playful', 'charming'],
            'height': [7, 9],
            'weight': (7, 'and under'),
            'lifespan': [12, 15],
            'group': 'toy',
            'description_short':
                '   The tiny Maltese, \'Ye Ancient Dogge of Malta,\' has been sitting in the lap of luxury since the\n'
                'Bible was a work in progress. Famous for their show-stopping, floor-length coat, Maltese are\n'
                'playful, charming, and adaptable toy companions.\n',
            'description_long':
                '   Maltese are affectionate toy dogs weighing less than seven pounds, covered by a long, straight,\n'
                'silky coat. Beneath the all-white mantle is a compact body moving with a smooth and effortless gait.\n'
                'The overall picture depicts free-flowing elegance and balance. The irresistible Maltese face—with\n'
                'its big, dark eyes and black gumdrop nose—can conquer the most jaded sensibility.\n\n'
                '   Despite their aristocratic bearing, Maltese are hardy and adaptable pets. They make alert\n'
                'watchdogs who are fearless in a charming toy-dog way, and they are game little athletes on the\n'
                'agility course. Maltese are low-shedding, long-lived, and happy to make new friends of all ages.\n'
                'Sometimes stubborn and willful, they respond well to rewards-based training.\n'
        },

        'Miniature_Schnauzer': {
            'temperament': ['friendly', 'smart', 'obedient'],
            'height': [12, 14],
            'weight': [11, 20],
            'lifespan': [12, 15],
            'group': 'terrier',
            'description_short':
                '   The Miniature Schnauzer, the smallest of the three Schnauzer breeds, is a generally healthy,\n'
                'long-lived, and low-shedding companion. Add an outgoing personality, a portable size, and sporty\n'
                'good looks, and you’ve got an ideal family dog.\n',
            'description_long':
                '   Stocky, robust little dogs standing 12 to 14 inches, Miniature Schnauzers were bred down from\n'
                'their larger cousins, Standard Schnauzers. The bushy beard and eyebrows give Minis a charming,\n'
                'human-like expression. The hard, wiry coat comes in three color patterns: salt and pepper, black and\n'
                'silver, and solid black. Created to be all-around farm dogs and ratters, they are tough, muscular,\n'
                'and fearless without being aggressive.\n\n'
                '   The Miniature Schnauzer is a bright, friendly, trainable companion, small enough to adapt to\n'
                'apartment life but tireless enough to patrol acres of farmland. They get along well with other\n'
                'animals and kids. Minis are sturdy little guys and enjoy vigorous play. Home and family oriented,\n'
                'they make great watchdogs.\n',
            'nicknames': {'Mini_Schnauzer'}
        },

        'Miniature_American_Shepherd': {
            'temperament': ['good-natured', 'intelligent', 'devoted'],
            'height': {'male': [14, 18], 'female': [13, 17]},
            'weight': [20, 40],
            'lifespan': [12, 13],
            'group': 'herding',
            'description_short':
                '   The Miniature American Shepherd resembles a small Australian Shepherd. True herders in spite of\n'
                'their compact size, Minis are bright, self-motivated workers and endearingly loyal and lively\n'
                'companion dogs who have an affinity for horses.\n',
            'description_long':
                '   The Miniature American Shepherd shares many physical traits with its forebear the Australian\n'
                'Shepherd—only on a smaller scale. Females stand between 13 and 17 inches at the shoulder; males\n'
                'range from 14 to 18 inches. Despite their size, Minis are every inch a true herding dog: energetic,\n'
                'versatile, rugged, and extremely bright. The eye-catching coat comes in black, blue merle, red, and\n'
                'red merle. (The merle will exhibit in any amount marbling, flecks, or blotches.) Minis move with the\n'
                'smooth and agile step of a dog built for hard work on punishing terrain.\n',
            'nicknames': {'Mini', 'Mini_American_Shepherd'}
        },
    },

    'n': {
        'Newfoundland': {
            'temperament': ['sweet', 'patient', 'devoted'],
            'height': {'male': 28, 'female': 26},
            'weight': {'male': [130, 150], 'female': [100, 120]},
            'lifespan': [9, 10],
            'group': 'working',
            'description_short':
                '   The massive Newfoundland is a strikingly large, powerful working dog of heavy bone and dignified\n'
                'bearing. The sweet-tempered Newfie is a famously good companion and has earned a reputation as a\n'
                'patient and watchful “nanny dog” for kids.\n',
            'description_long':
                '   A male Newfoundland can weigh up to 150 pounds and stand 28 inches at the shoulder; females\n'
                'typically go 100 to 120 pounds. The Newf head is majestic, the expression soft and soulful. The\n'
                'outer coat is flat and coarse. Colors are gray, brown, black, and a black-and-white coat named for\n'
                'artist Sir Edwin Landseer, who popularized the look in his paintings.\n\n'
                '   The Newfie breed standard says that a sweet temperament is the “most important single\n'
                'characteristic of the breed.” The Newf’s sterling character is expressed in their affinity for kids.\n'
                'Trusting and trainable, Newfs respond well to gentle guidance. These noble giants are among the\n'
                'world’s biggest dogs, and acquiring a pet that could outweigh you comes with obvious challenges.\n',
            'nicknames': {'Newf'}
        },
    },

    'p': {
        'Papillon': {
            'temperament': ['friendly', 'alert', 'happy'],
            'height': [8, 11],
            'weight': [5, 10],
            'lifespan': [14, 16],
            'group': 'toy',
            'description_short':
                '   The quick, curious Papillon is a toy dog of singular beauty and upbeat athleticism. Despite his\n'
                'refined appearance, the Pap is truly a \'doggy dog\' blessed with a hardy constitution. Papillon\n'
                'fanciers describe their breed as happy, alert, and friendly.\n',
            'description_long':
                '   A tiny dog, measuring 8 to 11 inches at the shoulder, you can still spot a Papillon a block away\n'
                'thanks to the large, wing-shaped ears that give the breed its name (\'papillon\' is French for\n'
                '\'butterfly\'). Some Paps have erect ears; in others, known as the Phalene type, the ears are down.\n'
                'Paps are dainty and elegant, with a plumed tail, and a long, silky coat of several color\n'
                'combinations, the base color being white. More robust than they look, Paps are little dogs for all\n'
                'seasons and reasons. They thrive in warm or cool climates, in town or country, and are eager to join\n'
                'family fun. They are excellent agility dogs and are consistent winners at the sport’s highest\n'
                'levels; less ambitious owners can train them to do all kinds of tricks.\n',
            'nicknames': {'Pap'}
        },

        'Pembroke_Welsh_Corgi': {
            'temperament': ['affectionate', 'smart', 'alert'],
            'height': [10, 12],
            'weight': {'male': (30, 'and under'), 'female': (28, 'and under')},
            'lifespan': [12, 13],
            'group': 'herding',
            'description_short':
                '   Among the most agreeable of all small housedogs, the Pembroke Welsh Corgi is a strong, athletic,\n'
                'and lively little herder who is affectionate and companionable without being needy. They are one of\n'
                'the world\'s most popular herding breeds.\n',
            'description_long':
                '   At 10 to 12 inches at the shoulder and 27 to 30 pounds, a well-built male Pembroke presents a big\n'
                'dog in a small package. Short but powerful legs, muscular thighs, and a deep chest equip him for a\n'
                'hard day’s work. Built long and low, Pembrokes are surprisingly quick and agile. They can be red,\n'
                'sable, fawn, and black and tan, with or without white markings.\n\n'
                '   The Pembroke is a bright, sensitive dog who enjoys play with his human family and responds well\n'
                'to training. As herders bred to move cattle, they are fearless and independent. They are vigilant\n'
                'watchdogs, with acute senses and a “big dog” bark. Families who can meet their bold but kindly\n'
                'Pembroke’s need for activity and togetherness will never have a more loyal, loving pet.\n',
            'nicknames': {'Welsh_Corgi'}
        },

        'Pomeranian': {
            'temperament': ['inquisitive', 'bold', 'lively'],
            'height': [6, 7],
            'weight': [3, 7],
            'lifespan': [12, 16],
            'group': 'toy',
            'description_short':
                '   The tiny Pomeranian, long a favorite of royals and commoners alike, has been called the ideal\n'
                'companion. The glorious coat, smiling, foxy face, and vivacious personality have helped make the Pom\n'
                'one of the world\'s most popular toy breeds.',
            'description_long':
                '   The Pomeranian combines a tiny body (no more than seven pounds) and a commanding big-dog\n'
                'demeanor. The abundant double coat, with its frill extending over the chest and shoulders, comes in\n'
                'almost two dozen colors, and various patterns and markings, but is most commonly seen in orange or\n'
                'red.\n\n'
                '   Alert and intelligent, Pomeranians are easily trained and make fine watchdogs and perky pets for\n'
                'families with children old enough to know the difference between a toy dog and a toy. Poms are\n'
                'active but can be exercised with indoor play and short walks, so they are content in both the city\n'
                'and suburbs. They will master tricks and games with ease, though their favorite activity is\n'
                'providing laughs and companionship to their special human.\n',
        },

        'Poodle': {
            'temperament': ['active', 'proud', 'very smart'],
            'height': (16, 'and over'),
            'weight': {'male': [60, 70], 'female': [40, 50]},
            'lifespan': [10, 18],
            'group': 'non-sporting',
            'description_short':
                '   Whether Standard, Miniature, or Toy, and either black, white, or apricot, the Poodle stands\n'
                'proudly among dogdom’s true aristocrats. Beneath the curly, low-allergen coat is an elegant athlete\n'
                'and companion for all reasons and seasons.\n',
            'description_long':
                '   Poodles come in three size varieties: Standards should be more than 15 inches tall at the\n'
                'shoulder; Miniatures are 15 inches or under; Toys stand no more than 10 inches. All three varieties\n'
                'have the same build and proportions. At dog shows, Poodles are usually seen in the elaborate\n'
                'Continental Clip. Most pet owners prefer the simpler Sporting Clip, in which the coat is shorn to\n'
                'follow the outline of the squarely built, smoothly muscled body.\n\n'
                '   Forget those old stereotypes of Poodles as sissy dogs. Poodles are eager, athletic, and wickedly\n'
                'smart “real dogs” of remarkable versatility. The Standard, with his greater size and strength, is\n'
                'the best all-around athlete of the family, but all Poodles can be trained with great success.\n',
        },

        'Portuguese_Water_Dog': {
            'temperament': ['affectionate', 'adventurous', 'athletic'],
            'height': {'male': [20, 23], 'female': [17, 21]},
            'weight': {'male': [42, 60], 'female': [35, 50]},
            'lifespan': [11, 13],
            'group': 'working',
            'description_short':
                '   The bright and biddable Portuguese Water Dog was bred to be an all-around fisherman’s helper. The\n'
                'robust, medium-sized body is covered by a coat of tight, low-shedding curls. They are eager and\n'
                'athletic companions built for water work.\n',
            'description_long':
                '   The Portuguese Water Dog is super-smart and very biddable—meaning he’s easy to train and eager to\n'
                'please. The breed can be groomed in two styles: The retriever clip (the entire coat is clipped to\n'
                'one inch in length, with the tail tip at full length) or the more check-me-out lion clip, where the\n'
                'coat on the hindquarters and muzzle is clipped down to the skin.\n',
            'nicknames': {'Portie'}
        },

        'Pug': {
            'temperament': ['charming', 'mischievous', 'loving'],
            'height': [10, 13],
            'weight': [14, 18],
            'lifespan': [13, 15],
            'group': 'toy',
            'description_short':
                '   Once the mischievous companion of Chinese emperors, and later the mascot of Holland’s royal House\n'
                'of Orange, the small but solid Pug is today adored by his millions of fans around the world. Pugs\n'
                'live to love and to be loved in return.\n',
            'description_long':
                '   The Pug’s motto is the Latin phrase “multum in parvo” (a lot in a little)—an apt description of\n'
                'this small but muscular breed. They come in three colors: silver or apricot-fawn with a black face\n'
                'mask, or all black. The large round head, the big, sparkling eyes, and the wrinkled brow give Pugs a\n'
                'range of human-like expressions—surprise, happiness, curiosity—that have delighted owners for\n'
                'centuries.\n\n'
                '   Pug owners say their breed is the ideal house dog. Pugs are happy in the city or country, with\n'
                'kids or old folks, as an only pet or in a pack. They enjoy their food, and care must be taken to\n'
                'keep them trim. They do best in moderate climates—not too hot, not too cold—but, with proper care,\n'
                'Pugs can be their adorable selves anywhere.\n'
        },
    },

    'r': {
        'Rhodesian_Ridgeback': {
            'temperament': ['affectionate', 'dignified', 'even-tempered'],
            'height': {'male': [25, 27], 'female': [24, 26]},
            'weight': {'male': 85, 'female': 70},
            'lifespan': 10,
            'group': 'hound',
            'description_short':
                '   The Rhodesian Ridgeback is an all-purpose \'Renaissance hound\' whose hallmark is the ridge, or\n'
                'stripe of backward-growing hair, on his back. Though the breed was made famous in its native Africa\n'
                'for its skill at tracking and baying – but never, ever killing – lions, today Ridgebacks are\n'
                'cherished family dogs whose owners must be prepared to deal with their independence and strong prey\n'
                'drive.\n',
            'description_long':
                '   Beneath the Ridgeback’s trademark ridge is a whole lot of hound: Ridgebacks are fast and powerful\n'
                'athletes who can weigh between 70 and 85 pounds, and oftentimes more. They come in only one color –\n'
                'wheaten – which spans every shade seen in a wheat field, from pale flaxen to the burnished red of a\n'
                'maturing crop. Ridgebacks also have two nose colors: black and the less commonly seen brown.\n\n'
                '   The formidable Ridgeback can be strong willed, independent, and sometimes domineering. Ridgebacks\n'
                'must be guided with a firm but fair hand from puppyhood. They are faithful friends, protective of\n'
                'their loved ones and meltingly affectionate with those whom they trust. Still, a Ridgeback can be\n'
                'too much hound for the novice dog owner.\n',
            'nicknames': {'Ridgeback'}
        },

        'Rottweiler': {
            'temperament': ['loyal', 'loving', 'confident guardian'],
            'height': {'male': [24, 27], 'female': [22, 25]},
            'weight': {'male': [95, 135], 'female': [80, 100]},
            'lifespan': [9, 10],
            'group': 'working',
            'description_short':
                '   The Rottweiler is a robust working breed of great strength descended from the mastiffs of the\n'
                'Roman legions. A gentle playmate and protector within the family circle, the Rottie observes the\n'
                'outside world with a self-assured aloofness.\n',
            'description_long':
                '   A male Rottweiler will stand anywhere from 24 to 27 muscular inches at the shoulder; females run\n'
                'a bit smaller and lighter. The glistening, short black coat with smart rust markings add to the\n'
                'picture of imposing strength. A thickly muscled hindquarters powers the Rottie’s effortless\n'
                'trotting gait.\n\n'
                '   A well-bred and properly raised Rottie will be calm and confident, courageous but not unduly\n'
                'aggressive. The aloof demeanor these world-class guardians present to outsiders belies the\n'
                'playfulness, and downright silliness, that endear Rotties to their loved ones. (No one told the\n'
                'Rottie he’s not a toy breed, so he is liable to plop onto your lap for a cuddle.) Early training and\n'
                'socialization will harness a Rottie’s territorial instincts in a positive way.\n',
            'nicknames': {'Rottie'}
        },
    },

    's': {
        'Samoyed': {
            'temperament': ['adaptable', 'friendly', 'gentle'],
            'height': {'male': [21, 23.5], 'female': [19, 21]},
            'weight': {'male': [46, 65], 'female': [35, 50]},
            'lifespan': [12, 14],
            'group': 'working',
            'description_short':
                '   The Samoyed is a substantial but graceful dog standing anywhere from 19 to a bit over 23 inches\n'
                'at the shoulder. Powerful, tireless, with a thick all-white coat impervious to cold—Sammies are\n'
                'perfectly beautiful but highly functional. Even their most delightful feature, a perpetual smile,\n'
                'has a practical function: The upturned corners of the mouth keep Sammies from drooling, preventing\n'
                'icicles from forming on the face.\n\n',
            'description_long':
                '   Samoyeds, the smiling sledge dogs, were bred for hard work in the world’s coldest locales. In the\n'
                'Siberian town of Oymyakon, for instance, temperatures of minus-60 degrees are common. The Sammy’s\n'
                'famous white coat is thick enough to protect against such brutal conditions. A Sammy sentenced to\n'
                'solitary confinement in the yard is a miserable—and destructive—creature. These are smart, social,\n'
                'mischievous dogs who demand love and attention. Sammies need a very firm but loving hand in\n'
                'training.\n'
        },

        'Saint_Bernard': {
            'temperament': ['playful', 'charming', 'inquisitive'],
            'height': {'male': [28, 30], 'female': [26, 28]},
            'weight': {'male': [140, 180], 'female': [120, 140]},
            'lifespan': [8, 10],
            'group': 'working',
            'description_short':
                '   The Saint Bernard does not rank very high in AKC registrations, but the genial giant of the Swiss\n'
                'Alps is nonetheless among the world’s most famous and beloved breeds. Saints are famously watchful,\n'
                'patient, and careful with children.\n',
            'description_long':
                '   The Saint Bernard’s written standard abounds with phrases like \'very powerful,\'\n'
                '\'extraordinarily muscular,\' \'imposing,\' and \'massive.\' A male stands a minimum 27.5 inches at\n'
                'the shoulder; females will be smaller and more delicately built. The huge head features a wrinkled\n'
                'brow, a short muzzle, and dark eyes, combining to give Saints the intelligent, friendly expression\n'
                'that was such a welcome sight to stranded Alpine travelers.\n',
        },

        'Scottish_Terrier': {
            'temperament': ['confident', 'independent', 'spirited'],
            'height': 10,
            'weight': {'male': [19, 22], 'female': [18, 21]},
            'lifespan': 12,
            'group': 'terrier',
            'description_short':
                '   A solidly compact dog of vivid personality, the Scottish Terrier is an independent, confident\n'
                'companion of high spirits. Scotties have a dignified, almost-human character. Their terrier\n'
                'persistence has earned the breed the nickname \'the Diehard.\'\n',
            'description_long':
                '   The well-known Scottie silhouette is that of a short-legged but substantial terrier with\n'
                'distinctive furnishings at the beard, legs, and lower body. The wiry topcoat and soft, dense\n'
                'undercoat coat can be black, wheaten yellow, or a brindle-stripe pattern. Bright, piercing eyes, and\n'
                'erect ears and tail, convey keen alertness—a hallmark of Britain’s terrier breeds.\n\n'
                '   The Scottie working style has been described as efficient and businesslike, and their aloofness\n'
                'toward strangers makes them excellent watchdogs. Their hunting instinct remains strong, which can\n'
                'complicate life for the neighbor’s cat, and Scotties are known to be cantankerous around other dogs.\n'
                'This bold and clever Scotsman enjoys brisk walks and upbeat play.\n',
            'nicknames': {'Scottie'}
        },

        'Shetland_Sheepdog': {
            'temperament': ['playful', 'energetic', 'bright'],
            'height': [13, 16],
            'weight': [15, 25],
            'lifespan': [12, 14],
            'group': 'herding',
            'description_short':
                '   The Shetland Sheepdog, also known as the Sheltie, is an extremely intelligent, quick, and\n'
                'obedient herder from Scotland’s remote and rugged Shetland Islands. Shelties bear a strong family\n'
                'resemblance to their bigger cousin, the Collie.\n',
            'description_long':
                '   The Shetland Sheepdog is a small, active, and agile herding dog standing between 13 and 16 inches\n'
                'at the shoulder. The long coat is harsh and straight, with a dense undercoat, and comes in black,\n'
                'blue merle, and sable, with white markings. The coat, along with a long, wedge-shaped head; small,\n'
                'three-quarter erect ears; and deep-chested, level-backed torso, give Shelties the look of a\n'
                'rough-coated Collie in miniature.\n\n'
                '   Bright and eager Shelties are easy trainers and world-class competitors in obedience, agility,\n'
                'and herding trials. They are sensitive and affectionate family dogs, highly in tune with the mood of\n'
                'the household. They like to bark and tend to be reserved toward strangers—two qualifications of an\n'
                'excellent watchdog.\n',
            'nicknames': {'Shelty'}
        },

        'Shiba_Inu': {
            'temperament': ['alert', 'active', 'attentive'],
            'height': {'male': [14.5, 16.5], 'female': [13.5, 15.5]},
            'weight': {'male': 23, 'female': 17},
            'lifespan': [13, 16],
            'group': 'non-sporting',
            'description_short':
                '   An ancient Japanese breed, the Shiba Inu is a little but well-muscled dog once employed as a\n'
                'hunter. Today, the spirited, good-natured Shiba is the most popular companion dog in Japan. The\n'
                'adaptable Shiba is at home in town or country.\n',
            'description_long':
                '   Brought to America from Japan as recently as 60 years ago, Shibas are growing in popularity in\n'
                'the West and are already the most popular breed in their homeland. Their white markings combined\n'
                'with their coloring (red, red sesame, or black and tan) and their alert expression and smooth stride\n'
                'makes them almost foxlike. They’re sturdy, muscular dogs with a bold, confident personality to\n'
                'match.\n',
            'nicknames': {'Shiba'}
        },

        'Shih_Tzu': {
            'temperament': ['affectionate', 'playful', 'outgoing'],
            'height': [9, 10.5],
            'weight': [9, 16],
            'lifespan': [10, 18],
            'group': 'toy',
            'description_short':
                '   That face! Those big dark eyes looking up at you with that sweet expression! It’s no surprise\n'
                'that Shih Tzu owners have been so delighted with this little “Lion Dog” for a thousand years. Where\n'
                'Shih Tzu go, giggles and mischief follow.\n',
            'description_long':
                '   Shih Tzu (pronounced in the West “sheed-zoo” or “sheet-su”; the Chinese say “sher-zer”), weighing\n'
                'between 9 to 16 pounds, and standing between 8 and 11 inches, are surprisingly solid for dogs their\n'
                'size. The coat, which comes in many colors, is worth the time you will put into it—few dogs are as\n'
                'beautiful as a well-groomed Shih Tzu.\n\n'
                '   Being cute is a way of life for this lively charmer. The Shih Tzu is known to be especially\n'
                'affectionate with children. As a small dog bred to spend most of their day inside royal palaces,\n'
                'they make a great pet if you live in an apartment or lack a big backyard. Some dogs live to dig\n'
                'holes and chase cats, but a Shih Tzu’s idea of fun is sitting in your lap acting adorable as you try\n'
                'to watch TV.\n',
            'nicknames': {'Shih-Tzu'}
        },

        'Siberian_Husky': {
            'temperament': ['loyal', 'mischievous', 'outgoing'],
            'height': {'male': [21, 23.5], 'female': [20, 22]},
            'weight': {'male': [45, 60], 'female': [35, 50]},
            'lifespan': [12, 14],
            'group': 'working',
            'description_short':
                '   The Siberian Husky, a thickly coated, compact sled dog of medium size and great endurance, was\n'
                'developed to work in packs, pulling light loads at moderate speeds over vast frozen expanses. This\n'
                'northern breed is friendly, fastidious, and dignified.\n',
            'description_long':
                '   The graceful, medium-sized Siberian Husky’s almond-shaped eyes can be either brown or blue—and\n'
                'sometimes one of each—and convey a keen but amiable and even mischievous expression. Quick and\n'
                'nimble-footed, Siberians are known for their powerful but seemingly effortless gait. Tipping the\n'
                'scales at no more than 60 pounds, they are noticeably smaller and lighter than their burly cousin,\n'
                'the Alaskan Malamute. In fact, breeders and fanciers prefer the moniker Siberians over huskies, as\n'
                'the latter suggests a bigger, brawnier dog than what is the standard for the breed.\n\n'
                '   As born pack dogs, Siberians enjoy family life and get on well with other dogs; their innate\n'
                'friendliness render them indifferent watchdogs. This breed is also energetic and can’t resist\n'
                'chasing small animals, so secure running room is a must. An attractive feature of the breed:\n'
                'Siberians are naturally clean, with little doggy odor.\n',
            'nicknames': {'Husky'}
        },
    },

    'v': {
        'Vizsla': {
            'temperament': ['affectionate, gentle, energetic'],
            'height': {'male': [22, 24], 'female': [21, 23]},
            'weight': {'male': [55, 60], 'female': [44, 55]},
            'lifespan': [12, 14],
            'group': 'sporting',
            'description_short':
                '   The Vizsla is a versatile, red-coated gundog built for long days in the field. For centuries,\n'
                'these rugged but elegant athletes have been the pride of Hungarian sportsmen and their popularity in\n'
                'America increases with each passing year.\n',
            'description_long':
                '   The Vizsla is easily recognized by his sleek golden-rust coat. They can stand between 21 to 24\n'
                'inches at the shoulder and are the picture of a lean, light-footed hunter’s companion. The long,\n'
                'silky ears frame a facial expression that is sensitive and loving around the house and intense when\n'
                'at work. As a hunter expected to work closely with humans, Vizslas form a tight bond with their\n'
                'owners and hate to be left alone.\n\n'''
                '   Athletes of many talents, Vizslas excel at various sports and activities. They are eager and\n'
                'graceful trotters of great stamina, making them ideal jogging or biking companions. An expert on the\n'
                'breed tells us, \'If you don’t have the time to encourage this breed’s full use of its brain, you’re\n'
                'wasting a good dog.\'\n'
        }

    },

    'w': {
        'Weimaraner': {
            'temperament': ['friendly', 'fearless', 'obedient'],
            'height': {'male': [25, 27], 'female': [23, 25]},
            'weight': {'male': [70, 90], 'female': [55, 75]},
            'lifespan': [10, 13],
            'group': 'sporting',
            'description_short':
                '   The Weimaraner, Germany’s sleek and swift “Gray Ghost,” is beloved by hunters and pet owners\n'
                'alike for their friendliness, obedience, and beauty. They enjoy exercise, and plenty of it, along\n'
                'with lots of quality time with their humans.\n',
            'description_long':
                '   Instantly recognized by a distinctive silvery-gray coat, male Weimaraners stand 25 to 27 inches\n'
                'at the shoulder, and females 23 to 25 inches. A properly bred Weimaraner will be solid colored, with\n'
                'maybe a small white spot on the chest. The face, with its amber or blue-gray eyes framed by long\n'
                'velvety ears, is amiable and intelligent. Overall, the breed presents a picture of streamlined grace\n'
                'and balance. A well-conditioned Weimaraner on point is a breathtaking sight.\n\n'
                '   Weimaraners are excellent with kids and yearn to be full-fledged family members. Easy grooming,\n'
                'trainability, a loving nature, and a can-do-attitude make them excellent pets, as long as owners are\n'
                'committed to keeping them physically active and mentally engaged.\n',
        },

        'West_Highland_White_Terrier': {
            'temperament': ['loyal', 'happy', 'entertaining'],
            'height': {'male': 11, 'female': 10},
            'weight': [15, 20],
            'lifespan': [13, 15],
            'group': 'terrier',
            'description_short':
                '   Smart, confident, and always entertaining at play, the adorable West Highland White Terrier\n'
                '(Westie, for short) has charmed owners for over 300 years. This diminutive but sturdy earthdog is\n'
                'among the most popular of the small terriers.\n',
            'description_long':
                '   Standing 10 to 11 inches at the shoulder, with dark piercing eyes, compact body, and a\n'
                'carrot-shaped tail wagging with delight, the Westie’s looks are irresistible. Beneath the plush-toy\n'
                'exterior, though, is a true working terrier of gameness and courage. Bred to hunt rats and other\n'
                'underground rodents, Westies are surprisingly strong and tough. The all-white double coat is hard to\n'
                'the touch, not soft and fluffy.\n\n'
                'Alert and active, Westies exhibit traits of a plucky and self-reliant ratting terrier: They require\n'
                'no pampering, they will chase after anything that moves, and their independence can make training a\n'
                'challenge. But, thanks to their faithfulness and keen intelligence, Westies will train nicely with\n'
                'time and patience.\n',
            'nicknames': {'Westy'}
        },

        'Wheaten': {
            'temperament': ['friendly', 'happy', 'deeply devoted'],
            'height': {'male': [18, 19], 'female': [17, 18]},
            'weight': {'male': [35, 40], 'female': [30, 35]},
            'lifespan': [12, 14],
            'group': 'terrier',
            'description_short':
                '   The Soft Coated Wheaten Terrier, an exuberant Irish farm dog, is happy, friendly, deeply devoted,\n'
                'and just stubborn enough to remind you he’s a terrier. The unique wheaten coat is low-shedding but\n'
                'needs diligent care to avoid matting.\n',
            'description_long':
                '   The hallmark of these merry extroverts, and what sets them apart from other terriers, is the\n'
                'silky, gently waving coat. It runs from a pale beige to a shimmering gold, recalling the color of\n'
                'ripening wheat. Topping out at 19 inches tall and 40 pounds, Wheatens are square, sturdy terriers\n'
                'with a peek-a-boo hairdo and dashing goatee. The overall picture is that of a hard-muscled but\n'
                'soft-coated working terrier or, as the breed has been described, an iron fist in a velvet glove.\n',
            'nicknames': {'Soft_Coated_Wheaten_Terrier'}
        },

        'Whippet': {
            'temperament': ['affectionate', 'playful', 'calm'],
            'height': {'male': [19, 22], 'female': [18, 21]},
            'weight': [25, 42],
            'lifespan': [12, 15],
            'group': 'hound',
            'description_short':
                '   The sleek, sweet-faced Whippet, the “Poor Man’s Racehorse,” is lightning quick. He is an amiable,\n'
                'dignified, and gentle soul, but give him something to chase and he’s all business. The name Whippet\n'
                'is synonymous with streamlined grace.\n',
            'description_long':
                '   At somewhere between 18 and 22 inches at the shoulder, the Whippet looks like a Greyhound, but\n'
                'smaller. The Whippet exhibits the classic “inverted S” lines of the sighthound. The deep chest and\n'
                'trim waist; a lean head supported by a long, arched neck; and slim but sturdy legs combine in a\n'
                'picture of an agile, fleet-footed athlete.\n\n'
                '   Between bursts of intense pursuit, Whippets love to stretch out and relax for long hours,\n'
                'enjoying the role of a loving, and loved, companion. Whippets like a fenced yard to run in, but they\n'
                'do nicely in cozy apartments too—as long as they are exercised properly. Another plus for city\n'
                'dwellers: Whippets rarely bark. Despite the breed’s elegant looks, the Whippet is a robust,\n'
                'low-maintenance dog.\n',
        }
    },

    'y': {
        'Yorkshire_Terrier': {
            'temperament': ['affectionate', 'sprightly', 'tomboyish'],
            'height': [7, 8],
            'weight': 7,
            'lifespan': [11, 15],
            'group': 'toy',
            'description_short':
                '   Beneath the dainty, glossy, floor-length coat of a Yorkshire Terrier beats the heart of a feisty,\n'
                'old-time terrier. Yorkies earned their living as ratters in mines and mills long before they became\n'
                'the beribboned lapdogs of Victorian ladies.\n',
            'description_long':
                '   The Yorkshire Terrier is a compact, toy-size terrier of no more than seven pounds whose crowning\n'
                'glory is a floor-length, silky coat of steel blue and a rich golden tan.\n\n'
                '   Don’t let the Yorkie’s daintiness fool you. Tenacious, feisty, brave, and sometimes bossy, the\n'
                'Yorkie exhibits all the traits of a true terrier. Often named the most popular dog breed in various\n'
                'American cities, Yorkies pack lots of big-town attitude into a small but self-important package.\n'
                'They are favorites of urbanites the world over.\n\n'
                '   Yorkies are long-lived and low-allergen (the coat is more like human hair than animal fur), and\n'
                'they make fine little watchdogs. This is a true “personality breed,” providing years of laughs,\n'
                'love, and close companionship.\n',
            'nicknames': {'Yorkie'}
        }
    },
}
