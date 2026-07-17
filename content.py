"""Coppercraft landing pages — all copy, per page.

Every claim traces to: the 3 offer briefs, the avatar sheet, the VoC research,
outputs/coppercraft/verified-claims.md (awards/press), the brand cheat sheet
(site-approved lines), or the live BarCart store (prices/variants, probed
2026-07-14). Quote attributions follow the shipped retargeting copy precedent
(fk_check.py self-test corpus: Gary Carter / Eric Burke).

Copy rules applied (coppercraft-batch gate): FK<=6 per block, contractions,
no negation stacks, no mirrored parallelism, no isn't/is flips, no youth vocab,
never-say (smooth/handcrafted/best/legendary/premium-w/o-proof), zero em dashes,
VoC verbatim over composed, claims true per SKU label.
"""

STORE = "barcart.coppercraftdistillery.com"
STOREFRONT_TOKEN = "e14c0086c2a8d5de9443de1e997156fd"  # public token, same one the brand's own BarCart buy-button widget ships
PIXEL_ID = "699233373265338"  # verified brand pixel (domain-verified) per flaviar-integration-research.md

VARIANTS = {
    "nine":  "51261476110642",   # 9-Year Straight Bourbon  $37.99
    "rye":   "45816466342194",   # Rye Whiskey              $37.99 (buy-button channel)
    "blend": "45816465686834",   # Blend of Straight Bourbons $42.95
}

SHIP_NOTE = "Ships to most US states. Not available in AL, AK, AR, DE, HI, MS, SD, UT, or WV."
FLAVIAR_LINE = "All sales are processed and fulfilled by licensed, third-party retailers on the Flaviar Checkout network."
PAYMENTS = [
    ("Visa", "assets/pay/visa.png"),
    ("Mastercard", "assets/pay/mastercard.png"),
    ("American Express", "assets/pay/amex.png"),
    ("Discover", "assets/pay/discover.png"),
    ("Apple Pay", "assets/pay/apple-pay.png"),
    ("Google Pay", "assets/pay/google-pay.png"),
]
PRESS = ["USA TODAY", "WHISKY ADVOCATE", "THE WHISKEY WASH", "THE MANUAL", "THE KNOCKTURNAL"]

STEPS = [
    ("Pick your bottles",
     "One bottle, the pair, or the Full Lineup. Checkout takes about a minute."),
    ("A licensed retailer fulfills it",
     "Licensed shops on the Flaviar network sell and ship each order. That's just how you buy spirits online. Fully legal."),
    ("Sign at your door",
     "An adult 21 or older signs for the package on delivery. " + SHIP_NOTE),
]

TRIO_PRICE = "$118.93"

PAGES = {
    # ================================================================ 9-YEAR
    "9-year": {
        "file": "9-year.html",
        "title": "Coppercraft 9-Year Straight Bourbon | $37.99, Aged 9 Years in Oak",
        "meta_desc": "A bourbon aged nine real years, with the 9 printed on the front of the bottle. 90.6 proof, $37.99, shipped to your door by a licensed retailer.",
        "sku_name": "Coppercraft 9-Year Straight Bourbon",
        "accent": "#B87333",
        "h1": "Coppercraft 9-Year Straight Bourbon Whiskey",
        "tagline": "A Real 9-Year Bourbon For $37.99",
        "sub": ("Aged nine full years in American oak. The critics found it. "
                "Most people haven't yet."),
        "bullets": [
            "The age is real: 9 years, printed on the front label",
            "90.6 proof, and the reviews call it big and rich",
            "Aged Indiana bourbon. The label says so, plain as day",
            "The easy gift: the 9 vouches for you before the bottle's opened",
        ],
        "price": "$37.99",
        "specs": "750 ml · 90.6 proof · Small batch",
        "carousel": [
            ("assets/9yr-hero-dark.jpg", "Coppercraft 9-Year Straight Bourbon bottle"),
            ("assets/9yr-label-closeup.jpg", "The 9 years printed on the label: 90.6 proof, 750 ml"),
            ("assets/9yr-rocksglass.jpg", "9-Year Straight Bourbon poured over a big cube"),
            ("assets/9yr-smoke-glasses.jpg", "Coppercraft bottles and glasses on a bar"),
            ("assets/9yr-gift-front.jpg", "The Coppercraft whiskey lineup"),
        ],
        "tiers": [
            {"key": "single", "label": "One Bottle", "name": "9-Year Straight Bourbon",
             "price": "$37.99", "items": [("nine", 1)],
             "why": "Nine years in oak. The slow sipper.", "popular": False},
            {"key": "duo", "label": "The Sip & Mix Pair", "name": "9-Year + 100-Proof Blend",
             "price": "$80.94", "items": [("nine", 1), ("blend", 1)],
             "why": "The slow sipper plus the cocktail workhorse, in one order.", "popular": True},
            {"key": "trio", "label": "The Full Lineup", "name": "9-Year + Blend + Rye",
             "price": TRIO_PRICE, "items": [("nine", 1), ("blend", 1), ("rye", 1)],
             "why": "The whole shelf: sipper, cocktail bottle, and the spice-forward rye. Covers your next two gifts.", "popular": False},
        ],
        "problem_h2": "Most craft bourbon is bottled too young.",
        "problem_ps": [
            "You've had the letdown bottle. The label looked right. The story sounded right. Then the pour tasted like sucking on a penny.",
            "That's what young whiskey does. Oak needs years to round off the raw edge, and most craft brands can't afford to wait. They bottle at two years and price it like ten.",
            "The genuinely aged bottles still exist. They're just allocated, marked up, or gone before you hear about them.",
            "This one sat in oak for nine years. And it's still $37.99, because the collectors haven't started chasing it.",
        ],
        "problem_img": ("assets/9yr-smoke-glasses.jpg", "Coppercraft 9-Year on the bar"),
        "mech_h2": "Three facts on the label.",
        "mech_intro": "Want to know if a bourbon's worth it? The front of the bottle will tell you.",
        "mech_cards": [
            ("9 YEARS", "A printed age has to be true. It's federal law. The 9 on this label means nine real years in the barrel."),
            ("90.6 PROOF", "Enough strength to carry the oak, the spice, and the dark sweets. Pour it neat or over one big cube."),
            ("HONEST SOURCING", "It's aged Indiana stock, and the label says so instead of hiding it. Whiskey folks respect that kind of honesty."),
        ],
        "mech_img": ("assets/9yr-label-closeup.jpg", "The 9 years on the front label"),
        "quotes": [
            ("It feels like a secret the whiskey world forgot to keep.",
             "Gary Carter · Sips & Sites & Bites"),
            ("It's definitely got a holiday molasses cookie type feel to it, and that's appreciated.",
             "From a Coppercraft 9-Year review"),
        ],
        "compare_h2": "What a real 9-year bourbon usually costs.",
        "compare_cols": ("The usual 9-year bottle", "Coppercraft 9-Year"),
        "compare_rows": [
            ("Collector markup", "Built into the price", "None yet"),
            ("How you buy it", "Waitlists and store lotteries", "Ships to your door"),
            ("The age on the label", "9 years", "9 years, printed on the front"),
            ("Price", "Climbing every year", "$37.99"),
        ],
        "compare_quote": '"I especially appreciate seeing an age-stated bourbon for under $40."',
        "compare_note": "That's Eric Burke at BourbonGuy. He's talking about this exact bottle, and honestly, we'll take it.",
        "gift_h2": "Buying it as a gift? The 9 makes it a safe pick.",
        "gift_ps": [
            "You can't taste a bottle before you give it. That's the anxiety. So let the label make your case. A bourbon that says nine years on the front reads as quality before the cork even comes out.",
            "“If you want something that puts a smile on most peoples faces, this is your whiskey.” That one's from a real Coppercraft review. It's about the nicest thing anyone can say about a gift bottle.",
            "And if the occasion is a big one, show up with the Full Lineup. Three bottles makes you the person who actually pays attention.",
        ],
        "gift_img": ("assets/9yr-lineup-smoke.jpg", "The Coppercraft whiskey lineup"),
        "faq": [
            ("Is the 9 on the label real?",
             "Yes. It's printed on the front label. Federal law requires a printed age to be true, so the age on the bottle is the age in the barrel."),
            ("Where is it distilled?",
             "The bourbon is aged Indiana stock. Coppercraft picks it and bottles it in Holland, Michigan. They say so plainly instead of hiding it. Bourbon folks respect that."),
            ("Is $37.99 too cheap to be good?",
             "The price is low because there's no collector markup on it yet. Well-aged bottles usually cost more once people start chasing them. Nobody's chasing this one so far. That's the opportunity."),
            ("Will a real bourbon drinker be impressed?",
             "The label does that work for you. Nine years in oak is the kind of fact an enthusiast checks first. One critic put it simply: he appreciates seeing a bourbon this old for under $40."),
            ("Can it ship to my state?",
             SHIP_NOTE + " Checkout confirms your address before you pay."),
            ("What if the bottle arrives damaged?",
             "The retailer that shipped it will make it right. Just reply to your order email and they'll take care of you."),
            ("Which bottle should I pick?",
             "The 9-Year is the sipper. The 100-proof Blend is the cocktail bottle. The Rye is the spice-forward pick. If you're gifting a bourbon drinker, start here with the 9-Year."),
        ],
        "final_h2": "Nine years in the barrel. A few days to your door.",
        "final_sub": "Bottled in small batches in Holland, Michigan. Your glass is ready when you are.",
        "cross": [("../rye/", "Coppercraft Rye Whiskey"), ("../blend/", "Blend of Straight Bourbons")],
    },

    # ================================================================== RYE
    "rye": {
        "file": "rye.html",
        "title": "Coppercraft Rye Whiskey | Spice-Forward, 90 Proof, $37.99",
        "meta_desc": "A spice-forward small batch rye: pepper, pine, and mint with cocoa and malt up front. 90 proof, $37.99, shipped to your door by a licensed retailer.",
        "sku_name": "Coppercraft Rye Whiskey",
        "accent": "#8a5a28",
        "h1": "Coppercraft Rye Whiskey",
        "tagline": "The Spice-Forward Rye For $37.99",
        "sub": ("It opens with cocoa and malt, then the peppercorn spice takes over. "
                "Pine and mint underneath."),
        "bullets": [
            "Spice forward: pepper, pine, and mint, with real depth under it",
            "Cocoa and malt up front, so it stays friendly to a bourbon drinker",
            "90 proof, and it makes a mean Sazerac or Manhattan",
            "Buying for a rye drinker? This is the bottle he doesn't already own",
        ],
        "price": "$37.99",
        "specs": "750 ml · 90 proof · Small batch",
        "carousel": [
            ("assets/rye-bottle.jpg", "Coppercraft Rye Whiskey, 90 proof, small batch"),
            ("assets/rye-label-closeup.jpg", "The Rye Whiskey label: 45% alc by vol, 90 proof, small batch"),
            ("assets/rye-dark-scene.jpg", "Coppercraft Rye Whiskey bottle"),
            ("assets/bar-pour.jpg", "A cocktail being strained at the Coppercraft bar"),
        ],
        "tiers": [
            {"key": "single", "label": "One Bottle", "name": "Rye Whiskey",
             "price": "$37.99", "items": [("rye", 1)],
             "why": "The spice-forward pick.", "popular": False},
            {"key": "duo", "label": "The Spice & Oak Pair", "name": "Rye + 9-Year Bourbon",
             "price": "$75.98", "items": [("rye", 1), ("nine", 1)],
             "why": "The spice bottle and the 9-year sipper, both sides of the shelf.", "popular": True},
            {"key": "trio", "label": "The Full Lineup", "name": "Rye + 9-Year + Blend",
             "price": TRIO_PRICE, "items": [("rye", 1), ("nine", 1), ("blend", 1)],
             "why": "The whole shelf: the rye, the sipper, and the 100-proof cocktail bottle. Covers your next two gifts.", "popular": False},
        ],
        "problem_h2": "Most rye is bourbon in disguise.",
        "problem_ps": [
            "Pick up a random rye and odds are it pours sweet, soft, and quiet. The spice you bought it for barely shows up.",
            "Young craft ryes have the opposite problem. Plenty of bite, zero depth. Thin, green, one note.",
            "Rye drinkers want both at once: the spice and the oak. Very little on the shelf delivers the two together at a fair price.",
            "That's the gap this bottle fills, at $37.99.",
        ],
        "problem_img": ("assets/bar-pour.jpg", "A cocktail being strained at the Coppercraft bar"),
        "mech_h2": "Why reviewers call it complete.",
        "mech_intro": "Here's what's waiting in the glass, layer by layer.",
        "mech_cards": [
            ("THE SPICE", "Peppercorn spice that's distinctly rye, with pine and mint behind it. It wakes the palate up."),
            ("THE DEPTH", "Reviewers point to oak and leather notes that young ryes can't offer. There's real weight under the spice."),
            ("90 PROOF", "Pour it neat or make it the spine of a Sazerac. Plenty of flavor for the price, as one review put it."),
        ],
        "mech_img": ("assets/rye-label-closeup.jpg", "Coppercraft Rye Whiskey label: 45% alc by vol, 90 proof"),
        "quotes": [
            ("I wasn't expecting the massive spice bomb detonation that pleasantly ripped across my tongue.",
             "From a Coppercraft Rye review"),
            ("This has darker flavors like oak and leather that no 2 year old rye could offer.",
             "From a Coppercraft Rye review"),
            ("It tastes like a 'complete' product.",
             "From a Coppercraft Rye review"),
        ],
        "compare_h2": "Where most rye falls short.",
        "compare_cols": ("The usual rye shelf", "Coppercraft Rye"),
        "compare_rows": [
            ("The spice", "Soft, sweet, barely there", "Pepper, pine, and mint"),
            ("The depth", "Thin and green when young", "Oak and leather under the spice"),
            ("The pour", "Sweet bourbon in disguise", "Distinctly rye"),
            ("Price", "Allocated ryes climb fast", "$37.99"),
        ],
        "compare_note": "Reviewers keep landing on the same word for this one: complete.",
        "gift_h2": "Buying for the rye drinker in your life?",
        "gift_ps": [
            "Rye drinkers are picky on purpose. They want the spice most brands water down. This one delivers it, and the cocoa and malt up front keep it friendly even for the bourbon-only crowd.",
            "A bottle like this starts a ritual. Birthday pours, holiday pours, the good glass that comes down off the shelf.",
        ],
        "gift_img": ("assets/rye-dark-scene.jpg", "Coppercraft Rye Whiskey"),
        "faq": [
            ("Is it actually spice forward?",
             "Yes. One reviewer called it a massive spice bomb, and he meant it as a compliment. Pepper, pine, and mint carry the pour."),
            ("Will a bourbon drinker still enjoy it?",
             "Usually, yes. Cocoa and malt open the pour before the spice arrives, so it lands closer to a bold bourbon than a harsh rye."),
            ("Is 90 proof enough for a serious rye?",
             "One review said it straight: plenty of flavor for the price. The spice does the heavy lifting, and 90 proof keeps it easy to pour neat."),
            ("What do the reviews say about depth?",
             "They call out oak and leather notes that young ryes can't offer. They say it tastes complete, not one-note."),
            ("Can it ship to my state?",
             SHIP_NOTE + " Checkout confirms your address before you pay."),
            ("What if the bottle arrives damaged?",
             "The retailer that shipped it will make it right. Just reply to your order email and they'll take care of you."),
            ("Which bottle should I pick?",
             "The Rye is the spice-forward pick. The 9-Year is the slow sipper. The 100-proof Blend is the cocktail bottle. If your person already loves rye, you're in the right place."),
        ],
        "final_h2": "The rye that actually tastes like rye.",
        "final_sub": "Small batch, 90 proof, $37.99. Made in Holland, Michigan, and happy to travel.",
        "cross": [("../9-year/", "Coppercraft 9-Year Bourbon"), ("../blend/", "Blend of Straight Bourbons")],
    },

    # ================================================================ BLEND
    "blend": {
        "file": "blend.html",
        "title": "Coppercraft Blend of Straight Bourbons | 100 Proof, $42.95",
        "meta_desc": "A 100-proof blend of straight bourbons: young Michigan punch married to aged Indiana depth. Bold enough to mix, good enough to sip. $42.95, shipped by a licensed retailer.",
        "sku_name": "Coppercraft Blend of Straight Bourbon Whiskies",
        "accent": "#7a4a20",
        "h1": "Coppercraft Blend of Straight Bourbon Whiskies",
        "tagline": "A 100-Proof Blend Of Straight Bourbons, Built For Cocktails",
        "sub": ("Every drop is straight bourbon. A young, punchy Michigan bourbon "
                "married to aged Indiana stock, bottled at 100 proof."),
        "bullets": [
            "A blend of two finished straight bourbons, never cut with neutral spirit",
            "100 proof, so it doesn't disappear under ice and bitters",
            "Punchy and spicy, exactly what an Old Fashioned asks for",
            "One bottle that covers the Old Fashioned and the neat pour",
        ],
        "price": "$42.95",
        "specs": "750 ml · 100 proof · Small batch",
        "carousel": [
            ("assets/blend-scene.jpg", "Coppercraft Blend of Straight Bourbon Whiskies with corn and rye grain"),
            ("assets/blend-cocktails.jpg", "Whiskey lemonade cocktails made with the Coppercraft Blend"),
            ("assets/blend-label-closeup.jpg", "The label: Blend of Straight Bourbon Whiskies, 100 proof"),
            ("assets/blend-dark-scene.jpg", "Coppercraft Blend of Straight Bourbon Whiskies bottle"),
        ],
        "tiers": [
            {"key": "single", "label": "One Bottle", "name": "Blend of Straight Bourbons",
             "price": "$42.95", "items": [("blend", 1)],
             "why": "The 100-proof cocktail workhorse.", "popular": False},
            {"key": "duo", "label": "The Sip & Mix Pair", "name": "Blend + 9-Year Bourbon",
             "price": "$80.94", "items": [("blend", 1), ("nine", 1)],
             "why": "The cocktail workhorse plus the 9-year slow sipper, in one order.", "popular": True},
            {"key": "trio", "label": "The Full Lineup", "name": "Blend + 9-Year + Rye",
             "price": TRIO_PRICE, "items": [("blend", 1), ("nine", 1), ("rye", 1)],
             "why": "The whole shelf: cocktail bottle, sipper, and the spice-forward rye. Covers your next two gifts.", "popular": False},
        ],
        "problem_h2": "“Blend” scared you off? Fair. Read this first.",
        "problem_ps": [
            "Cheap blended whiskey earned the bad name. That stuff is whiskey cut with neutral grain spirit, and it tastes like it.",
            "A blend of straight bourbons is a different thing. Each part is a finished straight bourbon on its own. The blending is the craft. A young, punchy bourbon gets married to older, deeper stock, on purpose.",
            "One visitor called it the biggest surprise of his trip to Michigan. That's what the right blend does.",
        ],
        "problem_img": ("assets/blend-dark-scene.jpg", "Coppercraft Blend of Straight Bourbon Whiskies"),
        "mech_h2": "Two bourbons doing what neither could do alone.",
        "mech_intro": "The label says it plainly: a blend of straight bourbon whiskies, 100 proof.",
        "mech_cards": [
            ("THE YOUNG ONE", "Coppercraft's own Michigan bourbon, four-plus years in the barrel. This is where the punch and the spice come from."),
            ("THE OLD ONE", "Aged Indiana straight bourbon, nine-plus years old. It settles the whole pour down with oak and dark sweets."),
            ("100 PROOF", "Bottled at full cocktail strength. Ice, citrus, and bitters won't wash it out."),
        ],
        "mech_img": ("assets/blend-label-closeup.jpg", "The label: Blend of Straight Bourbon Whiskies, 100 proof"),
        "quotes": [
            ("It was the biggest surprise of my trip to Michigan... great balance of sweetness, spiciness, and oak.",
             "From a Coppercraft Blend review"),
            ("Aggressive, spicy, punchy, bold... a flavor that lends itself ideal to cocktails.",
             "From a Coppercraft Blend review"),
        ],
        "compare_h2": "Why one bottle replaces two.",
        "compare_cols": ("The usual options", "Coppercraft Blend"),
        "compare_rows": [
            ("Cheap blends", "Cut with neutral spirit", "Straight bourbon only"),
            ("Aged sippers", "Too precious to mix", "Built to mix and to sip"),
            ("Standard 80 proof", "Vanishes under ice", "100 proof holds up"),
            ("Price", "Two bottles for two jobs", "$42.95 for one that does both"),
        ],
        "compare_note": "One bottle doing two jobs is the whole point. It's the mixer and the sipper at the same time.",
        "gift_h2": "The host gift that gets opened tonight.",
        "gift_ps": [
            "A wine bottle gets a polite thank-you. A 100-proof blend of straight bourbons gets opened, poured into Old Fashioneds, and talked about while you're still there.",
            "Bring it to the next dinner you didn't want to walk into empty-handed.",
        ],
        "gift_img": ("assets/blend-cocktails.jpg", "Cocktails made with the Coppercraft Blend"),
        "faq": [
            ("Is a blend just cheap whiskey?",
             "Cheap blends are cut with neutral grain spirit. This is a blend of straight bourbons, which means every component is a finished straight bourbon on its own. The word on the label is doing honest work."),
            ("Is 100 proof too hot to sip neat?",
             "It drinks bolder than an 80-proof pour, and that's the point. If it runs warm for you, one big cube settles it right down."),
            ("What are the two bourbons in it?",
             "Two bourbons. A young, punchy one that Coppercraft distills in Michigan, and an aged straight bourbon from Indiana. The young one brings the spice, and the old one brings the oak and dark sweets."),
            ("What cocktails does it work in?",
             "Start with the Old Fashioned and the Manhattan. It also carries a whiskey lemonade or a sour. At 100 proof it doesn't fade under ice and citrus."),
            ("Is $42.95 steep for a mixing whiskey?",
             "It's one bottle doing two jobs. It replaces the cheap mixer and the neat-pour bottle at the same time, so the math works out in its favor."),
            ("Can it ship to my state?",
             SHIP_NOTE + " Checkout confirms your address before you pay."),
            ("Which bottle should I pick?",
             "The Blend is the cocktail bottle. The 9-Year is the slow sipper. The Rye is the spice-forward pick. If your bar cart needs one workhorse, it's this one."),
        ],
        "final_h2": "Your bar cart's new workhorse.",
        "final_sub": "100 proof, small batch, $42.95. Treat the host or treat yourself.",
        "cross": [("../9-year/", "Coppercraft 9-Year Bourbon"), ("../rye/", "Coppercraft Rye Whiskey")],
    },
}
